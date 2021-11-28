import csv
from math import *

# Function to print banner 

def print_banner():
    banner_text = '''
*************************************************************************************
*    __ ____  ____   ________  _  ______   ___  ___ _________   ___  ___   ________ *
*   / // / / / / /  /  _/ __ \/ |/ / __/  / _ \/ _ /_  __/ _ | / _ )/ _ | / __/ __/ *
*  / _  / /_/ / /___/ // /_/ /    /\ \   / // / __ |/ / / __ |/ _  / __ |_\ \/ _/   *
* /_//_/\____/____/___/\____/_/|_/___/  /____/_/ |_/_/ /_/ |_/____/_/ |_/___/___/   *
*                                                                                   *
* HULIONS DATABASE v1.0                                                             *
* Coded By: AHSAN X EMAAN X BURHAN                                                  *
*                                                                                   *
*************************************************************************************
'''
    print(banner_text)

# check for user choice

def check_user_choice():

    # show user each correct input for using the program

    print("[1] Show the Database")
    print("[2] Add Students Data to Database")
    print("[3] Modify Student Data in Database")
    print("[4] Delete Student Data in Database")
    print("[5] Search Student Data in Database")
    print("[6] Exit\n")
    
    while True:
        user_choice = (input("Please enter your choice to continue:\n>>> ")).strip()

        # check for valid input by user

        def check_for_valid_input(user_choice):
            if user_choice.isdigit()== False or user_choice == '':
                print(f"'{user_choice}' was an invalid choice !")
                return False
            else:
                user_choice = int(user_choice)
                if user_choice > 0 and user_choice <7:
                    return True
                else:
                    return False

            # while user_choice.isdigit()==False:
            #     print(f"'{user_choice}' was an invalid choice !")
            #     user_choice = (input("Please enter your choice to continue:\n>>> ")).strip()
            # return user_choice
        
        is_choose_valid = check_for_valid_input(user_choice)
        
            
        # call for correct function according to given input

        if is_choose_valid == True:
            user_choice = int(user_choice)
            if user_choice == 1:
                show_data()
                main()
                break
            elif user_choice == 2:
                add_data(False)
                main()
                break
            elif user_choice == 3:
                modify_data(False,False)
                main()
                break
            elif user_choice == 4:
                modify_data(True,False)
                main()
                break
            elif user_choice == 5:
                search_data()
                main()
                break
            elif user_choice == 6:
                print("*************************************************************************************")
                print("                       Thankyou for using HULIONS DATABASE v1.0                      ")
                print("*************************************************************************************")
                break
        else:
            print(f"'{user_choice}' was an invalid choice !")

# show data function - show the whole data in database

