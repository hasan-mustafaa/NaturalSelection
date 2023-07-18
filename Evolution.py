import random
import time
import winsound
import turtle as t

win = t.Screen()

end = False
global LFR


def on_close():
    global end
    end = True


def getcolor(code):
    code = code.split()
    for w in range(0, len(code)):
        code[w] = code[w][0]
        R = code.count('a') * 5  # R
        G = code.count('b') * 6  # G
        B = code.count('c') * 7  # B
        R += code.count('d') * 10  # R
        G += code.count('e')  # G
        B += code.count('f') * 2  # B
        R += code.count('g') * 15  # R
        G += code.count('h') * 11  # G
        B += code.count('i') * 4  # B
        R += code.count('j') * 3  # R
        G += code.count('k') * 8  # G
        R = int(((R / 16) - int(R / 16)) * 16)
        G = int(((G / 16) - int(G / 16)) * 16)
        B = int(((B / 16) - int(B / 16)) * 16)
        R = str(hex(R)[2:4])[0]
        G = str(hex(G)[2:4])[0]
        B = str(hex(B)[2:4])[0]
        return '#' + R + R + G + G + B + B


((t.getcanvas()).winfo_toplevel()).protocol("WM_DELETE_WINDOW", on_close)

t.penup()
t.shape("square")
t.speed(0)
global bitpos
global bitftr
global Lbitpos
global Lbitftr
global date
global cycle
global corpses
global todelete
date = 0
todelete = []
bitftr = []
bitpos = []
Lbitftr = []
Lbitpos = []
arate = []
brate = []
crate = []
drate = []
erate = []
frate = []
grate = []
hrate = []
irate = []
jrate = []
krate = []
bitamount = []
print('This is your opportunity to maximize your turtle window. Please go ahead and maximize it.')
for i in range(0, 20):
    t.setpos(0, 0)
    time.sleep(0.2)

# adding the criteria
while True:
    criteria = int(float(input(
        "Good evening.\nThis project depicts evolution in the sense every creature needs to learn on its own to fit your criteria.\n"
        "Your criteria will be a region. You can have up to 12 regions but no more than that.\n"
        "Please type in a number telling me how many criterias you would like to add.\n")))
    if 0 <= criteria <= 12:
        break
    else:
        print("Sorry, that's not a valid value.")

M = []
C = []
MXC = []
XX = []
YY = []
t.hideturtle()
print("ok, it's time for the crafting!")
time.sleep(1)
for e in range(0, criteria):
    if bool(
            input(
                "Would you like to use Y=MX+C for this? If so, simply say yes.\nThe other option is simple X and Y.\n").upper().split()[
                0] == 'YES'):
        while True:
            placeholder = float(input("Please type in the value of M\n"))
            M.append(placeholder)
            placeholder = float(input(
                "Please type in the value of C.\nRemember, the screen dimentions are -700 to 700(x), and -350 to 350(y)\n"))
            C.append(placeholder)
            while True:
                placeholder = input(
                    "Would you want the criteria(y) to be greater than MX+C or lower than MX+C?\nPlease use symbols '<','>'.\n")
                if placeholder[0] in ('<', '>'):
                    MXC.append(placeholder)
                    break
                else:
                    print("Sorry, we didn't really catch that.")
            t.clear()
            t.setpos(0, C[e])
            t.pendown()
            print("The shaded region is where bits must be to survive\n\n")
            t.begin_fill()
            t.setpos(-700, (M[e] * -700) + C[e])
            if MXC[e] == '<':
                t.setpos(700, (M[e] * -700) + C[e])
            if MXC[e] == '>':
                t.setpos(-700, (M[e] * 700) + C[e])
            t.setpos(700, (M[e] * 700) + C[e])
            t.end_fill()
            t.penup()
            for i in range(0, 20):
                t.setpos(0, C[e])
                time.sleep(0.2)
            if bool(input('Your region is drawn on the turtle screen.\n'
                          "If you are satisfied with it, please type in the letter\n"
                          "'Y'\n"
                          "Any other letter shall give you the opportunity to re-choose your answer.\n")[
                        0].upper() == 'Y'):
                t.clear()
                break
            else:
                print("Alright, try it again!")
                M.pop(-1)
                C.pop(-1)
                MXC.pop(-1)
                t.clear()
    else:
        if input('Do you want to check your criteria by X or Y\n')[0].upper() == 'X':
            while True:
                placeholder = input("What would you like your x to be?\n"
                                    "Please format your answer with < or > sign to show where bits should be to survive.\n"
                                    "Example: \n>100\n")
                if placeholder[0] in ('<', '>') and len(placeholder) > 1:
                    print("The shaded region is where bits must be to survive\n\n")
                    if placeholder[0] == '<':
                        t.setpos(int(placeholder[1:len(placeholder)]), 400)
                        t.begin_fill()
                        t.setpos(int(placeholder[1:len(placeholder)]), 400)
                        t.setpos(-700, 400)
                        t.setpos(-700, -400)
                        t.setpos(int(placeholder[1:len(placeholder)]), -400)
                        t.end_fill()
                    elif placeholder[0] == '>':
                        t.setpos(int(placeholder[1:len(placeholder)]), 400)
                        t.begin_fill()
                        t.setpos(int(placeholder[1:len(placeholder)]), 400)
                        t.setpos(700, 400)
                        t.setpos(700, -400)
                        t.setpos(int(placeholder[1:len(placeholder)]), -400)
                        t.end_fill()
                    if bool(input('Are you satisfied with this criteria?\n')[0].upper() == 'Y'):
                        XX.append(placeholder)
                        t.clear()
                        break
                    else:
                        print("It seems like a 'no'.")
                        t.clear()
                else:
                    print("Sorry, we didn't really catch that.")
        else:
            while True:
                placeholder = input("What would you like your Y to be?"
                                    "Please format your answer with < or > sign to show where bits should be to survive."
                                    "Example: \n>100\n")
                if placeholder[0] in ('<', '>') and len(placeholder) > 1:
                    print("The shaded region is where bits must be to survive\n\n")
                    if placeholder[0] == '<':
                        t.setpos(-700, int(placeholder[1:len(placeholder)]))
                        t.begin_fill()
                        t.setpos(-700, int(placeholder[1:len(placeholder)]))
                        t.setpos(-700, -400)
                        t.setpos(700, -400)
                        t.setpos(700, int(placeholder[1:len(placeholder)]))
                        t.end_fill()
                    elif placeholder[0] == '>':
                        t.setpos(700, int(placeholder[1:len(placeholder)]))
                        t.begin_fill()
                        t.setpos(700, int(placeholder[1:len(placeholder)]))
                        t.setpos(700, 400)
                        t.setpos(-700, 400)
                        t.setpos(-700, int(placeholder[1:len(placeholder)]))
                        t.end_fill()
                    if bool(input('Are you satisfied with this criteria?\n')[0].upper() == 'Y'):
                        YY.append(placeholder)
                        t.clear()
                        break
                    else:
                        print("It seems like a 'no'.")
                        t.clear()
                else:
                    print("Sorry, we didn't really catch that.")

# starting the big questions
t.clear()
t.showturtle()
LFR = []  # Last Feature Run

bitsize = int(input("What size would you like the bits to be? \nThe default is '1'.\nThis will effect the bitmax.\n"))
if bitsize > 5:
    bitsize = 5
print('Bitsize =', bitsize)
maxx = 680 - (bitsize * 20)
maxy = 360 - (bitsize * 20)
maxx = maxx / 20
maxy = maxy / 20
minx = maxx - maxx * 2
miny = maxy - maxy * 2
bitmax = round(1000 / (bitsize ** 2))
bitamt = int(input("How many bits do you want in the map\n"))
if bitamt > 1000 / (bitsize ** 2):
    bitamt = round(1000 / (bitsize ** 2))
print('Starting bits on map =', bitamt)

fcap = int(input("What is the maximum amount of features you want attributed?\n"))  # feature cap
print('feature cap =', fcap)

