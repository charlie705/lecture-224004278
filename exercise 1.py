def isperfect(number):
     if number<1:
        return False
     sum=0
     for i in range(1,number):
         if number%i==0:
             sum+=i
             return sum==number
         #print(isperfect(28))
         #print(isperfect(12))

         def displayperfectnumbers(start,end):
            perfectnumbers=[]
            for i in range(start,end+1):
                if isperfect(i):
                   perfectnumbers.append(i)
                   return perfectnumbers
                print(displayperfectnumbers(1,1000000))

 

    

    