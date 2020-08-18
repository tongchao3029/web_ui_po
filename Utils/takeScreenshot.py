from selenium import webdriver
from Utils.DateAndTime import *
import os
from Config.ProjectVar import *




def takeScreenshots(driver):
    filename=str(TimeUtil().get_chinesedatetime())+".png"
    driver.get_screenshot_as_file(os.path.join(LOG_PATH,filename))
    print("截图")



if __name__=="__main__":
    driver = webdriver.Chrome(executable_path="d:\\chromedriverold")
    driver.get("http://www.baidu.com")
    takeScreenshots(driver)