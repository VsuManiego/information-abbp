import csv
import os
import sys
from csv import writer
from prettytable import from_csv, PrettyTable
from csv import DictReader, DictWriter
from tempfile import NamedTemporaryFile
import shutil


# create a CSV file if it is not created yet
def createCSV():
    with open('./borrowers_record.csv', 'w') as file:
        csv_writer = writer(file, lineterminator='\n')
        # header for the file
        header = ('RECORD NO.', 'FULL NAME', 'WORK POSITION', 'ITEM', 'NUMBER OF ITEMS', 'PURPOSE',
                  'CONDITION', 'TIME BORROWED', 'DATE BORROWED', 'EXPECTED RETURN DATE')
        csv_writer.writerow(header)
        file.close()


# check if the csv file is created already, create if not yet created
def isCSVCreated():
    if os.path.isfile('borrowers_record.csv'):
        return
    else:
        # calling the function to create the CSV file
        createCSV()


# add the user input into the CSV file
def addData():
    name = input('Enter Full Name: ')
    work_position = input('Work Position: ')

    print('Instruction: Please fill up the following.')
    print('Note: If you are acquiring multiple items, please fill them up one by one.')

    opt = "YES"
    while opt == "YES":
        item = input('Name of the item: ')
        number_of_items = input('No. of items: ')
        purpose = input('Purpose: ')
        condition = input('Condition : ')
        time_borrowed = input('Time Borrowed: ')
        date_borrowed = input('Date Borrowed: ')
        expected_return_date = input('Expected Return Date: ')

        with open('./borrowers_record.csv', 'a') as file:
            csv_writer = writer(file, lineterminator='\n')

            # inserting the user input into the csv file
            data = (name, work_position, item, number_of_items, purpose, condition,
                    time_borrowed, date_borrowed, expected_return_date)
            csv_writer.writerow(data)
            file.close()
        print("Data inserted successfully!\n")

        print('Great! Thank you for filling up! Please see the attached data below.')
        print("Borrower's Name: ", name, )
        print('Work Position: ', work_position, )
        print('Item Borrowed: ', item, )
        print('Quantity: ', number_of_items, )
        print('Purpose: ', purpose, )
        print('Time Borrowed: ', time_borrowed, )
        print('Date Borrowed: ', date_borrowed, )
        print('Expected Return Date: ', expected_return_date, )

        opt = input("Do you want to add more? YES/NO: ")

    opt = "NO"
    if opt == "NO":
        return


# search data from CSV file
def searchData():
    search_input = input('Enter name to search: ')
    csv_file = csv.reader(open('./borrowers_record.csv', "r"), delimiter=",")

    table = PrettyTable()
    count = 0
    for row in csv_file:
        if search_input == row[0]:
            count += 1
            table.add_row(row)

    if count != 0:
        table.field_names = ['FULL NAME', 'WORK POSITION', 'ITEM', 'NUMBER OF ITEMS', 'PURPOSE',
                             'CONDITION', 'TIME BORROWED', 'DATE BORROWED', 'EXPECTED RETURN DATE']
        print('FOUND: ', count)
        print(table)
    else:
        print('NO RECORDS FOUND.')


# remove row from csv file
def removeData():
    print('DELETE RECORD')
    fname = input('Enter name to delete: ')
    itemName = input('Enter name of the item to delete: ')
    timeBorrowed = input('Enter time borrowed: ')

    delete = input("Are you sure you want to delete (YES/NO)? ")
    if delete == 'YES':

        with open('./borrowers_record.csv') as file:
            csv_reader = DictReader(file)
            data = list(csv_reader)

        with NamedTemporaryFile(mode='w', delete=False) as temp_file:
            header = ('FULL NAME', 'WORK POSITION', 'ITEM', 'NUMBER OF ITEMS', 'PURPOSE',
                      'CONDITION', 'TIME BORROWED', 'DATE BORROWED', 'EXPECTED RETURN DATE')
            csv_writer = DictWriter(
                temp_file,
                fieldnames=header,
                lineterminator='\n'
            )
            csv_writer.writeheader()

            for row in data:
                if (row['FULL NAME'] == fname) & (row['ITEM'] == itemName) & (row['TIME BORROWED'] == timeBorrowed):
                    continue
                csv_writer.writerow(row)
            print('FILE DELETED SUCCESSFULLY')
            temp_file.close()
            shutil.move(temp_file.name, './borrowers_record.csv')

    else:
        print('Canceled!')


