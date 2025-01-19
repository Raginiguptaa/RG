films={
    "Tarzon":[15,5],
    "Ghost Busters":[12,5],
    "Bourne":[18,5],
    "finding Dory":[13,5]
    }
while True:
    choice=input("what film would you like to watch?:").strip().title()

    if choice in films:
        age=int(input("How old are you?:").strip())
        #check user age
        if age>=films[choice][0]:
            #check enough seats
            seats= films[choice][1]
            if seats>0:
                print("enjoy the film!")
                films[choice][1]=films[choice][1]-1 
            else:
                print("sorry, we are sold out!")
        else:
            print("you are too young to see that film!")
    else:
        print("we dont have that film...")
                


        
    
    
       
        



