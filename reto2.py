numString= "443355555566604466690277733099966688"
numCounter = 0;
auxString= ''
finalString=''
for i in range(0,len(numString)):
    numCounter += 1

    if numString[i] == "0":
        auxString = ' '
    if numString[i] == "1":
        auxString = ''
    if numString[i] =="2":
        if numCounter ==1:
            auxString = "a"
        elif numCounter==2:
            auxString = "b"
        elif numCounter==3:
            auxString = "c"
    if numString[i] =="3":
            if numCounter ==1:
                auxString = "d"
            elif numCounter==2:
                auxString = "e"
            elif numCounter==3:
                auxString = "f" 
    if numString[i] =="4":
            if numCounter ==1:
                auxString = "g"
            elif numCounter==2:
                auxString = "h"
            elif numCounter==3:
                auxString = "i"
    if numString[i] =="5":
            if numCounter ==1:
                auxString = "j"
            elif numCounter==2:
                auxString = "k"
            elif numCounter==3:
                auxString = "l"
    if numString[i] =="6":
            if numCounter ==1:
                auxString = "m"
            elif numCounter==2:
                auxString = "n"
            elif numCounter==3:
                auxString = "o"
    if numString[i] =="7":
            if numCounter ==1:
                auxString = "p"
            elif numCounter==2:
                auxString = "q"
            elif numCounter==3:
                auxString = "r"
            elif numCounter==4:
                auxString = "s"
    if numString[i] =="8":
            if numCounter ==1:
                auxString = "t"
            elif numCounter==2:
                auxString = "u"
            elif numCounter==3:
                auxString = "v"
    if numString[i] =="9":
            if numCounter ==1:
                auxString = "w"
            elif numCounter==2:
                auxString = "x"
            elif numCounter==3:
                auxString = "y"
            elif numCounter==4:
                auxString = "z"
    if i < len(numString)-1 :
        if (numString[i] != numString[i+1]) or numCounter==3:
            finalString += auxString
            numCounter = 0

finalString += auxString

print(finalString)


    