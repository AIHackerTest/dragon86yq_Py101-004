from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    next = input('<')
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man,learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy. you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_move = False

    while True:
        next = input(">input take honey or taunt bear or open door?")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_move:
            print("The bear has moved frome the door.")
            bear_move = True
        elif next == "taunt bear" and bear_move:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_move:
            gold_room()
        else:
             print("I got on idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    next = input(">input flee or head?")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room

def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are in a dark room.")
    print("Thee is a door to your right and left.")
    print("Which one do you take?")
    next = input("> input left or right?")
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
