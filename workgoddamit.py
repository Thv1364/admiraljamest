# fullbi = str(1101)
# listbi = list(fullbi)
# print(listbi)
a=1

index=0
newbi=[]
result=0
want=int(input("Do you want a binary number or a decimal number? Type 1 for binary (as in you want 1010101) and type 9 for decimal (as in you also want 10101010 but also 78) \n"))




if want==1:
    
    fullde=int(input("what do you want? \n"))
    newde=fullde

    if(fullde==1):
        result=1
    elif(fullde==2):
        result=2
    if(fullde==0):
        result=0
    else:
        while(a<fullde):
            a=a*2
            index=index+1
        newbi = [0] * index
        while(a>=1):
            if a<=newde:
                newbi[index]=1
                # print("hi" + str(a)+"ok"+str(newde))
                newde=newde-a
            # else:
            #     print("nope" + str(a)+"ok"+str(newde))
            a=a/2
            #print(a)
            index=index-1
            #print(newbi)
        result= ''.join(map(str, newbi))
    print("\n \n the binary answer is " + str(result))

elif want==9:
    inp=input("what do you want \n")
    lengt=len(inp)
    arra=list(inp)
    c=1
    for x in reversed(arra):
        result=c*int(x)+result
        c=c*2
        
    print("\n \n Your decimal number is " + str(result))   

else:
    print("idiot don't type in a different number, either 1 or 9 (which btw is 1001)")


