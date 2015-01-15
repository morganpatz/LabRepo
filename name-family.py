class Student:
    courseMarks = {}
    name=""
    def __init__(self, name, family):
        self.name = name
        self.family = family
        
    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark
        
    def average(self):
        summ = 0
        count = 0
        for name, mark in self.courseMarks.items():
            summ = summ + mark
            count = count + 1
        return summ/count
        
        
s = Student("Morgan", "Patzelt")
s.courseMarks["CMPUT410"] = 4.0
s.courseMarks["MATH222"] = 3.3
s.courseMarks["CMPUT401"] = 3.0
s.courseMarks["STS200"] = 3.7
s.addCourseMark("CMPUT302", 4.0)
avg = s.average()
print(avg)    
            
        
        
        
        