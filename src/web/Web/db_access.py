__author__ = 'Doug'


import sqlite3


def dictionary_factory(cursor, row):
    col_names = [d[0].lower() for d in cursor.description]
    return dict(zip(col_names, row))


""" convenience, allows update to sqlite file name in one spot"""
def get_connection():
    conn = sqlite3.connect('data-dev.sqlite')
    return conn


""" given company id, returns earliest data date """
def get_startdate_for_company(company_id):
    conn = get_connection()
    try:
        crs = conn.cursor();
        cmd = ('select distinct start_date from company where company_id = ' + str(company_id))
        crs.execute(cmd)
        result = crs.fetchone()
    finally:
        conn.close()
    return result


""" given company id, returns last data date """
def get_enddate_for_company(company_id):
    conn = get_connection()
    try:
        crs = conn.cursor();
        cmd = ('select distinct end_date from company where company_id = ' + str(company_id))
        crs.execute(cmd)
        result = crs.fetchone()
    finally:
        conn.close()
    return result

""" given company id, returns list of structured columns (filters) and values"""
def get_structured_data (company_id):
    conn = get_connection()
    try:
        result = []
        crs = conn.cursor();
        cmd = ('select column_name, column_values from structured_data where company_id = ' + str(company_id))
        crs.execute(cmd)
        crslist = crs.fetchall()
        for entry in crslist:
            result.append(dictionary_factory(crs, entry))
    finally:
        conn.close()
    return result


""" given company ID, return list of unstructured column names """
def get_unstructured_columns (company_id):
    conn = get_connection()
    try:
        result = []
        crs = conn.cursor();
        cmd = ('select * from unstructured_data where company_id = ' + str(company_id))
        crs.execute(cmd)
        crslist = crs.fetchall()
        for entry in crslist:
            result.append(dictionary_factory(crs, entry))
    finally:
        conn.close()
    return result