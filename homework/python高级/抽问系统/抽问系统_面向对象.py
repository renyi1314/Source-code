import random
import datetime


# 提问的数目

class ChoiceStudentQuestion:

    def __init__(self):
        self.questions = []
        self.students = []
        self.num_questions = 5

    def get_students(self):
        with open("student.txt", mode="r", encoding="utf-8") as f:
            self.students = [item.strip().strip("\n") for item in f.readlines()]
            while '' in self.students:
                self.students.remove('')
            return self.students

    def random_students(self):
        return random.choice(self.students)

    def get_questions(self):
        i = 0
        while True:
            try:
                with open((str(datetime.date.today() + datetime.timedelta(days=i)) + ".txt"), mode="r",
                          encoding="utf-8") as f:
                    question = [item.strip().strip("\n") for item in f.readlines()]
            except FileNotFoundError:
                continue
            else:
                self.questions.extend(question)
                while '' in self.questions:
                    self.questions.remove('')
            finally:
                i -= 1
                if len(self.questions) > 10:
                    self.questions = self.questions[0:10]
                    break
                if i < -4:
                    break

        return self.questions

    def random_questions(self):
        res = random.choice(self.questions)
        self.questions.remove(res)
        return res

    def choice_student_questions(self):
        self.get_students()
        self.get_questions()
        for num in range(self.num_questions):
            input("---请按任意键抽取问题---")
            print(self.random_questions())
            input("---请按任意键选择学生---")
            print(self.random_students())


a = ChoiceStudentQuestion()
a.choice_student_questions()
