import random
import time


# print with time sleep
def p1(w):
    print(w)
    time.sleep(1)


First_Field = 0
First_Lumberjack = 0
First_Wise_Man = 0
First_House = 0
Quest_1 = 0
Quest_1c = 0
Quest_2 = 0
Quest_2_Completion = 0
First_Forest = 0
fang = 0
Witch_Old_Friend = 0
First_Hunter = 0
Gold = 0
First_Old_Man = 0
Found_Witch_Pet = 0
Player_Health = 10
Fish_Stamina = 8
tries = 0
fur = 0
Wood = 0
Wise_Hunter_Meet = 0
Large_Fish = 0
Rare_Fish = 0
Small_Fish = 0
Medium_Sword = 0
Bad_Sword = 0
Rare_Sword = 0
Medium_Sword_Use = 10
Bad_Sword_Use = 10
Rare_Sword_Use = 15
axe = 0
Axe_Use = 7
iron = 0
coat = 0
Coat_Use = 15


# validating input
def validation(min, max):
    while True:
        try:
            Choice = int(input(f"choose from {min} to {max}: "))
            if Choice < min:
                print("too small")
            elif Choice > max:
                print("too big")
            else:
                return Choice
        except ValueError:
            print("Please enter a valid number")


""" a function to wait for and detect key presses
in the combat and fishing departments """


def key_check(target):
    target = str(target)
    try:
        key = input()
        numcount = 0
        for char in key:
            if char.isdigit():
                numcount += 1
                if numcount > 1:
                    raise ValueError
            else:
                raise ValueError
        if key == target:
            return True
    except ValueError:
        p1("press only one number, how hard is that")
    return False


# a wood chopping minigame
def chopping_game():
    global Wood
    global axe
    global Axe_Use
    if Axe_Use == 0:
        p1("you need a new axe to start chopping")
        p1("you can get the componets from the market place or other ways")
        p1("and go to the hunter to make him craft an axe")
    elif Axe_Use > 0:
        needs = 3
        goods = 0
        tries = 0
        top = 5
        p1("you found a good tree")
        while tries <= top:
            if goods < needs:
                key = random.randint(1, 5)
                p1(f"to chop press {key}")
                if key_check(key):
                    goods += 1
                    p1(f"good chop, you stand at {goods} of {needs}")
                else:
                    p1("the axe gets stuck")
            elif goods == needs:
                Wood += random.randint(1, 3)
                Axe_Use -= 1
                p1(
                    f"you now have {Wood} wood and your axe still "
                    f"has {Axe_Use} uses left"
                )
                return 1


# a combat minigame
def combat_system():
    global Player_Health
    global Rare_Sword
    global Bad_Sword
    global Medium_Sword
    global coat
    global Coat_Use
    global Rare_Sword_Use
    global Bad_Sword_Use
    global Medium_Sword_Use
    enemy = random.choice(["wolf", "bear", "crocodile", "snake"])
    if enemy == "bear":
        Enemy_Health = 15
        Enemy_Damage = random.randint(3, 6)
    elif enemy == "crocodile":
        Enemy_Health = 20
        Enemy_Damage = random.randint(5, 9)
    elif enemy == "snake":
        Enemy_Health = 5
        Enemy_Damage = random.randint(2, 5)
    elif enemy == "wolf":
        Enemy_Health = 10
        Enemy_Damage = random.randint(4, 8)
    p1(f"A wild {enemy} appears!")
    while True:
        if Enemy_Health <= 0:
            reward = random.choice(
                ["animal meat", "thick fur", "sharp fang", "mysterious herb"]
            )
            p1(f"You defeated the {enemy} and got {reward}!")
            if reward == "animal meat":
                global Quest_1
                Quest_1 += 1
                p1(f"(Total meat: {Quest_1}/15)")
                if Quest_1 >= 15:
                    p1("you should really go to the hunter")
            elif reward == "mysterious herb":
                Player_Health = min(15, Player_Health + 3)
                p1("You feel fresh")
            elif reward == "sharp fang":
                global fang
                fang += 1
            elif reward == "thick fur":
                global fur
                fur += 1
            return 1
        elif Player_Health <= 0:
            p1("You were killed")
            return 2
        key = random.randint(1, 3)
        p1(f"To attack press {key}")
        if key_check(key):
            h = random.randint(1, 10)
            if h <= 2:
                p1(f"You hit but {enemy} blocked!")
            else:
                if Rare_Sword != 0:
                    dmg = random.randint(7, 11)
                    Rare_Sword_Use -= 1
                    if Rare_Sword_Use == 0:
                        Rare_Sword -= 1
                elif Medium_Sword != 0:
                    dmg = random.randint(4, 8)
                    Medium_Sword_Use -= 1
                    if Medium_Sword_Use == 0:
                        Medium_Sword -= 1
                elif Bad_Sword != 0:
                    dmg = random.randint(3, 5)
                    Bad_Sword_Use -= 1
                    if Bad_Sword_Use == 0:
                        Bad_Sword -= 1
                else:
                    dmg = random.randint(1, 2)
                Enemy_Health -= dmg
                p1(f"You hit the {enemy}! Enemy HP: {Enemy_Health}")
        else:
            p1("You missed!")
        if Enemy_Health > 0:
            key = random.randint(1, 3)
            p1(f"To defend press {key}")
            if key_check(key):
                p1("You blocked the attack!")
            else:
                if coat == 1:
                    dmg = Enemy_Damage / 2
                    Coat_Use -= 1
                    if Coat_Use == 0:
                        coat -= 1
                else:
                    dmg = Enemy_Damage
                Player_Health -= dmg
                p1(f"You took {dmg} damage! Your HP: {Player_Health}")


