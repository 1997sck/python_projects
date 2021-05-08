lstEmployees = []
lstNames = []
counter = 0


def export_employees():
    for employee in lstEmployees:
        with open("file.txt", "w") as output:
            output.write(str(lstEmployees))


def search_ssn():
    ssn = input("Enter employee SSN: ")
    for employee in lstEmployees:
        if ssn == employee[1]:
            print("--------------" + employee[0] + "---------------")
            print("SSN: " + employee[1])
            print("Phone: " + employee[2])
            print("Email: " + employee[3])
            print("Salary: $" + employee[4])
            return employee
    return -1


def edit_employee():
    search = search_ssn()
    if search == -1:
        print("Employee not found...")
    else:
        name = input("Enter the new Name of employee: ")
        ssn = input("Enter the new SSN of employee: ")
        phone = input("Enter the new Phone Number of employee: ")
        email = input("Enter the new Email of employee: ")
        salary = input("Enter the new Salary of employee: ")
        search[0] = name
        search[1] = ssn
        search[2] = phone
        search[3] = email
        search[4] = salary


def add_employee():
    global counter
    while counter < 5:
        print("----------------------------------------------\n")
        print("         Number of Employee ({0:d})".format(counter))
        print("----------------------------------------------\n")
        name = input("Enter employee Name: ")
        lstNames.insert(counter, name)
        ssn = input("Enter employee SSN: ")
        phone = input("Enter employee Phone Number: ")
        email = input("Enter employee Email: ")
        salary = input("Enter employee Salary: ")

        lstEmployees.append([name, ssn, phone, email, salary])
        counter = counter + 1

        if (counter) > 5:
            break
        else:
            continue


def print_employee():
    for employee in lstEmployees:
        print("--------------" + employee[0] + "---------------")
        print("SSN: " + employee[1])
        print("Phone: " + employee[2])
        print("Email: " + employee[3])
        print("Salary: $" + employee[4])


def main():
    while True:
        print('----------------------------------------------\n')
        print('      Welcome to the Employee Data System    -\n')
        print('----------------------------------------------\n')
        print('[1] Add an Employee: \n')
        print('[2] View All Employees: \n')
        print('[3] Search Employees by SSN: \n')
        print('[4] Edit Employees information: \n')
        print('[5] Export Employees information: \n')
        user_option = input("Please select an option: ")
        if user_option == "1":
            add_employee()
        elif user_option == "2":
            print('\n' * 3)
            print_employee()
            print('\n' * 3)
        elif user_option == "3":
            found = search_ssn()
            if found == -1:
                print("Employee not found...")
        elif user_option == "4":
            edit_employee()
        elif user_option == "5":
            export_employees()
        else:
            print("Please select a valid option...")


if __name__ == "__main__":
    main()

