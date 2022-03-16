import collections

from readDataFile import  *

def readDataModueDescribe():
    data = readExcel()
    return data.describe()

def readDataModueCounter():
    data = readExcel()
    counter = collections.Counter(data['Module barcode'])
    return counter

def readDataModueSort():
    data = readExcel()
    sort = data.sort_values(['Line', 'Module barcode'], ascending=[0, 1])
    return sort

