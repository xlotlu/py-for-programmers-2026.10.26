import openpyxl

EXCEL_FILE = "test-dataset.xlsx"

workbook = openpyxl.load_workbook(EXCEL_FILE, read_only=True, data_only=True)

# get the first sheet:
sheet = workbook[workbook.sheetnames[0]]

for row in sheet.iter_rows():
    data = [cell.value for cell in row]

# să facem o funcție
def load_spreadsheet(fname):
    pass
# ce returnează un generator
# cu fiecare row drept lista de valori

def load_spreadsheet(fname):
    workbook = openpyxl.load_workbook(fname,
                                      read_only=True,
                                      data_only=True)

    sheet = workbook[workbook.sheetnames[0]]
    for row in sheet.iter_rows():
        yield [cell.value for cell in row]

# funcția cu yield de mai sus este perfect echivalentă
# cu funcția cu return de mai jos

def load_spreadsheet(fname):
    workbook = openpyxl.load_workbook(fname,
                                      read_only=True,
                                      data_only=True)

    sheet = workbook[workbook.sheetnames[0]]
    return (
        [cell.value for cell in row]
        for row in sheet.iter_rows()
    )

for idx, row in enumerate(load_spreadsheet(EXCEL_FILE)):
    print(row)
    if idx == 10: break