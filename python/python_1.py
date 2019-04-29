def script():
    grade_one={'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}
    grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}
    grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}
    a=list(grade_one.keys())
    b=list(grade_two.keys())
    c=list(grade_three.keys())
#print(len(grade_one))

#func1:
    def students_names(grade):
     if grade =='grade_one':
         print(a)
     elif grade =='grade_two':
         print(b)
     elif grade == 'grade_three':
         print(c)

#func2:
    def student_score(grade,student_name):
     if grade =='grade_one':
         lst=grade_one.get('student_name')
         print(sum(lst))
     elif grade =='grade_two':
         lst=grade_two.get('student_name')
         print(sum(lst))
     elif grade == 'grade_three':
         lst=grade_three.get('student_name')
         print(sum(lst))

#func3:
    def students_count(grade):
     if grade =='grade_one':
         print(len('grade_one'))
     elif grade =='grade_two':
         print(len('grade_two'))
     elif grade == 'grade_three':
         print(len('grade_three'))
#start script
     function=input('Choose one: students_names, student_score, students_count ' )
     if function =="students_names":
         Grade_num=input('choose Grade:  ')
         students_names(Grade_num)
     elif function =='students_count':
         Grade_num =input('choose Grade:  ')
         students_count(Grade_num)
     elif function =='student_score':
         grade=input("choose Grade: ")
         name=input("student_name: ")
         student_score(grade,name)
     else:
         print("not found")
     restart=input('enter done to exit or more to continue :')
     if restart =="more":
         script()
     else:
         exit()
script()
