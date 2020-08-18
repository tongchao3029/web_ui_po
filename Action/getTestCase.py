from Utils.ExcelParser import *
from Config.ProjectVar import *



def getTestAccountInfo(sheetname):
    wb=ExcelParser(ExcelFile_Path)
    wb.getSheetByName(sheetname)
    data=wb.getSheetAllCellValuesByRow()
    return data

def getTestData(test_data_sheet_name):
    wb=ExcelParser(ExcelFile_Path)
    wb.getSheetByName(test_data_sheet_name)
    test_data=wb.getSheetAllCellValuesByRow()
    return test_data





if __name__=="__main__":
    print(getTestAccountInfo(test_user_info_sheet))
    print(getTestData(test_data_sheet))
