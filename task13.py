numbers = [1, 34, 23, 56, 98, 12, 122, 121, 33, 12, 34]

max_num = numbers[0]

for number in numbers:
    if number >= max_num:
        max_num = number
        
print(max_num)