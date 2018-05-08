import random


def random_stu_score():
    stu_dict = {}
    stu_dict_gt_60 = {}
    for i in range(60):
        stu_name = "Name" + str(i + 1)
        score = random.randrange(40, 101)
        stu_dict[stu_name] = score
        if score > 60:
            stu_dict_gt_60[stu_name] = score
    return stu_dict, stu_dict_gt_60


if __name__ == '__main__':
    stu_all, stu_gt_60 = random_stu_score()
    print(stu_all)
    print(stu_gt_60)
