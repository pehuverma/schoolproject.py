'''
This project is based on file handling with the help of this we create a or handle h school management system
1. Sbse phle hum 2 choice rkhege 
a) Create New school list
b) Enter the existing school list
agr admin create new school krta h to vo usme basically school ki new list create krta h
or agr vo already existing school m enter krta h toh admin ko sare schools ki list show ho jayegi.

jab admin new school create kr leta hai then vo Enter in school kr leta h/skta h.
Or jb admin existing list m entry krta h uske baad vo school m enter krta h .
or agr adin chahye to enter in school se phle exit bhi kr skta h.
Agr admin create new school se enter krta h to hm isme 3 steps kr skte h .
1. New class name se folder create karna
2. Class name class list me addon karna
3. Enter in class and show options of see class studnets
********************************************************************************************
or agr existing school list se admin school in enter krta h to hm isme following steps kr skte h...
1. Register new student
2. Check existing student by rn
3. Update student data by rn
4. Delete existing student by rn
5. Exit
************************************************************************************************
After doing all this steps, we can categories into 4 options
1. Student registration form
2. Roll number
3. Name
4. Class
5. Parents name
6. Address
7. mobile
**************************************
Show student details by roll number
**************************************
Update student details by rn
Show existing student details and then change any of them.
***********************************************************
Delete student data by roll number
---------------------------------------------------------------


'''
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
def createfile(fileName ):
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

class studentDetail:
    #creating a constructor
    def __init__(self, name,rollnumber,course,parentName,address,phoneNumber):
        self.name = name
        self.rollnumber = rollnumber
        self.course = course
        self.parentName = parentName
        self.address = address
        self.phoneNumber = phoneNumber
    def mydetail(self):
        print('\n' +self.name +'and' + self.rollnumber +'and' +self.course + 'and'+self.parentName+ 'and'+self.address+ 'and'+self.phoneNumber)
    def studnetPersnoldetail(self, email) :
        print('''
        hello, how are you ?
        This is you mobile number {}
        This is you emailid {}
        '''.format(self.name,self.address,self.phoneNumber,self.parentName,self.course,self.rollnumber)) 
#Create object
# #myclass()
myobj = studentDetail('purnima','21','Bca','Pragy','Delhi','9129392939')      
myobj.mydetail
myobj.studnetPersnoldetail('pihu@gmail.com')

