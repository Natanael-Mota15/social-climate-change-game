from email.contentmanager import raw_data_manager
import random
import sys
from urllib import response 3


active = True
things_do = ["help pick up cigarettes off the streets", "reuse, reduce, recycle","do nothing", "protest", "advertise greener ways", "make poster"]


class Player:
    def __init__(self, name, gender):
        self.day = 1
        self.name = name
        self.gender = gender
        self.sc = 5
        self.c_c = 5
        self.meet_num = 1

    def __repr__(self):
        return f"Day: {self.day}, Name: {self.name}, Gender: {self.gender}, Depression counter: {self.sc}, Climate Change Counter: {self.c_c}"


player1 = Player("a", "b")


def intro():
    c_gender = input("\nSo tell me, are you a boy or a girl? \n").lower()
    if c_gender == "boy":
        player1.gender = "boy"
        c_name = input("\nOkay, and what's your name: ")
        player1.name = c_name
        print(player1)
        print("\nBe brave, because now your adventure begins here.\n")
        beginning()
    elif c_gender == "girl":
        player1.gender = "girl"
        c_name = input("\nOkay, and what's your name:")
        player1.name = c_name
        print(player1)
        print("\nBe brave, because now your adventure begins here. \n")
        beginning()
    else:
        print("Can you repeat?")
        intro()



def ran_fact():
    print(player1)
    questi = input("\nWould you like to see a fun fact?\nYes or no?\n").lower()
    if questi == "yes":
        num = (random.randrange(1, 21))
        print("Fun Fact:")
        if num == 1:
            print(
                "\nAccording to the IPCC's(Intergovernmental Panel on Climate Change) sixth assessment report on the state of our climate, the past decade(2012-2022) is likely to have been the hottest period in the last 125,000 years.\n"
            )

        elif num == 2:
            print(
                "\nA 2019 study found that oceans had sucked up 90% of the heat gained by the planet between 1971 and 2010.\nHeat we produce.\n"
            )

        elif num == 3:
            print("\nCO2 is at its highest in 2 Million Years\n")

        elif num == 4:
            print(
                "\nSince the mid-1990s, we???ve lost around 28 trillion tons of ice, with today???s melt rate standing at 1.2 trillion tons a year.\n"
            )

        elif num == 5:
            print("\nAir pollution kills more than 9 million people per year.\n")

        elif num == 6:
            print(
                "\nPolluting particles, such as PM10 or PM2.5, which cause adverse health effects similar to those of cigarettes, actually reflect the sun???s heat rather than trap it.\nThese particles have kept the planet at a lower tempeture.\n"
            )

        elif num == 7:
            print(
                "\nSea level rise would probably take a millennia to reverse its course.\n"
            )

        elif num == 8:
            print(
                "\nA report from The Lancet found that the number of work hours lost to heat across the globe increased from 199 billion in 2000 to 295 billion in 2020.\nThat is equivalent to 88 work hours per employed person.\n"
            )

        elif num == 9:
            print(
                "\nA study by Xu et al. (2020) called ???Future of the Human Niche??? found that by 2070, under a high emissions scenario, these unbearable temperatures could expand to affect up to 3 billion people.\n"
            )

        elif num == 10:
            print(
                "\nMore than 1 million species are at risk of extinction by climate change\n"
            )

        elif num == 11:
            print(
                "\nCountries contributing the most to global emissions have the best chance of curbing climate change, but leaders are doing little to address it.\n"
            )

        elif num == 12:
            print("\nExtreme heat events have become more frequent and severe\n")

        elif num == 13:
            print(
                "\nTwo-thirds of extreme weather events in the last 20 years were influenced by humans.\n"
            )

        elif num == 14:
            print(
                "\nDengue is the world's fastest-growing mosquito-borne virus, currently killing some 10,000 people and affecting around 100 million per year.\nAs global temperatures are rising, Aedes aegypti mosquitos that carry the disease could thrive in places that were previously unsuitable for them and benefit from shorter incubation periods.\nWhich means that Dengue would spread faster.\n"
            )

        elif num == 15:
            print(
                "\nAverage wildlife populations have dropped by 60 per cent in just over 40 years(2021)\n"
            )

        elif num == 16:
            print(
                "\nThe United States constitutes 5% of the world population and contributes to 22% of the world's carbon emission.\n"
            )

        elif num == 17:
            print(
                "\nAround 15% of the carbon released in the environment is due to deforestation and change in the use of land.\n"
            )

        elif num == 18:
            print(
                "\nAir conditions and heating elements consume 50% of electricity in America.\n"
            )

        elif num == 19:
            print(
                "\nCarbon dioxide is not the only contributing gas to climate change.\nOther gases like methane and nitrous oxide are far more dangerous than carbon dioxide alone.\n"
            )

        elif num == 20:
            print(
                "\nThe UN Intergovernmental Panel on Climate Change (IPCC) is a leading body fighting against climate change.\nThis body is a political organization, however, and not a scientific body.\n"
            )

        elif num == 21:
            print(
                "\nClimate change can have serious health impacts such as heat stress, extreme cold, which can cause major deaths due to heart diseases.\n"
            )
    meeting_decide()