# the combat minigame but with the hunter
def combat_with_hunter():
    global Quest_1, Quest_1_Completion, First_Forest, First_Hunter
    if Quest_1 < 15:
        while True:
            ae = combat_system()
            if ae == 1:
                p1("seams that you are pretty good")
                p1(
                    "tell you what. get me 15 animal meat and "
                    "i will tell you something"
                )
                First_Forest = 1
                First_Hunter = 1
                forest()
            elif ae == 2:
                break
            else:
                p1("don't worry, it isn't so easy. let's try again")
    else:
        p1("ok, you've done your end now it's time for mine")
        p1(
            "i have an old friend in the mountains that can "
            "tell you the location"
        )
        p1("of a tresure, you should talk to him when you get the chance")
        Quest_1_Completion += 1
        forest()


# a fishing minigame
def fishing():
    Fish_Stamina = 8
    tries = 0
    fish = random.choice(["trout", "salmon", "bass", "pike"])
    p1(f"there is a {fish} in the lake")
    while True:
        if Fish_Stamina <= 0:
            reward = random.choice(
                [
                    "small fish",
                    "large fish",
                    "rare fish",
                ]
            )
            p1(f"\nYou caught the {fish}! ({reward})")
            if reward == "small fish":
                global Small_Fish
                Small_Fish += 1
            elif reward == "large fish":
                global Large_Fish
                Large_Fish += 1
            elif reward == "rare fish":
                global Rare_Fish
                Rare_Fish += 1
                if Rare_Fish >= 15:
                    p1("you should talk to the fisher man in the lake")
            return True
            break
        elif tries <= 5:
            tries += 1
            key = random.randint(1, 4)
            p1(f"There it is, press {key} to reel it (try {tries} out of 5)")
            if key_check(key):
                Fish_Stamina -= random.randint(1, 3)
                p1(f"good job, fish stamina is {Fish_Stamina} now")
            else:
                p1("almost ran away")
        else:
            p1("and there it goes")
            return False


# the fishing minigame with the fisher
def fishing_with_fisher():
    global Quest_2, Quest_2_Completion
    if Quest_2 == 0:
        while True:
            if fishing():
                p1("seams that you are pretty good")
                p1(
                    "tell you what. get me 15 rare fish and i "
                    "will tell you something"
                )
                p1(
                    "and if you want to buy or sell your fish you "
                    "can go to the market in the swamp"
                )
                lake()
            else:
                p1("don't worry, it isn't so easy. let's try again")
    elif Quest_2 >= 1:
        while True:
            p1("wanna fish(1) or nothing(2)")
            fi1 = validation(1, 2)
            if fi1 == 1:
                fishing()
            elif fi1 == 2:
                p1("your loss")
                break
    else:
        p1("ok, you've done your end now it's time for mine")
        p1("the witch's pet is trapped in a landslide in the swamp")
        p1("you can go get him out and return it to the witch for a reward")
        Quest_2_Completion += 1
        lake()


# an event in which an animal could attack the player in the forest
def animal_attack_forest():
    global Quest_1
    h = random.randint(1, 10)
    if h <= 4:
        combat_system()
        forest()


