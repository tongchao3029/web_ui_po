from Utils.ConfigParser import *
from Utils.ObjectMap import *
from Config.ProjectVar import *
import time



class loginPage():

    def __init__(self,driver):
        self.driver=driver

    def visitWebsit(self,url):
        self.driver.get(url)

    def switchToFrame(self):
        framelink=getOption(PageElementLocator_path,"126_login","loginPage.frame")
        frameObj=findElement(self.driver,framelink.split(">")[0],framelink.split(">")[1])
        self.driver.switch_to.frame(frameObj)

    def inputUsername(self,username):
        usernamelink=getOption(PageElementLocator_path,"126_login","loginPage.usernameBox")
        usernamebox=findElement(self.driver,usernamelink.split(">")[0],usernamelink.split(">")[1])
        usernamebox.send_keys(username)

    def inputPasswd(self,passwd):
        passwdlink = getOption(PageElementLocator_path, "126_login", "loginPage.passwdBox")
        passwdbox = findElement(self.driver, passwdlink.split(">")[0], passwdlink.split(">")[1])
        passwdbox.send_keys(passwd)

    def login(self):
        loginbuttonlink=getOption(PageElementLocator_path, "126_login", "loginPage.loginButton")
        loginbutton=findElement(self.driver,loginbuttonlink.split(">")[0],loginbuttonlink.split(">")[1])
        loginbutton.click()
        print("登录成功")


if __name__=="__main__":
    driver=webdriver.Chrome(executable_path="d:\\chromedriverold")
    loginPage(driver).visitWebsit("https://www.126.com/")
    loginPage(driver).switchToFrame()
    loginPage(driver).inputUsername("dddd666")
    loginPage(driver).inputPasswd("12333")
    loginPage(driver).login()


