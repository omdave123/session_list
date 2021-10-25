

class students :

    def _init_(self,name,rollno,age):
        self.name = name
        self.rollno = rollno
        self.age = age


        def create(self,name,rollno,age):
            ob = student(name,rollno,age)
            is.append(ob)


            def display(self,ob):
                print("name: ",ob.name)
                print("rollno: ",ob.rollno)
                print("age: ",ob.age)


is = []


obj = student(" ",0,0)

print("opeartions used. . . .\n")
print("1.add the students details \n2.displlay the student details\n3.exit")

obj.create("om",1,10)
obj.create("pal",2,9)


print("\n")
print("list of students details")
for i in range(is.len()):
    obj.display(is[i])


print("data added successfully....")
