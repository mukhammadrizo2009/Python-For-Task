grades = [2,3,4,5,3,3,4,5,5,5,5,5,3,3,4,4,5,5,5]

total = 0

for grade in grades:
    total += grade
    
avarege = total / len(grades)
    
print(f"Umumiy baho: {total}")
print(f"O'rtacha baho: {avarege}")