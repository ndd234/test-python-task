import micro_framework

modules_folder = 'C:\\Users\\Роман\\Desktop\\работа\\python\\'+\
                 'wrike\\task\\test-python-task\\framework\\modules\\'
data_input_folder = 'C:\\Users\\Роман\\Desktop\\работа\\python\\'+\
                    'wrike\\task\\test-python-task\\data\\input\\'
metrics_output_folder = 'C:\\Users\\Роман\\Desktop\\работа\\python\\'+\
                        '\wrike\\task\\test-python-task\\data\\result\\'

micro_framework.run(modules_folder,
                    data_input_folder,
                    metrics_output_folder)
