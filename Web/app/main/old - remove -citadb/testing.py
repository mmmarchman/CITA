__author__ = 'Doug'

import CITAdb.db_access
import CITAdb.db_utility

test = CITAdb.db_utility.get_unstructured_column_names(1)
print (test)

print ("\n**should be 1**")
""" fetch company ID using the username
Note that username should be returned by WSGI script as in trends.html already """
companyid = CITAdb.db_access.get_company_id('Doug Oakes')
print (companyid)

print ("\n**should be 2015-01-01**")
teststartdate = CITAdb.db_access.get_startdate_for_company(companyid)
print (teststartdate)

print ("\n**should be 2015-09-25**")
testenddate = CITAdb.db_access.get_enddate_for_company(companyid)
print (testenddate)

print ("\n**builds sql string based on inputs**")
testbuildquery = CITAdb.db_utility.build_query("customer_complaint", ['state','Company'], ['"GA"','"Navy FCU"'])
print (testbuildquery)

print ("\n**executes the above sql query - entries for 'None' are legit blanks in database**")
queryresult = CITAdb.db_access.run_query(testbuildquery)
for entry in queryresult:
    print (entry)
print ("** to do reminder: 'None' has to be on exclusion list, otherwise dominates results **")
