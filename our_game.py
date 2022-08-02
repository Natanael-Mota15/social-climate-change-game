import random
import sys 
meet_num = 1

things_do = ["Help pick up cigarettes off the stre ets.", "reuse, reduce, recycle","Do nothing", "protest", "advertise greener ways", "make poster"]


class Player:
    def __init__(self, name, gender):
        self.day = 1
        self.name = name
        self.gender = gender
        self.sc = 5
        self.c_c = 5

    def __repr__(self):
        return f"Day: {self.day}, Name: {self.name}, Gender: {self.gender}, Depression counter: {self.sc}, Climate Change Counter: {self.c_c}"


player1 = Player("a", "b")


def intro():
    c_gender = input("So tell me, are you a boy or a girl? ").lower()
    if c_gender == "boy":
        player1.gender = "boy"
        c_name = input("Ok, and what is your name: ")
        player1.name = c_name
        print(player1)
        print("Be brave, because now your adventure begins.")
        beginning()
    elif c_gender == "girl":
        player1.gender = "girl"
        c_name = input("Ok, and what is your name: ")
        player1.name = c_name
        print(player1)
        print("Be brave, because now your adventure begins")
        beginning()
    else:
        print("Can you repeat")
        intro()


def ran_fact():
    num = (random.randrange(1, 21))
    if num == 1:
        print(
            "According to the IPCC‘s(Intergovernmental Panel on Climate Change) sixth assessment report on the state of our climate, the past decade(2012-2022) is likely to have been the hottest period in the last 125,000 years."
        )

    elif num == 2:
        print(
            "A 2019 study found that oceans had sucked up 90% of the heat gained by the planet between 1971 and 2010. Heat we produce."
        )

    elif num == 3:
        print("CO2 is at its highest in 2 Million Years")

    elif num == 4:
        print(
            "Since the mid-1990s, we’ve lost around 28 trillion tons of ice, with today’s melt rate standing at 1.2 trillion tons a year."
        )

    elif num == 5:
        print("Air pollution kills more than 9 million people per year.")

    elif num == 6:
        print(
            "Polluting particles, such as PM10 or PM2.5, which cause adverse health effects similar to those of cigarettes, actually reflect the sun’s heat rather than trap it. These particles have kept the planet at a lower tempeture"
        )

    elif num == 7:
        print(
            "Sea level rise would probably take a millennia to reverse its course."
        )

    elif num == 8:
        print(
            "A report from The Lancet found that the number of work hours lost to heat across the globe increased from 199 billion in 2000 to 295 billion in 2020. That is equivalent to 88 work hours per employed person."
        )

    elif num == 9:
        print(
            "A study by Xu et al. (2020) called “Future of the Human Niche” found that by 2070, under a high emissions scenario, these unbearable temperatures could expand to affect up to 3 billion people"
        )

    elif num == 10:
        print(
            "More than 1 million species are at risk of extinction by climate change"
        )

    elif num == 11:
        print(
            "Countries contributing the most to global emissions have the best chance of curbing climate change, but leaders are doing little to address it."
        )

    elif num == 12:
        print("Extreme heat events have become more frequent and severe")

    elif num == 13:
        print(
            "Two-thirds of extreme weather events in the last 20 years were influenced by humans."
        )

    elif num == 14:
        print(
            "Dengue is the world’s fastest-growing mosquito-borne virus, currently killing some 10,000 people and affecting around 100 million per year. As global temperatures are rising, Aedes aegypti mosquitos that carry the disease could thrive in places that were previously unsuitable for them and benefit from shorter incubation periods. Which means that Dengue would spread faster."
        )

    elif num == 15:
        print(
            "Average wildlife populations have dropped by 60 per cent in just over 40 years(2021)"
        )

    elif num == 16:
        print(
            "The United States constitutes 5% of the world population and contributes to 22% of the world’s carbon emission."
        )

    elif num == 17:
        print(
            "Around 15% of the carbon released in the environment is due to deforestation and change in the use of land."
        )

    elif num == 18:
        print(
            "Air conditions and heating elements consume 50% of electricity in America."
        )

    elif num == 19:
        print(
            "Carbon dioxide is not the only contributing gas to climate change. Other gases like methane and nitrous oxide are far more dangerous than carbon dioxide alone."
        )

    elif num == 20:
        print(
            "The UN Intergovernmental Panel on Climate Change (IPCC) is a leading body fighting against climate change. This body is a political organization, however, and not a scientific body."
        )

    elif num == 21:
        print(
            "Climate change can have serious health impacts such as heat stress, extreme cold, which can cause major deaths due to heart diseases."
        )


