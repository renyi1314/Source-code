class ConfigurationFileError(Exception):


    def __str__(self):
        return "配置文件错误!!!"


try:
    print("hello,world")
    raise  ConfigurationFileError()
except ConfigurationFileError:
    print("我捕捉到了错误")

