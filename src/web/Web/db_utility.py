__author__ = 'Doug'


import db_access


""" (filters for GUI)
given company id, returns just structured data column names """
def get_structured_column_names (company_id):
    data = db_access.get_structured_data(company_id)
    result = []
    for entry in data:
        result.append(entry['column_name'])
    return result


""" (filter values for GUI dropdowns)
given company id, returns just strucutred data column values"""
def get_structured_column_values (company_id):
    data = db_access.get_structured_data(company_id)
    resultlist = []
    for entry in data:
        resultlist.append(entry['column_values'])

    result = str(resultlist[0]).split("|")

    return result

""" potentially more than 1 unstructured column - should allow client to select"""
def get_unstructured_column_names (company_id):
    data = db_access.get_unstructured_columns(company_id)
    resultlist = []
    for entry in data:
        resultlist.append(entry['column_name'])
    return resultlist

"""build query string based on selections"""
def build_query (unstruct, filternamelist, filtervaluelist):
    result = "select " + str(unstruct) + " from a_data"
    if (len(filternamelist) > 0):
        result = result + " where "
        for x in range(0, len(filtervaluelist), 1):
            result = result + str(filternamelist[x])
            result = result + " = "
            result = result + str(filtervaluelist[x])
            if (x < len(filtervaluelist)-1):
                result = result + " and "
    return result