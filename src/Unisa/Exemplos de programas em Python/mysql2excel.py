import pymysql
from openpyxl import Workbook

conn = pymysql.connect(host='localhost', port=3311, user='root', passwd='root', db='northwind')

cur = conn.cursor()

# Create Excel (.xlsx) file
wb = Workbook()

cur.execute("""SELECT * from customers;""")

results = cur.fetchall()
ws = wb.create_sheet(0)
ws.title = 'Customers'
for row in results:
    ws.append(row)

workbook_name = "test_workbook"
wb.save(workbook_name + ".xlsx")

conn.commit()

conn.close()