# an event in which an animal could attack the player in the mountains
def animal_attack_mountains():
    global Quest_1
    h = random.randint(1, 10)
    if h <= 4 and First_Forest != 0:
        combat_system()
        Mountains()


# an event in which an animal could attack the player in the field
def animal_attack_field():
    global Quest_1
    h = random.randint(1, 10)
    if h <= 4 and First_Forest != 0:
        combat_system()
        field()


# an event in which an animal could attack the player in the swamp
def animal_attack_swamp():
    h = random.randint(1, 10)
    if h <= 4:
        combat_system()
        swamp()


# an event in which a fish could appear near the player in the lake
def fish_in_lake():
    h = random.randint(1, 10)
    if h <= 4:
        fishing()
        lake()


# wood chopping minigame with lumberjack
def lumberjack_chopping():
    global First_Lumberjack, First_Hunter
    if Quest_1 < 15:
        while True:
            ae = chopping_game()
            if ae == 1:
                p1("seams that you are pretty good")
                p1("you can come here any time you want")
                First_Lumberjack += 1
                forest()
                break
            else:
                p1("don't worry, it isn't so easy. let's try again")
                forest()


# the house in the fields
def house():
    global First_House, First_Field
    if First_House == 0:
        p1("a pretty young woman opens the door")
        p1("and she invites you in")
        p1("will you accept(1) or not(2)")
        h1 = validation(1, 2)
        if h1 == 1:
            p1("you ask her about other people while drinking the tea")
            p1("she tells you about her friend in the swamp")
            p1("and a man in the forest")
            p1("and that you should visit her friend and stay here for dinner")
            p1("will you stay for dinner(1) or will you leave(2)")
            h2 = validation(1, 2)
            if h2 == 1:
                h = random.randint(1, 10)
                if h <= 4:
                    p1("you decide to stay for dinner")
                    p1(
                        "but while you are waiting you start hearing "
                        "things that don't sound like food"
                    )
                    p1("will you stay(1) or get out(2)")
                    h3 = validation(1, 2)
                    if h3 == 1:
                        p1(
                            "even though your instincts warn you "
                            "you decide to stay"
                        )
                        p1(
                            "and suddenly you find her behind you "
                            "not with food though"
                        )
                        p1(
                            "but with something else that can cause "
                            "immense harm and hits you"
                        )
                        p1(
                            "but before it hits you wake up "
                            "and relise you have been dreaming"
                        )
                        p1(
                            "and take a lesson that people "
                            "aren't always as they seem"
                        )
                        p1("and get on with your day")
                    else:
                        First_House = 1
                        First_Field = 1
                        field()
                else:
                    p1(
                        "so you wait and find that she "
                        "comes out with a delish dinner"
                    )
                    p1("you eat and chat and she " "wishes you good luck")
                    First_House = 1
                    First_Field = 1
                    field()
            else:
                field()
        else:
            field()
    elif First_House == 1:
        p1(
            "you went, then you must be tired. come "
            "on inside and tell me about it"
        )
        p1("you sit, chat and relax alittle then thank her and get out")
        field()
    else:
        p1(
            "did you go yet. no, you can come tell me about "
            "it when you get back"
        )
        field()


# the cave in the fields
def cave():
    global First_Wise_Man, Medium_Sword
    if First_Wise_Man == 0:
        p1("you decide to enter the cave")
        h = random.randint(1, 10)
        if h <= 4:
            p1("you found a man in the cave")
            p1("he tells you about his friend in the forest")
            p1("and that you should find him " "because he will help you")
            p1("and he gives you a sword that you accept")
            Medium_Sword = 1
            First_Wise_Man = 1
            field()
        else:
            p1("you found nothing")
            field()
    else:
        p1("you found nothing")
        field()


# the last location in the game
def last():
    p1("you enter the the cave in the mountain")
    p1("and the second you are about to see the tresure")
    p1("you wake up and relise that " "life is that tresure")
    p1("and think about it and go on your day happily")


