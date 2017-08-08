import openpyxl

wb = openpyxl.load_workbook('Billable_Suppliers.xlsx')
wb.get_sheet_names()
print(wb)
ActSheet = wb.active
for rowOfCellObjects in ActSheet['A2':'C55']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value),
    print('--- END OF ROW ---')
