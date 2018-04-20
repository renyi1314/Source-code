import random
import datetime

# 提问的数目
num_questions = 5


def get_students():
    with open("student.txt", mode="r", encoding="utf-8") as f:
        students = [item.strip().strip("\n") for item in f.readlines()]
        while '' in students:
            students.remove('')
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
                question = [item.strip().strip("\n") for item in f.readlines()]
        except FileNotFoundError:
            continue
        else:
            questions.extend(question)
            while '' in questions:
                questions.remove('')
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
