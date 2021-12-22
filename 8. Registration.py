#Pin creation for phone

#does he already have an account?
account = input("Do you want to register an Account?")
if account == "yes":
    #input data
    userName = input("Input Username\n")
    pin = input("Input Password\n")
    loop = True
    while loop:
        #only allow valid Inputs
        if len(userName.split()) != 0:
            print("Your Username is:", userName)
        else:
            print("No valid Username")
            userName = input("Input Username\n")
        #pin has to be a number
        try:
            validPin = int(pin)
            print("Your Pin is:", validPin)
            loop = False
        except:
            print("Not a valid pin")
            pin = input("Input Pin\n")
    #write the valid Inputs onto a textfile
    with open("8. Registration.txt", "w") as register:
        register.writelines("Username: ")
        register.writelines(userName.lower())
        register.writelines("\n")
        register.writelines("Pin: ")
        register.writelines(pin.lower())

#if he already has an account
else:
    userName = input("Input Username: ")
    pin = input("Input Pin: ")

    #read the txt file and compare
    with open("8. Registration.txt", "r") as login:
        checkData = login.read()
        #make sure the right parts are read i.e beginning at the name and ending with it
        beginningName = 10
        endingName = 10+len(userName)
        compareName = checkData[beginningName:endingName]

        #same with pin
        beginningPin = 10+len(userName) + 6
        endingPin = beginningPin + len(pin)
        comparePin = checkData[beginningPin:endingPin]
        print(comparePin)

    #if they are the same, it was succesfull, else it was the wrong data     
    if compareName == userName and comparePin == pin:
        print("You have succesfully logged in")
    else:
        print("Wrong data, pls try again")
