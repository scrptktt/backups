def check_print(function, i, adj, message):
    print(f"\033[34m[{function}][{i}] {adj} : {repr(message)}\033[0m")
def string_to_array(user_string):
    arr = []
    
    for i in range(len(user_string)):
        arr.append(user_string[i])

    def remove_trailing(array):
        for i in range(len(array)-1):
            print(f"LOOKOUT!: {len(array)-1}")
            print(f"count: {i}, letter: {array[i]}")
            if i == 0: 
                check_print('remove_trailing', i, 'deleted', array[i])
                del arr[i]
            elif i == len(array[i])-2: 
                check_print('remove_trailing', i, 'deleted', array[i])
                del arr[i]

    remove_trailing(arr)
    return arr

def array_to_string(user_array):    
        user_string = ''
        for i in user_array:
            user_string = user_string + i
        return user_string
class_details ='''
Associated Term:Fall 2024
CRN:84038
Campus:Main Campus
Schedule Type: Lecture
Instructional Method: Face to Face
Section Number: 001
Subject: Software Engineering
Course Number: 1020
Title: Data Structures for Software Engineers
Credit Hours: 3
Grade Mode: Standard Letter Grade
'''

string = string_to_array(class_details)

print(f"string : {len(class_details)}")
print(f"{class_details}")
print()
print(f"array : {len(string)}")
print(f"{string}")
print()

def json_details(recipe):
    tmp_array = string
    # tmp_array = string_to_array(recipe)
    def array_range(array):
        chars = 0
        
        for i in range(len(array)):
            if array[i] == ':':
                chars = chars + 2

            elif array[i] == "\n":
                chars = chars + 2
        return int(chars + len(array))-2

    # for i in range(len(tmp_array)):
    #     if (i == 0) and (tmp_array[i] == '\n'): 
    #         tmp_array.pop(i)
    #         tmp_array.insert(i, "\"")
    #     elif ((i == len(tmp_array)-1) and (tmp_array[i] == '\n')):
    #         tmp_array.pop(i)
    #         tmp_array.insert(i, "\"")    
        
    changed = False
    check_space = 0   
    i2 = -1

    for i in range(array_range(tmp_array) - 1):
        # Determines if last
        # iteration was checked.
        if i > (i2 + 3):
            changed = False
        
        # Removes extra space in key value.
        if (i == check_space) and (tmp_array[i] == ' '):
                del tmp_array[i]
            
        # Checks next member of array
        # if change was not made last.
        # then,
        # Inserts new characters on
        # both sides of checked char.
        if changed == False:
            if (i == 0):
                changed = True
                tmp_array.insert(i,"\"")
                i2 = i

            elif tmp_array[i] == ':':
                changed = True
                
                tmp_array.insert(i,"\"")
                tmp_array.insert(i+2, " ")
                tmp_array.insert(i+3,"\"")
                
                check_space = i + 4
                i2 = i
            elif tmp_array[i] == "\n":
                changed = True
                tmp_array.insert(i,"\"")
                tmp_array.insert(i+1, ",")
                tmp_array.insert(i+3,"\"")

                i2 = i
    return array_to_string(tmp_array)
# print(json_details(class_details))

course_description ='''
P: SENG 1000; P/C: SENG 1010. Introduction to data structures and their implementation. Computational problem-solving using data structures.
'''

def json_description(recipe):
    def string_to_array(user_array):
        for i in range(len(user_array)):
            if (i == 0) and (user_array[i] == '\n'): 
                user_array.pop(i)
                user_array.insert(i, "\"")
            elif ((i == len(user_array)-1) and (user_array[i] == '\n')):
                user_array.pop(i)
                user_array.insert(i, "\"")
        return user_array
    
    for i in recipe:
        if i == '.':
            print('\n', end='')
    
class_meeting_times ="""
Instructor: Brian Dietrick (Primary)
Monday,Wednesday,Friday
S
M
T
W
T
F
S
08/19/2024 - 12/11/2024
Type: Classroom
10:00 AM - 10:50 AM
Main Campus Campus | Austin Building | Room 00201
"""
prerequisites ="""
Catalog Prerequisites
And/Or		Test	Score	Subject	Course Number	Level	Grade	
(			Software Engineering	1000	Undergraduate	C	
Or				Software Engineering	1000	Undergraduate	P	)
And	(			Software Engineering	1010	Undergraduate	C	
Or				Software Engineering	1010	Undergraduate	P
"""
textbook_information ="""
https://ecu.bncollege.com/course-material-listing-page?utm_campaign=storeId=89826_langId=-1_courseData=SENG_1020_001_2024801&utm_source=wcs&utm_medium=registration_integration
"""
catalog ='''
Title:Data Structures for Software Engineers
College: College of Engr and Technology TC
Department: Computer Science CS
Hours:
Credit Hours:3
Lecture: 3
Levels:
Undergraduate UG
Grading Modes:
Forgiveness F
Standard Letter Grade S
Schedule Types:
Lecture 04
Attributes:
'''

def UIpipeline(step):
    if step == 0:
        data = input("[Paste] text from class details tab: ")
        class_details = data
    if step == 1:
        data = input("[Paste] text from course_description tab: ")
        course_description = data
    if step == 2:
        data = input("[Paste] text from class_meeting_times tab: ")
        class_meeting_times = data
    if step == 3:
        data = input("[Paste] text from prerequisites tab: ")
        prerequisites = data
    if step == 4:
        data = input("[Paste] text from textbook_information tab: ")
        textbook_information = data
    if step == 5:
        data = input("[Paste] text from catalog tab: ")
        catalog = data
    return data
def generateJson(recipe):
    for step in range(len(recipe)):
        UIpipeline(step)
        class_details = json_details(class_details)
    
StringRecipe = [class_details, 
                course_description, 
                class_meeting_times,
                prerequisites,
                textbook_information,
                catalog
                ]

json_file_string = None