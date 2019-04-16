import pandas as pd


class BaseTable(object):
    # 用作value操作的表
    tempTables = dict()
    # 持续化的表
    lastingTables = dict()

    @classmethod
    def basicValueOpe(cls, tableName, key, value):
        if tableName not in cls.tempTables.keys():
            cls.tempTables[tableName] = dict()
            cls.tempTables[tableName]["data"] = pd.DataFrame()
        cls.tempTables[tableName]["data"][key] = [value]

    @classmethod
    def appendValue(cls, tableName, key, value):
        cls.basicValueOpe(tableName, key, value)

    @classmethod
    def basicDataOpe(cls, tableName, data):
        # 添加数据到临时表里
        for k, v in data.items():
            cls.basicValueOpe(tableName, k, v)

    @classmethod
    def appendData(cls, tableName, data):
        cls.basicDataOpe(tableName, data)

    @classmethod
    def cleanAll(cls):
        cls.lastingTables = dict()
        cls.tempTables = dict()

    @classmethod
    def cleanOneTable(cls, tableName):
        if cls.lastingTables.get(tableName) is not None:
            del cls.lastingTables[tableName]
        if cls.tempTables.get(tableName) is not None:
            del cls.tempTables[tableName]

    @classmethod
    def clean(cls, tableName=None):
        if tableName is None:
            cls.cleanAll()
        else:
            cls.cleanOneTable(tableName)

    @classmethod
    def pushAll(cls):
        for tempTableName in list(cls.tempTables.keys()):
            cls.pushOneTable(tempTableName)

    @classmethod
    def pushOneTable(cls, tableName):
        if tableName not in cls.lastingTables.keys():
            cls.lastingTables[tableName] = dict()
            cls.lastingTables[tableName]["data"] = pd.DataFrame()
        cls.lastingTables[tableName]["data"] = pd.concat(
            [cls.tempTables[tableName]["data"], cls.lastingTables[tableName]["data"]],
            axis=0,
            join="outer",
            ignore_index=True,
            sort=False
        )
        del cls.tempTables[tableName]

    @classmethod
    def push(cls, tableName=None):
        if tableName is None:
            cls.pushAll()
        else:
            cls.pushOneTable(tableName)

    @classmethod
    def queryAll(cls):
        allData = []
        for key in cls.lastingTables.keys():
            data = cls.query(key)
            allData.append(data)
        return allData

    @classmethod
    def queryOneTable(cls, tableName):
        keys = cls.lastingTables[tableName]["data"].columns.values.tolist()
        values = cls.lastingTables[tableName]["data"].values.tolist()
        runStatusTable = {"type": "table", "title": tableName, "cols": keys, "rows": values}
        return runStatusTable

    @classmethod
    def query(cls, tableName=None):
        if tableName is None:
            return cls.queryAll()
        else:
            return cls.queryOneTable(tableName)


if __name__ == '__main__':
    BaseTable.appendData("运行状态", {"name": "dsb", "age": 22, "sex": "man"})
    BaseTable.push("运行状态")
    print(BaseTable.query("运行状态"))
    BaseTable.appendData("运行状态", {"name": "hh", "age": 26, "sex": "girl"})
    BaseTable.push()
    print(BaseTable.query("运行状态"))
    BaseTable.appendData("运行状态", {"name": "xx", "age": 43, "sex": "girl", "height": 190})
    BaseTable.push()
    print(BaseTable.query("运行状态"))
    print("测试运行状态增加新值----------------")
    BaseTable.appendData("运行状态", {"name": "hjt", "age": 99, "sex": "boy"})
    BaseTable.push()
    print(BaseTable.query("运行状态"))
    print("测试appendValue-------------------")
    BaseTable.appendValue("运行状态", "height", "230")
    BaseTable.appendValue("运行状态", "tww", 50)
    BaseTable.appendValue("运行状态", "age", 91239)
    BaseTable.push()
    print(BaseTable.query("运行状态"))
    print("测试push空数据----------")
    BaseTable.push()
    print(BaseTable.query("运行状态"))
    print("测试增加新表value--------------")
    BaseTable.appendValue("运行状态2", "age", 99999)
    BaseTable.push()
    print(BaseTable.queryAll())
    print("测试清空表运行状态2------------")
    BaseTable.clean("运行状态2")
    print(BaseTable.queryAll())
    BaseTable.clean()
    print(BaseTable.queryAll())
