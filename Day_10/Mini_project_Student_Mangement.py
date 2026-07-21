data={}
def register():
    rollno=int(input("Enter rollno:"))
    name=input("Enter name:")
    age=int(input("Enter age:"))
    marks=0
    if rollno not in data:
        data[rollno]=[name,age,marks]
        print("Student registered successfully")
    else:
        print("Roll no already exist use another one ")    
def display():
    rollno=int(input("Enter the roll no:"))
    if rollno in data:
        print(f'Name->{data[rollno][0]}')
        print(f'Age->{data[rollno][1]}')
        print(f'Marks->{data[rollno][2]}')
    else:
        print("Student not exist")   
def search():
    rollno = int(input("Enter roll no: "))
    if rollno not in data:
        print("Student is not in Database")
    else:
        print("Student is in database")
def marks():
    rollno = int(input("Enter roll no: "))
    if rollno in data:
        marks = data[rollno][2]
        print(f"Marks of this student is {marks}")
    else:
        print("Student not found!")
def update():
    rollno = int(input("Enter roll no: "))
    if rollno in data:
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        marks = int(input("Enter new marks: "))
        data[rollno] = [name, age, marks]
        print("Student data updated successfully!")
    else:
        print("Student not found!")      
choice=1
while choice!=0:
    print("_______________Student Management System_____________")
    print("1.Register new student:")
    print("2.Display the data of student")
    print("3.Search the student")
    print("4.Enter the marks for student")
    print("5.Update the data of student")
    choice=int(input("Enter your choice : "))
    if (choice==1):
        register()
    elif (choice==2):
        display()
    elif (choice==3):
        search()
    elif(choice==4):
        marks()
    elif(choice==5):
        update()               
    
 