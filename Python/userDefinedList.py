# 08/11/2026
# userDefinedList.py

odd_num = []
userIn = int(input("Enter the max odd number: "))

def inputval():
    for _ in range(userIn):
        value = int(input("Enter a value: "))
        if value % 2 == 0:
            value += 1
        else:
            odd_num.append(value)
inputval()
print(odd_num)