timer = int(input("How many seconds would you like to wait till the day ends? When the day ends, all bits who didn't "
                  "fit the criterias will be assassinated.\n"))
print("time till judgement is", timer)

ROE = abs(int(input("How rare should mutations be? The chance is 1 in ")))  # Rate Of Evolution
print("the rate of evolution is 1 in", ROE)

COR = abs(int(input("How rare should reproducing 2 children be? The chance is 1 in ")))  # Chance Of Reproduction
print("the rate of 2 children popping out of a parent is 1 in", ROE)

REPRODUCE = bool(input("Do you want creatures to reproduce with 2 children at all?\n")[0].upper() == 'Y')

COK = abs(int(input("How rare must successful murders be? The chance is 1 in ")))  # Chance Of Kill
print("the rate of successful murdering is 1 in", COK)

RBATS = bool(input("Do you want random bits in the start\n")[0].upper() == 'Y')  # Random Bits At The Start

RPAEOD = bool(input("Do you want surviving bits to move to random places at the end of the day?\n")[
                  0].upper() == 'Y')  # Random Position At End Of Day

order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5
a6 = 6
a7 = 7
a8 = 8
a9 = 9
a10 = 10
a11 = 11
NoWeight = 0
if input('Would you like to change the weights of the 11 different features?\n')[0].lower() == 'y':
    NoWeight = input(
        'The weights are from most common to least. \nThe weights are;\n\n1,Forward\n2,Move right\n3,Move left\n4, '
        'Backwards\n5, Diagonal(Y=X)\n6, Diagonal(Y=-X)\n7, Repeat(features)(amount of times)\n8, If (value) of (axis) is '
        '(< or >) position, run (features)\n9, Useless feature\n10, Follow closest bit\n11, Kill closest bit\n'
        'If you however would want a every feature to have an equal chance to occur, simply type in (=).\nTo '
        'continue, type anything in.')
    print('Ok then,')
    PAI = False  # proper answer inserted
    while not PAI:
        if NoWeight == '=':
            break
        PAI = True
        a1 = int(input('(Please enter a number)\nPlease type in the number you want as the weighted feature 1\n'))
        if a1 > 11 or a1 < 1:
            print('Error, please type again. Ranges are purely between 1 and 8.')
            PAI = False
    order.remove(a1)
    PAI = False
    while not PAI:
        if NoWeight == '=':
            break
        PAI = True
        a2 = int(input('(Please enter a number)\nPlease type in the number you want as the weighted feature 2\n'))
        if a2 > 11 or a2 < 1 or a2 not in order:
            print('Error, please type again. Ranges are purely between 1 and 8. Options are:', order)
            PAI = False
    order.remove(a2)
    PAI = False
    while not PAI:
        if NoWeight == '=':
            break
        PAI = True
        a3 = int(input('(Please enter a number)\nPlease type in the number you want as the weighted feature 3\n'))
        if a3 > 11 or a3 < 1 or a3 not in order:
            print('Error, please type again. Ranges are purely between 1 and 8. Options are:', order)
            PAI = False
    order.remove(a3)
    PAI = False
    while not PAI:
        if NoWeight == '=':
            break
        PAI = True
        a4 = int(input('(Please enter a number)\nPlease type in the number you want as the weighted feature 4\n'))
        if a4 > 11 or a4 < 1 or a4 not in order:
            print('Error, please type again. Ranges are purely between 1 and 8. Options are:', order)
            PAI = False
    order.remove(a4)
    PAI = False
    while not PAI:
        if NoWeight == '=':
            break
        PAI = True
        a5 = int(input('(Please enter a number)\nPlease type in the number you want as the weighted feature 5\n'))
        if a5 > 11 or a5 < 1 or a5 not in order:
            print('Error, please type again. Ranges are purely between 1 and 8. Options are:', order)
            PAI = False
    order.remove(a5)
    PAI = False
    while not PAI:
        if NoWeight == '=':
            break
        PAI = True
        a6 = int(input('(Please enter a number)\nPlease type in the number you want as the weighted feature 6\n'))
        if a6 > 11 or a6 < 1 or a6 not in order:
            print('Error, please type again. Ranges are purely between 1 and 8. Options are:', order)
            PAI = False
    order.remove(a6)
    PAI = False
    while not PAI:
        if NoWeight == '=':
            break
        PAI = True
        a7 = int(input('(Please enter a number)\nPlease type in the number you want as the weighted feature 7\n'))
        if a7 > 11 or a7 < 1 or a7 not in order:
            print('Error, please type again. Ranges are purely between 1 and 8. Options are:', order)
            PAI = False
    order.remove(a7)
    PAI = False
    while not PAI:
        if NoWeight == '=':
            break
        PAI = True
        a8 = int(input('(Please enter a number)\nPlease type in the number you want as the weighted feature 8\n'))
        if a8 > 11 or a8 < 1 or a8 not in order:
            print('Error, please type again. Ranges are purely between 1 and 8. Options are:', order)
            PAI = False
    order.remove(a8)
    PAI = False
    while not PAI:
        if NoWeight == '=':
            break
        PAI = True
        a9 = int(input('(Please enter a number)\nPlease type in the number you want as the weighted feature 9\n'))
        if a9 > 11 or a9 < 1 or a9 not in order:
            print('Error, please type again. Ranges are purely between 1 and 8. Options are:', order)
            PAI = False
    order.remove(a9)
    PAI = False
    while not PAI:
        if NoWeight == '=':
            break
        PAI = True
        a10 = int(input('(Please enter a number)\nPlease type in the number you want as the weighted feature 10\n'))
        if a10 > 11 or a10 < 1 or a10 not in order:
            print('Error, please type again. Ranges are purely between 1 and 8. Options are:', order)
            PAI = False
    order.remove(a10)
    PAI = False
    while not PAI:
        if NoWeight == '=':
            break
        PAI = True
        a11 = int(input('(Please enter a number)\nPlease type in the number you want as the weighted feature 11\n'))
        if a11 > 11 or a11 < 1 or a11 not in order:
            print('Error, please type again. Ranges are purely between 1 and 8. Options are:', order)
            PAI = False
    order.append(a1)
    order.append(a2)
    order.append(a3)
    order.append(a4)
    order.append(a5)
    order.append(a6)
    order.append(a7)
    order.append(a8)
    order.append(a9)
    order.append(a10)
    order.append(a11)

respawn = bool(input("Would you like all the bits to respawn after every bit dies?\n")[0].lower() == 'y')
developer = []
FFTS = []  # Features Forced To Stop
dateofkill = 0
if bool(input("Would you like to try developer mode?\n")[0].lower() == 'y'):
    while True:
        try:
            developer.append(str(int(input("\n\nDo you want to\n\n"
                                           "1) Disable murder.\n"
                                           "2) Delete murder gene till date entered.\n"
                                           "3) Stop certain features from occurring.\n"
                                           "4) Count cycles instead of seconds to evaluate the end of the day.\n"
                                           "5) Make kill genes only murder creatures also bearing kill gene.\n"
                                           "6) !O!V!E!R!L!O!A!D!\n"  # overload bit amounts
                                           "7) Beep when a creature gets murdered(only from another bit).\n"
                                           "8) Trace bits.\n"))))
            if developer[-1] == '1':
                COK = 0
            if developer[-1] == '6':
                bitamt = 2000 / (bitsize ** 2)
            if developer[-1] == '2':
                dateofkill = (int(input('What day do you want it on?\n')))
            if developer[-1] == '3':
                while True:
                    FFTS.append(str(int(input('\nOk, please type in a number. The options are:\n\n1,Forward\n2,'
                                              'Move right\n3,Move left\n4, Backwards\n5, Diagonal(Y=X)\n6, '
                                              'Diagonal(Y=-X)\n7, '
                                              'Repeat(features)(amount of times) times.\n8, If (value) of (axis) is ('
                                              '< or >) position, '
                                              'run (features)\n9, Useless feature\n10, Follow closest bit\n11, '
                                              'Kill closest bit\n'))))

                    if input('Is that all?')[0].upper == 'Y':
                        break
                    print('Alright,')
            if developer[-1] == '4':
                timer = int(input('How many cycles should it take to end a day?\n'))
            if input('Is that all the developing you want done?\n')[0].upper() == 'Y':
                break
            else:
                print("Alright! Keep going pal!")
        except:
            print("Sorry, I didn't really catch that")

