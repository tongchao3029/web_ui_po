from configparser import ConfigParser
import os

def getSections(configFilePath):
    if not (os.path.exists(configFilePath) and os.path.basename(configFilePath).endswith(".ini")):
        print("输入的配置文件路径不存在或者文件不是.ini")
        return
    cp=ConfigParser()
    cp.read(configFilePath)
    return cp.sections()

def getOptionsOfSection(configFilePath,sectionName):
    if not (os.path.exists(configFilePath) and os.path.basename(configFilePath).endswith(".ini")):
        print("输入的配置文件路径不存在或者文件不是.ini")
        return
    cp=ConfigParser()
    cp.read(configFilePath)
    return cp.options(sectionName)

def getOption(configFilePath,sectionName,optionName):
    if not (os.path.exists(configFilePath) and os.path.basename(configFilePath).endswith(".ini")):
        print("输入的配置文件路径不存在或者文件不是.ini")
        return
    cp=ConfigParser()
    try:
        cp.read(configFilePath)
        value=cp.get(sectionName,optionName)
    except Exception as e:
        print("输入的sectionName或者optionName有误：%s"%e)
        return
    return value


if __name__=="__main__":
    print(getOption(r"D:\pydelete\0704\my.ini","dbinfo","dbname"))
    print(getSections(r"D:\pydelete\0704\my.ini"))
    print(getOptionsOfSection(r"D:\pydelete\0704\my.ini","web"))