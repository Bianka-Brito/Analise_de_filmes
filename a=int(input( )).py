a=int(input( ))
b=int(input( )) #int sempre fora do input 
print(a+b)
print(a-b)
print(a*b)

import math
import os
import random
import re
import sys

n = int(input())


if n %2 !=0: #verirfica de a divisao do numero por 2 é igual a 0
    print("Weird")
     
elif 2 <= n <= 5:
    print("Not Weird")

elif 6 <= n <= 20:
    print("Weird")
    
else:
    print("Not Weird")