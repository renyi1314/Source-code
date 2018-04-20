import random
import datetime


class Students:
    def __init__(self):
        self.students = []

    def get_students(self):
        with open("student.txt", mode="r", encoding="utf-8") as f:
            self.students = [item.strip().strip("\n") for item in f.readlines()]
            while '' in self.students:
                self.students.remove('')
            return self.students


class Questions:
    def __init__(self):
        self.questions = []

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


class ChoiceStudentQuestion:

    def __init__(self):
        self.num_questions = 5

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
            input("---请按任意键抽取问题---")
            print(self.random_questions(questions))
            input("---请按任意键选择学生---")
            print(self.random_students(students))


a = Students()
students_ydm = a.get_students()
b = Questions()
questions_ydm = b.get_questions()
choice = ChoiceStudentQuestion()
choice.choice_student_questions(questions_ydm, students_ydm)
