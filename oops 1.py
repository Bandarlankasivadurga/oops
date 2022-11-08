class student:
    def __init__(self,name,marks=0,subject='null'):
        self.name=name
        self.marks=marks
        self.subject=subject
    def display(self):
        print(self.name,self.marks,self.subject)

s1=student('chandu',99,'maths')
s1.display()
s2=student('virat',87)
s2.display()
