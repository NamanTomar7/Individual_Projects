import random as rd
guess=rd.randint(1,3)

user=int(input("\tPlace your move:-\n1.Rock\t2.Paper\t3.Scissor\n"))

if guess==1:
    move="Rock"
elif guess==2:
    move="Paper"
elif guess==3:
    move="Scissor"            

if user==1 or user==2 or user==3:
    if guess==user:
        print(f"\nOhh! Computer chose {move} too, Its a tie")
    elif guess==1 and user==2:
        print(f"Wooho! you won computer chose {move}")
    elif guess==1 and user==3:
        print(f"Defeat! computer chose {move}")
    elif guess==2 and user==3:
        print(f"Wooho! you won computer chose {move}") 
    elif guess==2 and user==1:
        print(f"Defeat! computer chose {move}")       
    elif guess==3 and user==1:
        print(f"Wooho! you won computer chose {move}")
    elif guess==3 and user==2:
        print(f"Defeat! computer chose {move}")
else:
    print("\nInvalid Choice")
    exit()      