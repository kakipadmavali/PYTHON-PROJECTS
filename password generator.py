import random 
characters="AZXCVBNMLKJHGFDSAQWERTUYIOP1234567890@#_$!"
password =""
for i in range(12):
    password+=random.choice(characters)
print(password)   