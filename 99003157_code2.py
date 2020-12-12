import csv
employee_data = ['name', 'PS_No', 'Age', 'Contact']
employee_db = 'employee.csv'


class Employee_Data:
    def menu():
        print("1. New Employee")
        print("2. View Employee")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

    def new_employee():
        global employee_data
        global employee_db
        print("Enter the information")
        employee = []
        for data in employee_data:
            value = input("Enter" + data + ": ")
            employee.append(value)

        with open(employee_db, "a") as f:
            writer = csv.writer(f)
            writer.writerows([employee])

        print("Data has been entered")
        print("Press any key to continue")
        return
    
class Employee_Data2(Employee_Data):
    def view_employee():
        global employee_data
        global employee_db

        print("Employee records")
        with open(employee_db, "r") as f:
            reader = csv.reader(f)
            for x in employee_data:
                print(x, end="\t")

            for row in reader:
                for item in row:
                    print(item, end="\t")
                print("\n")
        input("Enter any key to continue")

    def search_employee():
        global employee_data
        global employee_db

        print("search employee")
        PS = input("Enter PS number of the employee")
        with open(employee_db, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0:
                    if PS == row[1]:
                        print("Data of Employee")
                        print("Name", row[0])
                        print("PS No", row[1])
                        print("Age", row[2])
                        print("Contat", row[3])
                        break
                else:
                    print("Data not found")
        input("Enter any key to continue")

    def update_employee():
        global employee_data
        global employee_db

        print("Update Employee data")
        PS = input("Enter PD number of the employee")
        index_employee = None
        updated_data = []
        with open(employee_db, "r") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if PS == row[1]:
                        index_employee = counter
                        print("Employee Data", index_employee)
                        employee = []
                        for field in employee_data:
                            value = input("Enter " + field + ": ")
                            employee.append(value)
                        updated_data.append(employee)
                    else:
                        updated_data.append(row)
                    counter += 1

        if index_employee is not None:
            with open(employee_db, "w") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
        else:
            print("Employee data found")
        input("Enter any key to continue")

    def delete_employee():
        global employee_data
        global employee_db

        print("Delete employee data")
        PS = input("Enter employee ID")
        employee_found = False
        updated_data = []
        with open(employee_db, "r") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if PS != row[1]:
                        updated_data.append(row)
                        counter += 1
                    else:
                        employee_found = True

        if employee_found is True:
            with open(employee_db, "w") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
            print("Data of", PS, "deleted successfully")
        else:
            print("Data not found")
        input("Enter any key to continue")

obj = Employee_Data
obj2 = Employee_Data2
while True:
    obj.menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        obj.new_employee()
    elif choice == '2':
        obj2.view_employee()
    elif choice == '3':
        obj2.search_employee()
    elif choice == '4':
        obj2.update_employee()
    elif choice == '5':
        obj2.delete_employee()
    else:
        break
