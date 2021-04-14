#------------------------------------------------
# Syjer Asuncion
# Classes
# April 14, 2021
#------------------------------------------------

class student:
    num_of_stud = 0
    def __init__(self, first, last, grade):
        self.first = first
        self.last = last
        self.grade = grade

        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def av_grade(self):
        return self.grade

def main():
    print("""Options:
    -------------------
    1. All students
    2. Students average grade.
    3. Exit
    """)
    main_choice = input("Action: ")
    print()
    
    if main_choice == "1":
        stud_fullname()
        
    elif main_choice == "2":
        students_info()
        
    elif main_choice == "3":
        exit
        
    else:
        print("Error!")
        
def students_info():
    #to print all of their full names with their grades
    stud = 0
    num = 1

    for stud in range(0,5):
        name = print(num,".", "", all_stud[stud])
        stud += 1
        num += 1
    
    print()
    
    name_choice = input("Which student?")
    
    if name_choice == "1":
        print(stud_1.av_grade())
        
    elif name_choice == "2":
        print(stud_2.av_grade())
    
    elif name_choice == "3":
        print(stud_3.av_grade())
    
    elif name_choice == "4":
        print(stud_4.av_grade())
        
    elif name_choice == "5":
        print(stud_5.av_grade())
        
    else:
        print("Error!")
        
def stud_fullname():
#to print all of their full names
    stud = 0

    for stud in range(0,5):
        name = print(all_stud[stud])
        stud += 1
        
#----main program--------
#lists of students
stud_1 = student("Amy","Smith", 98)
stud_1n = stud_1.fullname()

stud_2 = student("Darren","Brown", 86)
stud_2n = stud_2.fullname()

stud_3 = student("Omen","Garcia", 92)
stud_3n = stud_3.fullname()

stud_4 = student("Gracie","Davis", 84)
stud_4n = stud_4.fullname()

stud_5 = student("Paula","Williams", 79)
stud_5n = stud_5.fullname()

all_stud = [stud_1n, stud_2n, stud_3n, stud_4n, stud_5n]

if __name__ == '__main__':
    main()
    


