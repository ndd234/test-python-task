from module_builder import ModuleBuilder


def mapper(df):
    df = df.reset_index(drop=True)
    home_views_index = df[df['page_name'] == "home.htm"].index
    solutions_after_home_index = (home_views_index+1)\
        .intersection(df[df['page_name'] == "solutions.htm"].index)
    return {
        'home views': len(home_views_index),
        'solutions_after_home': len(solutions_after_home_index),
    }

enable = True

module = ModuleBuilder(mapper = mapper)
