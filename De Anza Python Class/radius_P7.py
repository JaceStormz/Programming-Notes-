# radius_P7.py 
# Gautam Rao
# 1//15/26
# Python 3.13.9
# Program that takes radius input from user then calculates the circumference and area of a circle

# Ask the user for the radius
radius = float(input("Enter the radius of the circle: "))

# Validate input
if radius <= 0:
    print("Error: The radius must be a positive number.")
else:
    
    # Calculate circumference and area
    circumference = 2 * 3.1415 * radius
    area = 3.1415 * radius ** 2

    # Display results
    print("The entered radius is: %.1f" %radius)
    print("Circumference of the circle: %.1f" %circumference )
    print("Area of the circle:  %.1f" %area)

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python radius_P7.py
Enter the radius of the circle: -1
Error: The radius must be a positive number.
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python radius_P7.py
Enter the radius of the circle: 5
The entered radius is: 5.0
Circumference of the circle: 31.4
Area of the circle:  78.5
'''