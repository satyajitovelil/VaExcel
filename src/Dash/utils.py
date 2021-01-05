def extract_val(dictionary):
    ''' 
    
    This function extracts the individual values that can be applied as filters to a particular column from the filters dict. 
    Essentially creates a list where each item is a value that can be used to filter a column using slicing.
    
    NOT yet configured for use with ge and lt operators.
    
    '''
    
    vaex_filter_list = []
    for key, values in dictionary.items():
        if values != []:
            query_str = ""
            for value in values:
                if ',' in value:
                    for item in value.split(', '):
                        query_str += '(' + key +'=='+ item +')|'
                    query_str = query_str[:-1]
                else:
                    query_str += '(' + key +'=='+ value +')'
            vaex_filter_list.append(query_str)
    return vaex_filter_list