# update/edit cell values in the csv file
def updateRecord():
    name = input('Enter name to update: ')
    itemName = input('Enter name of the item to update: ')
    timeBorrowed = input('Enter time borrowed: ')
    print('What do you want to update?')
    print('ENTER [1] TO UPDATE NAME')
    print('ENTER [2] TO UPDATE WORK POSITION')
    print('ENTER [3] TO UPDATE ITEM NAME')
    print('ENTER [4] TO UPDATE NO. OF ITEMS')
    print('ENTER [5] TO UPDATE PURPOSE')
    print('ENTER [6] TO UPDATE CONDITION')
    print('ENTER [7] TO UPDATE TIME BORROWED')
    print('ENTER [8] TO UPDATE DATE BORROWED')
    print('ENTER [9] TO UPDATE EXPECTED RETURN DATE')
    opt = int(input('ENTER THE CORRESPONDING NUMBER TO UPDATE: '))

    with open('./borrowers_record.csv') as file:
        csv_reader = DictReader(file)
        data = list(csv_reader)

    with open('./borrowers_record.csv', 'w') as up_file:
        header = ('FULL NAME', 'WORK POSITION', 'ITEM', 'NUMBER OF ITEMS', 'PURPOSE',
                  'CONDITION', 'TIME BORROWED', 'DATE BORROWED', 'EXPECTED RETURN DATE')
        csv_writer = DictWriter(
            up_file,
            fieldnames=header,
            lineterminator='\n'
        )
        csv_writer.writeheader()
        for row in data:
            if (row['FULL NAME'] == name) and (row['ITEM'] == itemName) and (row['TIME BORROWED'] == timeBorrowed):
                if opt == 1:
                    up_name = input('ENTER VALUE TO UPDATE NAME: ')
                    row['FULL NAME'] = up_name
                if opt == 2:
                    work_position = input('ENTER VALUE TO UPDATE WORK POSITION: ')
                    row['WORK POSITION'] = work_position
                if opt == 3:
                    item = input('ENTER VALUE TO UPDATE ITEM NAME: ')
                    row['ITEM'] = item
                if opt == 4:
                    number_of_items = input('ENTER VALUE TO UPDATE NO. OF ITEMS: ')
                    row['NUMBER OF ITEMS'] = number_of_items
                if opt == 5:
                    purpose = input('ENTER VALUE TO UPDATE PURPOSE: ')
                    row['PURPOSE'] = purpose
                if opt == 6:
                    condition = input('ENTER VALUE TO UPDATE CONDITION: ')
                    row['CONDITION'] = condition
                if opt == 7:
                    time_borrowed = input('ENTER VALUE TO UPDATE TIME BORROWED: ')
                    row['TIME BORROWED'] = time_borrowed
                if opt == 8:
                    date_borrowed = input('ENTER VALUE TO UPDATE DATE BORROWED: ')
                    row['DATE BORROWED'] = date_borrowed
                if opt == 9:
                    expected_return_date = input('ENTER VALUE TO UPDATE EXPECTED RETURN DATE: ')
                    row['EXPECTED RETURN DATE'] = expected_return_date
                if (opt < 1) or (opt > 9):
                    print('ERROR! PLEASE CHECK YOUR INPUT.')
            else:
                print("INPUT DON'T MATCH WITH THE RECORDS. PLEASE TRY AGAIN")
            csv_writer.writerow(row)
        print('RECORD UPDATED SUCCESSFULLY')


# print all the data in the csv file
def viewAll():
    with open("./borrowers_record.csv", "r") as file:
        table = from_csv(file)
        file.close()
        print(table)


def main():
    while True:
        isCSVCreated()
        print('Information System for the Borrowed or Used Equipment in a Construction')
        print('ENTER [1] TO ADD RECORD')
        print('ENTER [2] TO SEARCH RECORD')
        print('ENTER [3] TO UPDATE RECORD')
        print('ENTER [4] TO DELETE RECORD')
        print('ENTER [5] TO VIEW ALL RECORD')
        print('ENTER [6] TO QUIT')
        user_input = int(input('PLEASE ENTER YOUR CHOICE: '))

        if not type(user_input) is int:
            raise TypeError("Only integers are allowed")

        if user_input == 1:
            addData()
        elif user_input == 2:
            searchData()
        elif user_input == 3:
            updateRecord()
        elif user_input == 4:
            removeData()
        elif user_input == 5:
            viewAll()
        elif user_input == 6:
            sys.exit(0)
        else:
            print('ERROR! PLEASE CHECK YOUR INPUT')


if __name__ == "__main__":
    main()
