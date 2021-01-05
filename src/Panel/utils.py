# Plotly Dash style filter functions

operators = [['>='],
             ['<='],
             ['<'],
             ['>'],
             ['!='],
             ['=='],
             ['contains '],
             ['datestartswith ']]

def split_filter_part(filter_part):
    for operator_type in operators:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                value_part = value_part.strip()
                v0 = value_part[0]
                if (v0 == value_part[-1] and v0 in ("'", '"', '`')):
                    value = value_part[1: -1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part
                return operator_type[0], value
                

    return [None] * 2

def create_query_string(key, op, value):
    query_str = ""
    if type(value)==str:
        if ', ' in value:
            for item in value.split(', '):
                print(item)
                query_str += "(" + key + op + "'"+item+"'" + ")|"
            query_str = query_str[:-1]
        else:
            query_str += "(" + key + op + "'"+value+"'" + ")"
    elif type(value)==float:
        query_str += "(" + key + op + str(value) + ")"
    return query_str