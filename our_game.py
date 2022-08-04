import random
import sys 

meet_num = 1

things_do = ["Help pick up cigarettes off the streets", "reuse, reduce, recycle","Do nothing", "protest", "advertise greener ways", "make poster"]


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
        print("No change in you depression state")

def d_c_b():
    num2 = (random.randrange(0, 2))
    if num2 == 1:
        player1.sc += 1
        print("Player depression: + 1")
    else:
        print("No change in you depression")

def home():
    print(
        "You go home in a hurry with you head low, hoping no one pays attention to you.\nAt you home you are greeted by your parents and then you go to your bed for a quick nap before dinner."
    )
    d_c_b()
    fd = input("As you lie on your bed, you wonder if it is the best idea to skip the meeting. Are you sure about skipping?").lower()
    if fd == "yes":
        print("You decide to stay, who will notice your absence?")
        player1.sc += 1
        print("Player depression: + 1")
    elif fd == "no":
        print("You suddenly feel the need to go to the meeting and you bolt up.\nYou are ready in minutes,\nYour parents are suprised when they see you downstiars.\nYou quickly say where you going and you dad says he will drive you to your school.\nSoon you are at the front of the school.\nBefore you leave, you father tells you\nSon, I am proud of you and what you doing, never forget, love you.\nYou are stunned for a second and then reply\nLove you too.\nThen you go rushing into the building.")
        player1.sc -= 2
        print("Player depression: - 2")
        print("You get there in the middle of the teacher's lecture.\nYou sit down at the nearest table and listen to the teacher.\nTeacher: ….it past the north forest. It is slowly spreading to our neighborhood.\nPlease be careful and stay away from the north forest as it is very much surrounded by carbon dioxide and is dangerous.\n\nAfter hearing this progress report, you worry more about the future of this neighborhood.\nYou head to your assigned workstation with another kid who you don't pay much attention to. \nYou begin brainstorming about what you can do to help.\n30 minutes later\nThe group came back together to discuss and a list of ideas were made.\nEach day each person chooses what he or she wants to do and con only do it once.\nThis will start the next meeting.\nTeacher: Thanks everyone for coming and I hope you to see you guys next time.\nYou silenly get up and go home, wondering what will you do next...")
    #NEXT STAGE 


def GT_meeting1():
    print(
        "You’ve made it to the green team.\nWow, you made it just in the nick of time.\nTeacher: Welcome back students. I hope you all had a lovely weekend.\nHere’s a progress report on the expanding wildfire.\nThe fire has made it past the north forest.\nIt is slowly spreading to our town.\nPlease be careful and stay away from the north forest as it is very much surrounded by smoke and is dangerous.\n\nAfter hearing this progress report, you worry more about the future of this neighborhood.\nYou head to your assigned workstation with another kid who you don't pay much attention to. \nYou begin brainstorming about what you can do to help.\n30 minutes later\nThe group came back together to discuss and a list of ideas were made.\nEach day each person chooses what he or she wants to do and con only do it once.\nThis will start the next meeting.\nTeacher: Thanks everyone for coming and I hope you to see you guys next time.\nYou silenly get up and go home, wondering what will you do next..."
    )

#next scene



def clean_s():
    print("You decided to help pick up cigarettes off the street.\nYou weren’t on this alone.\nLuckly, half of the green team committee gather to help clean the streets and you were able to work with them.")
  #to be continued



def rrr():
    print("You know that the main way to help the earth is by with the 3 r’s (reuse, reduce, recycle).\nAlthough the 3 r’s may not be the main way to reduce wildfires, it can help prevent other natural disasters from happening.\nGood job!")
    player1.c_c += 1
    d_c()
  #next scene


    



def do_none():
    print("You decide to do nothing that day, if so many people are working on the same problem what will your efforts do?")
    player1.sc += 1
    print("Player depression: + 1")
    player1.c_c += 1
    print("Climate Change : + 1")

def protest():
    print("You choose to protest in the streets hoping to draw attention to your cause.\nSome of the other green team members were willing to join you and after a little bit of prepping your team make their way to the city hall in hopes that people will notice you and your cause.\nYou see a lot of people looking at you as they pass.\nYou hope they are reading your poster and not judging you…\n2 hours later...\nYour team heads back to the school where you put away your stuff.\nYou know for a fact that now more people are aware of the problems the wild fire is causing and hope they will take action.\nGood Job!")
    player1.sc -= 1
    print("Player depression: - 1")
    player1.c_c -= 1
    print("Climate change: - 1")