# the hunter's place
def hunter():
    global First_Hunter
    global First_Forest
    global Wood
    global Wise_Hunter_Meet
    global Rare_Sword_Use
    global Coat_Use
    global Axe_Use
    global axe
    global iron
    global fang
    global Rare_Sword
    global fur
    global coat
    if Wise_Hunter_Meet > 0:
        p1(
            "hello, do you want to craft an item(1) or "
            "go hunting(2) or just relax(3)"
        )
        hu1 = validation(1, 3)
        if hu1 == 1:
            p1(
                "you need a fang and a piece of iron to craft the "
                "rare sword which will help you in combat"
            )
            p1("let's see what you can craft")
            if fang >= 1 and iron >= 1:
                p1("do you want to craft a rare sword(1) or not(2)")
                hu2 = validation(1, 2)
                if hu2 == 1:
                    fang -= 1
                    iron -= 1
                    Rare_Sword += 1
                    Rare_Sword_Use += 15
            p1(
                "you need three pieces of fur to craft the coat "
                "which will help you of you can't block the attack"
            )
            if fur >= 3:
                p1("you can craft a coat(1) or not(2)")
                hu2 = validation(1, 2)
                if hu2 == 1:
                    fur -= 3
                    coat += 1
                    Coat_Use += 10
            p1(
                "you need a piece of iron and two pieces of wood to"
                "craft the axe which will help you cut down trees"
            )
            if iron >= 1 and Wood >= 2:
                p1("you can craft an axe(1) or not(2)")
                hu2 = validation(1, 2)
                if hu2 == 1:
                    iron -= 1
                    Wood -= 2
                    axe += 1
                    Axe_Use += 7
            forest()
        elif hu1 == 2:
            combat_with_hunter()
        elif hu1 == 3:
            p1(
                "ok you can rest here, come sit "
                "i will make some tea and you just relax"
            )
            p1("you relax a little and get out")
            forest()
    elif First_Wise_Man == 1:
        p1("so you've seen my friend, eh")
        p1("glad to see he is doing well")
        p1("but you must have travelled a long way")
        p1("you can rest here, my friend")
        Wise_Hunter_Meet += 1
        p1("next morning")
        p1("you can come with me to teach you how to better use your sword(1)")
        p1("and you are free to leave(2) of course")
        f2 = validation(1, 2)
        if f2 == 1:
            combat_with_hunter()
        else:
            p1("you get out of the hunter's place")
            First_Hunter += 1
            First_Forest += 1
            forest()
    else:
        p1("that was very dangerous")
        p1("you can't walk in these parts without a sword")
        p1("here take this sword")
        p1("you can rest here, my friend")
        p1("next morning")
        p1("you can come with me to teach you how to better use your sword(1)")
        p1("and you are free to leave(2) of course")
        f2 = validation(1, 2)
        if f2 == 1:
            combat_with_hunter()
        else:
            p1("you get out of the hunter's place")
            First_Hunter += 1
            First_Forest += 1
            forest()


# the lumberjack's place
def Lumberjack():
    global axe
    global First_Lumberjack
    if First_Lumberjack == 0:
        p1("hi, oh you must be new here. i am the lumberjack")
    elif First_Lumberjack != 0:
        p1("oh, you returned")
    p1("wanna help me cut some wood(1) or not(2)")
    w1 = validation(1, 2)
    if w1 == 1:
        if First_Lumberjack == 0:
            p1("you are interested huh, ok take this axe and follow me")
            axe += 1
        else:
            p1("ok follow me")
        lumberjack_chopping()
    elif w1 == 2:
        p1("ok, i understand")
        p1("but if you ever change your mind i'll be here")
        forest()


# the oldman's place
def oldman():
    global First_Old_Man
    if First_Old_Man == 0:
        p1("hello, my son. i am sorry for your troubles to get here")
        p1("you are surely here to know about the tresure")
        p1("you'll find it in the mountains next to the fields")
        First_Old_Man = 1
        Mountains()
    else:
        p1("unfourtunatly i told you everything i know")
        Mountains()


# the fisher's place
def fisher():
    p1("oh hello there. did the witch send you")
    p1("ok, wanna get fishing(1) or not(2)")
    f1 = validation(1, 2)
    if f1 == 1:
        fishing_with_fisher()
    else:
        p1("ok, suit your self")
        lake()


# the witch's place
def witch():
    global Found_Witch_Pet, Witch_Old_Friend
    if First_House == 1:
        p1("so you've met my friend, glad to see she is doing well")
        p1("well you have come at a very good time because you see")
        p1("my pet has gone missing and if you return it you'll get a reward")
        p1("if you meet her, tell her i said hi")
        p1("also my friend likes fishing, you can find him in the lake")
        Witch_Old_Friend += 1
        swamp()
    elif Found_Witch_Pet == 1:
        p1("oh you found him, you have done your end of the deal")
        p1("now time for mine, there is an old man in the mountains")
        p1(
            "he belives a tresure is in this island somewhere "
            "and claims he found it"
        )
        p1(
            "nobody knows if he is talking truthfully or lying. "
            "you should go and shoot your shot"
        )
        swamp()
    else:
        p1("hello, what brings you here today. maybe help me brew my potions")
        p1("no, oh well you can help me in other ways too because you see")
        p1("my pet has gone missing, if you find it you'll be rewarded")
        p1("also there is my friend in the lake which you can go and see")
        p1("he might be of help to you in this regard")
        if Witch_Old_Friend == 0:
            Witch_Old_Friend += 1
        swamp()


