# asc2_p18.py
# 1//23/26
# Python 3.13.9
# Program that displays the characters in the ASCII character table from ! to ~. 

# ASCII value for '!' this is the startinf value hard coded
ascii_value = 33   
count = 0

# ASCII value for '~' or 126
while ascii_value <= 126:  
    # prints from ! to ~ with a space in the middle setting the ascii to char to print
    print(chr(ascii_value), end=" ") 
    count += 1
    # limits each row to ten chars but iterates through if less than that or zero
    if count == 10:
        print()
        count = 0
    
    ascii_value += 1


'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python asc2_p18.py                                                                                                   
! " # $ % & ' ( ) * 
+ , - . / 0 1 2 3 4 
5 6 7 8 9 : ; < = >
? @ A B C D E F G H
I J K L M N O P Q R
S T U V W X Y Z [ \
] ^ _ ` a b c d e f
g h i j k l m n o p
q r s t u v w x y z
{ | } ~

'''