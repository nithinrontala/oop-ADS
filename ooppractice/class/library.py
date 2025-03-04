class Card:
    def __init__(self, title, author, subject):
        self.title = title
        self.author = author
        self.subject = subject

    def getTitle(self):
        return self.title

class cardCatalog:
    def __init__(self):
        self.a = []

    def addCard(self, title, author, sub):
        c = Card(title, author, sub)
        self.a.append(c)
        return f"sucess"

    def getTitle(self,title):
        l = []
        # print(self.a)
        for i in self.a:
            if title == i.title:
                return i.title
                

    def getAuthor(self,author):
        aut = []
        # print("hi")
        for i in self.a:
            if author == i.author:
                aut.append(i.title)
        return aut

    def getSubject(self,sub):
        sub = []
        for i in self.a:
            if sub == i.subject:
                sub.append(i.subject)
        return sub

    def removeTitle(self,title):
        for i in self.a:
            if i.title == title:
                self.a.remove(i.title)
        return self.a

    def printCatalog(self):
        for i in self.a:
            print(f"title: {i.getTitle()}, author: {i.author}, sub: {i.subject}")

    
def runCatalog():
        c = cardCatalog()
        while True:
            try:
                s = input().split()
                # print(s[2])
                if s[0] == "add":
                    # print(s[2])
                    print(c.addCard(s[1],s[2],s[3]))
                elif s[0] == "display":
                    c.printCatalog()
                elif s[0] == "gettitle":
                    print(c.getTitle(s[1]))
                elif s[0] == "getaut":
                    print(c.getAuthor(s[1]))
                elif s[0] == "getsub":
                    print(c.getSubject(s[1]))
                elif s[0] == "remove":
                    print(c.removeTitle(s[1]))
            except:
                break

if __name__ == "__main__":
    runCatalog()