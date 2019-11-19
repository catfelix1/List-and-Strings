##num_list = [1,3,5,7,9,11,13,15,17,19]
##sum = 0
##num = 2
##for num in num_list:
##    sum+= num
##    print(sum)
##
##print("The total sum is:", sum)
##
##grade_list = []
max_grade = 100
grade_counter = 0
grade_sum = 0

while True:
    grade = float(input("Enter a grade, type -1 to quit"))

    if grade == -1:
        break
    else:
        if grade <= max_grade:
            grade_sum += grade
            grade_list.append(grade)
            grade_counter +=1
            print(grade_sum/grade_counter)
        else:
            print("Invalid grade, please try again")
##for x in range(100,2,-2):
##    print("Day" , x)
##how_many = int(input("Enter how many numbers to add into the list."))
##operation = input("Enter an operation: A for addition or M for multiplication>")
##
##count = 0
##total = 0
##num_list= list()
##message =  """It. is a. good day."""
##
##message_list = message.split(".")
##
##for word in message_list:
##    print(word)


curlers = ['Brad Jacobs', 'Brad Gushue', 'Brendan Bottcher', 'Jennifer Jones', 'Rachel Homan', 'Anna Hasselborg'] 
loop = 0
while loop == 0:
    a = input("Give me a curler ")
    if curlers == []:
        loop = 1
    elif a == '':
        curlers.pop(-1)
    elif a not in curlers:
        curlers.append(a)
    elif a in curlers:
        curlers.remove(a)
    
    print (curlers)
print(curlers)

