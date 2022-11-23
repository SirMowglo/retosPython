#Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0
import random

array = []
counter= 0
counterFinal = 0
mostFrecuent= 0

for num in range(0,10):
    array.append(random.randint(0,5))

for i in range(0,len(array)):
    counter =0
    for j in range(0,len(array)):
        if array[i] == array[j]:
            counter += 1
        if counter>counterFinal:
            counterFinal = counter
            mostFrecuent =array[i]
        
if array == []:
    print(0)
else:
    print("El mas frecuente es: "+str(mostFrecuent)+ " y se repite "+ str(counterFinal) +" veces")