developer = list(set(developer))
FFTS = list(set(FFTS))


# describing the bit logic

try:
    def stamp():
        t.setpos(t.xcor()-(10*bitsize), t.ycor()-(10*bitsize))
        t.begin_fill()
        t.setpos(t.xcor(), t.ycor()+(20*bitsize))
        t.setpos(t.xcor() + (20 * bitsize), t.ycor())
        t.setpos(t.xcor(), t.ycor() - (20 * bitsize))
        t.setpos(t.xcor() - (20 * bitsize), t.ycor())
        t.end_fill()
        t.setpos(t.xcor()+(10*bitsize), t.ycor()+(10*bitsize))


    def delete(pos):
        run = True
        if '2' in developer:
            if date <= dateofkill:
                run = False
        if random.randint(1, COK) == 1 and COK != 0 and run:
            counterrr = 0
            for ba in bitpos:
                if ba == pos:
                    if 'k' in list(map(lambda iiiii: iiiii[0],
                                       bitftr[counterrr].split())) and '5' in developer or '5' not in developer:
                        corpses.append(ba)
                        print('Bit at position', pos, 'tragically died after another Bit',
                              ['made fun of his mother.', 'ate him alive.', 'gave him an STD.',
                               'played a little too much with fire.', 'found out he had a different opinion than him.'][
                                  random.randint(0, 4)])
                        Lbitpos.append(bitpos[counterrr])
                        Lbitftr.append(bitftr[counterrr])
                        LFR.pop(counterrr)
                        bitpos.pop(counterrr)
                        bitftr.pop(counterrr)
                        if '7' in developer:
                            winsound.Beep(1000, 10)
                counterrr = counterrr + 1
        else:
            pass


    def regulate():
        counter = 0
        for oo in bitpos:
            if oo[0] < minx*20 or oo[0] > maxx*20 or oo[1] < miny*20 or oo[1] > maxy*20:
                print('Bit at pos', oo, 'spontaneously combusted after leaving the visible plane of existence.\n'
                      "His features were:", bitftr[counter])
                corpses.append(oo)
                Lbitpos.append(bitpos[counter])
                Lbitftr.append(bitftr[counter])
                LFR.pop(counter)
                bitpos.pop(counter)
                bitftr.pop(counter)
            counter += 1


    def f(distance):
        for i in range(0, int(distance)):
            t.forward(bitsize * 20)
            if t.pos() in bitpos:
                t.backward(bitsize * 20)
            if t.pos()[0] > maxx * 20:
                t.backward(bitsize * 20)
            if t.pos()[1] > maxy * 20:
                t.backward(bitsize * 20)
            if t.pos()[0] < minx * 20:
                t.backward(bitsize * 20)
            if t.pos()[1] < miny * 20:
                t.backward(bitsize * 20)


    def rw(distance):
        t.right(90)
        for i in range(0, int(distance)):
            t.forward(bitsize * 20)
            if t.pos() in bitpos:
                t.backward(bitsize * 20)
            if t.pos()[0] > maxx * 20:
                t.backward(bitsize * 20)
            if t.pos()[1] > maxy * 20:
                t.backward(bitsize * 20)
            if t.pos()[0] < minx * 20:
                t.backward(bitsize * 20)
            if t.pos()[1] < miny * 20:
                t.backward(bitsize * 20)
        t.left(90)


    def lw(distance):
        t.left(90)
        for i in range(0, int(distance)):
            t.forward(bitsize * 20)
            if t.pos() in bitpos:
                t.backward(bitsize * 20)
            if t.pos()[0] > maxx * 20:
                t.backward(bitsize * 20)
            if t.pos()[1] > maxy * 20:
                t.backward(bitsize * 20)
            if t.pos()[0] < minx * 20:
                t.backward(bitsize * 20)
            if t.pos()[1] < miny * 20:
                t.backward(bitsize * 20)
        t.right(90)


    def b(distance):
        for i in range(0, int(distance)):
            t.backward(bitsize * 20)
            if t.pos() in bitpos:
                t.forward(bitsize * 20)
            if t.pos()[0] > maxx * 20:
                t.forward(bitsize * 20)
            if t.pos()[1] > maxy * 20:
                t.forward(bitsize * 20)
            if t.pos()[0] < minx * 20:
                t.forward(bitsize * 20)
            if t.pos()[1] < miny * 20:
                t.forward(bitsize * 20)


    def cw(distance):
        f(distance)
        rw(distance)


    def acw(distance):
        f(distance)
        lw(distance)


    def rep(types, times):
        if '|' in times:
            times = times[0:-1]
        if '|' in types[0]:
            if types[0] == '|':
                types = types[1:len(types)]
        if '|' in types[len(types) - 1]:
            types = types[0:-1]
        counter = int(types.split(':')[0])
        types = types.replace(':', ' ', 1)
        types = types[1:len(types)]
        if '|' in types[0]:
            if types[0] == '|':
                types = types[1:len(types)]
        nocount = False
        count = 0
        placeholder = list(types)
        for q in placeholder:
            if q == '|':
                if nocount == False:
                    nocount = True
                else:
                    nocount = False
            if q == ':' and nocount == False:
                counter = counter - 1
                if counter > 0:
                    types = list(types)
                    types.pop(count)
                    types.insert(count, ' ')
            count = count + 1
        if type(types) == list:
            types = ''.join(types)
        for n in range(0, int(times)):
            decode(types)


    def u():
        pass


    def k(x, y, distance):
        x = int(x)
        y = int(y)
        distance = int(distance)
        for pos in bitpos:
            if pos[0] + x - distance <= distance:
                if pos[1] + y - distance <= distance:
                    todelete.append(pos)


    def follow(x, y, distance):
        global poss2, poss1
        x = int(x)
        y = int(y)
        distance = int(distance)
        closest = (100, 100)
        for pos in bitpos:
            if pos[0] + x - distance <= distance:
                if pos[1] + y - distance <= distance:
                    if pos[0] < closest[0] and pos[1] < closest[1]:
                        closest = pos
        poss1 = x
        poss2 = y
        if abs(closest[0]) >= abs(closest[1]):
            if closest[0] < x - bitsize * 20:
                poss1 = x - bitsize * 20
            elif closest[0] > x + bitsize * 20:
                poss1 = x + bitsize * 20
            else:
                poss1 = x
        else:
            if closest[1] < y - bitsize * 20:
                poss2 = y - bitsize * 20
            elif closest[1] > y + bitsize * 20:
                poss2 = y + bitsize * 20
            else:
                poss2 = y
        if (poss1, poss2) not in bitpos:
            t.setpos(poss1, poss2)


    def iff(x, y, axis, value, number, features):  # value is < or >
        if '|' in features[len(features) - 1]:
            features = features[0:-1]
        if '|' in features[0]:
            features = features[1:len(features)]
        x = int(x)
        y = int(y)
        number = int(number)
        counter = int(features.split(':')[0]) + 1
        features = features[1:len(features)]
        if '|' in features[0]:
            features = features[1:len(features)]
        nocount = False
        count = 0
        for q in list(features):
            if q == '|':
                if nocount == False:
                    nocount = True
                else:
                    nocount = False
            if q == ':' and nocount == False:
                counter = counter - 1
                if counter > 0:
                    features = list(features)
                    features.pop(count)
                    features.insert(count, ' ')
                    features = ''.join(features)
            count = count + 1
        if type(features) == list:
            features = ''.join(features)
        if axis == 'x':
            if value == '<':
                if x < number:
                    decode(features)
            elif value == '>':
                if x > number:
                    decode(features)
        elif axis == 'y':
            if value == '<':
                if y < number:
                    decode(features)
            elif value == '>':
                if y > number:
                    decode(features)


    # ending the bit logic
    # starting the decoding of the bit code
    features = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')


    def decode(featurelist):
        featurelist = featurelist.split()
        for i in range(0, len(featurelist)):
            if featurelist[i][0] == 'a':
                f(featurelist[i][1:len(featurelist[i])])
            elif featurelist[i][0] == 'b':
                cw(featurelist[i][1:len(featurelist[i])])
            elif featurelist[i][0] == 'c':
                acw(featurelist[i][1:len(featurelist[i])])
            elif featurelist[i][0] == 'd':
                temp = featurelist[i][1:len(featurelist[i])]
                temp = temp[::-1]
                temp = temp.replace('`', ' ', 1)
                temp = temp[::-1]
                temp = temp.split()
                rep(temp[0], temp[1])
            elif featurelist[i][0] == 'e':
                u()
            elif featurelist[i][0] == 'f':
                temp = featurelist[i][1:len(featurelist[i])]
                temp = temp.replace('!', ' ', 2)
                temp = temp.split()
                k(temp[0], temp[1], temp[2])
            elif featurelist[i][0] == 'g':
                temp = featurelist[i][1:len(featurelist[i])]
                temp = temp.replace('!', ' ', 2)
                temp = temp.split()
                follow(temp[0], temp[1], temp[2])
            elif featurelist[i][0] == 'h':
                temp = featurelist[i][1:len(featurelist[i])]
                temp = temp.replace('&', ' ', 5)
                temp = temp.split()
                iff(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5])
            elif featurelist[i][0] == 'i':
                rw(featurelist[i][1:len(featurelist[i])])
            elif featurelist[i][0] == 'j':
                lw(featurelist[i][1:len(featurelist[i])])
            elif featurelist[i][0] == 'k':
                b(featurelist[i][1:len(featurelist[i])])


    # ending the decoding of the bit code
    # starting the function for giving a starting bit random code

    def rana():
        ans = ('a' + str(random.randint(1, 10)))
        return ans


    def ranb():
        ans = ('b' + str(random.randint(-5, 5)))
        return ans


    def ranc():
        ans = ('c' + str(random.randint(-5, 5)))
        return ans


    def rand(x, y):
        ans = ('d|' + str(getfeature(1, x, y)) + '|`' + str(random.randint(1, 16)))
        return ans


    def rand2(x, y):
        ans = ('d|' + str(getfeature(2, x, y)) + '|`' + str(random.randint(1, 16)))
        return ans


    def rane():
        return 'e'


    def ranf(x, y):
        ans = ('f' + str(x) + '!' + str(y) + '!' + str(random.randint(1, 3) * bitsize * 20))
        return ans


    def rang(x, y):
        ans = ('g' + str(x) + '!' + str(y) + '!' + str(random.randint(1, 3) * bitsize * 20))
        return ans


    def ranh(x, y):
        value = '><'
        axis = 'xy'
        axis = axis[random.randint(0, 1)]
        if axis == 'y':
            number = random.randint(miny, maxy) * bitsize * 20
        if axis == 'x':
            number = random.randint(minx, maxx) * bitsize * 20
        ans = ('h' + str(x) + '&' + str(y) + '&' + str(axis) + '&' + str(value[random.randint(0, 1)]) + '&' + str(
            number) + '&|' + str(getfeature(1, x, y)) + '|')
        return ans


    def ranh2(x, y):
        value = '><'
        axis = 'xy'
        axis = axis[random.randint(0, 1)]
        if axis == 'y':
            number = random.randint(miny, maxy) * bitsize * 20
        if axis == 'x':
            number = random.randint(minx, maxx) * bitsize * 20
        ans = ('h' + str(x) + '&' + str(y) + '&' + str(axis) + '&' + str(value[random.randint(0, 1)]) + '&' + str(
            number) + '&|' + str(getfeature(2, x, y)) + '|')
        return ans


    def getfeature(typ, x,
                   y):  # fresh can either mean 'true' meaning ' ' instead of ':' placed between features. If it is 1,
        # make getting d or h rare.
        # use rana() ranb() ranc() rand(x, y) rane() ranf(x, y) rang(x, y) ranh(x, y)
        result = []
        join = ':'
        if typ == 'true':
            join = ' '
        cap = fcap
        if typ == 3:
            cap = 2
        for s in range(random.randint(int(cap / 2), cap)):
            if NoWeight != '=':
                choice = random.randint(0, 100)
                if 0 <= choice <= 1:
                    result.append(a11)
                elif 2 <= choice <= 7:
                    result.append(a10)
                elif 8 <= choice <= 14:
                    result.append(a9)
                elif 15 <= choice <= 22:
                    result.append(a8)
                elif 23 <= choice <= 31:
                    result.append(a7)
                elif 32 <= choice <= 41:
                    result.append(a6)
                elif 42 <= choice <= 51:
                    result.append(a5)
                elif 52 <= choice <= 62:
                    result.append(a4)
                elif 63 <= choice <= 74:
                    result.append(a3)
                elif 75 <= choice <= 86:
                    result.append(a2)
                elif 87 <= choice <= 100:
                    result.append(a1)
                loss = 0
                if '2' in developer:
                    if date < dateofkill:
                        loss = 1
                        result[-1] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10][random.randint(0,9)]

                if '3' in developer:
                    posibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
                    if loss == 1:
                        posibilities.pop(-1)
                    for y in FFTS:
                        posibilities.remove(y)
                    if result[-1] not in posibilities:
                        result[-1] = posibilities[random.randint(0, len(posibilities) - 1)]

                if result[-1] == 1:
                    result[-1] = rana()
                elif result[-1] == 2:
                    result[-1] = ('i' + str(random.randint(1, 10)))
                elif result[-1] == 3:
                    result[-1] = ('j' + str(random.randint(1, 10)))
                elif result[-1] == 4:
                    result[-1] = ('k' + str(random.randint(1, 10)))
                elif result[-1] == 5:
                    result[-1] = ranb()
                elif result[-1] == 6:
                    result[-1] = ranc()
                elif result[-1] == 7:
                    if typ == 1 and random.randint(0, 32) != 1:
                        result[-1] = [rana(), ranb(), ranc(), rane()][random.randint(0, 3)]
                    else:
                        if typ == 1 or typ == 3:
                            result[-1] = rand2(x, y)
                        elif typ == 2:
                            result[-1] = [rana(), ranb(), ranc(), rane()][random.randint(0, 3)]
                        elif typ == 'true':
                            result[-1] = rand(x, y)
                elif result[-1] == 8:
                    if typ == 1 and random.randint(0, 32) != 1:
                        result[-1] = ([rana(), ranb(), ranc(), rane()][random.randint(0, 3)])
                    else:
                        if typ == 1 or typ == 3:
                            result[-1] = (ranh2(x, y))
                        elif typ == 2:
                            result[-1] = ([rana(), ranb(), ranc(), rane()][random.randint(0, 3)])
                        elif typ == 'true':
                            result[-1] = ranh(x, y)
                elif result[-1] == 9:
                    result[-1] = rane()
                elif result[-1] == 10:
                    result[-1] = rang(x, y)
                elif result[-1] == 11:
                    result[-1] = ranf(x, y)
            else:
                result.append([rana(), ranb(), ranc(), rand(x, y), rane(), ranf(x, y), rang(x, y), ranh(x, y),
                               ('i' + str(random.randint(1, 10))), ('j' + str(random.randint(1, 10))),
                               ('k' + str(random.randint(1, 10)))][random.randint(1, 11)])
                loss = 0
                if '2' in developer and result[-1][1] == 'f' and date < dateofkill:
                    result[-1] = ([rana(), ranb(), ranc(), rand(x, y), rane(), ranf(x, y), rang(x, y), ranh(x, y),
                                  ('i' + str(random.randint(1, 10))), ('j' + str(random.randint(1, 10))),
                                  ('k' + str(random.randint(1, 10)))][random.randint(1, 11)])
                    loss = 1
                if '3' in developer:
                    posibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
                if loss == 1:
                    posibilities.pop(-1)
                for y in FFTS:
                    posibilities.remove(y)
                if ['balls', 'a', 'i', 'j', 'k', 'b', 'c', 'd', 'h', 'e', 'g', 'f'].index(result[-1][0]) not in posibilities:
                    result[-1] = posibilities[random.randint(0, len(posibilities)-1)]
                    if result[-1] == 1:
                        result[-1] = rana()
                    elif result[-1] == 2:
                        result[-1] = ('i' + str(random.randint(1, 10)))
                    elif result[-1] == 3:
                        result[-1] = ('j' + str(random.randint(1, 10)))
                    elif result[-1] == 4:
                        result[-1] = ('k' + str(random.randint(1, 10)))
                    elif result[-1] == 5:
                        result[-1] = ranb()
                    elif result[-1] == 6:
                        result[-1] = ranc()
                    elif result[-1] == 7:
                        if typ == 1 and random.randint(0, 32) != 1:
                            result[-1] = [rana(), ranb(), ranc(), rane()][random.randint(0, 3)]
                        else:
                            if typ == 1 or typ == 3:
                                result[-1] = rand2(x, y)
                            elif typ == 2:
                                result[-1] = [rana(), ranb(), ranc(), rane()][random.randint(0, 3)]
                            elif typ == 'true':
                                result[-1] = rand(x, y)
                    elif result[-1] == 8:
                        if typ == 1 and random.randint(0, 32) != 1:
                            result[-1] = ([rana(), ranb(), ranc(), rane()][random.randint(0, 3)])
                        else:
                            if typ == 1 or typ == 3:
                                result[-1] = (ranh2(x, y))
                            elif typ == 2:
                                result[-1] = ([rana(), ranb(), ranc(), rane()][random.randint(0, 3)])
                            elif typ == 'true':
                                result[-1] = ranh(x, y)
                    elif result[-1] == 9:
                        result[-1] = rane()
                    elif result[-1] == 10:
                        result[-1] = rang(x, y)
                    elif result[-1] == 11:
                        result[-1] = ranf(x, y)

        if typ == 1 or typ == 2:
            result.insert(0, str(len(result)))
        if typ == 3:
            result = result[0]
        if len(result) > 0:
            if len(result) > 1 and typ != 3 and type(result) != str:
                return join.join(result)
            else:
                if type(result) == str:
                    return result
                else:
                    return result[0]
        else:
            print('ERROR NONE TYPE CREATED. typ ==', typ)


    def FATE(typ, x, y):
        choice = random.randint(1, 12)
        if 4 >= choice:  # replace
            if random.randint(0, 3) == 0:
                return getfeature(3, x, y)
            else:
                if typ == 'm':
                    return [rana(), ranb(), ranc(), rang(x, y), ('i' + str(random.randint(1, 10))),
                            ('j' + str(random.randint(1, 10))), ('k' + str(random.randint(1, 10)))][random.randint(0, 6)]
                if typ == 'c':
                    return [rand(x, y), ranh(x, y)][random.randint(0, 1)]
                if typ == 'r':
                    return [ranf(x, y), rane()][random.randint(0, 1)]
        elif choice == 5:  # new feature
            return 'NF'
        elif choice == 6:  # destroy feature
            return 'NA'
        elif choice == 7:  # YOU SWAP
            return 'SWAP'
        elif 8 <= choice <= 12:  # YOU remake feature
            return 'REP'


    def EVALUATE():
        countt = 0
        fail = []
        for d in bitpos:
            for g in range(0, len(MXC)):
                if MXC[g] == '<':
                    if d[1] > (M[g] * d[0]) + C[g]:
                        fail.append(countt)
                elif MXC[g] == '>':
                    if d[1] < (M[g] * d[0]) + C[g]:
                        fail.append(countt)
            for g in range(0, len(XX)):
                if XX[g][0] == '<':
                    if d[0] > int(XX[g][1:len(XX[g])]):
                        fail.append(countt)
                elif XX[g][0] == '>':
                    if d[0] < int(XX[g][1:len(XX[g])]):
                        fail.append(countt)
            for g in range(0, len(YY)):
                if YY[g][0] == '<':
                    if d[1] > int(YY[g][1:len(YY[g])]):
                        fail.append(countt)
                elif YY[g][0] == '>':
                    if d[1] < int(YY[g][1:len(YY[g])]):
                        fail.append(countt)
            countt += 1
        fail = list(set(fail))
        fail.sort(reverse=True)
        for c in fail:
            corpses.append(bitpos[c])
            Lbitpos.append(bitpos[c])
            Lbitftr.append(bitftr[c])
        for c in fail:
            bitftr.pop(c)
            bitpos.pop(c)


    def REFRESH():
        index = 0
        for kk in bitftr:
            bitftr[index] = force_refresh(kk, bitpos[index][0], bitpos[index][1])
            index += 1


    def force_refresh(items, x, y):
        if type(items) == str:
            items = items.split()
        for i in range(0, len(items)):
            if items[i][0] == 'd':
                pl = items[i]
                pl = pl[::-1].replace('|', ' ', 1).split()
                pl[0], pl[1] = pl[1][::-1], pl[0][::-1]
                pl[0] = pl[0].replace('|', ' ', 1).split()
                pl.insert(1, pl[0][1])
                pl[0] = pl[0][0]
                temporary = pl[1]
                nocount = False
                count = 0
                placeholder = list(temporary)
                for q in placeholder:
                    if q == '|':
                        if nocount == False:
                            nocount = True
                        else:
                            nocount = False
                    if q == ':' and nocount == False:
                        temporary = list(temporary)
                        temporary.pop(count)
                        temporary.insert(count, ' ')
                        temporary = ''.join(temporary)
                    count = count + 1
                pl[1] = force_refresh(temporary.split(), int(x), int(y)).replace(' ', ':')
                items[i] = '|'.join(pl)
            elif items[i][0] == 'f':
                pl = items[i]
                pl = (pl[1:len(pl)]).split('!')
                pl[0] = int(x)
                pl[1] = int(y)
                items[i] = 'f' + str(pl[0]) + '!' + str(pl[1]) + '!' + str(pl[2])
            elif items[i][0] == 'g':
                pl = items[i]
                pl = (pl[1:len(pl)]).split('!')
                pl[0] = int(x)
                pl[1] = int(y)
                items[i] = 'g' + str(pl[0]) + '!' + str(pl[1]) + '!' + str(pl[2])
            elif items[i][0] == 'h':
                pl = items[i][1:len(items[i])]
                pl = pl.replace('&', ' ', 5)
                pl = pl.split()
                pl[0] = str(int(x))
                pl[1] = str(int(y))
                temp = pl[5]
                temp = list(temp)[1:-1]
                nocount = False
                counter = 0
                for e in temp:
                    if e == '|' and nocount == True:
                        nocount = False
                    elif e == '|' and nocount == False:
                        nocount = True
                    if nocount == False and e == ':':
                        temp[counter] = ' '
                    counter += 1
                temp = ''.join(temp)
                pl[5] = '|' + str(force_refresh(temp.split(), int(x), int(y)).replace(' ', ':')) + '|'
                items[i] = 'h' + str('&'.join(pl))
        return ' '.join(items)


    def respawn():
        print("ALL CREATURES HAVE DIED THEREFORE THEY ARE RESPAWNING...")
        LFR = []
        bitpos = []
        if Lbitftr > bitmax:
            while True:
                if Lbitftr < bitmax:
                    break
                Lbitftr.pop(0)
        if Lbitpos > bitmax:
            while True:
                if Lbitpos < bitmax:
                    break
                Lbitftr.pop(0)
        ALL_POSSIBLE_POSITIONS = []
        tempx = []
        tempy = []
        for w in range(0, int(640 / (bitsize * 20))):
            tempx.append(-(w * 20 * bitsize))
        for w in range(0, int(640 / (bitsize * 20))):
            tempx.append(w * 20 * bitsize)
        for w in range(0, int(320 / (bitsize * 20))):
            tempy.append(-(w * 20 * bitsize))
        for w in range(0, int(320 / (bitsize * 20))):
            tempy.append(w * 20 * bitsize)
        for i in tempx:
            for g in tempy:
                ALL_POSSIBLE_POSITIONS.append((i, g))
        for i in range(0, bitamt):
            winsound.Beep(3700, 50)
            temppos = ALL_POSSIBLE_POSITIONS[random.randint(0, (len(ALL_POSSIBLE_POSITIONS) - 1))]
            ALL_POSSIBLE_POSITIONS.pop(ALL_POSSIBLE_POSITIONS.index(temppos))
            bitpos.append(temppos)
        bitftr = Lbitftr
        for i in range(0, bitamt):
            LFR.append((0, (bitftr[i].split())[0]))


    def new(index):
        bitftr.append(bitftr[index])
        LFR.append(LFR[index])
        newcheck = True
        while newcheck == True:
            newcheck = False
            temppos = (random.randint(minx, maxx) * bitsize * 20, random.randint(miny, maxy) * bitsize * 20)
            if temppos in bitpos:
                newcheck = True
        bitpos.append(temppos)


    def EVOLVE():
        win.bgcolor("light grey")
        chance = 0
        for j in range(0, len(bitftr)):
            temp = bitftr[j].split()
            for p in range(0, len(bitftr[j].split())):
                try:
                    if bitftr[j].split()[p][0] == 'a' or bitftr[j].split()[p][0] == 'b' or bitftr[j].split()[p][0] == 'c' or \
                            bitftr[j].split()[p][0] == 'g' or bitftr[j].split()[p][0] == 'i' or bitftr[j].split()[p][
                        0] == 'j' or bitftr[j].split()[p][0] == 'k':
                        chance = 'm'  # movement
                    elif bitftr[j].split()[p][0] == 'd' or bitftr[j].split()[p][0] == 'h':
                        chance = 'c'  # complex
                    elif bitftr[j].split()[p][0] == 'f' or 'e':
                        chance = 'r'  # rarity
                except:
                    break
                if random.randint(1, ROE) == 1:
                    placeholder = FATE(chance, bitpos[j][0], bitpos[j][1])
                    if placeholder == 'NF':
                        if not len(temp) >= fcap:
                            temp.insert(random.randint(0, len(temp)), getfeature(3, bitpos[j][0], bitpos[j][1]))
                    elif placeholder == 'NA':
                        temp.pop(random.randint(0, len(temp) - 1))
                    elif placeholder == 'SWAP':
                        place = random.randint(0, len(temp) - 1)
                        item = temp[place]
                        temp.pop(place)
                        temp.insert(random.randint(0, len(temp)), item)
                    elif placeholder == 'REP':
                        if bitftr[j].split()[p][0] == 'a':
                            temp[p] = rana()
                        elif bitftr[j].split()[p][0] == 'b':
                            temp[p] = ranb()
                        elif bitftr[j].split()[p][0] == 'c':
                            temp[p] = ranc()
                        elif bitftr[j].split()[p][0] == 'd':
                            temp[p] = rand(bitpos[j][0], bitpos[j][1])
                        elif bitftr[j].split()[p][0] == 'e':
                            temp[p] = rane()
                        elif bitftr[j].split()[p][0] == 'f':
                            temp[p] = ranf(bitpos[j][0], bitpos[j][1])
                        elif bitftr[j].split()[p][0] == 'g':
                            temp[p] = rang(bitpos[j][0], bitpos[j][1])
                        elif bitftr[j].split()[p][0] == 'h':
                            temp[p] = ranh(bitpos[j][0], bitpos[j][1])
                        elif bitftr[j].split()[p][0] == 'i':
                            temp[p] = ('i' + str(random.randint(1, 10)))
                        elif bitftr[j].split()[p][0] == 'j':
                            temp[p] = ('j' + str(random.randint(1, 10)))
                        elif bitftr[j].split()[p][0] == 'k':
                            temp[p] = ('k' + str(random.randint(1, 10)))
                    else:
                        temp[p] = placeholder
                bitftr[j] = ' '.join(temp)
        win.bgcolor("white")


    ALL_POSSIBLE_POSITIONS = []
    tempx = []
    tempy = []
    for w in range(0, int(640 / (bitsize * 20))):
        tempx.append(-(w * 20 * bitsize))
    for w in range(0, int(640 / (bitsize * 20))):
        tempx.append(w * 20 * bitsize)
    for w in range(0, int(320 / (bitsize * 20))):
        tempy.append(-(w * 20 * bitsize))
    for w in range(0, int(320 / (bitsize * 20))):
        tempy.append(w * 20 * bitsize)
    for i in tempx:
        for g in tempy:
            ALL_POSSIBLE_POSITIONS.append((i, g))
    if RBATS == True:
        for i in range(0, bitamt):
            winsound.Beep(3700, 5)
            temppos = ALL_POSSIBLE_POSITIONS[random.randint(0, (len(ALL_POSSIBLE_POSITIONS) - 1))]
            ALL_POSSIBLE_POSITIONS.pop(ALL_POSSIBLE_POSITIONS.index(temppos))
            bitftr.append(getfeature('true', temppos[0], temppos[1]))
            bitpos.append(temppos)
            LFR.append((0, (bitftr[i].split())[0]))
    else:
        temppos = ALL_POSSIBLE_POSITIONS[random.randint(0, (len(ALL_POSSIBLE_POSITIONS) - 1))]
        ALL_POSSIBLE_POSITIONS.pop(ALL_POSSIBLE_POSITIONS.index(temppos))
        tempftr = getfeature('true', temppos[0], temppos[1])
        for i in range(0, bitamt):
            bitftr.append(tempftr)
            bitpos.append(temppos)
            temppos = ALL_POSSIBLE_POSITIONS[random.randint(0, (len(ALL_POSSIBLE_POSITIONS) - 1))]
            ALL_POSSIBLE_POSITIONS.pop(ALL_POSSIBLE_POSITIONS.index(temppos))
            LFR.append((0, (bitftr[i].split())[0]))

    # ending the function for giving a starting bit random code
    regulating = []   # remove
    decoding = []  # remove
    stamping = []   # remove
    updating = []   # remove
    # time to start the engine(figuratively)
    t.setpos(0, 0)
    t.hideturtle()
    for i in range(1, 11):
        winsound.Beep(i * 40, 10)
    t.clear()
    t.write('5', font=('Ariel', 10, "bold"))
    winsound.Beep(200, 500)
    time.sleep(1)
    t.clear()
    t.write('4', font=('Ariel', 20, "bold"))
    winsound.Beep(300, 500)
    time.sleep(1)
    t.clear()
    t.write('3', font=('Ariel', 30, "bold"))
    winsound.Beep(400, 500)
    time.sleep(1)
    t.clear()
    t.write('2', font=('Ariel', 60, "bold"))
    winsound.Beep(500, 500)
    time.sleep(1)
    t.clear()
    t.write('1', font=('Ariel', 90, "bold"))
    winsound.Beep(600, 500)
    time.sleep(1)
    t.clear()
    t.showturtle()
    for i in range(0, 8):
        winsound.Beep(1000, 20)
    t0 = time.perf_counter()
    date = 0
    cycle = 0
    corpses = []
    t.hideturtle()
    t.tracer(0, 0)
    for i in range(0, len(bitpos)):
        t.color(getcolor(bitftr[i]))
        t.setpos(bitpos[i])
        stamp()
    t.update()
    t.tracer(0, 0)
    prevendday = 1
    while True:
        t.clear()
        v = 0
        t.color('#000000')
        t.shape('circle')
        for qq in corpses:
            t.setpos(qq)
            t.pensize(5*bitsize*2)
            t.pendown()
            t.penup()
        t.pensize(1)
        corpse_count = len(corpses)
        corpses = []
        t.shape('square')
        for a in bitpos:
            t.color(getcolor(bitftr[v]))
            t.setpos(bitpos[v])
            nextt = LFR[v][0]
            answer = LFR[v][1]
            if '8' in developer:
                t.pendown()
            t1 = time.perf_counter()  # remove
            decode(answer)
            decoding.append(time.perf_counter()-t1)  # remove
            t.penup()
            if nextt == len(bitftr[v].split()) - 1:
                newnext = 0
            else:
                newnext = nextt + 1
            try:
                LFR[v] = (newnext, (bitftr[v].split())[newnext])
            except:
                newnext = 0
                try:
                    LFR[v] = (newnext, (bitftr[v].split())[newnext])
                except:
                    break
            bitpos[v] = (int(t.pos()[0]), int(t.pos()[1]))
            t1 = time.perf_counter()  # remove
            stamp()
            stamping.append(time.perf_counter() - t1)  # remove
            for jj in todelete:
                delete(jj)
            v = v + 1
            t1 = time.perf_counter()  # remove
            # regulate()   CHECK WHAT HAPPENS WHEN REGULATE IS TURNED OFF.
            regulating.append(time.perf_counter() - t1)  # remove
        cycle += 1
        t1 = time.perf_counter()   # remove
        t.update()
        updating.append(time.perf_counter() - t1)   # remove
        t.tracer(0, 0)
        t.setpos(-600, 300)
        t.color('#000000')
        t.write(('Day: ' + str(date)), align='center', font=('Ariel', 20, "bold"))
        t.setpos(0, 300)
        t.write(('Cycle: ' + str(cycle)), align='center', font=('Ariel', 20, "bold"))
        t.setpos(500, 300)
        t.write(('Num of Bits: ' + str(len(bitpos)) + ' (- ' + str(corpse_count) + ')'), align='center',
                font=('Ariel', 20, "bold"))
        REFRESH()
        endday = 0
        if '4' in developer:
            if cycle / prevendday >= timer:
                endday = 1
                prevendday += 1
        else:
            if time.perf_counter() - t0 >= timer:
                endday = 1
        if endday == 1:
            print('updating =', updating[-1])
            print('regulating =', regulating[-1])
            print('decoding =', decoding[-1])
            print('stamping =', stamping[-1])
            date += 1
            tempa = 0
            tempb = 0
            tempc = 0
            tempd = 0
            tempe = 0
            tempf = 0
            tempg = 0
            temph = 0
            tempi = 0
            tempj = 0
            tempk = 0
            for iiii in bitftr:
                temporary = list(map(lambda iiiii: iiiii[0], iiii.split()))
                tempa += temporary.count('a')
                tempb += temporary.count('b')
                tempc += temporary.count('c')
                tempd += temporary.count('d')
                tempe += temporary.count('e')
                tempf += temporary.count('f')
                tempg += temporary.count('g')
                temph += temporary.count('h')
                tempi += temporary.count('i')
                tempj += temporary.count('j')
                tempk += temporary.count('k')
            arate.append(tempa)
            brate.append(tempb)
            crate.append(tempc)
            drate.append(tempd)
            erate.append(tempe)
            frate.append(tempf)
            grate.append(tempg)
            hrate.append(temph)
            irate.append(tempi)
            jrate.append(tempj)
            krate.append(tempk)
            bitamount.append(len(bitpos))
            EVALUATE()
            EVOLVE()
            if REPRODUCE == True:
                if not len(bitpos) > bitmax:
                    for pap in range(0, len(bitpos)):
                        if not len(bitpos) > bitmax:
                            if random.randint(1, COR) == 1:
                                new(pap)
            if RPAEOD:
                timess = len(bitpos)
                bitpos = []
                ALL_POSSIBLE_POSITIONS = []
                tempx = []
                tempy = []
                for w in range(0, int(660 / (bitsize * 20))):
                    tempx.append(-(w * 20 * bitsize))
                for w in range(0, int(660 / (bitsize * 20))):
                    tempx.append(w * 20 * bitsize)
                for w in range(0, int(330 / (bitsize * 20))):
                    tempy.append(-(w * 20 * bitsize))
                for w in range(0, int(330 / (bitsize * 20))):
                    tempy.append(w * 20 * bitsize)
                for i in tempx:
                    for g in tempy:
                        ALL_POSSIBLE_POSITIONS.append((i, g))
                for lmao in range(timess):
                    temppos = ALL_POSSIBLE_POSITIONS[random.randint(0, (len(ALL_POSSIBLE_POSITIONS) - 1))]
                    ALL_POSSIBLE_POSITIONS.pop(ALL_POSSIBLE_POSITIONS.index(temppos))
                    bitpos.append(temppos)
            win.bgcolor('white')
            t0 = time.perf_counter()
        if len(bitpos) == 0:
            if respawn == True:
                respawn()
            else:
                t.update()
                t.setpos(0, 0)
                t.write(('All the creatures have died. Please close this tab to see the results.'),
                        align='center', font=('Ariel', 20, "bold"))
                print('All the creatures have died. Please close this tab to see the results.')
                winsound.MessageBeep()
                while end != True:
                    winsound.Beep(100, 20)
                    t.clear()
                    t.write(('All the creatures have died. Please close this tab to see the results.\nIt took them ' + str(cycle) + ' Cycles.'),
                            align='center', font=('Ariel', 20, "bold"))
                    time.sleep(0.1)
        if end == True:
            break

    win.bgcolor('white')
    for i in range(0, 24):
        winsound.Beep(3000 - (i * 50), 10)
        time.sleep(0.1)

