import random

random_num_list = [random.randrange(-30, 31) for i in range(15)]
random_num_gt_60_list = [i for i in random_num_list if i > 0]
stu_score_all = {"name" + str(j): random.randrange(40, 101) for j in range(1, 61)}
stu_score_gt_60 = {k: v for k, v in stu_score_all.items() if v > 60}
print(random_num_list)
print(random_num_gt_60_list)
print(sorted(random_num_gt_60_list))
print(stu_score_all)
print(stu_score_gt_60)
