from Action.getTestCase import *
from Action.action import *
from Utils.ExcelParser import *
from Utils.takeScreenshot import *
from Utils.Logger import *



def main():
    result=[]
    test_user_account=getTestAccountInfo(test_user_info_sheet)
    wb=ExcelParser(ExcelFile_Path)
    wb.createNewSheet("测试结果")
    wb.getSheetByName("测试结果")
    logger=getLogger()

    for value in test_user_account[1:]:
        sub_result=[]
        logger.debug(value)
        account_num = value[account_num_col-1]
        account_uname=value[account_uname_col-1]
        account_passwd = value[account_passwd_col-1]
        account_testdata= value[account_testdata_col-1]
        account_if_execute = value[account_if_execute_col-1]
        account_testtime = value[account_testtime_col-1]
        account_testresult = value[account_testresult_col-1]
        if account_if_execute.lower()=="n":
            logger.debug("第【%s】个账户【%s】不需要测试"%(account_num,account_uname))
            continue
        else:
            test_data=getTestData(account_testdata)
            try:
                driver=login(account_uname,account_passwd)
                driver=swithNewContactTab(driver)
                result.append(test_user_account[0])
            except Exception as e:
                logger.debug(e)
                takeScreenshots(driver)
                continue
            for value in test_data[1:]:
                contact_num = value[contact_num_col-1]
                contact_name = value[contact_name_col-1]
                contact_email = value[contact_email_col-1]
                contact_star = value[contact_star_col-1]
                contact_phonenum = value[contact_phonenum_col-1]
                contact_comment = value[contact_comment_col-1]
                contact_keyword = value[contact_keyword_col-1]
                contact_if_execute = value[contact_if_execute_col-1]
                contact_testtime = value[contact_testtime_col-1]
                contact_testresult = value[contact_testresult_col-1]
                if contact_if_execute.lower()=="n":
                    logger.debug("第【%s】个账户【%s】的第【%s】条用例不需要测试"%(account_num,account_uname,contact_num))
                else:
                    addContactInfo(driver,contact_name,contact_email,contact_star,contact_phonenum,contact_comment)
                    if contact_keyword in driver.page_source:
                        logger.debug([contact_num,contact_name,contact_email,contact_star,contact_phonenum,contact_comment,contact_keyword,contact_if_execute,
                                              TimeUtil().get_chinesedatetime(),"Pass"])
                        sub_result.append([contact_num,contact_name,contact_email,contact_star,contact_phonenum,contact_comment,contact_keyword,contact_if_execute,
                                              TimeUtil().get_chinesedatetime(),"Pass"])
                    else:
                        sub_result.append([contact_num, contact_name, contact_email, contact_star, contact_phonenum,contact_comment, contact_keyword, contact_if_execute,
                                          TimeUtil().get_chinesedatetime(), "Fail"])
        for value in sub_result:
            if value[-1]=="Fail":
                result.append([account_num,account_uname,account_passwd,account_testdata,account_if_execute,TimeUtil().get_chinesedatetime(),"Fail"])
                break
        else:
            result.append([account_num, account_uname, account_passwd, account_testdata, account_if_execute,TimeUtil().get_chinesedatetime(), "Pass"])
        result.append(test_data[0])
        result.extend(sub_result)
        logger.debug("result:%s"%result)
        logger.debug("sub_result:%s"%sub_result)
    wb.writeRowsInSheet(result)
    for row in wb.getAllRows():
        for cell in row:
            if cell.value=="序号":
                wb.addRowStyle(row)
                break
            elif cell.value=="Pass":
                wb.addCellStyle(cell,"green")
                break
            elif cell.value=="Fail":
                wb.addCellStyle(cell,"red")
                break
    wb.saveExcel()


if __name__=="__main__":
    main()