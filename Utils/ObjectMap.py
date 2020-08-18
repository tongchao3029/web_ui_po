from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,TimeoutException



def findElement(driver,locateMethod,locateExp):
    try:
        element=WebDriverWait(driver,10).until(lambda x:x.find_element(locateMethod,locateExp))
        return element
    except NoSuchElementException as e:
        raise e
    except TimeoutException as e:
        raise e


def findElements(driver,locateMethod,locateExp):
    try:
        elements=WebDriverWait(driver,10).until(lambda x:x.find_elements(locateMethod,locateExp))
        return elements
    except NoSuchElementException as e:
        raise e
    except TimeoutException as e:
        raise e



if __name__=="__main__":
    driver=webdriver.Chrome(executable_path="d:\\chromedriverold")
    driver.get("http://www.baidu.com")
    #findElement(driver,"id", "kw").send_keys("高考")
    elements=findElements(driver,"xpath", "//input")
    print(len(elements))