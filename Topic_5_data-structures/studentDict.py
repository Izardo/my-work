# This program creates a dictionary called student containing 
# a list containing further dictionaries
# Author: Isabella Doyle

# the following assigns a dictionary to the variable student
# the square brackets create a list within the dictionary
# the curly brackets inside the list create more dictionaries
student = {
    "name" : "Mary",
    "modules": [ 
        {
            "course_name" : "Programming", 
            "grade" : 45
        },
        {
            "course_name" : "History",
            "grade" : 99
        }
    ]
}
# uses print statement to access the key "name" and prints its corresponding value
print("Student: {}".format(student["name"]))
# uses a for loop to access and print the key "module" and its corresponding value
for module in student["modules"]:
    print("\t {} \t: {}".format(module["course_name"], module["grade"]))