def d_c():
    num = (random.randrange(0, 2))
    if num == 1:
        player1.sc -= 1
        print("\nPlayer depression - 1\n")
    else:
        print("\nThere is no change in your depression state. \n")

def d_c_b():
    num2 = (random.randrange(0, 2))
    if num2 == 1:
        player1.sc += 1
        print("\nPlayer depression: + 1\n")
    else:
        print("\nThere is no change in your depression state.\n")

def home():
    player1.meet_num += 1
    print(
        "\nYou go home in a hurry with you your head low, hoping no one pays attention to you.\nAt you home you are greeted by your parents, then you go to your bed for a quick nap before dinner.\n"
    )
    d_c_b()
    fd = input("\nAs you lie on your bed, you wonder if it is the best idea to skip the meeting.\nAre you sure about skipping?").lower()
    if fd == "yes":
        print("\nYou decide to stay, who will notice your absence?\n")
        player1.sc += 1
        print("\nPlayer depression: + 1\n")
        ran_fact()
        meeting_decide()
    else:
        print("\nYou suddenly feel the need to go to the meeting and you bolt up.\nYou are ready in minutes,\nYour parents are suprised when they see you downstiars.\nYou quickly say where you going and you dad says he will drive you to your school.\nSoon you are at the front of the school.\nBefore you leave, your father tells you\nSon, I am proud of you and what you are doing, never forget, love you.\nYou are stunned for a second and then reply:\nLove you too.\nThen you go rushing into the building.\n")
        player1.sc -= 2
        print("\nPlayer depression: - 2\n")
        print("\nYou get there in the middle of the teacher's lecture.\nYou sit down at the nearest table and listen to the teacher.\nTeacher: ???.it past the north forest. It is slowly spreading to our neighborhood.\nPlease be careful and stay away from the north forest as it is very much surrounded by carbon dioxide and is dangerous.\n\nAfter hearing this progress report, you worry more about the future of this neighborhood.\nYou head to your assigned workstation with another kid who you don't pay much attention to. \nYou begin brainstorming about what you can do to help.\n30 minutes later\nThe group came back together to discuss and a list of ideas were made.\nEach day each person chooses what he or she wants to do and con only do it once.\nThis will start the next meeting.\nTeacher: Thanks everyone for coming and I hope you to see you guys next time.\nYou silenly get up and go home, wondering what will you do next...\n")
        ran_fact()
        meeting_decide()



def clean_s():
    print("\nYou decided to help pick up cigarettes off the street.\nYou weren't on this alone.\nLuckly, half of the green team committee gather to help clean the streets and you were able to work with them.\n That really helped with the cleanup.\nGood job on completing this!\n")
    player1.c_c -= 1
    d_c()
    ran_fact()
    meeting_decide()



