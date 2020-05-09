position=[0,0]
condition =True

while condition == True:
    command=input("Enter the direction (L,R,U,D) --- ")[0]
    if command.islower():
        command=command.upper()
    
    if command=="L":
        temp=position[0]
        position.pop(0)
        position.insert(0,temp-1)
    
    elif command=="R":
        temp=position[0]
        position.pop(0)
        position.insert(0,temp+1)
    
    elif command=="U":
        temp=position[1]
        position.pop(1)
        position.insert(1,temp+1)
    
    elif command=="D":
        temp=position[1]
        position.pop(1)
        position.insert(1,temp-1)
    
    else:
        print("Invalid Command !")
    
    print()
    print(position)
    x=input("More Commands ? (y/n) ---")[0] 
    if x=="n" or x=="N":       
        condition=False

print()    
print("Final Position --- ",position)    