from configparser import ConfigParser


def getConfigByKey(key):
    #初始化类
    cp = ConfigParser()
    cp.read("../resources/application.cfg")
    param = ""
    # 得到所有的section，以列表的形式返回
    for section in cp.sections():
        try:
           param = cp.get(section, key)
        except Exception as e:
            # print("logger>>>>",section,"没有key为%s的值"%key)
            continue
        # 得到该section中的option的值，返回为string类型
        # print(cp.get(section, "db"))
        # 得到该section中的option的值，返回为int类型
        # print(cp.getint(section, "port"))
    return param


