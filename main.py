import datetime

def data_transfer(directory):
    """This function transfer data from file and append them in a list of dictionaries"""
    #https://stackoverflow.com/questions/34976122/import-data-from-file-to-dictionary-in-python
    #using with statement to open a file in read mode.
    #https://www.geeksforgeeks.org/python-datetime-strptime-function/
    #use this link to format date
    employee_data = []
    with open(directory, 'r') as f:
        for line in f:
            ID, username, date, gender, salary = line.split(', ')
            #appending data into list of dictionaries:
            employee_data.append({'date': datetime.datetime.strptime(date, "%Y%m%d"), 'gender': gender, 'salary': int(salary), 'ID': ID, 'username': username})
    return employee_data

def admin_menu():
    """Displays the menu of admin"""
    print("\nAdmin Menu:")
    print("1. Display Statistics")
    print("2. Add Employee")
    print("3. Display All Employees")
    print("4. Change Employee Salary")
    print("5. Remo Employee")
    print("6. Raise Employee Salary")
    print("7. Exit")

def employee_menu():
    """Display menu of employee"""
    print("\nEmployee Menu:")
    print("1. Check Salary")
    print("2. Exit")

def save(directory, employee_data):
    """Saves the data edited by admin in Employees.txt file"""
    #https://www.w3schools.com/python/python_file_write.asp
    #used with statement to open a file in write mode
    with open(directory, 'w') as f:
        for data in employee_data:
            date = data['date'].strftime("%Y%m%d")
            #https://stackoverflow.com/questions/14619494/how-to-understand-strptime-vs-strftime
            f.write(f"{data['ID']}, {data['salary']}, {date}, {data['username']}, {data['gender']}\n")



