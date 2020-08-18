import os

PROJECT_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH=os.path.join(PROJECT_PATH,"Config")
TEST_DATA_PATH=os.path.join(PROJECT_PATH,"TestData")
LOG_PATH=os.path.join(PROJECT_PATH,"Log")
Loggerconf_path=os.path.join(CONFIG_PATH,"Logger.conf")
PageElementLocator_path=os.path.join(CONFIG_PATH,"PageElementLocator.ini")
ExcelFile_Path=os.path.join(TEST_DATA_PATH,"126邮箱联系人.xlsx")



#sheetinfo
test_user_info_sheet="126账号"
test_data_sheet="联系人"

#excel testdata
account_num_col=1
account_uname_col=2
account_passwd_col=3
account_testdata_col=4
account_if_execute_col=5
account_testtime_col=6
account_testresult_col=7

contact_num_col=1
contact_name_col=2
contact_email_col=3
contact_star_col=4
contact_phonenum_col=5
contact_comment_col=6
contact_keyword_col=7
contact_if_execute_col=8
contact_testtime_col=9
contact_testresult_col=10


if __name__=="__main__":
    print(PROJECT_PATH)
    print(CONFIG_PATH)
    print(PageElementLocator_path)
    print(LOG_PATH)
    print(Loggerconf_path)