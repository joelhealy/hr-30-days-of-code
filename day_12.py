#  HackerRank: 30 Days of Code - Day 12: Inheritance
#  
#  Task
#  
#  You are given two classes, Person and Student, where Person is the base
#  class and Student is the derived class. Completed code for Person and a
#  declaration for Student are provided for you in the editor. Observe that
#  Student inherits all the properties of Person.
#  
#  Complete the Student class by writing the following:
#  
#      A Student class constructor, which has 4 parameters: A string,
#      firstName.  A string, lastName.  An integer, id.  An integer array
#      (or vector) of test scores, scores.
#  
#      A char calculate() method that calculates a Student object's average
#      and returns the grade character representative of their calculated
#      average:
#  
#              Grading Scale
#              
#              O   90 <= a <= 100 
#              E   80 <= a <   90 
#              A   70 <= a <   80 
#              P   55 <= a <   70 
#              D   40 <= a <   55 
#              T         a <   40
#  
#  Input Format
#  
#  The first line contains firstName, lastName, and id, respectively. The
#  second line contains the number of test scores. The third line of
#  space-separated integers describes scores.


class Person:


    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber


    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        avg = sum(self.scores) / len(scores)  
        if avg >= 90:
            return 'O'
        elif avg >= 80:
            return 'E'
        elif avg >= 70:
            return 'A'
        elif avg >= 55:
            return 'P'
        elif avg >= 40:
            return 'D'
        else:
            return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numscores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

