from module_builder import ModuleBuilder

def mapper(df):
    #magic
    return {'size': df.size, 'len': len(df), 'pages': df['page_name'].count()}

enable = False
	
module = ModuleBuilder(mapper = mapper)
