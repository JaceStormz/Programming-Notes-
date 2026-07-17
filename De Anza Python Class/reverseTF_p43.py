# reverseTF_p43.py 
# 2/21/26
# Python 3.13.9
'''
The function returns the sorted list in ascending order if parameter 'reverse' is False. 
The function returns the sorted list in descending order if parameter 'reverse' is True.
'''

def sort(alist, reverse):
    n = len(alist)

    # Manual copy 
    new_list = [0] * n
    for i in range(n):
        new_list[i] = alist[i]

    # Selection sort
    for i in range(n):
        selected_index = i

        for j in range(i + 1, n):
            if reverse == False:  # Ascending
                if new_list[j] < new_list[selected_index]:
                    selected_index = j
            else:  # Descending
                if new_list[j] > new_list[selected_index]:
                    selected_index = j

        # Swap values
        temp = new_list[i]
        new_list[i] = new_list[selected_index]
        new_list[selected_index] = temp

    return new_list

# execute the code
alist = [5,1,4,3,2]

print(sort(alist, False))
print(sort(alist, True))

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python reverseTF_p43.py                                                                                              
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]

'''