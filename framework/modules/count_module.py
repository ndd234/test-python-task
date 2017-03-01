from module_builder import ModuleBuilder


def mapper(df):
    pages_views = \
        df[df['page_name'].notnull()].reset_index(drop=True)
    home_views_index = \
        pages_views[pages_views['page_name'] == "home.htm"].index
    solutions_views_index = \
        pages_views[pages_views['page_name'] == "solutions.htm"].index
    solutions_after_home_index = \
        (home_views_index+1).intersection(solutions_views_index)
    return {
        'home views': len(home_views_index),
        'solutions_after_home': len(solutions_after_home_index),
    }

enable = True

module = ModuleBuilder(mapper = mapper)
