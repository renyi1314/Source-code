import random
import datetime

# 提问的数目
num_questions = 5


def get_config():
    with open("systemconfig2", "r", encoding="utf-8") as f:
        dict_settings = {key.split("=")[0]: key.split("=")[1].strip("\" \n") for key in f if not key.startswith("#")}

def get_students():
    with open("student.txt", mode="r", encoding="utf-8") as f:
        students = [item.strip(" \n") for item in f if item.strip("\n")]
        return students


def random_students(students_list):
    return random.choice(students_list)


def get_questions():
    questions = []
    i = 0
    while True:
        try:
            with open((str(datetime.date.today() + datetime.timedelta(days=i)) + ".txt"), mode="r",
                      encoding="utf-8") as f:
                question = [item.strip(" \n") for item in f.readlines() if item.strip(" \n")]
        except FileNotFoundError:
            continue
        else:
            questions.extend(question)
        finally:
            i -= 1
            if len(questions) > 10:
                questions = questions[0:10]
                break
            if i < -4:
                break

    return questions


def random_questions(questions_list):
    res = random.choice(questions_list)
    questions_list.remove(res)
    return res


def choice_student_questions(num):
    students = get_students()
    questions = get_questions()
    for num in range(num):
        input("---请按任意键抽取问题---")
        print(random_questions(questions))
        input("---请按任意键选择学生---")
        print(random_students(students))


choice_student_questions(num_questions)