def d_c():
    num = (random.randrange(0, 2))
    if num == 1:
        player1.sc -= 1
        print("Player depression - 1")
    else:
        print("No change")


def home():
    print(
        "You go home in a hurry with you head low, hoping no one pays attention to you. At you home you are greeted by your parents and then you go to your bed for a quick nap before dinner."
    )
    player1.sc += 1
    print("Player depression: + 1")
    #NEXT STAGE


def GT_meeting1():
    print(
        "You’ve made it to the green team.\nWow, you made it just in the nick of time.\nTeacher: Welcome back students. I hope you all had a lovely weekend.\nHere’s a progress report on the expanding wildfire.\nThe fire has made it past the north forest.\nIt is slowly spreading to our town/neighborhood.\nPlease be careful and stay away from the north forest as it is very much surrounded by smoke and is dangerous.\n\nAfter hearing this progress report, you worry more about the future of this neighborhood.\nYou head to your assigned workstation with another kid who you don't pay much attention to. \nYou begin brainstorming about what you can do to help.\n30 minutes later\nThe group came back together to discuss and a list of ideas were made.\nEach day each person chooses what he or she wants to do and con only do it once./nThis will start the next meeting./nTeacher: Thanks everyone for coming and I hope you to see you guys next time.\nYou silenly get up and go home, wondering what will you do next..."
    )

#next scene


def GT_meeting():
    print("It's another Green Team meeting.\nTime to choose an activity")
    print(things_do)
    numb = int(input("Choose what you want to do./n(First option = 1, second = 2, etc"))
    


def nap():
    print("You take a nap in the janitor closet")
    player1.sc += 1
    print("Player depression: + 1")
    print(
        "You decide to stay in your comfort zone and take a nap.\n4 hours later… you wake up the sound of someone unlocking the door.\nYou quickly gather your stuff and check the time on your phone.\n7:24 it says.\nWow, it must have been an amazing sleep.\nYou hear the knob being turned and you start to panic.\nLuckily you find a box of garbage bags to use so you can cover yourself with it.\nCREaAKkkkk…."
    )


def beginning():
    print(
        "Okay player. You’re currently in the janitor closet, which have become your hiding place. It’s currently the afternoon, school just ended and it’s the green team meeting is going to happen soon. What should you do?"
    )
    action_o = input(
        "\n1:Go home\n2:Go to the Green Tean Meeting\n3:Go to sleep in the closet.\n(Put number)"
    )
    if (action_o == "1") or (action_o == "one"):
        check1 = input(
            "Are you sure you want to go home? It will increase depression."
        ).lower()
        if check1 == "yes":
            print("You went home")
            home()
        else:
            beginning()
    elif (action_o == "2") or (action_o == "two"):
        check2 = input(
            "Are you sure you want to go to the meeting? It can maybe decrease your depression."
        ).lower()
        if check2 == "yes":
            d_c()
            if meet_num == 1:
                GT_meeting1()
            else:
                GT_meeting()
        else:
            beginning()
    elif (action_o == "3") or (action_o == "three"):
        check1 = input(
            "Are you sure you want to nap? It can increase depression.").lower(
            )
        if check1 == "yes":
            d_c()
            nap()
    else:
        print("Not an option")
        beginning()


print(
    "\nWelcome player. \nIn this game, you’ll be playing a character who’s going through an enormous amount of challenges. \nYou will be playing as a high school student who is suffering from depression and is to an extent depressed.\nYou have to figure out how to save your neighborhood from the damaging wild fires of climate change.\nThe character has joined the green team in hopes of being able to make their neighborhood more sustainable.”"
)

print(
    "\nHow to play:\nIn order to win you must keep the climate change bar and social issues bar as low as possible. \nYour decisions will determine what happens in this game. \nPositive influences will decrease the bar while negative influences will increase the bar. \nIf one bar reaches the end, you lose. \nWill you be able to save your town or will you let it crumble?"
)
intro()

while player1.sc >= 10:
    print(
        "You got so depressed that you were put in a hospital. Better luck next time"
    )
    sys.exit()
while player1.c_c >= 10:
    print(
        "Your neighborhood became so affected by climate change that you had to leave in a rush due to a big wildfire that started in it. Your family were able to escape and now you are on your aunt's house. Better luck next time"
    )
    sys.exit()
while player1.sc <= 0:
    print(
        "You were able to get out of your depression and now you are decided to put all of you efforts on helping your communitie. Great job"
    )
    sys.exit()
while player1.c_c <= 0:
    print(
        "You saved neighborhood from the affects of climate change and know you can start working on yourself and reconstructing your life. Great job."
    )
    sys.exit()
