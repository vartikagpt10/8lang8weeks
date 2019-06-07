from sys import exit
def goldroom():
    print("this room is full of gold. how much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        howmuch = int(choice)
    else:
        dead("man, learn to type a number.")

    if howmuch < 50:
        print("nice, you are not greedy, you you win!")
        exit(0)
    else:
        dead("you greedy bastard!")

def bearroom():
    print("blah blah blah")
    bearmoved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("boooo")
        elif choice == "yayyyy" and not bearmoved:
            print("boreddddd")
            bearmoved = True
        elif choice == "hehe" and bearmoved:
            print("stoooopid hooooman")
        else:
            print("fo!")

start()