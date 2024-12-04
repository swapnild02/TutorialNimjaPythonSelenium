from configparser import ConfigParser

def read_configuration(category,key):
    config= ConfigParser()
    config.read("D:\SeleniumPythonHybridFramework\configuration\configs.ini")
    key_value=config.get(category,key)
    return key_value