# ciphar_p56.py 
# 3/14/26
# Python 3.13.9
''' 
You are given the encrypted sentence: CLGUBA VF TERNG

Using a Shift of 13, what is the original (decyphered) message?
'''
#write a loop to show the 'Original Alphabet'
alphabet = ''
for i in range(65, 91):
    alphabet += chr(i)
print('alphabet = ', alphabet)

shift = 13
print('shift= ', shift, 'letters')

encrypted = ''
for i in range(65, 91):

    if i + shift < 91:
        encrypted += chr(i+shift)
    else:
        encrypted += chr(65 + (i + shift - 91))

print('encrypted =', encrypted)

encrypt = {}
decypher = {}

encrypt[' '] = ' '
decypher[' '] = ' '

for i in range(len(alphabet)):
    encrypt[alphabet[i]] = encrypted[i]
    decypher[encrypted[i]] = alphabet[i]

# given encrypted message
encrypted_message = "CLGUBA VF TERNG"

print('encrypt. sentence:', encrypted_message)

print(' ... decyphered : ', end='')
for i in range(len(encrypted_message)):
    print(decypher[encrypted_message[i]], end='')

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python ciphar_p56.py
alphabet =  ABCDEFGHIJKLMNOPQRSTUVWXYZ
shift=  13 letters
encrypted = NOPQRSTUVWXYZABCDEFGHIJKLM
encrypt. sentence: CLGUBA VF TERNG
 ... decyphered : PYTHON IS GREAT

'''