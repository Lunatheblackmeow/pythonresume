class certsearch:
    def __init__(self,course,year,school):
        self.course = course
        self.year = year
        self.school = school

    def getcertname(self):
        return self.course
    
    def getcertyear(self):
        return self.year

    def getcertschool(self):
        return self.school