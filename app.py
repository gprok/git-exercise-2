
# Calculates power of raised to b
def power_of(a, b):
    return a ** b #fixed


# Caclulates ths sum of all numbers in the data list
def list_total(data):
    total = 0
    for number in data:
        total += number
    return total 


# Calculates the average of the data in the list
def average_of_list(data):
    total = list_total(data) 
    avg = total / len(data)
    return avg



# Should print 9
print(power_of(3, 2))

# Should print 12
print(list_total([3, 4, 5]))

# Should print 4
print(average_of_list([3, 4, 5]))



