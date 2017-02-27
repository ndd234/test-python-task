from module_builder import ModuleBuilder

def mapper(df):
    #magic
    return {'foo': 'bar'}

enable = True
	
module = ModuleBuilder(mapper = mapper)
