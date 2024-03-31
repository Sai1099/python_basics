class student:
    def __init__(self,name,rollno,age,gpa):
        self.name=name
        self.rollno=rollno
        self.age=age
        self.gpa=gpa
        
    def is_best(self):
            if(self.gpa >= 3.5):
                return True
            else:
                return False