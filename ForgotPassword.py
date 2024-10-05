import random
otp=random.randint(000000,100000)

mypass=open("Pass.txt","r")
check=input("Enter your password or press 'f' if forgot password: ")

if check=='f':
    print("Here is your OTP for login",otp)
    user=int(input("Enter the OTP to login: "))
    if user==otp:
        print("Login succesfull")
        passwordNew=input("Enter your new Password:")
        mypass=open("Pass.txt","w")
        mypass.write(passwordNew)
        print("Your password has been changed")
    else:
        print("Wrong OTP")
        exit()    
elif check==mypass.read():
    print("Login succesfull")
else:
    print("Wrong Password")
            