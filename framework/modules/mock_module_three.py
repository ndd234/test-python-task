from module_builder import ModuleBuilder

def mapper(df):
    #magic
    return {'foo': 'bar'}

enable = False
	
module = ModuleBuilder(mapper = mapper)
