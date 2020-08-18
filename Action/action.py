from PageObject.addContactPage import *
from PageObject import loginPage,homePage,addContactPage
from selenium import webdriver

def login(username,password):
    driver = webdriver.Chrome(executable_path="d:\\chromedriverold")
    loginObj=loginPage.loginPage(driver)
    loginObj.visitWebsit("https://www.126.com/")
    loginObj.switchToFrame()
    loginObj.inputUsername(username)
    loginObj.inputPasswd(password)
    loginObj.login()
    return driver

def swithNewContactTab(driver):
    newContactTabObj=homePage.homePage(driver)
    newContactTabObj.tapNewContactTab()
    return driver

def addContactInfo(driver,name,email,flag,phonenum,comment):
    addContactObj=addContactPage.addContactPage(driver)
    addContactObj.tapAddContact()
    addContactObj.inputContactName(name)
    addContactObj.inputContactEmail(email)
    addContactObj.markStar(flag)
    addContactObj.inputContactPhoneNum(phonenum)
    addContactObj.inputContactComment(comment)
    addContactObj.tapSubmit()

if __name__=="__main__":
    driver=login("dddd","dddd")
    driver=swithNewContactTab(driver)
    addContactInfo(driver,"小娇","567891090@qq.com","n",18999999999,"我的朋友")