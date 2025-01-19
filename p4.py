students=["ragini","marsh","anushka","sonakshi","tejas","abhay","mom","dad"]
while True:
    print("Hi! My name is AI")
    name=input("what is your name?:").strip().lower()

    if name in students:
        print("Hello {}!".format(name))
        remove=input("would you like to be removed from the system(y/n)?:").strip().lower()
    
        if remove=="y":
            students.remove(name)
        elif remove=="n":
            print("no problem, i didn't want you to leave anyways!")
        
    else:
        print("hmmm I dont think i have met you yet {}".format(name))
        add_me=input("would you like to be added to the system (y/n)?:").strip().lower()
        if add_me=="y":
            students.append(name)
            print(students)
        elif add_me=="n":
            print("no worries, see you around!")
        
        
    
    
       
        



