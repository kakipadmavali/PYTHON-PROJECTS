students= []
name=input("enter student name")
marks=int(input("enter student marks"))
if marks>=35:
       result="pass"
else:
        result="fail"  
student=[name,marks,result] 
students.append(student)
print(students)      