except:
    print('PROGRAM ENDED DUE TO ERROR')
    winsound.Beep(500, 5000)
    pass

# NOW FOR THE GRAPH!!!       NOW FOR THE GRAPH!!!       NOW FOR THE GRAPH!!!       NOW FOR THE GRAPH!!!       NOW FOR THE GRAPH!!!
t.clear()
t.clearscreen()
t.penup()
t.speed(0)
t.setpos(0, 0)
t.write(('Please answer question.' + str(cycle)), align='center', font=('Ariel', 20, "bold"))
mean = bool(input('Do you want the graph to calculate its results using a mean?\n')[0].upper() == 'Y')
t.clear()
t.clearscreen()
t.penup()
t.speed(0)


def textx(text, xn, yn, x, y):
    t.penup()
    t.setpos(xn, yn)
    t.write(str(text), align='center', font=('Ariels', 5, "bold"))
    t.width(1)
    t.setpos(x, y)
    t.pendown()
    t.setpos(x, 300)
    t.setpos(x, y)
    t.width(10)


def texty(text, xn, yn, x, y):
    t.penup()
    t.setpos(xn, yn)
    t.write(str(text), align='center', font=('Ariels', 5, "bold"))
    t.width(1)
    t.setpos(x, y)
    t.pendown()
    t.setpos(EOL, y)
    t.setpos(x, y)
    t.width(10)


