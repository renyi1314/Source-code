# import re
#
# a = """SELECT t3.id, t3. NAME, t3.plan_start, t3.plan_end, t3.exec_value, t4.exec_value, t3.commit, t3.batch_alias FROM ( SELECT t2.id, t2. NAME, t2.plan_start, t2.plan_end, t2.batch_alias, t1.exec_value, t1.exec_status, t1.exception_msg, t1.commit FROM batch_log t1 JOIN batch_task t2 ON t1.batch_id = t2.id AND t2.type = {type} AND t1.create_time > "{startTime}" AND t1.create_time < "{endTime}" AND ( t1.exec_status = "0" OR t1.exec_status = "1" ) ) t3 JOIN ( SELECT t2. NAME, t2.plan_start, t2.plan_end, t1.exec_value, t1.exec_status, t1.exception_msg FROM batch_log t1 JOIN batch_task t2 ON t1.batch_id = t2.id AND t2.type = {type} AND t1.create_time > "{startTime}" AND t1.create_time < "{endTime}" AND (t1.exec_status = "0"OR t1.exec_status = "1" ) ) t4 ON t3. NAME = t4. NAME AND t3.exec_status = 1 AND t4.exec_status = 0 ORDER BY id"""
#
# print(re.sub('[\n]+', '', a))
# b = re.sub('[\n]+', '', a)
# c = re.sub('[ ]+', ' ', b)
# print(re.sub('[\t]+', ' ', c))
# # print(a.replace("\n", ""))


def a(name):
    return name


print("666" + a("six"))
