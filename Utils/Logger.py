from Config.ProjectVar import *
import logging.config



def getLogger():
    logging.config.fileConfig(Loggerconf_path)
    logger=logging.getLogger("mylogger01")
    return logger



print(Loggerconf_path)