t.width(10)
t.setpos(-550, -300)
t.penup()

t.pendown()
divider = 1

if date > 40:
    while True:
        if date / divider <= 40:
            break
        else:
            divider = divider + 1
step = 1100 / date

for i in range(0, date + divider, divider):
    t.setpos(-550, -300)
    t.setx(-550 + (i * (1100 / date)))
    textx(str(i), t.xcor(), t.ycor() - 20, t.xcor(), t.ycor())
    winsound.Beep(200, 10)
EOL = t.xcor()  # end of line
t.penup()
t.setpos(600, -315)

t.write('DAY', font=('Terminal', 15, "bold"))

t.setpos(-550, -300)
t.pendown()
maximum = max(max(arate), max(brate), max(crate), max(drate), max(erate), max(frate), max(grate), max(hrate),
              max(irate), max(jrate), max(krate), max(bitamount))
if mean:
    maximum = int(max(max(arate), max(brate), max(crate), max(drate), max(erate), max(frate), max(grate), max(hrate),
                  max(irate), max(jrate), max(krate)) / max(bitamount)) + 3
divider = 1
if maximum > 40:
    while True:
        if maximum / divider <= 20:
            break
        else:
            divider = divider + 1
for i in range(0, maximum + divider, divider):
    t.setpos(-550, -300)
    t.sety(-300 + (i * (600 / maximum)))
    texty(str(i), t.xcor() - 20, t.ycor(), t.xcor(), t.ycor())
    winsound.Beep(400, 10)