def rrr():
    print("\nYou know that the main way to help the earth is by with the 3 r's (reuse, reduce, recycle).\nAlthough the 3 r???s may not be the main way to reduce wildfires, it can help prevent other natural disasters from happening.\nGood job!\n")
    player1.c_c -= 1
    d_c()
    ran_fact()
    meeting_decide()
  



def do_none():
    print("\nYou decide to do nothing that day, if so many people are working on the same problem what will your efforts do?\n")
    player1.sc += 1
    print("\nPlayer depression: + 1\n")
    player1.c_c += 1
    print("\nClimate Change : + 1\n")
    ran_fact()
    meeting_decide()

def protest():
    print("\nYou choose to protest in the streets hoping to draw attention to your cause.\nSome of the other green team members were willing to join you and after a little bit of prepping your team makes their way to the city hall in hopes that people will notice you and your cause.\nYou see a lot of people looking at you as they pass.\nYou hope they will read your posters and not judge you???\n2 hours later...\nYour team heads back to the school where you put your stuff away.\nYou know for a fact that more people are aware of the problems the wildfires is causing and hope that they will take action.\nGood Job!\n")
    player1.sc -= 2
    print("\nPlayer depression: - 1\n")
    player1.c_c -= 2
    print("\nClimate change: - 1\n")
    ran_fact()
    meeting_decide()

def advertise():
    print("\nYou remember a friend of yours named Karl was a pretty famous youtuber and decided to ask him for help.\nYou called him and told him that you wanted to spread the word on the wildfires, and he agreed to help.\nA few minutes later???\nYour friend is here and he helped you record a message on the wildfires and how the community can help out.\nKarl:This looks good, I???ll upload it later and see what happens, see you?\nHe leaves and you go home happy that you took a big step on solving the wildfires.\nGood job!\n")
    player1.sc -= 1
    print("\nPlayer depression - 1\n")
    player1.c_c -= 1
    print("\nClimate change - 1\n")
    ran_fact()
    meeting_decide()

def make_p():
    print("\nYou realize that making posters would be the most effective way to make a statement about climate change.\nWhile making these posters, you notice that you???re able to take your mind off of the distractions and problems that you???ve faced.\nAlthough you haven???t been feeling your best, you decide to continue on and ignore the feelings of sadness and disinterest.\nYou haven???t felt so useful in a long time.\n")
    player1.sc -= 1
    print("\nPlayer depression - 1\n")
    player1.c_c -= 1
    print("\nClimate change - 1\n")
    ran_fact()
    meeting_decide()
  
def shock():
    print("\nYou feel like upset about the news of Ms. Hert.\nYou have a hard time thinking about anything but Ms. Hert.\nYou don???t know how to feel about this???\nYou let your partner do all the work and you're just sitting there staring off into the distance.\n1 hour later???\nAs soon as the sub dismisses you from class, you run home immediately crying and not knowing why.\nThe only thing you can think of is Ms. Hert.\nYou ask yourself, ???Am I really crying over her?\n")
    player1.sc -= 1
    print("\nPlayer depression - 1\n")
    player1.c_c -= 1
    print("\nClimate change - 1\n")
    ran_fact()
    meeting_decide()



def GT_meeting():
    print("\nIt's another Green Team meeting.\nTime to choose an activity\n")
    print(things_do)
    numb = input("Choose what you want to do.").lower()
    if (numb == "help pick up cigarettes off the streets") and (numb in things_do):
        print("\nYou chose to help pick up cigarettes off the streets\n")
        things_do.remove("Help pick up cigarettes off the streets")
    elif (numb == "reuse, reduce, recycle") and (numb in things_do):
        print("\nYou chose to reuse, reduce, recycle\n")
        things_do.remove("reuse, reduce, recycle")
        rrr()
    elif (numb == "do nothing") and (numb in things_do):
        print("\nDo nothing\n")
        do_none()
    elif (numb == "protest") and (numb in things_do):
        print("\nProtest")
        things_do.remove("protest")
        protest()
    elif (numb == "advertise greener ways") and (numb in things_do):
        print("\nAdvertise greener ways\n")
        things_do.remove("advertise greener ways")
        advertise()
    elif( numb == "make poster") and (numb in things_do):
        print("\nMake poster\n")
        things_do.remove("make poster")
        make_p()
    else:
        GT_meeting()
        
    
