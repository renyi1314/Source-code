import pandas as pd


class BaseTable(object):
    # 用作value操作的表
    tempTablesValues = dict()
    # 持续化的表
    lastingTables = dict()

    @classmethod
    def basicValueOpe(cls, table, key, value, model):
        if table not in cls.tempTablesValues.keys():
            cls.tempTablesValues[table] = dict()
            cls.tempTablesValues[table]["data"] = pd.DataFrame()
        cls.tempTablesValues[table]["data"][key] = [value]
        cls.tempTablesValues[table]["dataOperateModel"] = model

    @classmethod
    def appendValue(cls, table, key, value):
        cls.basicValueOpe(table, key, value, "append")

    @classmethod
    def updateValue(cls, table, key, value):
        cls.basicValueOpe(table, key, value, "update")

    @classmethod
    def basicDataOpe(cls, tableName, data, model):
        # 添加数据到临时表里
        for k, v in data.items():
            cls.basicValueOpe(tableName, k, v, model)

    @classmethod
    def appendData(cls, tableName, data):
        cls.basicDataOpe(tableName, data, model="append")

    @classmethod
    def updataData(cls, tableName, data):
        cls.basicDataOpe(tableName, data, model="update")

    @classmethod
    def multiUpdateValue(cls):
        pass

    @classmethod
    def push(cls):
        for table in cls.tempTablesValues.keys():
            if cls.tempTablesValues[table]["dataOperateModel"] == "append":
                if table not in cls.lastingTables.keys():
                    cls.lastingTables[table] = dict()
                    cls.lastingTables[table]["data"] = pd.DataFrame()
                cls.lastingTables[table]["data"] = pd.concat(
                    [cls.tempTablesValues[table]["data"], cls.lastingTables[table]["data"]],
                    axis=0,
                    join="outer",
                    ignore_index=True,
                    sort=False
                )
            if cls.tempTablesValues[table]["dataOperateModel"] == "update":
                cls.lastingTables[table] = cls.tempTablesValues[table]
        cls.tempTablesValues = dict()

    @classmethod
    def query(cls, table):
        keys = cls.lastingTables[table]["data"].columns.values.tolist()
        values = cls.lastingTables[table]["data"].values.tolist()
        runStatusTable = {"type": "table", "title": table, "cols": keys, "rows": values}
        return runStatusTable

    @classmethod
    def queryAll(cls):
        allData = []
        for key in cls.lastingTables.keys():
            data = cls.query(key)
            allData.append(data)
        return allData


if __name__ == '__main__':
    BaseTable.appendData("运行状态", {"name": "dsb", "age": 22, "sex": "man"})
    BaseTable.push()
    print(BaseTable.query("运行状态"))
    BaseTable.appendData("运行状态", {"name": "hh", "age": 26, "sex": "girl"})
    BaseTable.push()
    print(BaseTable.query("运行状态"))
    BaseTable.appendData("运行状态", {"name": "xx", "age": 43, "sex": "girl", "height": 190})
    BaseTable.push()
    print(BaseTable.query("运行状态"))
    BaseTable.appendData("运行状态", {"name": "hjt", "age": 99, "sex": "boy"})
    BaseTable.push()
    print("------------------")
    print(BaseTable.query("运行状态"))
    BaseTable.appendValue("运行状态", "height", "230")
    BaseTable.appendValue("运行状态", "tww", 50)
    BaseTable.appendValue("运行状态", "age", 99999)
    BaseTable.push()
    print(BaseTable.query("运行状态"))
    BaseTable.updateValue("运行状态", "spider", 99999)
    BaseTable.push()
    print(BaseTable.query("运行状态"))
    BaseTable.appendValue("运行状态2", "age", 99999)
    BaseTable.push()
    print(BaseTable.queryAll())
