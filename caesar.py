print("enter 1 to encode and 2 to decode")
choice=int(input())
#input choice
if choice not in [1,2]:
    print("error, unknown value")
    exit()
if choice == 1:
    #encoding using caesar cipher
    print("enter your string")
    data=input()
    print("enter shift value")
    val=int(input())
    cap=0
    encoded=""
    for x in data:
        y=ord(x)
        if y in range(65,91):
            y+=32
            cap=1
        if y in range(97,123):
            y+=val
            if y>122: y-=26
        if cap==1: y-=32
        encoded+=chr(y)
        cap=0
    print(encoded)
else:
    #decoding via caesar cipher
    print("enter your string")
    data=input()
    print("enter 1 if shift value is known, otherwise enter 0")
    choice=int(input())
    if choice not in [1,0]:
        print("unknown value")
        exit()
    if choice ==1: 
        print("enter shift value")
        val=int(input())
        cap=0
        decoded=""
        for x in data:
            y=ord(x)
            if y in range(97,123):
                y-=32
                cap=1
            if y in range(65,91):
                y-=val
                if y<65 :
                    y+=26
            if cap==1: y+=32
            decoded+=chr(y)
            cap=0
        print(decoded)
    else: # CAUTION THIS WILL NOT ALWAYS PRODUCE CORRECT OUTPUT
        print("shift value unknown, taking the most occuring character as 'e'") # in english, the most occured alphabet across all words is 'e'
        most_common = max(set(data), key=data.count)
        print("most common character is "+most_common+", taking it as e")
        diff=ord('e')-ord(most_common)
        cap=0
        decoded=""
        for x in data:
            y=ord(x)
            if y in range(97,123):
                y-=32
                cap=1
            if y in range(65,91):
                y+=diff
                if y<65 :
                    y+=26
            if cap==1: y+=32
            decoded+=chr(y)
            cap=0
        print(decoded)