import random
import datetime


class GetConfig:
    with open("systemconfig2", "r", encoding="utf-8") as f:
        dict_settings = {key.split("=")[0]: key.split("=")[1].strip("\" \n") for key in f if not key.startswith("#")}
    num_student = int(dict_settings["num_student"])
    max_questions = int(dict_settings["max_questions"])
    max_deep_file = int(dict_settings["max_deep_file"])


class Students:
    def __init__(self):
        self.students = []

    def get_students(self):
        with open("student.txt", mode="r", encoding="utf-8") as f:
            self.students = [item.strip("\n") for item in f if item.strip("\n")]
            return self.students


class Questions:
    def __init__(self):
        self.questions = []
        self.max_questions = GetConfig.max_questions
        self.max_deep_file = GetConfig.max_deep_file

    def get_questions(self):
        i = 0
        while True:
            try:
                with open((str(datetime.date.today() + datetime.timedelta(days=i)) + ".txt"), mode="r",
                          encoding="utf-8") as f:
                    question = [item.strip(" \n") for item in f if item.strip(" \n")]
            except FileNotFoundError:
                continue
            else:
                self.questions.extend(question)
            finally:
                i -= 1
                if len(self.questions) > self.max_questions:
                    self.questions = self.questions[0:self.max_questions]
                    break
                if i < -(self.max_deep_file - 1):
                    break

        return self.questions


class ChoiceStudentQuestion:

    def __init__(self):
        self.num_questions = GetConfig.num_student

    @staticmethod
    def random_students(students):
        return random.choice(students)

    @staticmethod
    def random_questions(questions):
        res = random.choice(questions)
        questions.remove(res)
        return res

    def choice_student_questions(self, questions, students):
        for num in range(self.num_questions):
            input("---请按回车键抽取问题---")
            print(self.random_questions(questions))
            input("---请按回车键选择学生---")
            print(self.random_students(students))


a = Students()
students_ydm = a.get_students()
b = Questions()
questions_ydm = b.get_questions()
choice = ChoiceStudentQuestion()
choice.choice_student_questions(questions_ydm, students_ydm)
