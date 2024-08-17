#1. Write a Python program to add an item to a tuple.
a=(1, 2, 3)
b=(4, 5, 6)
print(tuple(a+b))

#Write a Python program to sum all the items in a list.
x=[1,2,3,4,5,6,7,8,9,10]
print(sum(x))

#3. Write a Python program to multiply all the items in a list
def multiply_list(x):
    result = 1
    for item in x:
        result *= item
    return result
print(multiply_list(x))

#4. Write a Python program to get the smallest number from a list.
x = [3, 7, 5, 9, 4]
smallest_number = min(x)
print(smallest_number)

#5. Write a Python program to get the largest number from a list.
x = [3, 7, 5, 9, 4]
largest_number= max(x)
print(largest_number)

#6 . Write a Python program to count the number of strings from a given list of strings.
x=("I love Python")
number_of_strings= sum(1 for item in x if isinstance(item, str))
print(number_of_strings) #it will count the spaces as well

#7. Write a Python program to clone or copy a list
u = ["Ahmed", "Kiko", "Marely", "ziko"]
y = u.copy()
print(y)

#8. Write a Python program to remove item(s) from a given set.

set={"Amit", "Deep Learning", "Machine"}
set.remove("Amit")
print(set)

#9. Write a Python program to check if a set is a subset of another set.

set1={1,2,3,4,5}
set2={1,2,3,4,5,6,7,8,9,10}
check=set1.issubset(set2)
print(check)

#10, Write a Python program to remove all elements from a given set.

set_cleared={"Amit", "Deep Learning", "Machine"}
set_cleared.clear()
print(set_cleared)

#11. Write a Python program to find the maximum and minimum values in a set.
set={1,2,3,4,5,6,7,8,9,10}
max_num=max(set)
min_num=min(set)
print(max_num,",",min_num)

#12. Write a Python program to find the index of an item in a tuple
tuple=(1, 2, 3, 4, 5, 6)
print(tuple[2])

#13. Write a Python program to convert a tuple to a dictionary.
tuple=(("age",24) , ("name","kiko") , ("city","october"))
dictionary=dict(tuple)
print(dictionary)


#14. Write a Python program to unzip a list of tuples into individual lists.
tuple=(("age",24) , ("name","kiko") , ("city","october"))
list=list(tuple)
print(list)
list1, list2, list3=zip(list)
print(list1)
print(list2)
print(list3)

#15. Write a Python program to reverse a tuple.

tuple1 = (1, 2, 3, 4, 5)
reverse = tuple1[::-1]
print(reverse)


#16. Write a Python program to convert a list of tuples into a dictionary.
list_of_tuples=[("Amit","ma3ady"), ("Diploma","Machine Learning"), ("Duration","8 months")]
dictionary2=dict(list_of_tuples)
print(dictionary2)

#17. Write a Python program to replace the last value of tuples in a list.
Sample_list=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_value=100
print([(Sample_list[0][0] , Sample_list[0][1] , new_value)])
print([(Sample_list[1][0] , Sample_list[1][1] , new_value)])
print([(Sample_list[2][0] , Sample_list[2][1] , new_value)])

#18. Write a Python program to sort a tuple by its float element.
data = (('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'), ('item4', '2.90'))

sorted_data = sorted(data, key=lambda x: float(x[1]))

print("Sorted tuple:", sorted_data)



