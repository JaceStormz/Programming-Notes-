# fiveFunction_p42.py 
# 2/21/26
# Python 3.13.9
# write five functions such as sum() average() min() max()

def sum(first):
    total = 0
    for num in first:
        total += num
    return total

def average(first):
    count = 0
    for _ in first:
        count += 1
    return sum(first) / count

def min(first):
    smallest = first[0]
    for num in first[1:]:        
        if num < smallest:
            smallest = num
    return smallest

def max(first):
    largest = first[0]
    for num in first[1:]:       
        if num > largest:
            largest = num
    return largest

def main():
    numbers = [26, 23, 48, 32, 44, 21, 32, 20, 49, 48, 34]

    print(f"List: {numbers}")
    print(f"Sum = {sum(numbers)}")
    print(f"Average = {average(numbers):.1f}")
    print(f"Smallest = {min(numbers)}")
    print(f"Largest = {max(numbers)}")


if __name__ == "__main__":
    main()


'''
S C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python fiveFunction_p42.py                                                                                           
List: [26, 23, 48, 32, 44, 21, 32, 20, 49, 48, 34]
Sum = 377
Average = 34.3
Smallest = 20
Largest = 49

'''