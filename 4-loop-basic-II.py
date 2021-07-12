# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

big_list = [-1, 3, 5, -5]

def biggie():
    for x in range(0, len(big_list)):
        if big_list[x] > 0:
            big_list[x] = "big"

biggie()

print(big_list)

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
countlist = [1,6,-4,-2,-7,-2]

def count_postives():
    t = 0
    z = len(countlist) - 1
    for x in range(0, len(countlist)):
        if countlist[x] > 0:
            t = t + 1
    countlist[z] = t
count_postives()
print(countlist)
# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(list):
    t = 0
    for x in range(0, len(list)):
        t = list[x] + t
    print(t)
    return t
    
sum_total([1,2,3,4])
sum_total([6,3,-2])
# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def average(list):
    t = 0
    z = len(list)
    for x in range(0, len(list)):
        t = list[x] + t

    print(t/z)
    return t/z
average([1,2,3,4])
# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(list):
    print(len(list))
    return len(list)

length([37,2,1,-9])
length([])
# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(list):
    if len(list) != 0:
        t = list[0]
        for x in range(0, len(list)):
            if list[x] < t:
                t = list[x]
        print(t)
        return t
    else:
        print("False")
        return False

minimum([37,2,1,-9])
minimum([])
# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(list):
    if len(list) != 0:
        t = list[0]
        for x in range(0, len(list)):
            if list[x] > t:
                t = list[x]
        print(t)
        return t
    else:
        print("False")
        return False

maximum([37,2,1,-9])
maximum([])

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(list):
    dict = {}
    sum = 0
    minimum = list[0]
    maximum = list[0]
    for x in range(0, len(list)):
        sum = list[x] + sum
        if list[x] < minimum:
                minimum = list[x]
        if list[x] > maximum:
                maximum = list[x]
    dict["sumTotal"] = sum
    dict["average"] = sum/len(list)
    dict["minimum"] = minimum
    dict["maximum"] = maximum
    dict["length"] = len(list)

    print(dict)
    return dict

ultimate_analysis([37,2,1,-9])
# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(list):
    list.reverse()
    print(list)
    return list
reverse_list([37,2,1,-9])