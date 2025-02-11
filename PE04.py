#Script to concatenate following dictionaries to create a new one
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

# The new dictionary
d4= {**dic1, **dic2, **dic3}

print(d4)

#To generate and print dictionary that contains a number (between 1 and n) in the form of (x,x*x)
n = int(input("Enter the value of n: "))

#To generate dictionary
d = {x: x * x for x in range(1, n + 1)}

print("d:", d)

from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

#Combine Dictionaries using Counter
d3 = Counter(d1) + Counter(d2) 
print ("d3:", d3)



Sample_Data = [{"V": "S001"}, {"V": " S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
     {"V": "S009"}, { "VIII": "S007"}]

unique_values = {value for dic in Sample_Data for value in dic.values()}

print ("Unique Values:", unique_values)


#Sample Dicitonaries
d1_x = {'key1': 1, 'key2': 3, 'key3': 2}
d2_y = {'key1': 1, 'key2': 2}

#checking for matching key values pairs
for key in d1_x:
    if key in d2_y and d1_x[key] == d2_y[key]:
        print(f"{key}: {d1_x[key]} is present in both x and y")