""" street = '1234 ShopStreet'
city = 'Bengluru'
country = 'India'
address = street + "\n" + city + "\n" + country
print(address)
 """
#output
'''
1234 ShopStreet
Bengluru
India

'''
#########################
""" Phrase = "Earth revolves around the sun"
print(Phrase[6:15])
print(Phrase[-3:]) """
#output :
'''
revolves 
sun
'''
#########################
""" x = "carrots, green beens, chik peas, potatoes"
y = "apples, bananas, blueberries, oranges"
print(f"I eat {x} and {y} daily") """
#output: I eat carrots, green beens, chik peas, potatoes and apples, bananas, blueberries, oranges daily
s = "maine 200 bananas khaye"
print( s.replace("200","10").replace("bananas", "samosas"))