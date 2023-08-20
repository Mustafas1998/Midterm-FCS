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
            employee_data.append({
                'date': datetime.datetime.strptime(date, "%Y%m%d"),
                'gender': gender,
                'salary': int(salary),
                'ID': ID,
                'username': username
            })