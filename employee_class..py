class Employee:
    id=0
    name=""
    gender=""
    city=""
    salary=0
	
    def setData(self,id,name,gender,city,salary):
        self.id=id
        self.name = name
        self.gender = gender
        self.city = city
        self.salary = salary
	
    def showData(self):
        print("Id\t\t:",self.id)
        print("Name\t:", self.name)
        print("Gender\t:", self.gender)
        print("City\t:", self.city)
        print("Salary\t:", self.salary)

def main():
    emp=Employee()
    id=input('enter id:')
    name=input('enter name :')
    gender=input('enter gender:')
    city=input('enter city:')
    salary=input('enter salary:')
    emp.setData(id,name,gender,city,salary)
    emp.showData()
	
if __name__=="__main__":
    main()
