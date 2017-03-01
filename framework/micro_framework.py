from os import path, listdir, makedirs
from importlib import import_module
import pandas as pd

#workaround for loading metrics modules 
def load_modules(folder):
    modules = []
    parent = path.relpath(folder).replace('\\','.') + '.'
    for elem in listdir(folder):
        if elem.endswith(".py") and elem != '__init__.py':
            module_name = parent + elem.rsplit('.', 1)[0]
            module_candidate = import_module(module_name)
            if(module_candidate.enable):
                modules.append(module_candidate.module)
    return modules

#loading data
#UNION logs, JOIN user data, ORDER by timestamp
#maybe merge later?
def load_data(folder):
    users_df = pd.read_csv(folder + "users.csv", "|")
    pages_df = pd.read_csv(folder + "Pageviews.csv", "|")
    backend_df = pd.read_csv(folder + "Backend.csv", "|")
    user_events_df = (pages_df
                        .append(backend_df)
                        .merge(users_df, how='left', on='user_id')
                        .sort_values(by=['timestamp'])
                      );
    return user_events_df

#GROUP by user_id and hour
def get_groups(df):
    group_by = [
        pd.to_datetime((df['timestamp']/3600).map(int), unit='h'),
        df['user_id']
    ]
    return df.groupby(group_by)

#map df to dict of modules metrics
def process_metrics(df, modules):
    df_metrics = {} 
    for module in modules:
        df_metrics.update(module.mapper(df))
    return df_metrics

#process and reducing groups df metrics to result df
def reduce_metrics(groups, modules):
    metrics_df = pd.DataFrame()
    for group in groups:
        group_metrics = process_metrics(group[1], modules)
        group_metrics.update({'user': group[0][0], 'datetime':group[0][1]})
        #maybe concat
        metrics_df = metrics_df.append(
            group_metrics, ignore_index=True)
    return metrics_df

#setting user and datetime to fist columns
def normalize_columns(df):
    header = list(df)
    for column_name in ['datetime', 'user']:
        header.remove(column_name)
        header.insert(0, column_name)
    return df[header]

#dump to csv
def write_metrics(df, folder):
    if not path.exists(folder):
        makedirs(folder)
    df.to_csv(folder + 'Metrics.csv', sep='|', index = False)
    
#some logic
def run(modules_folder, data_input_folder, metrics_output_folder):
    modules = load_modules(modules_folder)
    data = load_data(data_input_folder)

    groups = get_groups(data) 
    metrics_df = reduce_metrics(groups, modules)
    metrics_df = normalize_columns(metrics_df)

    write_metrics(metrics_df, metrics_output_folder)

    print('metrics:\n', metrics_df)