# the place in which you find the witch's pet
def witch_pet():
    global Found_Witch_Pet
    if Found_Witch_Pet == 0:
        p1("you go to the place the fisherman talked about")
        p1("and actually find the remains of a landslide")
        p1("and you find the witch's pet and save it")
        p1("and go to the witch and give it to her so she thanks you")
        p1("and tells you to go to her so she tells you something")
        Found_Witch_Pet += 1
        swamp()
    else:
        p1("you already came here")
        swamp()


# the game's market
def market():
    global Gold, Rare_Fish, Small_Fish, Large_Fish, fang
    global fur, iron, Wood

    while True:
        p1(f"\nCurrent gold: {Gold}")
        p1("Market options:")
        p1("1. Check inventory")
        p1("2. Buy items")
        p1("3. Sell items")
        p1("4. Leave market")

        choice = validation(1, 4)

        if choice == 1:
            items = [
                ("Rare fish", Rare_Fish),
                ("Small fish", Small_Fish),
                ("Large fish", Large_Fish),
                ("Fang", fang),
                ("Thick fur", fur),
                ("Iron", iron),
                ("Wood", Wood),
            ]
            p1("\nYour inventory:")
            for name, amount in items:
                p1(f"- {name}: {amount}")
        elif choice == 2:
            items = [
                ("1. Rare fish", 30, "Rare_Fish"),
                ("2. Small fish", 5, "Small_Fish"),
                ("3. Large fish", 10, "Large_Fish"),
                ("4. Fang", 8, "fang"),
                ("5. Thick fur", 7, "fur"),
                ("6. Iron", 15, "iron"),
                ("7. Wood", 3, "Wood"),
                ("8. Back", 0, ""),
            ]
            p1("\nBuy items:")
            for item in items[:-1]:
                p1(f"{item[0]} - {item[1]} gold")

            buy_choice = validation(1, 7)
            if buy_choice != 9:
                selected = items[buy_choice - 1]
                if Gold >= selected[1]:
                    Gold -= selected[1]
                    globals()[selected[2]] += 1
                    p1(f"Bought 1 {selected[0].split('. ')[1]}!")
                else:
                    p1("Not enough gold!")

        elif choice == 3:
            items = [
                ("1. Rare fish", 30, "Rare_Fish"),
                ("2. Small fish", 5, "Small_Fish"),
                ("3. Large fish", 10, "Large_Fish"),
                ("4. Fang", 8, "fang"),
                ("5. Thick fur", 7, "fur"),
                ("6. Iron", 15, "iron"),
                ("7. Wood", 3, "Wood"),
                ("8. Back", 0, ""),
            ]
            p1("\nSell items:")
            for item in items[:-1]:
                p1(f"{item[0]} - {item[1]} gold")

            sell_choice = validation(1, 8)
            if sell_choice != 9:
                selected = items[sell_choice - 1]
                if globals()[selected[2]] > 0:
                    Gold += selected[1]
                    globals()[selected[2]] -= 1
                    p1(f"Sold 1 {selected[0].split('. ')[1]}!")
                else:
                    p1("You don't have any to sell!")

        elif choice == 4:
            p1("you left the market")
            swamp()
            break