t.penup()
t.setpos(-670, 330)
t.write('GENE ABUNDANCE', font=('Terminal', 10, "bold"))
t.width(4)
time.sleep(1)
t.setpos(-700, 240)
t.fillcolor('#c4c4c4')
t.begin_fill()
t.setpos(-575, 240)
t.setpos(-575, -240)
t.setpos(-700, -240)
t.setpos(-700, 240)
t.end_fill()
time.sleep(1)
t.color('#4d4d4d')
t.setpos(-670, 220)
t.write('FORWARD', font=('Ariel', 8, "bold"))
t.tracer(0, 0)
t.setpos(-550, -300 + 600 / maximum * arate[0] / (bitamount[0] if mean else 1))
t.pendown()
counter = 0
x = -550
while counter != date:
    t.setpos(x, -300 + 600 / maximum * arate[counter] / (bitamount[counter] if mean else 1))
    counter += 1
    x += 1100 / date
t.penup()
t.update()
winsound.Beep(800, 10)
time.sleep(1)
t.color('#865ea6')
t.setpos(-670, 180)
t.write('DIAGONAL(Y=X)', font=('Ariel', 8, "bold"))
t.tracer(0, 0)
t.setpos(-550, -300 + 600 / maximum * brate[0] / (bitamount[0] if mean else 1))
t.pendown()
counter = 0
x = -550
while counter != date:
    t.setpos(x, -300 + 600 / maximum * brate[counter] / (bitamount[counter] if mean else 1))
    counter += 1
    x += 1100 / date
