#Prasunet task 3 checking strength of password

print("enter the password to check its strength")
pwd=input()
score=0

# Increment score of password by rarity of each character encountered in common passwords

for e in pwd:
    k=ord(e)
    if k in range(97,123):
        score +=1
    elif k in range(65,91):
        score +=2
    elif k in range(48,58):
        score +=3
    else:
        score +=5
# Further changing the score based on how long the password is
score *= len(pwd)/10

if score<10:
    print("password is too weak")
elif score<20:
    print("weak password")
elif score<30:
    print("average password")
elif score<50:
    print("strong password")
else:
    print("secure password")