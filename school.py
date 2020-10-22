#function for creating a new folder 
import os
def createNewfolder(foldername):
    try:
        os.mkdir('schoolproject/demo/'+foldername)
    except FileExistsError:
         print('\nThis folder'+ foldername+'is already exists.')
         userchoice()
    else:
        print('\nYour folder'+foldername+'is sucessfully cretaed')
        userchoice()

#function for creating file
def createfile(fileName):
    try:
        myfile = open('schoolproject/demo/'+fileName +'.txt','x')
    except FileExistsError:
        print('\nThis file ['+ fileName+']is aready exists.Try with some new.')   
    finally:
        print('\nThis file[' +fileName +'] is created sucessfully') 
        myfile.close()  

# create a menu bar for user input to their need..
def userchoice():
    #get user choice
    choicelist ='''
       ****************************************
                 Select your choice
       ****************************************
    1) New Resgistration.
    2)Show existing school file list.
    3)Enter in school.
    4)Exit.
    '''     
print('\nchoicelist: ')
choice = int(input('\nEnter your choice(1/2/3/4): '))

if choice == 1:
    print('Your want to create new registration folder:')
    foldername = input('\nEnter your folder name: ')
    createNewfolder(foldername)

elif choice == 2:
    print('\nCreating a new file: ')
    fileName = input('\nEnter your file name: ')
    createfile(fileName)    
elif choice == 3:
    print('\nEnter in school: ')
else:
    print('\nexit')

class student():
    # Constructor 
    def __init__(self, name, rollno, marks1, marks2): 
        self.name = name 
        self.rollno = rollno 
        self.marks1 = marks1 
        self.marks2 = marks2 
        # Function to create and append new student    
    def accept(self, Name, Rollno, marks1, marks2 ): 
        # use  ' int(input()) ' method to take input from user 
        ob = student(Name, Rollno, marks1, marks2 ) 
        list.append(ob) 
  
    # Function to display student details      
    def display(self, ob): 
            print("Name   : ", ob.name) 
            print("RollNo : ", ob.rollno) 
            print("Marks1 : ", ob.marks1) 
            print("Marks2 : ", ob.marks2) 
            print("\n")  

