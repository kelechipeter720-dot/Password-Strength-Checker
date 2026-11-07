name = input (" what is your name\n")
score=0
while True:
    password= str (input ("enter your password \n"))
    if len(password)< 10: 
        print(" password too shoort ")
    else :
        print ("lenght is okay ")
        score += 1
    has_number = False
    has_capital= False
    has_special =False
    for ch in password:      
        
        if ch.isdigit():
            has_number = True
            
        if ch.isupper():
         has_capital= True
        
        if ch in "@!#$" :
            has_special= True 
    if has_number :
        print ("has number")
        score+=1
    else: 
        print ("no number ")  

    if has_capital:
        print (" has capital")
        score+=1
    else :
        print (" no capital")    
    if has_special:
        print("has special")
        score+=1
    else:
        print(" no specials ")    
    print ("score=",score)            
    if score <2 :
        print ("weak password")
    elif score <3:
        print("medium") 
    elif score ==4:
        print("strong password ")  
        break     
