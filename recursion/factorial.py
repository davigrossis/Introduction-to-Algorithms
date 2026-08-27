def fat(x):
     if x == 1: #base
          return 1
     else:
       return x * fat(x - 1) #recurssivo

     
print(fat(5))