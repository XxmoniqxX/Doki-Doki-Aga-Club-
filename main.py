import pgzrun
import random

from sys import exit


WIDTH=1280
HEIGHT=720
TITLE="Doki Doki Aga Club!"
mode = "menu"
day = 1
FPS=30
lovemeter=0
d=0
herside=False
demir=False
classroom = Actor("class")
closet =Actor("closet")
club =Actor("club")
outside =Actor("outside")
sayoroom=Actor("sayoroom")
menu=Actor("mainmenu")
sayori = Actor("sayoriconcerned2", center=(640,360))
natsuki = Actor("natsukihappy1", center=(640,360))
monika=Actor("monika", center=(340,360))
yuri=Actor("yuri", center=(140,360))
newgame=Actor("newgame", (150,420))
quit=Actor("quit",(150,600))
textbox=Actor("textboxddlc", center=(640,642))#816 146
choice=Actor("choice_hover_background", center=(640, 360))
outside=Actor("outside")
fortnite=Actor("fortintegameplay",center=(640,340))
choice2=Actor("choice_hover_background",center=(640, 400))
room=Actor("room")
wolf=Actor("wolf")
fort=True
roblox=Actor("indir",center=(640,340))
wnat=False
def draw():
    global day
    global d
    global lovemeter
    global fort
    global mode
    global wnat
    global herside
    global demir
    if day == 1:
        if mode == "menu":
            menu.draw()
            newgame.draw()
            quit.draw()
            screen.draw.text("THIS GAME CONTAINS CRINGE DIALOGUE WRITTEN BY ME AT VARIOUS LATE NIGHT HOURS WHILE IM VERY TIRED",center=(640,500),color="black")
            screen.draw.text("CONTINUE AT YOUR OWN RISK.",center=(640,520),color="black")
        elif mode == "game":
            if d == 0:
                screen.fill("black")
                textbox.draw()
                screen.draw.text("???:Kuzey, Kuzey, wake up!",(242,584))
            elif d == 1:
                screen.fill("black")
                textbox.draw()
                screen.draw.text("Me:Uhh, what is it dude?", (242, 584))
            elif d == 2:
                classroom.draw()
                sayori.draw()
                textbox.draw()
                screen.draw.text("???:Wake up you dummy! You slept through the whole lesson!",(242, 584))
            elif d == 3:
                classroom.draw()
                sayori.draw()
                textbox.draw()
                screen.draw.text("This is Duru, my childhood frie- wait... I met with her this year. Where'd that childhood friend thing come",(242, 584))
                screen.draw.text("from?",(242, 604))
                screen.draw.text("I guess she just reminded me of someone?", (242, 624))
            elif d == 4:
                classroom.draw()
                sayori.image="sayori1"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Duru:C'mon, we're gonna be late for the club!",(242, 584))
                screen.draw.text("Me:Oh yeah... The Aga Club.",(242, 604))
                screen.draw.text("When school first started I was all alone but she one day decided to text me from Discord I guess she ", (242, 624))
                screen.draw.text("felt bad seeing my inability to make friends, but now after 8 months she's my best friend so we ", (242, 644))
                screen.draw.text("created a club named The Aga Club with other people to just hang out and chill.", (242, 664))
            elif d == 5:
                classroom.draw()
                sayori.image="sayori1"
                sayori.draw()
                textbox.draw()
                screen.draw.text("...",(242, 584))
            elif d == 6:
                classroom.draw()
                sayori.image="sayori1"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Nothing more.",(242, 584))
            elif d == 7:
                classroom.draw()
                sayori.image="sayori1"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Just... friends.",(242, 584))
            elif d == 8:
                classroom.draw()
                sayori.image="sayoriconcerned1"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Duru: Uhh, you OK?",(242, 584))
                screen.draw.text("You've been just starin' at me without sayin' anything.",(242, 604))
                screen.draw.text("Do you have something on your mind?",(242, 624))
            elif d == 9:
                classroom.draw()
                sayori.image="sayoriconcerned1"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Frick",(242, 584))
                screen.draw.text("Me: no, nothin' just still a lil' sleepy.",(242, 604))
            elif d == 10:
                classroom.draw()
                sayori.image="sayori1"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Duru:You know you should really sleep better and NOT",(242, 584))
                screen.draw.text("watch anime.", (242, 604))
            elif d == 11:
                classroom.draw()
                sayori.image="sayori2"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Me:NOT RELEVANT LET'S GO TO THE CLUB!",(242, 584))
                screen.draw.text("Duru:You can't just ignore me, your health's important y'know?",(242,604))
            elif d == 12:
                club.draw()
                sayori.image="sayorihappy2"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Duru:Hello Demir!",(242, 584))
                screen.draw.text("Me:AYYYYYYYYYYYYYYYYY IS THAT THE LEGEND?",(242,604))
            elif d == 13:
                club.draw()
                sayori.x= 1050
                natsuki.x=650
                yuri.draw()
                monika.draw()
                natsuki.draw()
                sayori.image="sayorihappy2"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Demir:YOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",(242, 584))
            elif d == 14:
                club.draw()
                sayori.x= 1050
                natsuki.x=650
                yuri.draw()
                monika.draw()
                natsuki.draw()
                sayori.image="sayorihappy2"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Demir:Ma' man how ya doing",(242, 584))
                screen.draw.text("Me:Nothin' much, you know I apparently slept through the school.",(242, 604))
                screen.draw.text("Demir:Isn't that more of a Duru thing though?",(242,624))
                screen.draw.text("Duru:Well it's not my fault I'm so sleepy now is it?",(242, 644))
                screen.draw.text("Demir:It kinda is.",(242,664))
            elif d == 15:
                club.draw()
                sayori.x = 1050
                natsuki.x = 650
                yuri.draw()
                monika.draw()
                natsuki.image = "natsukicute1"
                natsuki.draw()
                sayori.image = "sayoricute1"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Duru:HOW IS IT MY FAULT?", (242, 584))
                screen.draw.text("Demir:IT JUST IS YOU BAKA!",(242,604))
            elif d == 16:
                club.draw()
                sayori.x= 1050
                natsuki.x=650
                yuri.draw()
                monika.draw()
                natsuki.draw()
                sayori.image="sayoricute1"
                sayori.draw()
                textbox.draw()
                screen.draw.text("So the pink haired girl is my other friend Demir, she's more of a tsundere as I call em.",(242, 584))
                screen.draw.text("Wait why am I introducing her I already know he-",(242, 604))
            elif d == 17:
                club.draw()
                sayori.x= 1050
                natsuki.x=650
                yuri.draw()
                monika.draw()
                natsuki.draw()
                sayori.image="sayorisuprised1"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Duru:Wait guys, my phone's ringing.",(242, 584))
            elif d == 18:
                club.draw()
                sayori.x= 1050
                natsuki.x=650
                yuri.draw()
                monika.draw()
                natsuki.image=("natsukiembarrassed1")
                natsuki.draw()
                sayori.image="sayoricute1"
                textbox.draw()
                screen.draw.text("Demir:H-Hey, Kuzey y-yo- you-",(242, 584))
            elif d == 18:
                club.draw()
                sayori.x= 1050
                natsuki.x=650
                yuri.draw()
                monika.draw()
                natsuki.image=("natsukiembarrassed2")
                natsuki.draw()
                sayori.image="sayoricute1"
                textbox.draw()
                screen.draw.text("Demir:...",(242, 584))
            elif d == 19:
                club.draw()
                sayori.x= 1050
                natsuki.x=650
                yuri.draw()
                monika.draw()
                natsuki.image=("natsukiconfess1")
                natsuki.draw()
                sayori.image="sayoricute1"
                textbox.draw()
                screen.draw.text("Me:Demir you OK?",(242, 584))
            elif d == 20:
                club.draw()
                sayori.x= 1050
                natsuki.x=650
                yuri.draw()
                monika.draw()
                natsuki.image="natsukiconfess1"
                natsuki.draw()
                sayori.image="sayoricute1"
                textbox.draw()
                screen.draw.text("Demir:Y-Y-You down for s-some Fortnite tonight?(uwu)",(242, 584))
            elif d == 21:
                club.draw()
                sayori.x= 1050
                natsuki.x=650
                yuri.draw()
                monika.draw()
                natsuki.image="natsukiconfess1"
                natsuki.draw()
                sayori.image="sayoricute1"
                textbox.draw()
                choice.draw()
                choice2.draw()
                screen.draw.text("Demir:Y-Y-You down for s-some Fortnite tonight?(uwu)",(242, 584))
                screen.draw.text("Yeah, sure.",center=(640, 360),color="black")
                screen.draw.text("I'm sorry but I'll play frickin' Adopt Me or smh with Duru", center=(640, 400),color="black")
            elif d == 22:
                if fort == False:
                    club.draw()
                    sayori.x= 1050
                    natsuki.x=650
                    yuri.draw()
                    monika.draw()
                    natsuki.image="natsukitittle"
                    natsuki.draw()
                    sayori.image="sayoricute1"
                    textbox.draw()
                    screen.draw.text("Demir:Hmph! Not like I care anyway.",(242, 584))
                    screen.draw.text("Why'd she get so mad?",(242,604))
                elif fort == True:
                    club.draw()
                    sayori.x = 1050
                    natsuki.x = 650
                    yuri.draw()
                    monika.draw()
                    natsuki.image = "natsukihappy2"
                    natsuki.draw()
                    sayori.image = "sayoricute1"
                    textbox.draw()
                    screen.draw.text("Demir:Nice, uhh... 2:30 A.M. soundin' good?", (242, 584))
                    screen.draw.text("Me:2:30? Ya sure?",(242,604))
                    screen.draw.text("Demir:You're gonna chicken out you dummy?",(242,624))
            elif d == 23:
                club.draw()
                sayori.x= 1050
                natsuki.x=650
                yuri.draw()
                monika.draw()
                natsuki.image="natsuki1"
                natsuki.draw()
                sayori.image="sayoriconcerned2"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Duru:I'm back guys!",(242, 584))
                screen.draw.text("Demir:It's time to go already, baka.",(242, 604))
                screen.draw.text("Duru:WHAAAAT? Aww maaan...",(242, 624))
                screen.draw.text("Me:Tomorrow is another day to hang out.",(242, 644))
            elif d == 24:
                club.draw()
                sayori.x= 1050
                natsuki.x=650
                yuri.draw()
                monika.draw()
                natsuki.image="natsuki1"
                natsuki.draw()
                sayori.image="sayori1"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Me:Bye, guys.",(242, 584))
                screen.draw.text("Demir:Byeee~",(242, 604))
                screen.draw.text("Duru:C'ya.",(242, 624))
                screen.draw.text("",(242, 644))
            elif d == 25:
                outside.draw()
                sayori.x= 1050
                natsuki.x=650
                natsuki.image="natsukiconfess1"
                sayori.image="sayoricute1"
                textbox.draw()
                screen.draw.text("Gettin' to spend everyday with all o' those cute girls, huh?",(242, 584))
                screen.draw.text("Not bad of a fate for sure.",(242, 604))
                screen.draw.text("",(242, 624))
                screen.draw.text("",(242, 644))
            elif d == 26:
                outside.draw()
                sayori.x= 1050
                natsuki.x=650
                natsuki.image="natsukiconfess1"
                sayori.image="sayoricute1"
                textbox.draw()
                screen.draw.text("Why do I feel like 2 of those girls are gonna have no",(242, 584))
                screen.draw.text("significance in the plot?",(242, 604))
                screen.draw.text("",(242, 624))
                screen.draw.text("",(242, 644))
            elif d == 27:
                if fort==True:
                    room.draw()
                    sayori.x= 1050
                    natsuki.x=650
                    natsuki.image="natsukiconfess1"
                    sayori.image="sayoricute1"
                    fortnite.draw()
                    textbox.draw()
                    screen.draw.text("Me:Demir, I think I'll hop off now.",(242, 584))
                    screen.draw.text("Demir:Why?",(242, 604))
                    screen.draw.text("Me:I'm tired.",(242, 624))
                    screen.draw.text("Demir:God damn, this early?",(242, 644))
                elif fort == False:
                    room.draw()
                    sayori.x = 1050
                    natsuki.x = 650
                    natsuki.image = "natsukiconfess1"
                    sayori.image = "sayoricute1"
                    textbox.draw()
                    roblox.draw()
                    screen.draw.text("Duru:I'm sleepy Kuzey I'll go now.", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif  d== 28:
                if fort== True:
                    room.draw()
                    sayori.x = 1050
                    natsuki.image = "natsukiconfess1"
                    sayori.image = "sayoricute1"
                    textbox.draw()
                    fortnite.draw()
                    screen.draw.text("Me:IT'S LITERALLY 6 A.M. THERE'S SCHOOL IN 3 HOURS!", (242, 584))
                    screen.draw.text("Demir:Yes and?", (242, 604))
                    screen.draw.text("Me:I'm goin' good night.", (242, 624))
                    screen.draw.text("Demir:Good night I lo-.", (242, 644))
                else:
                    textbox.draw()
                    roblox.draw()
                    screen.draw.text("Me:Good night then.", (242, 584))
                    screen.draw.text("Duru:Good night lov-", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d==29:
                room.draw()
                textbox.draw()
                screen.draw.text("WHAT WAS SHE GONNA SAY!", (242, 584))
                day=2
                d=0
    elif day ==2:
        if mode == "game":
            if d==1:
                club.draw()
                yuri.draw()
                monika.draw()
                sayori.x=1050
                sayori.image= "sayorihappy1"
                natsuki.image= "natsukihappy1"
                natsuki.draw()
                sayori.draw()
                textbox.draw()
                screen.draw.text("Duru:Hi everyoneee~",(242, 584))
                screen.draw.text("DemirH-hi guys~", (242, 604))
                screen.draw.text("Me:Ayoooo how y'all doing?", (242, 624))
                screen.draw.text("", (242, 644))
            elif d==2:
                club.draw()
                yuri.draw()
                monika.draw()
                sayori.x=1050
                sayori.image= "sayoriconfess1"
                natsuki.image= "natsukiconfess1"
                natsuki.draw()
                sayori.draw()
                textbox.draw()
                screen.draw.text("Duru:Demir wanna meet up tomorrow?",(242, 584))
                screen.draw.text("Demir:Kuzey U-umm wanna meet up tomorrow?", (542, 584))
                screen.draw.text("Me:Duru Let's hang out after school tomorrow?", (382, 604))
                screen.draw.text("", (242, 644))
            elif d==3:
                club.draw()
                yuri.draw()
                monika.draw()
                sayori.x=1050
                sayori.image= "sayorisuprised1"
                natsuki.image= "natsukisuprised1"
                natsuki.draw()
                sayori.draw()
                textbox.draw()
                screen.draw.text("...",(242, 584))
                screen.draw.text("", (242, 604))
                screen.draw.text("", (242, 624))
                screen.draw.text("", (242, 644))
            elif d==4:
                club.draw()
                yuri.draw()
                monika.draw()
                sayori.x=1050
                sayori.image= "sayoriconfess1"
                natsuki.image= "natsukisuprised2"
                natsuki.draw()
                sayori.draw()
                textbox.draw()
                screen.draw.text("Duru:I guess all the 3 of us could go...",(242, 584))
                screen.draw.text("Demir:Y-yeah not like we were gonna do anything p-private.", (242, 604))
                screen.draw.text("", (242, 624))
                screen.draw.text("", (242, 644))
            elif d==5:
                club.draw()
                yuri.draw()
                monika.draw()
                sayori.x=1050
                sayori.image= "sayoriconfess1"
                natsuki.image= "natsukisuprised2"
                natsuki.draw()
                sayori.draw()
                choice.draw()
                choice2.draw()
                textbox.draw()
                screen.draw.text("Duru:I guess all the 3 of us could go...",(242, 584))
                screen.draw.text("Demir:Y-yeah not like we were gonna do anything p-private", (242, 604))
                screen.draw.text("I'd rather be alone with Demir.", center=(640, 360),color="black")
                screen.draw.text("Yeah, sure why not?", center=(640, 400),color="black")
            elif d==6:
                if wnat == True:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x=1050
                    sayori.image= "sayorireject1"
                    natsuki.image= "natsukimad2"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Demir:W-What do you mean you pervert?",(242, 584))
                    screen.draw.text("Duru:I'm coming weather you like it or not!", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif wnat == False:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayoriconfess1"
                    natsuki.image = "natsukiembarrassed2"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Demir:...", (242, 584))
                    screen.draw.text("Duru:...", (242, 604))
                    screen.draw.text("Me:...", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d==7:
                if wnat== True:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayorireject1"
                    natsuki.image = "natsukiembarrassed1"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Demir:Well I guess I wouldn't mi-", (242, 584))
                    screen.draw.text("Demir:I MEAN I guess if it can't be helped...", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif wnat==False:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayorihappy1"
                    natsuki.image = "natsukihappy1"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Demir:Anyway so where we meetin' up tomorrow?", (242, 584))
                    screen.draw.text("Duru:Anywhere works!", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d== 8:
                club.draw()
                yuri.draw()
                monika.draw()
                sayori.x = 1050
                sayori.image = "sayori2"
                natsuki.image = "natsuki2"
                natsuki.draw()
                sayori.draw()
                textbox.draw()
                screen.draw.text("Now if you couldn't tell tomorrow is the big day.", (242, 584))
                screen.draw.text("", (242, 604))
                screen.draw.text("", (242, 624))
                screen.draw.text("", (242, 644))
            elif d== 9:
                club.draw()
                yuri.draw()
                monika.draw()
                sayori.x = 1050
                sayori.image = "sayori2"
                natsuki.image = "natsuki2"
                natsuki.draw()
                sayori.draw()
                textbox.draw()
                screen.draw.text("Where I...", (242, 584))
                screen.draw.text("", (242, 604))
                screen.draw.text("", (242, 624))
                screen.draw.text("", (242, 644))
            elif d== 10:
                club.draw()
                yuri.draw()
                monika.draw()
                sayori.x = 1050
                sayori.image = "sayori1"
                natsuki.image = "natsuki1"
                natsuki.draw()
                sayori.draw()
                textbox.draw()
                screen.draw.text("I ask Duru out.", (242, 584))
                screen.draw.text("", (242, 604))
                screen.draw.text("", (242, 624))
                screen.draw.text("", (242, 644))
            elif d== 11:
                club.draw()
                yuri.draw()
                monika.draw()
                sayori.x = 1050
                sayori.image = "sayorihappy1"
                natsuki.image = "natsukihappy2"
                natsuki.draw()
                sayori.draw()
                textbox.draw()
                screen.draw.text("Me:Guys, let's meet up at that very specific place which never changes for some reason?", (242, 584))
                screen.draw.text("Duru:Oh yeaaah, THAT place.", (242, 604))
                screen.draw.text("Demir:Oh I know EXACTLY the place.", (242, 624))
                screen.draw.text("", (242, 644))
            elif d== 12:
                club.draw()
                yuri.draw()
                monika.draw()
                sayori.x = 1050
                sayori.image = "sayorihappy1"
                natsuki.image = "natsukihappy2"
                natsuki.draw()
                sayori.draw()
                textbox.draw()
                screen.draw.text("Come to think of it why is Demir named Demir?", (242, 584))
                screen.draw.text("", (242, 604))
                screen.draw.text("", (242, 624))
                screen.draw.text("", (242, 644))
            elif d== 13:
                club.draw()
                yuri.draw()
                monika.draw()
                sayori.x = 1050
                sayori.image = "sayorihappy2"
                natsuki.image = "natsukihappy1"
                natsuki.draw()
                sayori.draw()
                textbox.draw()
                screen.draw.text("Oh welp pretty poor naming scheme I guess.", (242, 584))
                screen.draw.text("", (242, 604))
                screen.draw.text("", (242, 624))
                screen.draw.text("", (242, 644))
            elif d== 14:
                if fort == True:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayoricute1"
                    natsuki.image = "natsuki1"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Duru:By the way, you meanies played Fortnite without me yesterday!", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif fort == False:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayori1"
                    natsuki.image = "natsukimad1"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Demir:By the way, you dummies played Roblox without me yesterday!", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d== 15:
                if fort == True:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayoricute1"
                    natsuki.image = "natsukimad3"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Demir:It's because you don't even LIKE Fortinte!", (242, 584))
                    screen.draw.text("Duru:Well that's no excuse!", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif fort==False:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayorisuprised1"
                    natsuki.image = "natsukimad1"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Duru:I thought you found Roblox cringe?", (242, 584))
                    screen.draw.text("Demir:Well, that still doesn't justify why you would play without me!", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d == 16:
                if fort==True:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayoricute1"
                    natsuki.image = "natsukicute1"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Demir:How is it not an excuse?", (242, 584))
                    screen.draw.text("Duru:I still would like to hang out!", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif fort == False:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayoricute1"
                    natsuki.image = "natsukicute1"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Duru:But you'd always make fun of me for it!", (242, 584))
                    screen.draw.text("Demir:I was just messing with you!", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d == 17:
                if fort==True:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayoricute1"
                    natsuki.image = "natsukicute1"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    choice.draw()
                    choice2.draw()
                    screen.draw.text("Demir:How is it not an excuse?", (242, 584))
                    screen.draw.text("Duru:I still would like to hang out!", (242, 604))
                    screen.draw.text("We'll invite you next time Duru.", center=(640, 360),color="black")
                    screen.draw.text("You shoulda told it to us.", center=(640, 400),color="black")
                elif fort == False:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayoricute1"
                    natsuki.image = "natsukicute1"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    choice.draw()
                    choice2.draw()
                    screen.draw.text("Duru:But you'd always make fun of me for it!", (242, 584))
                    screen.draw.text("Demir:I was just messing with you!", (242, 604))
                    screen.draw.text("Demir it perfectly justifies it.", center=(640, 360),color="black")
                    screen.draw.text("Duru let's invite her the next time around.", center=(640, 400),color="black")
            elif d == 18:
                if fort==True:
                    if herside==True:
                        club.draw()
                        yuri.draw()
                        monika.draw()
                        sayori.x = 1050
                        sayori.image = "sayorihappy1"
                        natsuki.image = "natsukimad2"
                        natsuki.draw()
                        sayori.draw()
                        textbox.draw()
                        screen.draw.text("Duru:Thanks Kuzey.", (242, 584))
                        screen.draw.text("Me:No problem.", (242, 604))
                        screen.draw.text("Duru:Good to know I have some REAL friends.", (242, 624))
                        screen.draw.text("Demir:YOU LITTLE-", (242, 644))
                    elif herside==False:
                        club.draw()
                        yuri.draw()
                        monika.draw()
                        sayori.x = 1050
                        sayori.image = "sayoriconcerned1"
                        natsuki.image = "natsuki2"
                        natsuki.draw()
                        sayori.draw()
                        textbox.draw()
                        screen.draw.text("Demir:Well you can still play with us whenever you wanna.", (242, 584))
                        screen.draw.text("Me:Yeah.", (242, 604))
                        screen.draw.text("", (242, 624))
                        screen.draw.text("", (242, 644))
                elif fort==False:
                    if herside==True:
                        club.draw()
                        yuri.draw()
                        monika.draw()
                        sayori.x = 1050
                        sayori.image = "sayorihappy1"
                        natsuki.image = "natsukitittle"
                        natsuki.draw()
                        sayori.draw()
                        textbox.draw()
                        screen.draw.text("Duru:Haha, eat THAT Demir!", (242, 584))
                        screen.draw.text("Demir:Simp.", (242, 604))
                        screen.draw.text("", (242, 624))
                        screen.draw.text("", (242, 644))
                    elif herside==False:
                        club.draw()
                        yuri.draw()
                        monika.draw()
                        sayori.x = 1050
                        sayori.image = "sayoriconcerned1"
                        natsuki.image = "natsukiemberrassed2"
                        natsuki.draw()
                        sayori.draw()
                        textbox.draw()
                        screen.draw.text("Duru:Be more clear next time around Demir.", (242, 584))
                        screen.draw.text("Demir:S-Sure", (242, 604))
                        screen.draw.text("", (242, 624))
                        screen.draw.text("", (242, 644))
            elif d==19:
                if lovemeter==3:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayorisuprised1"
                    natsuki.image = "natsuki1"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Duru:Oops, I forgot my book at the class I'll go pick that up.", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayori1"
                    natsuki.image = "natsuki2"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Demir:I forgot something in the closet I gotta get that.", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayori1"
                    natsuki.image = "natsuki2"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Nothing...Happens?", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d == 20:
                if lovemeter == 3:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayorisuprised1"
                    natsuki.image = "natsuki1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Me:I'll go after her.", (242, 584))
                    screen.draw.text("Demir:O-oh okay then?", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter == -3:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayori1"
                    natsuki.image = "natsuki2"
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Me:I'll go check up on her.", (242, 584))
                    screen.draw.text("Duru:Ok then.", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayori1"
                    natsuki.image = "natsuki2"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("I have a REALLY bad feeling about this", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d==21:
                if lovemeter==3:
                    classroom.draw()
                    sayori.image = "sayorisuprised1"
                    natsuki.image = "natsuki1"
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Duru:O-oh hi Kuzey...", (242, 584))
                    screen.draw.text("Me:'Sup", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    closet.draw()
                    sayori.x = 1050
                    sayori.image = "sayori1"
                    natsuki.image = "natsukiembarrassed1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir:Why are you here idiot-.", (242, 584))
                    screen.draw.text("Me:Duru left to get a book she forgot and I wanted to check up on you.", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayori1"
                    natsuki.image = "natsuki2"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Like I did something wrong?", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d==22:
                if lovemeter==3:
                    classroom.draw()
                    sayori.image = "sayorisuprised1"
                    natsuki.image = "natsuki1"
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Duru:...", (242, 584))
                    screen.draw.text("Me:...", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    closet.draw()
                    sayori.x = 1050
                    sayori.image = "sayori1"
                    natsuki.image = "natsukiembarrassed1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir:...", (242, 584))
                    screen.draw.text("Me:...", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayori1"
                    natsuki.image = "natsuki2"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("...", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d==23:
                if lovemeter==3:
                    classroom.draw()
                    sayori.image = "sayoriconcerned1"
                    natsuki.image = "natsuki1"
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Duru:W-why are you being this kind to me Kuzey?", (242, 584))
                    screen.draw.text("Me:What do you mean?", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    closet.draw()
                    sayori.x = 1050
                    sayori.image = "sayori1"
                    natsuki.image = "natsukiembarrassed1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir:Why did you not go after her then?", (242, 584))
                    screen.draw.text("Me:No reason...", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayori1"
                    natsuki.image = "natsuki2"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Like I coulda reached a better situation?", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d==24:
                if lovemeter==3:
                    classroom.draw()
                    sayori.image = "sayoriconcerned1"
                    natsuki.image = "natsuki1"
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Duru:You're so...caring and make me feel special", (242, 584))
                    screen.draw.text("Me:That's cause well I care 'bout you and you're special to me.", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    closet.draw()
                    sayori.x = 1050
                    sayori.image = "sayori1"
                    natsuki.image = "natsukiembarrassed2"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Me:Well there is one.", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayori1"
                    natsuki.image = "natsuki2"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Maybe in another universe where I tried harder?", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d==25:
                if lovemeter==3:
                    classroom.draw()
                    sayori.image = "sayoriconcerned1"
                    natsuki.image = "natsuki1"
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Duru:I...love you.", (242, 584))
                    screen.draw.text("Me:I love you too.", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    closet.draw()
                    sayori.x = 1050
                    sayori.image = "sayoriconcerned1"
                    natsuki.image = "natsukicute1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Me:I love you Demir.", (242, 584))
                    screen.draw.text("Demir:Wha-I... I also love you.", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    club.draw()
                    yuri.draw()
                    monika.draw()
                    sayori.x = 1050
                    sayori.image = "sayori1"
                    natsuki.image = "natsuki2"
                    natsuki.draw()
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Well no reason to be sad over another universe.", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d == 26:
                outside.draw()
                sayori.x= 1050
                natsuki.x=650
                natsuki.image="natsukiconfess1"
                sayori.image="sayoricute1"
                textbox.draw()
                screen.draw.text("I wonder what'll happen tomorrow...",(242, 584))
                screen.draw.text("",(242, 604))
                screen.draw.text("",(242, 624))
                screen.draw.text("",(242, 644))
            elif d==27:
                if lovemeter==3:
                    classroom.draw()
                    sayori.image = "sayoriconcerned1"
                    natsuki.image = "natsuki1"
                    sayori.draw()
                    textbox.draw()
                    screen.draw.text("Duru.", (242, 584))
                    screen.draw.text("What does she have to say?", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    closet.draw()
                    sayori.x = 1050
                    sayori.image = "sayoriconcerned1"
                    natsuki.image = "natsukicute1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir", (242, 584))
                    screen.draw.text("What does she have to say?", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    outside.draw
                    textbox.draw()
                    screen.draw.text("What'll happen tomorrow?", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d == 28:
                outside.draw()
                sayori.x= 1050
                natsuki.x=650
                natsuki.image="natsukiconfess1"
                sayori.image="sayoricute1"
                textbox.draw()
                screen.draw.text("These thoughts follow me home.",(242, 584))
                screen.draw.text("",(242, 604))
                screen.draw.text("",(242, 624))
                screen.draw.text("",(242, 644))
            elif d == 29:
                if lovemeter<3 and lovemeter>-3:
                    room.draw()
                    sayori.x= 1050
                    natsuki.x=650
                    natsuki.image="natsukiconfess1"
                    sayori.image="sayoricute1"
                    textbox.draw()
                    screen.draw.text("I have a bad feeling",(242, 584))
                    screen.draw.text("",(242, 604))
                    screen.draw.text("",(242, 624))
                    screen.draw.text("",(242, 644))
                else:
                    room.draw()
                    sayori.x = 1050
                    natsuki.x = 650
                    natsuki.image = "natsukiconfess1"
                    sayori.image = "sayoricute1"
                    textbox.draw()
                    screen.draw.text("I miss her already.", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d == 30:
                screen.fill("black")
                textbox.draw()
                screen.draw.text("I manage to fall asleep.", (242, 624)
                day=3
                d=1
    elif day ==3:
        if mode=="game":
            if d==1:
                classroom.draw()
                textbox.draw()
                screen.draw.text("Today is Friday.",(242, 584))
            elif d==2:
                classroom.draw()
                textbox.draw()
                screen.draw.text("Tomorrow is Saturday.",(242, 584))
            elif d==3:
                classroom.draw()
                textbox.draw()
                screen.draw.text("I'm kiddin' please no cringe song ruinin' my last day.",(242, 584))
            elif d==4:
                classroom.draw()
                textbox.draw()
                screen.draw.text("Those are the correct lyrics right?",(242, 584))
            elif d==5:
                classroom.draw()
                textbox.draw()
                screen.draw.text("Who am I talkin' to?",(242, 584))
            elif d==6:
                classroom.draw()
                textbox.draw()
                screen.draw.text("Anyway Friday means there are no club hours so Nothing important until school is over",(242, 584))
            elif d==7:
                classroom.draw()
                textbox.draw()
                sayori.image="sayori2"
                sayori.draw()
                screen.draw.text("Duru:Let's go meet up with Demir, Kuzey.",(242, 584))
            elif d==8:
                classroom.draw()
                sayori.image="sayori2"
                sayori.draw()
                textbox.draw()
                screen.draw.text("WHAT THE HELL WAS THAT?",(242, 584))
            elif d==9:
                classroom.draw()
                sayori.image="sayori2"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Oh Duru.",(242, 584))
            elif d==10:
                classroom.draw()
                sayori.image="sayori2"
                sayori.draw()
                textbox.draw()
                screen.draw.text("That was weird.",(242, 584))
            elif d==11:
                classroom.draw()
                sayori.image="sayoriconcerned2"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Duru:Kuzey, are you OK?",(242, 584))
            elif d==12:
                classroom.draw()
                sayori.image="sayoriconcerned2"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Duru:You look like you saw a ghost.",(242, 584))
            elif d==13:
                classroom.draw()
                sayori.image="sayoriconcerned2"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Me:No,It's fine.",(242, 584))
            elif d==14:
                classroom.draw()
                sayori.image="sayorihappy2"
                sayori.draw()
                textbox.draw()
                screen.draw.text("Duru:I'm glad to hear! Tell me if anything's buggin' ya!",(242, 584))
            elif d==15:
                classroom.draw()
                sayori.x=350
                natsuki.x=850
                sayori.image="sayorihappy2"
                sayori.draw()
                natsuki.image="natsukihappy1"
                natsuki.draw()
                textbox.draw()
                screen.draw.text("Demir:Hey guys!",(242, 584))
            elif d == 16:
                classroom.draw()
                sayori.x = 350
                natsuki.x = 850
                sayori.image = "sayorisuprised1"
                sayori.draw()
                natsuki.image = "natsukihappy1"
                natsuki.draw()
                textbox.draw()
                screen.draw.text("Duru:Whoa isn't your class the upper floor?", (242, 584))
            elif d == 17:
                classroom.draw()
                sayori.x = 350
                natsuki.x = 850
                sayori.image = "sayorihappy1"
                sayori.draw()
                natsuki.image = "natsukihappy1"
                natsuki.draw()
                textbox.draw()
                screen.draw.text("Demir:It is but y'all took your sweet time! So I decided to come myself.", (242, 584))
            elif d == 18:
                classroom.draw()
                sayori.x = 350
                natsuki.x = 850
                sayori.image = "sayorihappy1"
                sayori.draw()
                natsuki.image = "natsukihappy1"
                natsuki.draw()
                textbox.draw()
                screen.draw.text("Me:Well then, let's go.", (242, 584))
            elif d == 19:
                outside.draw()
                sayori.x = 350
                natsuki.x = 850
                sayori.image = "sayori2"
                sayori.draw()
                natsuki.image = "natsukiembarrassed1"
                natsuki.draw()
                textbox.draw()
                screen.draw.text("Me:From yesterday it looked like we all have something to say.", (242, 584))
                screen.draw.text("Demir:Y-yeah we do now don't we...", (242, 604))
                screen.draw.text("Duru:...", (242, 624))
                screen.draw.text("", (242, 644))
            elif d == 20:
                if lovemeter==3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayori2"
                    sayori.draw()
                    natsuki.image = "natsukiembarrassed3"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir:I-", (242, 584))
                    screen.draw.text("Me:I'll start first.", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayoriconfess2"
                    sayori.draw()
                    natsuki.image = "natsukiembarrassed1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Duru:I wanna start first!", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayori2"
                    sayori.draw()
                    natsuki.image = "natsukiembarrassed1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir:I'll start first.", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d == 21:
                if lovemeter==3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayori2"
                    sayori.draw()
                    natsuki.image = "natsukiembarrassed3"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Me:Duru...", (242, 584))
                    screen.draw.text("Duru:Yes?", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayoriconfess1"
                    sayori.draw()
                    natsuki.image = "natsukiembarrassed1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Duru:Demir.", (242, 584))
                    screen.draw.text("Demir:Y-yes?", (242, 604))
                    screen.draw.text("Duru:Since I laid my eyes on you skies have been forever blue.", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayoriconfess1"
                    sayori.draw()
                    natsuki.image = "natsukiconfess1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir:Duru...", (242, 584))
                    screen.draw.text("Duru:Demir...", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d == 22:
                if lovemeter==3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayoriconfess1"
                    sayori.draw()
                    natsuki.image = "natsukiembarrassed3"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Me:Ever since the day we met a parcel of my mind's lost to you.", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayorireject1"
                    sayori.draw()
                    natsuki.image = "natsukiconfess1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir:I-I'm sorry, Duru but I'm already into Kuzey...", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayoriconfess1"
                    sayori.draw()
                    natsuki.image = "natsukiembarrassed1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir:The reason I called everyone here was cuz.", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d == 23:
                if lovemeter==3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayoriconcerned1"
                    sayori.draw()
                    natsuki.image = "natsukireject1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayorireject1"
                    sayori.draw()
                    natsuki.image = "natsukisad1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayori2"
                    sayori.draw()
                    natsuki.image = "natsukiconfess1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir:Cuz I liked you", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d == 24:
                if lovemeter==3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayoriconcerned2"
                    sayori.draw()
                    natsuki.image = "natsukireject2"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayorireject2"
                    sayori.draw()
                    natsuki.image = "natsukisad1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayoriconcerned1"
                    sayori.draw()
                    natsuki.image = "natsukiconfess1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir:For the longest time now I've loved you.", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d == 25:
                if lovemeter==3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayoriconcerned2"
                    sayori.draw()
                    natsuki.image = "natsukireject3"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayorireject2"
                    sayori.draw()
                    natsuki.image = "natsukisad1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir:Duru, I-", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayori2"
                    sayori.draw()
                    natsuki.image = "natsukiembarrassed1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Duru:I also love you, Demir.", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d == 26:
                if lovemeter==3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayoriconcerned1"
                    sayori.draw()
                    natsuki.image = "natsukiembarrassed3"
                    textbox.draw()
                    screen.draw.text("Demir ran away...", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayoriconfess2"
                    natsuki.image = "natsukiembarrassed1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Duru ran away...", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayori2"
                    sayori.draw()
                    natsuki.image = "natsukiembarrassed1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir:Will you accept me to be your boyfriend?", (242, 584))
                    screen.draw.text("Oh maaan...", (242, 604))
                    screen.draw.text("WAIT BOYFRIEND?", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d == 27:
                if lovemeter==3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayorihappy3"
                    sayori.draw()
                    natsuki.image = "natsukiembarrassed3"
                    textbox.draw()
                    screen.draw.text("Duru:She'll be chill with it don't worry", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayoriconfess2"
                    natsuki.image = "natsukihappy1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir:That dummy will be back later don't mind her.", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayorihappy2"
                    sayori.draw()
                    natsuki.image = "natsukihappy1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("I won't question it.", (242, 584))
                    screen.draw.text("I'm happy as long as they are.", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d == 28:
                if lovemeter==3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayorihappy3"
                    sayori.draw()
                    natsuki.image = "natsukiembarrassed3"
                    textbox.draw()
                    screen.draw.text("Me:Duru, will you be my girlfriend?", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayoriconfess2"
                    natsuki.image = "natsukiconfess1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir:Will you be my boyfriend, Kuzey?", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayorihappy3"
                    sayori.draw()
                    natsuki.image = "natsukihappy1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir:Of course you dummy!", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d == 29:
                if lovemeter==3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayorihappy3"
                    sayori.draw()
                    natsuki.image = "natsukiembarrassed3"
                    textbox.draw()
                    screen.draw.text("Duru:Why did you wait so long you meanie!", (242, 584))
                    screen.draw.text("Duru:Of course!", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayoriconfess2"
                    natsuki.image = "natsukiconfess1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir:Will you be my boyfriend?", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("Hell yeah I will.", (242, 604))
                else:
                    if fort == True:
                        outside.draw()
                        sayori.x = 350
                        natsuki.x = 850
                        sayori.image = "sayori2"
                        sayori.draw()
                        natsuki.image = "natsuki1"
                        natsuki.draw()
                        textbox.draw()
                        screen.draw.text("Duru:What were you gonna say Kuzey?", (242, 584))
                        screen.draw.text("I can't believe this.", (242, 604))
                        screen.draw.text("Me:If y'all wanted to hop on some Fortnite tonight.", (242, 624))
                        screen.draw.text("", (242, 644))
                    elif fort == False:
                        outside.draw()
                        sayori.x = 350
                        natsuki.x=850
                        sayori.image="sayori2"
                        sayori.draw()
                        natsuki.image="natsuki1"
                        natsuki.draw()
                        textbox.draw()
                        screen.draw.text("Duru:What were you gonna say Kuzey?", (242,584))
                        screen.draw.text("I can't believe this.", (242, 604))
                        screen.draw.text("Me:If y'all wanted to hop on some Roblox tonight.")
            elif d == 30:
                if lovemeter==3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayorisuprised1"
                    sayori.draw()
                    natsuki.image = "natsukiembarrassed3"
                    textbox.draw()
                    screen.draw.text("Duru:Let's go to the mall then how's that sound?.", (242, 584))
                    screen.draw.text("Me:Fine by me.", (242, 604))
                    screen.draw.text("Duru:Let's go then~", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayoriconfess2"
                    natsuki.image = "natsukihappy2"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Demir:Oh by the way.", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayori2"
                    sayori.draw()
                    natsuki.image = "natsukiembarrassed1"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Duru:Sure, that sounds good.", (242, 584))
                    screen.draw.text("Demir:Why not?", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
            elif d == 31:
                if lovemeter==3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayori2"
                    natsuki.image = "natsukiembarrassed3"
                    textbox.draw()
                    screen.draw.text("Duru:By the way Demir is a guy.", (242, 584))
                    screen.draw.text("Me:What th-", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    outside.draw()
                    sayori.x = 350
                    natsuki.y = 500
                    sayori.image = "sayoriconfess2"
                    natsuki.image = "menu_art_n_ghost"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("I'm a guy.", (242, 584))
                    screen.draw.text("", (242, 604))
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    outside.draw()
                    sayori.x = 350
                    natsuki.x = 850
                    sayori.image = "sayorihappy1"
                    sayori.draw()
                    natsuki.image = "natsukihappy2"
                    natsuki.draw()
                    textbox.draw()
                    screen.draw.text("Duru:We're goin' to the mall.", (242, 584))
                    screen.draw.text("Demir:Then stoppin' at the park!", (242, 604))
                    screen.draw.text("Duru:Sure why not.", (242, 624))
                    screen.draw.text("Me:C'ya around guys.", (242, 644))
            elif d == 32:
                if lovemeter==3:
                    wolf.draw()
                    textbox.draw()
                    screen.draw.text("Demir:Another alone night...", (242, 584))
                    screen.draw.text("GOOD END", center=(640, 200),fontsize=30)
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                elif lovemeter==-3:
                    wolf.draw()
                    textbox.draw()
                    screen.draw.text("Duru:Another night spent alone...", (242, 584))
                    screen.draw.text("BAD END", center=(640, 200),fontsize=30)
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))
                else:
                    wolf.draw()
                    textbox.draw()
                    screen.draw.text("Me:Another night by myself...", (242, 584))
                    screen.draw.text("INCEL END", center=(640, 200),fontsize=30)
                    screen.draw.text("", (242, 624))
                    screen.draw.text("", (242, 644))


















def on_mouse_down(button, pos):
    global mode
    global lovemeter
    global day
    global d
    global fort
    global wnat
    global herside
    if button == mouse.LEFT and mode == "menu":
        if newgame.collidepoint(pos):
            mode = "game"
    if button == mouse.LEFT and mode == "menu":
        if quit.collidepoint(pos):
            quit()
    elif button == mouse.LEFT and mode == "game" and day ==1 and d!=21:
        if textbox.collidepoint(pos):
            d=d+1
    if button == mouse.LEFT and mode == "game" and day== 1 and d==21:
        if choice.collidepoint(pos):
            fort= True
            d=22
            lovemeter-=1
        if choice2.collidepoint(pos):
            fort=False
            d=22
            lovemeter+=1
    if button==mouse.LEFT and mode == "game" and day == 2 and d!=5 and d!=17:
        if textbox.collidepoint(pos):
            d=d+1
    if button==mouse.LEFT and mode == "game" and day== 2 and d==5:
        if choice.collidepoint(pos):
            wnat=True
            lovemeter-=1
            d=6
        if choice2.collidepoint(pos):
            wnat=False
            lovemeter+=1
            d=6
    if button==mouse.LEFT and mode=="game" and day == 2 and d==17:
        if fort ==True:
            if choice.collidepoint(pos):
                herside=True
                lovemeter+=1
                d = 18
            elif choice2.collidepoint(pos):
                herside=False
                lovemeter-=1
                d = 18
        else:
            if choice.collidepoint(pos):
                herside=True
                lovemeter+=1
                d = 18
            elif choice2.collidepoint(pos):
                herside=False
                lovemeter-=1
                d=18
    if button==mouse.LEFT and day==3 and mode =="game":
        if textbox.collidepoint(pos):
            d+=1
sounds.love_literature.play()


pgzrun.go()
