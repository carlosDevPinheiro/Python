import sqlite3
from openpyxl import Workbook

conn = sqlite3.connect('agenda.db')
cursor = conn.cursor()

# Create Excel (.xlsx) file
wb = Workbook()

c = ("""
SELECT * FROM Contatos;
""")
cursor.execute(c)
results = cursor.fetchall()
ws = wb.create_sheet(0)
ws.title = 'Contatos'
for row in results:
    ws.append(row)

workbook_name = "test_workbook"
wb.save(workbook_name + ".xlsx")

conn.commit()

conn.close()

