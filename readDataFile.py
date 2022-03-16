import pandas as pd

def readExcel():
    return pd.read_excel(r'files/YapayZeka.xlsx', sheet_name='Data')

def readExcel2(file, sheet):
    return pd.read_excel(file, sheet_name=sheet)