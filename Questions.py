 #Write a Python script to merge two Python dictionaries
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)


#Write a Python program to convert a list into a nested dictionary of keys

num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)

#Write a Python program to get next day of a given date using if-elif-else
year = int(input("Input a year: "))


if (year % 400 == 0):

   leap_year = True

elif (year % 100 == 0):

   leap_year = False

elif (year % 4 == 0):

   leap_year = True

else:

   leap_year = False


month = int(input("Input a month [1-12]: "))


if month in (1, 3, 5, 7, 8, 10, 12):

   month_length = 31

elif month == 2:

   if leap_year:

       month_length = 29

   else:

       month_length = 28

else:

   month_length = 30



day = int(input("Input a day [1-31]: "))


if day < month_length:

   day += 1

else:

   day = 1

   if month == 12:

       month = 1

       year += 1

   else:

       month += 1

print("The next date is [dd-mm-yyyy] %d-%d-%d." % (day, month, year))

#Write a Python program to find the second smallest number in a list

def second_smallest(numbers):
    m1 = m2 = float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

#Write a Python program to change the position of every n-th value with the (n+1)th in a list


 def change_pos(my_list):
     for i in range(0, len(my_list), 2):
         my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

         return my_list


 my_list = [0, 1, 2, 3, 4, 5]

 print(change_pos(my_list))

 #Write a Python program to find maximum and the minimum value in a set

seta = set([5, 10, 3, 15, 2, 20])
print(max(seta))
print(min(seta))

#Write a Python program to find the repeated items of a tuple

tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7
print(tuplex)
count = tuplex.count(4)
print(count)

#Write a Python program to convert a list of tuples into a dictionary



 def Convert(tup, di):
     for a, b in tup:
         di.setdefault(a, []).append(b)
     return di
 tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
         ("suraj", 20), ("akhil", 25), ("ashish", 30)]
 dictionary = {}
 print(Convert(tups, dictionary))
