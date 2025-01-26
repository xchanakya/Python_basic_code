marks=[97,667,34,135,1245,77,9,6]

marks[1]=100
print(marks)

#slicing
print (marks[1:4])
print(marks[:5])
print(marks[2:])
print(marks[::])

# list methods
# append
marks.append(100)
print(f'append: {marks}')

# insert
marks.insert(2, 200)
print(f'insert: {marks}')


# remove
marks.remove(200)
print(f'remove: {marks}')

# pop
marks.pop()
print(f'pop: {marks}')

# pop with index
marks.pop(2)
print(f'pop with index: {marks}')

# del
del marks[2]
print(f'del: {marks}')

# clear
marks.clear()
print(f'clear: {marks}')



# write a program to ask input from user and store in a list



# wap to check wheter the list conttains a palindrome or not

palindrome_list=[1,1,1,2,1]

copy_palindrome_list=palindrome_list.copy()
copy_palindrome_list.reverse()
if palindrome_list==copy_palindrome_list:
    print("palindrome")
else:
    print("not palindrome")


 # reverse without using built in function

reverse_list=[1,2,3,4,5,6,7,8,9,10]

for i in range (len(reverse_list)):
    reverse_list[i]=reverse_list[len(reverse_list)-i-1]
    print(reverse_list)

print(reverse_list)

grade=("a","b","c","d","a","a")

print(grade.count("a"))

list_grade=list(grade)
print(list_grade)

