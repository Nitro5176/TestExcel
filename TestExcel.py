import xlsxwriter as xl

workbook = xl.Workbook("Testing.xlsx")
worksheet1 = workbook.add_worksheet()

#on column A row 1 name test
worksheet1.write("A1", "test")

workbook.close()