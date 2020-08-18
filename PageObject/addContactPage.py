from Utils.ConfigParser import *
from Utils.ObjectMap import *
from Config.ProjectVar import *
from PageObject.loginPage import *
from PageObject.homePage import *
import time



class addContactPage():

    def __init__(self,driver):
        self.driver=driver

    def tapAddContact(self):
        add_contact_button=getOption(PageElementLocator_path,"126_addContactPage","addContactPage.createNewContactButton")
        button=findElement(self.driver,add_contact_button.split(">")[0],add_contact_button.split(">")[1])
        button.click()
        time.sleep(1)

    def inputContactName(self,contactname):
        input_box=getOption(PageElementLocator_path,"126_addContactPage","addContactPage.contactInfo.name")
        name_box=findElement(self.driver,input_box.split(">")[0],input_box.split(">")[1])
        name_box.send_keys(contactname)
        time.sleep(1)

    def inputContactEmail(self,contactemail):
        input_box=getOption(PageElementLocator_path,"126_addContactPage","addContactPage.contactInfo.email")
        emailbox=findElement(self.driver,input_box.split(">")[0],input_box.split(">")[1])
        emailbox.send_keys(contactemail)
        time.sleep(1)

    def markStar(self,flag=None):
        if flag==None or flag.lower()=="n" or flag.lower()=="no":
            return
        mark_star_box=getOption(PageElementLocator_path,"126_addContactPage","addContactPage.contactInfo.isStar")
        star_box=findElement(self.driver,mark_star_box.split(">")[0],mark_star_box.split(">")[1])
        star_box.click()
        time.sleep(1)


    def inputContactPhoneNum(self,phonenum):
        input_box=getOption(PageElementLocator_path,"126_addContactPage","addContactPage.contactInfo.phoneNumber")
        phone_box=findElement(self.driver,input_box.split(">")[0],input_box.split(">")[1])
        phone_box.send_keys(phonenum)
        time.sleep(1)

    def inputContactComment(self, comment):
        input_box = getOption(PageElementLocator_path, "126_addContactPage", "addContactPage.contactInfo.comments")
        comment_box = findElement(self.driver, input_box.split(">")[0], input_box.split(">")[1])
        comment_box.send_keys(comment)
        time.sleep(1)

    def tapSubmit(self):
        submit_box = getOption(PageElementLocator_path, "126_addContactPage", "addContactPage.contactInfo.submitButton")
        box = findElement(self.driver, submit_box.split(">")[0], submit_box.split(">")[1])
        box.click()
        time.sleep(1)

if __name__=="__main__":
    driver = webdriver.Chrome(executable_path="d:\\chromedriverold")
    loginPage(driver).visitWebsit("https://www.126.com/")
    loginPage(driver).switchToFrame()
    loginPage(driver).inputUsername("wwwww")
    loginPage(driver).inputPasswd("wwwwww")
    loginPage(driver).login()s
    homePage(driver).tapNewContactTab()
    addContactPage(driver).tapAddContact()
    addContactPage(driver).inputContactName("小米")
    addContactPage(driver).inputContactEmail("3233333@qq.com")
    addContactPage(driver).markStar("yes")
    addContactPage(driver).inputContactPhoneNum(15888888888)
    addContactPage(driver).inputContactComment("my best friend")
    addContactPage(driver).tapSubmit()