def nap():
    player1.meet_num += 1
    print("\nYou decide to take a nap in the janitor closet\n")
    player1.sc += 1
    print("\nPlayer depression: + 1\n")

    ik = input("\nYou decide to stay in your comfort zone not feeling like going to the meeting.\nThe realities of depression truly catching up to you huh?\nYou take what was supposed to be a short nap???\n(new line)\n4 hours later???\nyou wake up the sound of someone unlocking the door.\nYou quickly gather your stuff and check the time on your phone.\n7:24 it says.\nWow, it must have been an amazing sleep.\nYou hear the knob being turned and you start to panic.\nLuckily you find a box of garbage bags to use so you can cover yourself with it.\nCREaAKkkkk???\nYou hold as still as possible not knowing who just entered.\nYou think to yourself???\nShould you stay still or run?\n").lower()
    if ik == "stay still":
        print("\nWorrying about what could happen if you ran, you stayed put.\nYou feel your heart racing and your breathing becoming heavier.\nYou wonder who would be in school at such late hours.\nThe janitor?\nYou ask yourself.\nYou slowly move your head to the small gap between the floor and the bag.\nWhoever it is enters grabs some things and leaves.\nAfter a few minutes you get up and hurry out, not wanting to get caught\nIt would have been better just to run huh?\n")
        ran_fact()
        meeting_decide()
    elif ik == "run":
        print("\nYou made a bold move and decided to run.\nAlthough you don???t know who it is, you worry about what could happen if you did stay.\nYou grip tightly to your backpack and make a run for it.\nYou jump up from under the bag scaring the person but you don???t care.\nYou don???t look back and continue to run until you feel tired.\nYou look around to see where you are and it turns out you ran all the way home.\nGood for you!\nThe rest of the week speeds on???\n")
        ran_fact()
        meeting_decide()
    else:
        print("\nYou had a hard time deciding and you knocked down a broom that was next to you.\nIn fear that you were discovered, you bolted out of the room, scaring the person but you don't care.\nYou don't look back and continue to run until you feel tired.\nYou look around to see where you are and it turns out you ran all the way home.\nGood for you!\nThe rest of the week speeds on???\n")
        ran_fact()
        meeting_decide()
  
  


def beginning():
    print(
        "\nOkay player.\nYou're currently in the janitor closet, which have become your hiding place.\nIt's currently the afternoon, school just ended and it's the green team meeting is going to happen soon.\nWhat should you do?\n"    )
    action_o = input(
        "\n1:Go home\n2:Go to the Green Team Meeting\n3:Go to sleep in the closet.\n(Put number)\n"
    )
    if (action_o == "1") or (action_o == "one"):
        check1 = input(
            "\nAre you sure you want to go home? It will increase your depression.\n"
        ).lower()
        if check1 == "yes":
            print("\nYou went home\n")
            home()
        else:
            beginning()
    elif (action_o == "2") or (action_o == "two"):
        check2 = input(
            "\nAre you sure you want to go to the meeting? It can maybe decrease your depression.\n"
        ).lower()
        if check2 == "yes":
            d_c()
            meeting_decide()
        else:
            beginning()
    elif (action_o == "3") or (action_o == "three"):
        check1 = input(
            "\nAre you sure you want to nap? It can increase your depression.\n").lower(
            )
        if check1 == "yes":
            nap()
        else:
                beginning()
        
    else:
        print("\nNot an option\n")
        beginning()