t.penup()
t.update()
winsound.Beep(800, 10)
time.sleep(1)
t.color('#00acdb')
t.setpos(-670, 140)
t.write('DIAGONAL(Y=-X)', font=('Ariel', 8, "bold"))
t.tracer(0, 0)
t.setpos(-550, -300 + 600 / maximum * crate[0] / (bitamount[0] if mean else 1))
t.pendown()
counter = 0
x = -550
while counter != date:
    t.setpos(x, -300 + 600 / maximum * crate[counter] / (bitamount[counter] if mean else 1))
    counter += 1
    x += 1100 / date
t.penup()
t.update()
winsound.Beep(800, 10)
time.sleep(1)
t.color('#272554')
t.setpos(-670, 90)
t.write('REPEAT\n(embedded\n features)', font=('Ariel', 8, "bold"))
t.tracer(0, 0)
t.setpos(-550, -300 + 600 / maximum * drate[0] / (bitamount[0] if mean else 1))
t.pendown()
counter = 0
x = -550
while counter != date:
    t.setpos(x, -300 + 600 / maximum * drate[counter] / (bitamount[counter] if mean else 1))
    counter += 1
    x += 1100 / date
t.penup()
t.update()
winsound.Beep(800, 10)
time.sleep(1)
t.color('#9e9e00')
t.setpos(-670, 50)
t.write('NULL\n(useless)', font=('Ariel', 8, "bold"))
t.tracer(0, 0)
t.setpos(-550, -300 + 600 / maximum * erate[0] / (bitamount[0] if mean else 1))
t.pendown()
counter = 0
x = -550
while counter != date:
    t.setpos(x, -300 + 600 / maximum * erate[counter] / (bitamount[counter] if mean else 1))
    counter += 1
    x += 1100 / date
