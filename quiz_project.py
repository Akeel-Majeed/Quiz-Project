#---------------------------Quiz.py--------------------------------------------#
#by Akeel Majeed

#Question class
class Question:
    def __init__(self, questions, answers, options, opt_answers):
        self.questions = questions
        self.answers = answers
        self.options = options
        self.opt_answers = opt_answers

    def question_printer(self):
        score = 0
        question_no = 0
        while question_no < len(self.questions):
            for questions_no in self.questions:
                user_answer = input("{}) {}\nYour answer: ".format(question_no + 1, self.questions[question_no]))
                if user_answer == self.answers[question_no]:
                    print("Well done!\n")
                    question_no += 1
                    score += 1
                else:
                    print("Unlucky. the correct answer is {}\n".format(self.answers[question_no]))
                    question_no += 1
                    score -= 1
            print("this is the end of the quiz thanks for participating! your score is {}".format(score))

#Option class
class Option(Question):
    def opt_question_printer(self):
        score = 0
        question_no = 0
        while question_no < len(self.questions):
            for questions_no in self.questions:
                user_answer = input("{}) {}\n{}\nYour answer: ".format(question_no + 1, self.questions[question_no], self.options[question_no]))
                if user_answer == self.opt_answers[question_no]:
                    print("Well done!\n")
                    question_no += 1
                    score += 1
                else:
                    print("Unlucky. the correct answer is {}\n".format(self.opt_answers[question_no]))
                    question_no += 1
                    score -= 1
            print("this is the end of the quiz thanks for participating! your score is {}".format(score))

quiz = Option(["30 - 4 + 23 = ?", "6 x 9 + 6 + 9 = ?", "What is pi to 3 significant figures?", "tan(45) = ?", "what is the cube root of 27", "Add the appropiate operations to make this correct:\n0 0 0 = 6"], ["49", "69", "3.14", "1*", "3", "(0! + 0! + 0!)! = 6"], ["\n(a) Tony Blair\n(b) 26\n(c) 49", "\n(a) 69\n(b) Tekashi\n(c) 420", "\n(a) 3.13\n(b) 3.14\n(c) 3.17", "\n(a) 69*\n(b) 1*\n(c) 45*", "\n(a)3\n(b) 4\n(c) 5", "\n(a) 0! + 0! + 0! = 6\n(b) sqrt of 0! + 0! + 0! = 6\n(c) (0! + 0! + 0!)! = 6 "], ["c", "a", "b", "b", "a", "c"] )

print("Welcome to the quiz!\nCorrect answers win you a point!\nBe careful, as incorrect answers lose you a point!\n")

easy_hard = input("would you like to have a multiple choices to help you?\n").lower()

if easy_hard == "yes":
    quiz.opt_question_printer()
else:
    quiz.question_printer()
