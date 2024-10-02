print("\tWELCOME TO DOMINOS")

print("\n\t\tMENU")
print("Pizza\n")
menu1={"margherita":119,"peppy paneer":269,"cheese and corn":189,"chicken pizza":329,"cheese volccano":209}
for x,y in menu1.items():
    print(f"{x}:{y}")
print("\ngarlic bread and more\n")
menu2={"stuffed garlic bread":159,"garlic breadsticks":109,"mexican taco":139,"burger pizza":119}
for x,y in menu2.items():
    print(f"{x}:{y}")
print("\nBeverages\n")
menu3={"pepsi":60,"mirinda":60,"water":20,"ice tea":60}
for x,y in menu3.items():
    print(f"{x}:{y}")
print("\nDesrerts\n")
menu4={"choco lava":109,"red velvet":139,"mouse cake":109}
for x,y in menu4.items():
    print(f"{x}:{y}")

menu={**menu1,**menu2,**menu3,**menu4}
total=0
n=int(input("\tEnter total number of Orders you want to order:"))

for i in range(n):
    ele=input(f"Enter Order {i+1}:")
    if ele in menu:
        print(f"Your Order of {ele} has been added")
        total+=menu[ele]
    else:
        print(f"Sorry we dont serve {ele}")
        pass

print(f"Your total Bill to pay is: {total}")          