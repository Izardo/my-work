# Author: Isabella Doyle

# this is the menu
def displayMenu():

    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    # strips any whitespace from the left/right of the string
    option = input("Please select an option (a/v/q): ").strip()  
    return option

def doAdd(students):
    studentDict = {}
    studentDict["Name"] = input("Enter student's name: ")
    studentDict["module"] = readModules()
    students.append(studentDict)

def readModules():
    modules = []
    moduleName = input("\tEnter the first module name (blank to quit): ").strip()

    while moduleName != "":
        module = {}
        module["Name"] = moduleName
        module["Grade"] = int(input("\t\tEnter grade: ").strip())
        modules.append(module)
        moduleName = input("\tEnter the next module name (blank to quit): ").strip()
        return modules

def doView():
    print(students)

# main program
students = []
selection = displayMenu()
while (selection != ""):
    if selection == "a":
        doAdd(students)
    elif selection == "v":
        doView()
    else:
        print("Invalid input entered.")

print(students)