def ending():
    print("\nThere are no more meetings\n")
    if (player1.sc <= 7) and (player1.c_c <= 7):
        print("\nAfter getting home, your parents quickly prepare to leave.\nIn less than an hour your family is making their way to your Aunt Sandy's house.\nYou wonder what will happen next...\n1 day later.\nYour family is preparing to return home.\nSome houses were damaged but they can be reconstructed.\nThe governor is planning to make an official town green team to help minimize climate change efects and prevent events like this from happening.\nYou are ready for a new start and you feel better than ever, knowing that your efforts weren't in vain.\nThe End\nPS:\nGood Job! :)")   
        
        sys.exit()
    elif (player1.sc >= 7) and (player1.c_c >= 7):
        print("\nAfter getting home, your parents quickly prepare to leave.\nIn less than an hour your family is making their way to your Aunt Sandy's house.\nYou wonder what will happen next...\n1 day later.\nYour family is seeking a new home.\nThe town was burned to what seems that can take a long time to repair.\nAll houses were damaged but they can be reconstructed eventually.\n You become more depressed than ever and you overhear your parents talking about getting a therapist.\nYou wonder if your efforts were in vain as your world starts to crumble into ashes.\nThe End\nPS:\nBetter luck next time!")
        
        sys.exit()
    elif (player1.sc <= 7) and (player1.c_c >= 7):
        print("\nAfter getting home, your parents quickly prepare to leave.\nIn less than an hour your family is making their way to your Aunt Sandy's house.\nYou wonder what will happen next...\n1 day later.\nYour family is seeking a new home.\nThe town was burned to what seems that can take a long time to repair.\nYou are not depressed because you know you gave your 110% on trying to save your town and you are ready for a new beginig.\nThe End\nPS\nBetter luck next time!")
        
        sys.exit()
    elif (player1.sc <= 7) and (player1.c_c <= 7):
        print("\nAfter getting home, your parents quickly prepare to leave.\nIn less than an hour your family is making their way to your Aunt Sandy's house.\nYou wonder what will happen next...\n1 day later.\nYour family is preparing to return home.\nSome houses were damaged but they can be reconstructed.\nYou are a little depressed because you know you gave your 110 percent on trying to save your town and you didn't quite, but you are ready for a new begining\nThe end\nPS\nGood Job! :)")


def GT_meeting5():
    player1.meet_num += 1
    response5 = input("\nIt's broadcasted everywhere...\nHalf the town is burning up.\nEveryone from that part of town is now moving here.\nEven though there is so much going on right now, the green team meeting is still ongoing.\nThis may be the last green team meeting.\nThere's no debating about this one.\nYou head back into school and make your way into the classroom.\nWell, at least the sub is still here.\nUsually, whenever you came in, she would greet you, but not today...\nYou walked towards your seat and sat down.\nSub: Hey guys.. Um, so today is just a chill day.\nDo whatever you like but just be careful. I don't feel like teaching any lessons today so it's not going to be much of a lesson.\nI know that some of you would like to head home so go ahead.\nOr  if you  really want to help, the fire department is accepting volunteers, just ask your parents first.\nWould you like to head home or help?\n").lower()
    if (response5 == "home") or (response5 == "go home"):
        print("\nLuckily the teacher dismissed you early this meeting so you decided to head home.\nWhat was the point of staying there if you weren't going to learn anything?\nYou walk back home and you feel the scorching heat from the fire\n.")
        ran_fact()
        ending()
    elif response5 == "help":
        print("\nYou decided to help the fire department instead of going home.\nYou didn't want to waste this day by staying at home.\nYou ran out of the school and towards the fire department, ready to help in any way you could.\nYou entered the fire house and saw that there were a couple of firefighters getting ready to suit up.\nYou went up to one of them and asked them \n???Is there any way I can help you????.\nThe fireman looked at you and chuckled,\nYeah kiddo, you should get out of here.\nIt's dangerous and we're about to help extinguish the fire.\nYou looked at him disappointed but he had a point.\nWhat was the purpose of staying here if they were going out to the front lines to help save this town?\nYou walked away sad but knowing that you at least tried...\n")
        ran_fact()
        ending()
    else: 
         GT_meeting5()

