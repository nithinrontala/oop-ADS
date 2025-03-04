class Question:
    def __init__(self,questiontext,choices,corectoption,max_marks,penality):
        self.question_text = questiontext
        self.choice = choices
        self.correctoption = corectoption
        self.max_marks = max_marks
        self.penalty = penality
        self.userchoice = -1
        self.score = -1

    def evaluateAnswer(self):
        if self.userchoice == self.correctoption:
            # print(self.max_marks)
            return self.max_marks
        else:
            # print(self.penalty)
            return self.penalty * -1
    
class Quiz:
    def __init__(self):
        self.questions = []
        self.total_score = 0

    def parseQuestions(self,s):
        s = s.split("\n")
        for i in s:
            i = i.split(":")
            q = Question(i[0],i[1].split(","),int(i[2]),int(i[3]),int(i[4]))
            self.questions.append(q)

    def startQuiz(self,l):
        j = 0
        for i in self.questions:
            # print(i.question_text())
            i.userchoice = l[j]
            j+=1
            i.score = i.evaluateAnswer()
            self.total_score += i.score

    def scoreReport(self):
        print()
        print("Score Report:")
        for i in self.questions:
            print(f"Question: {i.question_text}")
            a = ", ".join(i.choice)
            print(f"Choices: {a}")
            print(f"Your Answer: {i.userchoice} | Correct Answer: {i.correctoption}")
            if i.userchoice == i.correctoption:
                print(f"Correct Answer! Marks Awarded: {i.max_marks}")
            else:
                print(f"Wrong Answer! Penalty Applied: {i.penalty}")
                # print(i.evaluateAnswer())
            print()
        print("Total Score:",self.total_score)