def show_data():

    # save data from csv file to array within nested dictionary

    names = ["name",'id','age','major','batch','phone']
    all_data = []

    with open("E:\HABIB UNI WORK\First Semester\Programming Fundamentals\Final Project\HU Lions Database\databases\hu_lions.csv") as database:
        read_data = csv.DictReader(database,fieldnames=names, delimiter=',')
        for data in read_data:
            all_data.append(data)

    # print database in tabular form

    print("-"*80)
    print("    ID   "+" |"+"            NAME           "+" |  "+"AGE"+" |  "+"MAJOR"+"  |  "+"BATCH"+" | "+"   PHONE    |")
    print(80*"-")

    for row in all_data:
        print(" "+"  "+"0"+row["id"]+"  |",end='')
        print(" "+" "*ceil((26-(len(row["name"])))/2)+row["name"]+" "*((26-(len(row["name"])))//2)+" |",end='')
        print(" "+" "+row["age"]+"  |",end='')
        print(" "+"  "+row["major"]+"    |",end='')
        print(" "+" "+row["batch"]+"  |",end='')
        if row["phone"] !="0":
            print(" "+row["phone"]+" |",end='')
        else:
            print("      -      |",end='')
        print()
    print(80*"-")
    print()
    
    #  user need to press ENTER to exit viewing database

    while True:
        check_for_enter = input("Press ENTER to continue to the main menu! ").strip()
        if check_for_enter == "":
            break
    

# add students data function - add data of student to the existing csv file

def add_data(mod):
    
    #  all data provided by user will appended in below variable

    student_data = []

    # check for valid input by user

    def check_for_valid_student_data(data_by_user,data_type):

        if data_type == "name":
            if data_by_user == "" or data_by_user.isdigit() or len(data_by_user) > 27:
                print(f"'{data_by_user}' was an invalid input for full name!")
                return False
            else:
                return True

        elif data_type == "id":
            if data_by_user == "" or data_by_user.isdigit() == False:
                print(f"'{data_by_user}' was an invalid input for student id!")
                return False
            else:
                data_by_user = int(data_by_user)
                if data_by_user > 1000 and data_by_user < 10000:
                    return True
                else:
                    print(f"'{data_by_user}' was an invalid input for student id!")
                    return False

        elif data_type == "age":
            if data_by_user == "" or data_by_user.isdigit() == False:
                print(f"'{data_by_user}' was an invalid input for student age!")
                return False
            else:
                data_by_user = int(data_by_user)
                if data_by_user > 16 and data_by_user < 30:
                    return True
                else:
                    print(f"'{data_by_user}' was an invalid input for student age!")
                    return False
        
        elif data_type == "major":
            data_by_user = data_by_user.upper()
            if data_by_user == "" or data_by_user.isdigit() or len(data_by_user) > 2 or (data_by_user != "CS" and data_by_user != "EE" and data_by_user != "CE"):
                print(f"'{data_by_user}' was an invalid input for student major!")
                return False
            else:
                return True

        elif data_type == "batch":
            
            if data_by_user == "" or data_by_user.isdigit()== False :
                print(f"'{data_by_user}' was an invalid input for student batch!")
                return False
            else:
                data_by_user = int(data_by_user)
                if data_by_user > 2020 and data_by_user < 9999:
                    return True
                else:
                    print(f"'{data_by_user}' was an invalid input for student batch!")
                    return False

        elif data_type == "phone":

            if data_by_user == "" or data_by_user.isdigit()== False or len(data_by_user) != 11:
                print(f"'{data_by_user}' was an invalid input for student phone number!")
                return False
            else:
                return True

    while True:
        student_name = input("Enter Student Full Name:\n>>> ").strip()

        is_valid = check_for_valid_student_data(student_name,"name")
        if is_valid == True:
            student_data.append(student_name)
            break


    while True:
        student_id = input("Enter Student HU ID:\n>>> ").strip()
        is_valid = check_for_valid_student_data(student_id,"id")
        if is_valid == True:
            student_data.append(str(student_id))
            break

    while True:
        student_age = input("Enter Student Age:\n>>> ").strip()
        is_valid = check_for_valid_student_data(student_age,"age")
        if is_valid == True:
            student_data.append(student_age)
            break

    while True:
        student_major = input("Enter Student Major:\n>>> ").strip()
        is_valid = check_for_valid_student_data(student_major,"major")
        if is_valid == True:
            student_data.append(student_major.upper())
            break

    while True:
        student_batch = input("Enter Student Batch:\n>>> ").strip()
        is_valid = check_for_valid_student_data(student_batch,"batch")
        if is_valid == True:
            student_data.append(student_batch)
            break

    while True:
        student_phone = input("Enter Student Phone Number:\n>>> ").strip()
        is_valid = check_for_valid_student_data(student_phone,"phone")
        if is_valid == True:
            student_data.append(student_phone)
            break


    if mod == False:

        # write each row got by user

        with open("E:\HABIB UNI WORK\First Semester\Programming Fundamentals\Final Project\HU Lions Database\databases\hu_lions.csv","a",newline='') as database:
            write_data = csv.writer(database)
            write_data.writerow(student_data)
        
        database.close()

        print("Data has been added Successfully!\n\nNote: You can view the updated database from main menu.")

        #  user need to press ENTER to go back to main menu

        while True:
            check_for_enter = input("Press ENTER to return to the main menu! ").strip()
            if check_for_enter == "":
                break

    else:
        return student_data

# modify students data function - modify data of existing student in csv file

def modify_data(should_delete_data,should_return_search_by_id):
    
    # first read data from csv file

    dict_keys = ["name",'id','age','major','batch','phone']
    all_students_data = []

    with open("E:\HABIB UNI WORK\First Semester\Programming Fundamentals\Final Project\HU Lions Database\databases\hu_lions.csv") as database:
        object_dictionary = csv.DictReader(database,fieldnames=dict_keys, delimiter=',')
        for dictionary in object_dictionary:
            all_students_data.append(dictionary)

    # check for valid input by user

    def check_for_valid_id_input(data_by_user):
        if data_by_user == "" or data_by_user.isdigit() == False:
                    print(f"'{data_by_user}' was an invalid input for student id!")
                    return False
        else:
            data_by_user = int(data_by_user)
            if data_by_user > 1000 and data_by_user < 10000:
                return True
            else:
                print(f"'{data_by_user}' was an invalid input for student id!")
                return False
    
    # find student with the same id

    while True:
        if should_delete_data == False:
            student_id = input("Enter the student HU ID which you wanna change: \n>>> ")
        elif should_return_search_by_id == True:
            student_id = input("Enter the student HU ID which you wanna search: \n>>> ")
        else:
            student_id = input("Enter the student HU ID which you wanna delete: \n>>> ")

        is_valid = check_for_valid_id_input(student_id)
        if is_valid==True:
            is_id_exist = False
            index_of_student = -1
            for dictionary in all_students_data:
                index_of_student = index_of_student+1
                if dictionary['id'] == student_id:
                    
                    is_id_exist = True
                    if should_return_search_by_id == False:
                        print(f"Following student is found in the database with ID [{student_id}] : \n")
                        print("------------------------------------------------")
                        print("NAME :  "+ dictionary['name']+"\nID   :  "+dictionary['id']+"\nAGE  :  "+dictionary['age']+"\nMAJOR:  "+dictionary['major']+"\nBATCH:  "+dictionary['batch']+"\nPHONE:  "+dictionary['phone'])
                        print("------------------------------------------------")
                        print()
                        if should_delete_data == False:
                            print(f"Note: You need to enter new details for '{dictionary['name']}' \n")
                        break
                    else:
                        print("------------------------------------------------")
                        print("NAME :  "+ dictionary['name']+"\nID   :  "+dictionary['id']+"\nAGE  :  "+dictionary['age']+"\nMAJOR:  "+dictionary['major']+"\nBATCH:  "+dictionary['batch']+"\nPHONE:  "+dictionary['phone'])
                        print("------------------------------------------------")
                        print()
                        return dictionary
            

            if is_id_exist == False:
                print(f"Sorry, Student with ID: {student_id} does not exist in our Database!")
            else:
                break
    
    
    # if modify is called then data will be updated, so delete is false
     
    if should_delete_data == False:

        # call add data function to update existing student data

        student_updated_data = add_data(True)
        student_updated_data_to_dict = {
            "name" : student_updated_data[0],
            "id" : student_updated_data[1],
            'age' : student_updated_data[2],
            'major' : student_updated_data[3],
            'batch' : student_updated_data[4],
            'phone' : student_updated_data[5],
        }
        all_students_data[index_of_student] = student_updated_data_to_dict
        all_students_data_as_lists = []
        for row in all_students_data:
            all_students_data_as_lists.append([row['name'],row['id'],row['age'],row['major'],row['batch'],row['phone']])

        # update the csv files using new inputs
        
        with open("E:\HABIB UNI WORK\First Semester\Programming Fundamentals\Final Project\HU Lions Database\databases\hu_lions.csv",'w', newline='') as database:
            write_dictionary = csv.writer(database) 
            write_dictionary.writerows(all_students_data_as_lists)

        database.close()
        
        print(f"Student data for selected ID [{student_updated_data[1]}] has been succesfully modified!\n")
        
        print("Note: You can view the updated database from main menu.")


    # if delete is called then data will be deleted, so delete is true here

    else:

        all_students_data[index_of_student] = ""
        all_students_data_as_lists = []
        for row in all_students_data:
            if row != "":
                all_students_data_as_lists.append([row['name'],row['id'],row['age'],row['major'],row['batch'],row['phone']])

        # update the csv files using new inputs
        
        with open("E:\HABIB UNI WORK\First Semester\Programming Fundamentals\Final Project\HU Lions Database\databases\hu_lions.csv",'w', newline='') as database:
            write_dictionary = csv.writer(database) 
            write_dictionary.writerows(all_students_data_as_lists)

        database.close()
        
        print(f"Student data for selected ID [{student_id}] has been succesfully deleted!\n")
        
        print("Note: You can view the updated database from main menu.")


    #  user need to press ENTER to go back to main menu

    while True:
        check_for_enter = input("Press ENTER to return to the main menu! ").strip()
        if check_for_enter == "":
            break

def search_data():

    # while True:
    #     search_choice = input("Please enter your choice to continue:\n>>> ")

    #     function 

    x = modify_data(False,True)
    print(x)


    #  user need to press ENTER to go back to main menu

    while True:
        check_for_enter = input("Press ENTER to return to the main menu! ").strip()
        if check_for_enter == "":
            break

# Main Function which will call All Functions

def main():
    print_banner()
    check_user_choice()

main()