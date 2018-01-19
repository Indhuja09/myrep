class Student():

    def __init__ (self, name="Joe", surname="Smith", studentnumber=3245, course="Maths"):
        self.name = name
        self.surname = surname
        self.studentnum = studentnumber
        self.course = course

    def showDetails(self):
        print(self.name, self.surname, self.studentnum, self.course)



from Student import *

s0 = Student() # default object
s1 = Student("Joe","Smith", 3245, "Maths")
s2 = Student("Laura","Jones", 3445, "English Literature")
s3 = Student("Rebecca","Foley", 3655, "Civil engineering")
