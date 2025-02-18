

import random

uper_alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N",
               "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower_alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
                "o","p","q","r","s","t","u","v","w","x","y","z"]
number=["1","2","3","4","5","6","7","8","9","0",]
character=["!","@","#","$","%","&","*","(",")","_","?","/"," "]

combined_list= uper_alphabet+lower_alphabet+number+character

print("The minimum length of the password is 4")
print("")
length = int(input("Enter the length of the password :" ))

if (length>=4):
    def Generate():
        random_numbers = [
            random.choice(uper_alphabet),
            random.choice(lower_alphabet),
            random.choice(number),
            random.choice(character)
        ]
        random_numbers += random.sample(combined_list, length-4 )

        random.shuffle(random_numbers) 

        return ''.join(random_numbers)

else:
    print("Warning!\nMinimum password length is 4")
    


print(f"Your password is : {Generate()}")






























    
