# allPrimes_p45.py 
# Gautam Rao
# 2/21/26
# Python 3.13.9
'''
Write a program that calculates and shows all prime numbers between 3 - 100.

Prime numbers can only be evenly (remainder 0) divided by itself and 1.

'''

# 1st loop: numbers 3 to 100
for N in range(3, 101):                 
    # 2nd loop: 2 to N-1
    for J in range(2, N):               
        # 3a) Not prime
        if N % J == 0:                  
            # stop checking this N
            break                       
        # 3b) Checked all J's
        if N % J != 0 and J == N - 1:   
            print(N)

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python allPrimes_p45.py
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97

'''