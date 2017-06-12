print("Hello, World.")

name = input("Name:")

print("Hello", name)

while True:
    
    print("Would you like to play Mario", name,"?")
    play = input("Y or N?")

    if play == "Y":
        print("Alright!")
        break
    elif play == "N":
        print("\'Tis a shame!")
        break
    else:
        print("Error, try again.")
        continue