def GT_meeting4():
    player1.meet_num += 1
    bla = input("\nAnother week, another meeting.\nYou recently have watched the news and learned that the fires has officially touched grounds in the neighborhood and leaves destruction where ever it is found.\nYou feel somewhat defeated that you weren???t able to do more to hold back the fire.\nYou are unsure if you should go to the meeting today.\n Should you go?\n").lower()
    if bla == "yes":
        print("\nYou head into the room hoping something fun or interesting would happen.\nYou look at your table and find that your partner and the pair in front of you aren???t here.\nSub: As you can, some of the students that were once in our class are not here.\nThey and their families have decided to evacuate due to the increase of wild fires appearing so they will not be here for the rest of the meetings.\nWe don???t know if they will come back or not but we hope they do soon.\nAnyways, our meetings must continue on\nIf you guys at any time feel unsafe or anything and would like to leave, feel free to.\nToday will be no different than previous meetings.\nYou will continue on with your projects based on whatever project you decided to do, we will continue on from there.\nWhat project would you like to do?\n")
        GT_meeting()
    elif bla == "no":
        print("\nYou thought about whether or not you should go to the meeting and have made a decision on not going.\nWhy bother?\nThis town's gonna burn up no matter what we do.\nYou skip the meeting and head over to the cafe.\nIt???s too early to go home, you say to yourself.\nIn the cafe???\nWhile in the cafe, you think about your previous choices that you???ve made.\nSome you deeply regretted and some you're proud of.\nYou feel frustrated that you weren???t able to do enough to help protect this neighborhood.\nBut you also know that this isn???t a one person job...\nStill, you are angry that you couldn???t do more to help.\n")
        player1.sc += 1
        print()
        player1.c_c += 2
        ran_fact()
        meeting_decide()


def GT_meeting3():
    player1.meet_num += 1
    print("\nWow.\nIt???s already the end of the day.\nTime surely goes by fast.\nToday you felt happier and more confident than usual.\nYou feel at your best and decide to head to the green team meeting.\nYou head into the classroom and see that your teacher isn???t here.\nYou wonder where she is.\nSub: ???Ms. Hert is not in today and will not be from now on.\nI???m Mr. Walke.\nI will be subbing for her.\nMs. Hert has left the school and resigned from her job.\nAccording to the principal, Ms. Hert felt like this wasn???t a safe environment and has moved to somewhere far from here.\nYou feel sick on the inside, knowing that one of the best teachers here has moved away suddenly.\nNot even a good-bye?\nWow...\nHow could she just leave us when we need her the most?\nSub: ???But, she did leave a lesson plan.\nYou are supposed to be working on ways to help combat the current wildfires.\nSo, you will just continue on that or start a new project about that.\n")
    thi = input("\nStay in shock.\nYes or no?\n").lower()
    if thi == "yes":
        shock()
    else:
        GT_meeting()

