from Utils.ConfigParser import *
from Utils.ObjectMap import *
from Config.ProjectVar import *
from PageObject.loginPage import *
import time




class homePage():

    def __init__(self,driver):
        self.driver=driver

    def tapNewContactTab(self):
        newcontactlink=getOption(PageElementLocator_path,"126_homePage","homePage.addressBookTab")
        newcontactbutton=findElement(self.driver,newcontactlink.split(">")[0],newcontactlink.split(">")[1])
        newcontactbutton.click()
        time.sleep(3)


if __name__=="__main__":
    driver = webdriver.Chrome(executable_path="d:\\chromedriverold")
    loginPage(driver).visitWebsit("https://www.126.com/")
    loginPage(driver).switchToFrame()
    loginPage(driver).inputUsername("wwwww")
    loginPage(driver).inputPasswd("1233")
    loginPage(driver).login()
    homePage(driver).tapNewContactTab()