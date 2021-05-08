class Student(object):
    def __init__(self, name, age, gender, grade) :
        self.name = name
        self.age = age
        self.gender = gender
        self.grade = grade
    
student01 = Student("john",35,"Male",5)
student02 = Student("Dundubi",11,"Female",6)
student03 = Student("Shruthi",37,"Female",12)
student04 = Student("Shravya",6,"Female",1)
print(student01.name,student02.name, student03.name, student04.name)
#print(student02.name,student02.age,student02.gender,student02.grade)