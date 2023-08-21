import datetime
from collections import Counter
def data_transfer(directory): # Big 0notation is O(n), n is the number of line in file.txt
    """This function transfer data from file and append them in a list of dictionaries"""
    #https://stackoverflow.com/questions/34976122/import-data-from-file-to-dictionary-in-python
    #using with statement to open a file in read mode.
    #https://www.geeksforgeeks.org/python-datetime-strptime-function/
    #use this link to format date.
    employee_data = []
    with open(directory, 'r') as f:
        for line in f:
            ID, username, date, gender, salary = line.split(', ')
            #appending data into list of dictionaries:
            employee_data.append({'ID': ID, 'username': username, 'date': datetime.datetime.strptime(date, "%Y%m%d"), 'gender': gender, 'salary': int(salary)})
    return employee_data

def admin_menu(): # Big 0notation is O(1)
    """Displays the menu of admin"""
    print("\nAdmin Menu:")
    print("1. Display Statistics")
    print("2. Add Employee")
    print("3. Display All Employees")
    print("4. Change Employee Salary")
    print("5. Remo Employee")
    print("6. Raise Employee Salary")
    print("7. Exit")

def employee_menu(): # Big 0notation is O(1)
    """Display menu of employee"""
    # Big 0notation is O(1)
    print("\nEmployee Menu:")
    print("1. Check Salary")
    print("2. Exit")

def save(directory, employee_data): # Big 0notation is O(n), n is the number of employees in employee_data
    """Saves the data edited by admin in Employees.txt file"""
    #https://www.w3schools.com/python/python_file_write.asp
    #used with statement to open a file in write mode.
    with open(directory, 'w') as f:
        for data in employee_data:
            date = data['date'].strftime("%Y%m%d")
            #https://stackoverflow.com/questions/14619494/how-to-understand-strptime-vs-strftime
            f.write(f"{data['ID']}, {data['username']}, {date}, {data['gender']}, {data['salary']}\n")

def salary_raise(employee_data): # 0(n log n) since 2 for loops and the second one runs if ID is == employee['ID], n is number of employees
    """Raise the salary of an employee by percentage"""
    #https://stackoverflow.com/questions/73604254/big-o-notation-of-a-for-loop-with-an-conditional-inner-loop
    ID = input("Enter ID of the employee: ")
    #https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension
    #used list comprehension to create True_employee.
    Chosen = [employee for employee in employee_data if employee['ID'] == ID ]
    if Chosen:
        for e in Chosen:
            raise_percent = float(input("Enter percentage of the raise: "))
            e['salary'] = int(e['salary'] + (raise_percent / 100) * e['salary'])
            print("salary raised.")
    else:
        print("No employee with such ID")


def stats(employee_data): # O(n) where n is the number of employees
    """Displays the number of male and female employees separately"""
    # https://stackoverflow.com/questions/37438550/how-can-i-count-occurrences-of-values-in-a-list-of-dicts
    # usage of Counter
    Gender = Counter()
    for employee in employee_data:
        Gender[employee['gender']] += 1
    print(Gender)


def remove_employee(employee_data): # O(n log n) same as 'salary raise function'
    """Removes and employee from list of employees by asking for its ID"""
    #https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension
    #list.remove(i)
    ID = input("Enter ID of employee you want to remove: ")
    Chosen = [employee for employee in employee_data if employee['ID'] == ID]
    if Chosen:
        for e in Chosen:
            employee_data.remove(e)
            print("Employee Removed")
    else:
        print("No employee with such ID!")

def display_employees(employee_data): # Big 0notation is O(n log n), n is number of employees in employee_data
    """Displays all employees in system in ascending order of the joining date """
    #https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
    employee = sorted(employee_data, key=lambda x:x['date'])
    #using sorted to sort the employees by the date of joining from oldest to newest.
    for data in employee:
        join_date = data['date'].strftime("%Y%m%d")
        print(f"{data['ID']}, {data['username']}, {join_date}, {data['gender']}, {data['salary']}")

def add_employee(employee_data): # O(n) where n is O(1)
    # https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/string/zfill/python-string-zfill/
    # usage of rjust() to format new emp ID
    new_ID = f"emp{str(len(employee_data) +1).rjust(3, '0')}"
    username = input("Enter username of new employee: ")
    salary = int(input("Enter his salary: "))
    gender = input("Enter his gender, (male/female): ")
    employee_data.append({'ID': new_ID, 'username': username, 'date': datetime.datetime.now(), 'gender': gender, 'salary': int(salary)})
    # usage of now(): https://www.geeksforgeeks.org/python-now-function/
    print("Employee was added")

def Main(): # Big 0notation is O(n),n is number of employees in system
    """Main program where functions are called according to the menu"""
    employee_data = data_transfer("Employees.txt")
    attempt_number = 0
    attempts_max_number = 5
    while attempt_number < attempts_max_number:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "admin" and password == "admin123123":
            print("Welcome Admin!")
            while True:
                admin_menu()
                choice = input("Enter choice:")
                if choice == '1':
                    stats(employee_data)
                elif choice == '2':
                    add_employee(employee_data)
                elif choice == '3':
                    display_employees(employee_data)
                elif choice == '4':
                    print(2)
                elif choice == '5':
                    remove_employee(employee_data)
                elif choice == '6':
                    salary_raise(employee_data)
                elif choice == '7':
                    save("Employees.txt", employee_data)
                    print("Saving Data, Exiting...")
                    break
                else:
                    print("Please select a valid option!")
        elif (username == 'admin' or password != 'admin123123') or (username != 'admin' or password == 'admin123123'):
            print("Invalid password and/or username")
        is_employee = False
        for employee in employee_data:
            if employee['username'] == username and password == "":
                sex = employee['gender']
                if sex == 'male':
                    notation = 'Mr.'
                else:
                    notation = 'Ms.'
                print(f"Hello {notation}{username}")
                while True:
                    employee_menu()
                    goal = input("Enter goal: ")
                    if goal == '1':
                        print(f"Your salary is ${employee['salary']}")
                    elif goal == '2':
                        print("Terminating System")
                        #https://www.geeksforgeeks.org/python-now-function/ usage of now() function
                        #link in first function for hours, minutes and seconds formatting
                        Timestamp = datetime.datetime.now()
                        formatted_timestamp = Timestamp.strftime("%Y%m%d %H:%M:%S")
                        with open("Timestamp-login.txt", 'a') as f:  # using with statement in append mode.
                            f.write(f"{username}, {formatted_timestamp}\n")
                        break
                    else:
                        print("Please select a valid option!")
                break
        if not is_employee and (username != "admin" or password != 'admin123123'):
            attempt_number += 1
        if attempt_number >= attempts_max_number:
            print("You have reached maximum number f login attempts. Goodbye.")
Main()