# the field and the starting place of the game
def field():
    global First_Field, First_Old_Man
    if First_Field == 0:
        p1("you wake up in a wide field")
        p1("and find that you were unconcience")
        p1("you get up to explore and find that there is a house and a cave")
        p1("there is also a forest on your right and a swamp on your left")
        p1("and a lake infront of you")
        p1(
            "you can go to the house(1) or in the cave(2) or "
            "visit the forest(3) or the swamp(4)"
        )
        First_Field += 1
        f2 = validation(1, 4)
        if f2 == 1:
            house()
        elif f2 == 2:
            cave()
        elif f2 == 3:
            forest()
        elif f2 == 4:
            swamp()
    elif First_Old_Man == 1:
        p1("you return to the field. what do you want to do")
        animal_attack_field()
        p1(
            "you can go to the house(1) or in the cave(2) or visit "
            "the forest(3) or the swamp(4)"
        )
        p1("or you can check out that place the old man told you about(5)")
        f4 = validation(1, 5)
        if f4 == 1:
            house()
        elif f4 == 2:
            cave()
        elif f4 == 3:
            forest()
        elif f4 == 4:
            swamp()
        elif f4 == 5:
            last()
    else:
        p1("you return to the field. what do you want to do")
        animal_attack_field()
        p1(
            "you can go to the house(1) or in the cave(2) or "
            "visit the forest(3) or the swamp(4)"
        )
        f4 = validation(1, 4)
        if f4 == 1:
            house()
        elif f4 == 2:
            cave()
        elif f4 == 3:
            forest()
        elif f4 == 4:
            swamp()


# the forest
def forest():
    if First_Forest > 0:
        p1("you return to the forest")
        animal_attack_forest()
        p1(
            "you can go to the hunter(1) or the lumberjack(2) "
            "or the mountains(3) or the field(4)"
        )
        f4 = validation(1, 4)
        if f4 == 1:
            hunter()
        elif f4 == 2:
            Lumberjack()
        elif f4 == 3:
            Mountains()
        elif f4 == 4:
            field()
    else:
        p1("you enter the forest")
        p1("you wander alittel")
        p1("suddenly an animal rushes towards you")
        if First_Wise_Man == 1:
            p1("but you use your sword and cut it in half")
            p1("and the local hunter sees you and is amazed by what you done")
            hunter()
        else:
            p1("you stand not knowing what to do")
            p1("but suddenly a local hunter jumps and saves you")
            hunter()


# the mountains
def Mountains():
    global First_Hunter
    if Quest_1c > 0 or Found_Witch_Pet > 1:
        animal_attack_mountains()
        p1("there is nothing here")
        p1("you can go to the swamp(1) or to the forest(2) or the old man(3)")
        m1 = validation(1, 3)
        if m1 == 1:
            swamp()
        elif m1 == 2:
            forest()
        elif m1 == 3:
            oldman()
    else:
        animal_attack_mountains()
        p1("you can go to the swamp(1) or the forest(2)")
        m2 = validation(1, 2)
        if m2 == 1:
            swamp()
        elif m2 == 2:
            forest()


# the lake
def lake():
    p1("you entered the lakeside ground")
    p1("you can talk to the fisher man(1) or return to the swamp(2)")
    l1 = validation(1, 2)
    if l1 == 1:
        fisher()
    else:
        swamp()


# the swamp
def swamp():
    global Quest_2_Completion, Witch_Old_Friend
    if Quest_2_Completion == 1:
        animal_attack_swamp()
        p1("you entered the swamp")
        p1("you found a house and a market")
        p1(
            "you can enter the house(1) or to the "
            "field(2) or the mountains(3) "
            "or the witch's pet(4) or the witch's old "
            "friend(5) or the market(6)"
        )
        s1 = validation(1, 6)
        if s1 == 1:
            witch()
        elif s1 == 2:
            field()
        elif s1 == 3:
            Mountains()
        elif s1 == 4:
            fisher()
        elif s1 == 5:
            witch_pet()
        elif s1 == 6:
            market()
    if Witch_Old_Friend != 0:
        animal_attack_swamp()
        p1("you entered the swamp")
        p1("you found a house and a market")
        p1(
            "you can enter the house(1) or to the "
            "field(2) or the mountains(3) "
            "or to the lake with the witch's old friend(4) or the market(5)"
        )
        s1 = validation(1, 5)
        if s1 == 1:
            witch()
        elif s1 == 2:
            field()
        elif s1 == 3:
            Mountains()
        elif s1 == 4:
            lake()
        elif s1 == 5:
            market()
    else:
        animal_attack_swamp()
        p1("you entered the swamp")
        p1("you found a house and a market")
        p1(
            "you can enter the house(1) or to the field(2) or "
            "the mountains(3) or the market(4)"
        )
        s1 = validation(1, 4)
        if s1 == 1:
            witch()
        elif s1 == 2:
            field()
        elif s1 == 3:
            Mountains()
        elif s1 == 4:
            market()


# the start of the game
def game():
    while True:
        z = input("wanna play? y/n: ")
        if z == "y":
            field()
        elif z == "n":
            break
        else:
            print("not an answer")


game()
