import pandas as pd


class BaseTable(object):
    # 用作完整data操作的表
    tempTables = dict()
    # 用作value操作的表
    tempTablesValues = dict()
    # 持续化的表
    lastingTables = dict()

    @classmethod
    def concat(cls, table, model):
        # 将临时表的数据整合到永续表里
        if model == "append":
            if table not in cls.lastingTables.keys():
                cls.lastingTables[table] = cls.tempTables[table]
            else:
                cls.lastingTables[table] = pd.concat([cls.lastingTables[table], cls.tempTables[table]], axis=0,
                                                     join="outer",
                                                     ignore_index=True, sort=False)
        elif model == "update":
            cls.lastingTables[table] = cls.tempTables[table]
        del cls.tempTables[table]

    @classmethod
    def basicDataOpe(cls, data, model):
        # 获取table名字
        table = data.get("table")
        # 没有table则新建
        if table not in cls.tempTables.keys():
            cls.tempTables[table] = pd.DataFrame()
        del data["table"]
        for k, v in data.items():
            cls.tempTables[table][k] = [v]
        cls.concat(table, model=model)

    @classmethod
    def appendData(cls, data):
        cls.basicDataOpe(data, model="append")

    @classmethod
    def updataData(cls, data):
        cls.basicDataOpe(data, model="update")

    @classmethod
    def multiAppendData(cls, data):
        pass

    @classmethod
    def basicValueOpe(cls, table, key, value, model):
        if table not in cls.tempTablesValues.keys():
            cls.tempTablesValues[table] = pd.DataFrame()
        cls.tempTablesValues[table][key] = [value]
        cls.tempTablesValues[table]["DataModelsIfNoPersonUseTHkey"] = model

    @classmethod
    def appendValue(cls, table, key, value):
        cls.basicValueOpe(table, key, value, "append")

    @classmethod
    def updateValue(cls, table, key, value):
        cls.basicValueOpe(table, key, value, "update")

    @classmethod
    def multiUpdateValue(cls):
        pass

    @classmethod
    def push(cls):
        for table in cls.tempTablesValues.keys():
            if list(cls.tempTablesValues[table]["DataModelsIfNoPersonUseTHkey"].values)[0] == "append":
                del cls.tempTablesValues[table]["DataModelsIfNoPersonUseTHkey"]
                if table not in cls.lastingTables.keys():
                    cls.lastingTables[table] = cls.tempTablesValues[table]
                else:
                    cls.lastingTables[table] = pd.concat([cls.lastingTables[table], cls.tempTablesValues[table]],
                                                         axis=0,
                                                         join="outer",
                                                         ignore_index=True, sort=False)
            elif list(cls.tempTablesValues[table]["DataModelsIfNoPersonUseTHkey"].values)[0] == "update":
                del cls.tempTablesValues[table]["DataModelsIfNoPersonUseTHkey"]
                cls.lastingTables[table] = cls.tempTablesValues[table]
        cls.tempTablesValues = dict()

    @classmethod
    def query(cls, table):
        keys = cls.lastingTables[table].columns.values.tolist()
        values = cls.lastingTables[table].values.tolist()
        runStatusTable = {"type": "table", "title": table, "cols": keys, "rows": values}
        return runStatusTable


if __name__ == '__main__':
    BaseTable.appendData({"table": "运行状态", "name": "dsb", "age": 22, "sex": "man"})
    print(BaseTable.query("运行状态"))
    BaseTable.appendData({"table": "运行状态", "name": "hh", "age": 26, "sex": "girl"})
    print(BaseTable.query("运行状态"))
    BaseTable.appendData({"table": "运行状态", "name": "xx", "age": 43, "sex": "girl", "height": 190})
    print(BaseTable.query("运行状态"))
    BaseTable.updataData({"table": "运行状态", "name": "hjt", "age": 21, "sex": "boy"})
    print(BaseTable.query("运行状态"))
    BaseTable.appendValue("运行状态", "height", "hmp")
    BaseTable.appendValue("运行状态", "tww", 50)
    BaseTable.push()
    print(BaseTable.query("运行状态"))