def advertise():
    print("You remember a friend of yours named Karl was a pretty famous youtuber and decided to ask him for help.\nYou called him and told him that you wanted to spread the word on the wild fires, and he agreed to help.\nA few minutes later…\nYour friend is here and he helped you record a message on the wildfires and how the community can help out.\nKarl:We look good, I’ll upload it later and see what happens, see you?\nHe leaves and you go home happy that you took a big step on solving the wildfires.\nGood job!")
    player1.sc -= 1
    print("Player depression - 1")
    player1.c_c -= 1
    print("Climate change - 1")

def make_p():
    print("You realize that making posters would be the most effective way to make a statement about climate change.\nWhile making these posters, you notice that you’re able to take your mind off of the distractions and problems that you’ve faced.\nAlthough you haven’t been feeling your best, you decide to continue on and ignore the feelings of sadness and disinterest.\nYou haven’t felt so useful in a long time.")
    player1.sc -= 1
    print("Player depression - 1")
    player1.c_c -= 1
    print("Climate change - 1")
  

def GT_meeting():
    print("It's another Green Team meeting.\nTime to choose an activity")
    print(things_do)
    numb = input("Choose what you want to do.").lower()
    if numb in things_do:
        GT_meeting.remove("numb")
        if numb == "help pick up cigarettes off the streets":
            print("you chose to help pick up cigarettes off the streets")
        elif numb == "reuse, reduce, recycle":
            print("you chose to reuse, reduce, recycle")
            rrr()
        elif numb == "do nothing":
            print("do nothing")
            do_none()
        elif numb == "protest":
            print("protest")
            protest()
        elif numb == "advertise greener ways":
            print("advertise greener ways")
            advertise()
        elif numb == "make poster":
            print("make poster")
            make_p()
    else:
      GT_meeting()
        
        
        
        
        
    
    


def nap():
    print("You take a nap in the janitor closet")
    player1.sc += 1
    print("Player depression: + 1")

    ik = input("You decide to stay in your comfort zone not feeling like going to the meeting.\nThe realities of depression truly catching up to you huh?\nYou take what was supposed to be a short nap…\n(new line)\n4 hours later…\nyou wake up the sound of someone unlocking the door.\nYou quickly gather your stuff and check the time on your phone.\n7:24 it says.\nWow, it must have been an amazing sleep.\nYou hear the knob being turned and you start to panic.\nLuckily you find a box of garbage bags to use so you can cover yourself with it.\nCREaAKkkkk…\nYou hold as still as possible not knowing who just entered.\nYou think to yourself…\nShould you stay still or run?").lower()
    if ik == "stay still":
        print("Worrying about what could happen if you ran, you stayed put.\nYou feel your heart racing and your breathing becoming heavier.\nYou wonder who would be in school at such late hours.\nThe janitor?\nYou ask yourself.\nYou slowly move your head to the small gap between the floor and the bag.\nWhoever it is enters grabs some things and leaves.\nAfter a few minutes you get up and hurry out, not wanting to get caught\nIt would have been better just to run huh?")
      #next scene
    elif ik == "run":
        print("You made a bold move and decided to run.\nAlthough you don’t know who it is, you worry about what could happen if you did stay.\nYou grip tightly to your backpack and make a run for it.\nYou jump up from under the bag scaring the person but you don’t care.\nYou don’t look back and continue to run until you feel tired.\nYou look around to see where you are and it turns out you ran all the way home.\nGood for you!\nThe rest of the week speeds on…")
#next scene
    else:
        print("You had a hard time deciding and you knocked down a broom that was next to you.\nIn fear that you were discovered, you bolted out of the room, scaring the person but you don’t care.\nYou don’t look back and continue to run until you feel tired.\nYou look around to see where you are and it turns out you ran all the way home.\nGood for you!\nThe rest of the week speeds on…")
  
  


def beginning():
    print(
        "Okay player. You’re currently in the janitor closet, which have become your hiding place. It’s currently the afternoon, school just ended and it’s the green team meeting is going to happen soon. What should you do?"
    )
    action_o = input(
        "\n1:Go home\n2:Go to the Green Tean Meeting\n3:Go to sleep in the closet.\n(Put number)"
    )
    if (action_o == "1") or (action_o == "one"):
        check1 = input(
            "Are you sure you want to go home? It will increase your depression."
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
            "Are you sure you want to nap? It can increase your depression.").lower(
            )
        if check1 == "yes":
            nap()
        else:
                GT_meeting()
        
    else:
        print("Not an option")
        beginning()


print(
    "\nWelcome player. \nIn this game, you’ll be playing a character who’s going through an enormous amount of challenges. \nYou will be playing as a high school student who is suffering from long-term depression.\nYou have to figure out how to save your neighborhood from the damaging wild fires of climate change while also combating the characters disorder.\nThis character has joined the green team in hopes of being able to make their neighborhood more sustainable and protecting it from current and future problems.”"
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