def GT_meeting2():
    decision1 = input("\nYou???ve just gotten out of class and you head for the Green Team meeting.\nOne part of you wants to go to the meeting and the other says not to. You ask yourself whether or not you truly want to go to the meeting.\nConfused and unsure???\nDo you want to go to the meeting?\n").lower()
    if decision1 == "yes":
        player1.sc += 1
        print("\nYou decided to side with the side that says you should go to the meeting.\nYou walk into the classroom ready to learn.\nYou silently slip into your seat and wave to your partner.\nYou turn back to the board and carefully listen to the teacher.\nTeacher: ???Students, as you may know, the dixon fire has grown and spread.\nAlthough it has not touched our neighborhood, it is closed by.\nI was to ensure you, firefighters are doing all they can to protect us and our land.\nBut they cannot combat their disaster on their own.\nWe must do our part to help.\nAs a member of the green team, we are obligated to help.\nDo your part to help this disaster.\n")
        player1.meet_num += 1
        GT_meeting()
    elif decision1 == "no":
        player1.sc += 1
        print("\nDepression counter + 1\n")
        print("\nAlthough one side of you wanted you to go to the meeting, you decided not to go and just head home.\nWhen you get home, you question yourself again, asking ???why didn???t I go to the meeting???? You feel hopeless and like you're unable to do your part to help\nYou don???t feel as interested in being on the green team as you once did.\nFeeling an overwhelming amount of shame, you silently let it out???\n")
        d_c_b()
        player1.meet_num += 1
        ran_fact
        

def GT_meeting1():
    print("\nYou have made it to the green team.\nYour depression has really gotten to you and you hope that the green team will help relieve someone of that stress.\nWow, you made it just in the nick of time.\nTeacher: 'Welcome back students. I hope you all had a lovely weekend.\nHere???s a progress report on the expanding wildfire.\nThe fire has made it past the north forest.\nIt is slowly spreading to our town.\nPlease be careful and stay away from the north forest as it is very much surrounded by smoke and is dangerous.'\n\nAfter hearing this progress report, you worry more about the future of this neighborhood.\nYou head to your assigned workstation with another kid who you don't pay much attention to. \nYou begin brainstorming about what you can do to help.\n30 minutes later\nThe group came back together to discuss and a list of ideas were made.\nEach day each person chooses what he or she wants to do and can only do it once.\nTeacher: 'Thanks everyone for coming and I hope you to see you guys next time.'\nYou silenly get up and go home, wondering what will you do next...\n")
    player1.meet_num += 1
    meeting_decide()

def meeting_decide():
    if player1.meet_num == 1:
        GT_meeting1()
    elif player1.meet_num == 2:
        print("\nNext week\n")
        GT_meeting2()
    elif player1.meet_num == 3:
        print("\nNext week\n")
        GT_meeting3()
    elif player1.meet_num == 4:
        print("\nNext week\n")
        GT_meeting4()
    elif player1.meet_num == 5:
        print("\nNext week\n")
        GT_meeting5()
    else:
        ending()






print("\nWelcome player. \nIn this game, you???ll be playing a character who???s going through an enormous amount of challenges. \nYou will be playing as a high school student who is suffering from long-term depression.\nYou have to figure out how to save your neighborhood from the damaging wild fires of climate change while also combating the characters disorder.\nThis character has joined the green team in hopes of being able to make their neighborhood more sustainable and protecting it from current and future problems.\n")

print("\nHow to play:\nIn order to win you must keep the climate change bar and social issues bar as low as possible. \nYour decisions will determine what happens in this game. \nPositive influences will decrease the bar while negative influences will increase the bar. \nMoxt decisions will have an options of actions or will be yes or no questions. \nWill you be able to save your town or will you let it crumble?\nNote:if any counter reaches 10 you lose but if any hits 0 you win, so be careful")
intro()

while active:
    if player1.sc >= 10:
        print(
            "\nYou are so depressed that you were put in a hospital.\nBetter luck next time!\n"
        )
        sys.exit()
    elif player1.c_c >= 10:
        print(
            "\nYour neighborhood became so affected by the wildfires that you had to leave in a rush. Your family was able to escape and now you are living in your aunt's house.\nBetter luck next time!\n"
        )
        sys.exit()
    elif player1.sc <= 0:
        print(
            "\nYou were able to get out of depression and now you are decided to put all of you efforts on helping your communitity.\nGreat job!\n"
        )
        sys.exit()
    elif player1.c_c <= 0:
        print(
            "\nYou saved neighborhood from the effects of climate change and know you can start working on yourself and reconstructing your life.\nGreat job!\n"
        )
        sys.exit()
