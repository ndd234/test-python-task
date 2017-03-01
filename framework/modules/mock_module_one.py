from module_builder import ModuleBuilder

def mapper(df):
    #magic
    return {'metric1': '1', 'events': df['event_name'].count()}

enable = False
	
module = ModuleBuilder(mapper = mapper)