t.penup()
t.update()
winsound.Beep(800, 10)
time.sleep(1)
t.color('#f000cc')
t.setpos(-670, 20)
t.write('FOLLOW', font=('Ariel', 8, "bold"))
t.tracer(0, 0)
t.setpos(-550, -300 + 600 / maximum * grate[0] / (bitamount[0] if mean else 1))
t.pendown()
counter = 0
x = -550
while counter != date:
    t.setpos(x, -300 + 600 / maximum * grate[counter] / (bitamount[counter] if mean else 1))
    counter += 1
    x += 1100 / date

t.penup()
t.update()
winsound.Beep(800, 10)
time.sleep(1)
t.color('#ff0000')
t.setpos(-670, -10)
t.write('KILL', font=('Ariel', 8, "bold"))
t.tracer(0, 0)
t.setpos(-550, -300 + 600 / maximum * frate[0] / (bitamount[0] if mean else 1))
t.pendown()
counter = 0
x = -550
while counter != date:
    t.setpos(x, -300 + 600 / maximum * frate[counter] / (bitamount[counter] if mean else 1))
    counter += 1
    x += 1100 / date
t.penup()
t.update()
winsound.Beep(800, 10)
time.sleep(1)
t.color('#328200')
t.setpos(-670, -80)
t.write('IF(runs \nfeatures \nif criteria \nmet)', font=('Ariel', 8, "bold"))
t.tracer(0, 0)
t.setpos(-550, -300 + 600 / maximum * hrate[0] / (bitamount[0] if mean else 1))
t.pendown()
counter = 0
x = -550
while counter != date:
    t.setpos(x, -300 + 600 / maximum * hrate[counter] / (bitamount[counter] if mean else 1))
    counter += 1
    x += 1100 / date

t.penup()
t.update()
winsound.Beep(800, 10)
time.sleep(1)
t.color('#ff8400')
t.setpos(-670, -108)
t.write('MOVE RIGHT', font=('Ariel', 8, "bold"))

t.tracer(0, 0)
t.setpos(-550, -300 + 600 / maximum * irate[0] / (bitamount[0] if mean else 1))
t.pendown()
counter = 0
x = -550
while counter != date:
    t.setpos(x, -300 + 600 / maximum * irate[counter] / (bitamount[counter] if mean else 1))
    counter += 1
    x += 1100 / date
t.penup()
t.update()
winsound.Beep(800, 10)
time.sleep(1)
t.color('#a64a2d')
t.setpos(-670, -144)
t.write('MOVE LEFT', font=('Ariel', 8, "bold"))
t.tracer(0, 0)
t.setpos(-550, -300 + 600 / maximum * jrate[0] / (bitamount[0] if mean else 1))
t.pendown()
counter = 0
x = -550
while counter != date:
    t.setpos(x, -300 + 600 / maximum * jrate[counter] / (bitamount[counter] if mean else 1))
    counter += 1
    x += 1100 / date
t.penup()
t.update()
winsound.Beep(800, 10)
time.sleep(1)
t.color('#03a866')
t.setpos(-670, -180)
t.write('BACKWARDS', font=('Ariel', 8, "bold"))
t.tracer(0, 0)
t.setpos(-550, -300 + 600 / maximum * krate[0] / (bitamount[0] if mean else 1))
t.pendown()
counter = 0
x = -550
while counter != date:
    t.setpos(x, -300 + 600 / maximum * krate[counter] / (bitamount[counter] if mean else 1))
    counter += 1
    x += 1100 / date
t.penup()
t.update()
time.sleep(1)
t.color('#000000')
t.setpos(-670, -210)
t.write('Bit Amount', font=('Ariel', 8, "bold"))
t.tracer(0, 0)
t.setpos(-550, -300 + 600 / maximum * bitamount[0])
t.pendown()
counter = 0
x = -550
while counter != date:
    t.setpos(x, -300 + 600 / maximum * bitamount[counter])
    counter += 1
    x += 1100 / date
print('Compositions of winning bits:')
EVALUATE()
for i in range(0, len(bitpos)):
    print(bitpos[i], bitftr[i])
t.penup()
t.update()
t.hideturtle()
win.exitonclick()
