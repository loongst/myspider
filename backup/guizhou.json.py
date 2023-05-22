import json
import pymysql
from cve_spider.settings import *
from pymysql.converters import escape_string
s={"CVE_ID": "CVE-2022-34810", "CWE_ID": "862", "Vulnerability_Type": "", "Publish_Date": "2022-06-30", "Update_Date": "2022-07-08", "Score": "4.0", "Gained_Access_Level": "None", "Access": "Remote", "Complexity": "Low", "Authentication": "???", "Confidentiality": "Partial", "Integrity": "None", "Availability": "None", "Description": "A missing check in Jenkins RQM Plugin 2.8 and earlier allows attackers with Overall/Read permission to enumerate credentials IDs of credentials stored in Jenkins."}
# print(dict(s))
a=dict(s)

b=list(a.values())
print(len(b))

con=pymysql.connect(host=MYSQL_HOST,user=MYSQL_USER,password=MYSQL_PASS,db=MYSQL_DB)
cursor=con.cursor()

c=tuple((escape_string(a['CVE_ID']),escape_string(a['CWE_ID']),escape_string(a['Vulnerability_Type']),escape_string(a['Publish_Date']),escape_string(a['Update_Date']),escape_string(a['Score']),escape_string(a['Gained_Access_Level']),escape_string(a['Access']),escape_string(a['Complexity']),escape_string(a['Authentication']),escape_string(a['Confidentiality']),escape_string(a['Integrity']),escape_string(a['Availability']),escape_string(a['Description'])))

insert_sql="""
        insert into `cve`(`CVE_ID`,`CWE_ID`,`Vulnerability_Type`,`Publish_Date`,`Update_Date`,`Score`,`Gained_Access_Level`,`Access`,`Complexity`,`Authentication`,`Confidentiality`,`Integrity`,`Availability`,`Description`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
cursor.execute(insert_sql,[x for x in b])
con.commit()