## Chapter ???

![Chapter select button. A Magic 8 Ball.](./images/chapterselect/8ball.png)

<p class="command-box">Check back later!</p>

init python:
    build.archive("chapter6", "all")
    build.classify('game/chapters/6/**', 'chapter6')

image bg davepeta_8ball:
    size (950,650) yalign 0.5 xalign 0.5
    "chapters/6/images/Davepeta_8ball.png"

image bg davepeta_vriska_hug:
    size (950,650) yalign 0.5 xalign 0.5
    "chapters/6/images/Davepeta_Vriska-hug.png"

image bg 8ball:
    size (950,650) yalign 0.5 xalign 0.5
    "chapters/6/images/8ball.png"

image bg 8ball_1:
    size (950,650) yalign 0.5 xalign 0.5
    "chapters/6/images/8ballVoid_1.png"

image bg 8ball_2:
    size (950,650) yalign 0.5 xalign 0.5
    "chapters/6/images/8ballVoid_2.png"

image bg 8ball_3:
    size (950,650) yalign 0.5 xalign 0.5
    "chapters/6/images/8ballVoid_3.png"

image bg 8ball_4:
    size (950,650) yalign 0.5 xalign 0.5
    "chapters/6/images/8ballVoid_4.png"

image bg vris_beach:
    size (950,650) yalign 0.5 xalign 0.5
    "chapters/6/images/Vriska_Beach.png"

image horses:
    "chapters/6/images/horses.png"

transform fadeout:
    alpha 1.0
    easeout 2.0 alpha 0.0

transform spinfade:
    alpha 1.0
    parallel:
        easeout 0.5 xzoom -1.0
        easeout 0.5 yzoom 1.0
        repeat
    parallel:
        easeout 1.0 alpha 0.0

label chapter6:
    scene black

<p class="box">LATER</p>

![Background: Vriska's room](./images/vriskaroom.png)

    show davepeta neutral onlayer talksprites at right with slideinright
    DAVEPETASPRITE "well here we are"
    hide davepeta with slideoutright


    show vriska adult proud onlayer talksprites at left with slideinleft
    VRISKA adult "Here we fucking are!"
    hide vriska with slideoutleft


    show davepeta thinking onlayer talksprites at right with slideinright
    DAVEPETASPRITE "its b33n a long ass time but were cr33ping up behind the grand finale"
    DAVEPETASPRITE neutral "that finale is never gonna s33 it coming"
    hide davepeta with slideoutright


    show vriska adult smiling onlayer talksprites at left with slideinleft
    VRISKA adult "The final 8oss."
    hide vriska with slideoutleft


    show davepeta laugh onlayer talksprites at right with slideinright
    DAVEPETASPRITE "master hand, your days are fucking numbered"
    hide davepeta with slideoutright


    show vriska adult smiling onlayer talksprites at left with slideinleft
    VRISKA adult "More like minutes!"
    hide vriska with slideoutleft


    show davepeta neutral onlayer talksprites at right with slideinright
    DAVEPETASPRITE "finally ready to take that final step"
    hide davepeta with slideoutright


    show vriska adult smiling onlayer talksprites at left with slideinleft
    VRISKA adult "I needed a 8reather!"
    hide vriska with slideoutleft


    show davepeta neutral onlayer talksprites at right with slideinright
    DAVEPETASPRITE "you sure did!"
    DAVEPETASPRITE neutral "*a tear begins to well up in dps eye behind their shades*"
    DAVEPETASPRITE neutral "*they f33l like a mom s33ing their freshly pupated charge about to finish their final trials and march off to the subgrubs or maybe a dope ass cave*"
    DAVEPETASPRITE thinking "*dp wonders will they be safe out there? will she make use of all the lessons theyve learned here?*"
    DAVEPETASPRITE thinking "*will she remember to wipe the lid?*"
    hide davepeta with slideoutright


    show fefeta neutral onlayer talksprites at right with slideinright
    FEFETASPRITE "3833 < 383"
    hide fefeta with slideoutright


    show vriska adult proud onlayer talksprites at left with slideinleft
    VRISKA adult "*The Thief proudly puffs out her chest with her hands on her hips and her 8ack to the sun, looking heroic and 8adass.*"
    VRISKA adult proud "Ha! You've got nothing to fear."
    VRISKA adult proud "I'm older and wiser now."
    VRISKA adult smiling "I want to thank you, too."
    hide vriska with slideoutleft


    show davepeta thinking onlayer talksprites at right with slideinright
    DAVEPETASPRITE "what for"
    DAVEPETASPRITE laugh "i barely did shit"
    hide davepeta with slideoutright


    show vriska adult smiling onlayer talksprites at left with slideinleft
    VRISKA adult "Haha yeah, 8ut I'm glad you were here anyway."
    VRISKA adult smiling "You and everyone else!"
    hide vriska with slideoutleft


    show fefeta neutral onlayer talksprites at right with slideinright
    FEFETASPRITE "3833 < 383"
    hide fefeta with slideoutright


    show vriska adult smiling onlayer talksprites at left with slideinleft
    VRISKA adult "........"
    VRISKA adult stoic "Okay, I have to say something."
    VRISKA adult neutral "So, DP, you're half Nepeta, right?"
    hide vriska with slideoutleft


    show davepeta neutral onlayer talksprites at right with slideinright
    DAVEPETASPRITE "yeah"
    hide davepeta with slideoutright


    show vriska adult neutral onlayer talksprites at left with slideinleft
    VRISKA adult "Well, more of a whole Nepeta, along with a whole other dude."
    hide vriska with slideoutleft


    show davepeta neutral onlayer talksprites at right with slideinright
    DAVEPETASPRITE "... yeah?"
    hide davepeta with slideoutright


    show fefeta neutral onlayer talksprites at right with slideinright
    FEFETASPRITE "3833 < 383"
    hide fefeta with slideoutright


    show vriska adult neutral onlayer talksprites at left with slideinleft
    VRISKA adult "8ut Fefeta's also a whole Nepeta!"
    hide vriska with slideoutleft


    show fefeta neutral onlayer talksprites at right with slideinright
    FEFETASPRITE "3833 < ..."
    hide fefeta with slideoutright


    show vriska adult neutral onlayer talksprites at left with slideinleft
    VRISKA adult "So like... how does that work?"
    hide vriska with slideoutleft


    show davepeta uncomfortable onlayer talksprites at right with slideinright
    DAVEPETASPRITE_800 "vriska wait dont say it!!!!"
    hide davepeta with slideoutright


    show vriska adult neutral onlayer talksprites at left with slideinleft
    VRISKA adult "Why are there two Nepetas?"
    hide vriska with slideoutleft


    play sfx "chapters/6/audio/disappear.ogg" volume 0.75 noloop
    show fefeta xc onlayer talksprites at right, fadeout with slideinright
    FEFETASPRITE "3X(( < 3X(("
    hide fefeta with Dissolve(0.3)


    show vriska adult confused onlayer talksprites at left with slideinleft
    VRISKA adult "... What the fuck was that?"
    hide vriska with slideoutleft


    show davepeta pokerface onlayer talksprites at right with slideinright
    DAVEPETASPRITE "you just fucking sent dear sw33t precious fefeta to sprite city."
    hide davepeta with slideoutright


    show vriska adult confused onlayer talksprites at left with slideinleft
    VRISKA adult "????????"
    hide vriska with slideoutleft


    show davepeta laugh onlayer talksprites at right with slideinright
    DAVEPETASPRITE "hahahaha anyway"
    DAVEPETASPRITE neutral "i was just fucking around earlier but honestly, im actually gonna miss you"
    DAVEPETASPRITE cute "i think im f33ling a goodbye glomp coming on"
    hide davepeta with slideoutright


    show vriska adult glaring onlayer talksprites at left with slideinleft
    VRISKA adult "Hey hey, we talked a8out this."
    hide vriska with slideoutleft


    show davepeta pokerface onlayer talksprites at right with slideinright
    DAVEPETASPRITE "oh yeah sorry"
    DAVEPETASPRITE uncomfortable "{size=14}*dp deflates like a cartoon meowbeast thats b33n blown up by some freaky pervert, tied to a balloon, handed off to a snot nosed kid at a theme park who just fucking lets it go because he got distracted by goofy and mickey duking it out (that summer heat makes people crazy)*{/size}"
    hide davepeta with slideoutright


    show vriska adult neutral onlayer talksprites at left with slideinleft
    VRISKA adult "Alright fine, one hug 8efore I crush this and I'm outta here."
    hide vriska with slideoutleft

![A simplistic MS Paint sketch of Davepeta hugging the reluctant Vriska. "Glomp!!!!"](./images/6/images/Davepeta_Vriska-hug.png)

    DAVEPETASPRITE_center "yay"

![Closeup: Davepeta clutches the 8 ball and extends it toward Vriska.](images/6/images/Davepeta_8ball.png)

    DAVEPETASPRITE_center "here you go, your last hell"


    VRISKA_center "I've 8een waiting for this one."
    VRISKA_center "I have a pretty good feeling I know who's waiting on the other side."

    DAVEPETASPRITE_center "*sniffs* you're a real pro at this silent hill mind prison shit now, youve come so far"

    VRISKA_center "It's 8een real Davepeta, see you around!"

    DAVEPETASPRITE_center "good luck vriska!"

    show blue with Dissolve(1.0)
    stop music fadeout 2.0
    show black with Dissolve(1.0)

    scene black
    VRISKA_center "..."

![The inside of the 8 ball. A dark void. A tree is barely visible.](./images/6/images/8ballVoid_1.png)

    VRISKA_center "...?"
    VRISKA_center "Hey!!!!!!!!"

    play music "chapters/6/audio/terezi_vn.ogg" fadein 1.0 volume 0.5 loop

![The scene gets closer and clearer. A tree in a field of green and red. At the center, stands a young troll girl, facing away.](./images/6/images/8ballVoid_2.png)

    VRISKA_center "Terezi!!!!!!!!"
    VRISKA_center "Is that you?"
    VRISKA_center "I knew it would 8e you!"
    VRISKA_center "You were the one thing missing from this!"
    VRISKA_center "Even if you're just a phantom designed explicitly to torture me, I'm so happy to see-"
    VRISKA_center "you...?"
    
![Closer. The troll from behind. She's wearing a gray tank top, and her hair is pulled back into braids, resembling Meenah's.](./images/6/images/8ballVoid_3.png)

    VRISKA_center "What?"
    VRISKA_center "Who are..."

![Closeup. She turns around, revealing a teenage Vriska with empty white eyes. It's (Vriska), the ghost of her younger self from the Game Over timeline.](./images/6/images/8ballVoid_4.png)

    stop music
    pause

![Background. A dream bubble. Green grass, red mountains, and a large green tree with red blossoms.](./images/6/images/8ball.png)

    play music "chapters/6/audio/11-6.wav" fadein 1.0 volume 0.5 loop
    show vriska adult glaring onlayer talksprites at left with slideinleft
    VRISKA adult "..."
    hide vriska with slideoutleft

    show vriska_paren sad onlayer talksprites at right with slideinright
    VRISKA_paren "..."
    hide vriska_paren with slideoutright

    show vriska adult glaring onlayer talksprites at left with slideinleft
    VRISKA adult glaring "..."
    hide vriska with slideoutleft

    show vriska_paren sad onlayer talksprites at right with slideinright
    VRISKA_paren "..."
    hide vriska_paren with slideoutright


    show vriska adult uncomfortable onlayer talksprites at left with slideinleft
    VRISKA adult uncomfortable "........"
    VRISKA adult uncomfortable "Alright, fine."
    VRISKA adult uncomfortable "Makes sense I'd have to do this eventually."
    VRISKA adult neutral "I'm sorry."
    VRISKA adult uncomfortable "For all that shit I said to- did to you."
    VRISKA adult uncomfortable "It was wrong of me to hate you for getting soft."
    VRISKA adult uncomfortable "For knowing when to quit."
    VRISKA adult sad "For choosing to be happy."
    VRISKA adult neutral "I get that now."
    hide vriska with slideoutleft

    show vriska_paren hug onlayer talksprites at right with slideinright
    VRISKA_paren "..."
    hide vriska_paren with slideoutright

    show vriska adult shocked onlayer talksprites at left with slideinleft
    VRISKA adult shocked "HUH???????? What the hell..."
    hide vriska with slideoutleft

    show vriska_paren hug onlayer talksprites at right with slideinright
    VRISKA_paren "..."
    hide vriska_paren with slideoutright

    show vriska adult uncomfortable onlayer talksprites at left with slideinleft
    VRISKA adult uncomfortable "Come on now..."
    hide vriska with slideoutleft

    show vriska_paren hug onlayer talksprites at right with slideinright
    VRISKA_paren "..."
    hide vriska_paren with slideoutright

    show vriska adult uncomfortable onlayer talksprites at left with slideinleft
    VRISKA adult uncomfortable "You're asking for too much."
    VRISKA adult glaring "You're really going to make me do this?"
    VRISKA adult uncomfortable "..."
    hide vriska with slideoutleft

    box "What will you do?"

    show vriska adult uncomfortable onlayer talksprites at left with slideinleft
    VRISKA adult "..."
    VRISKA adult sad "I..."
    VRISKA adult stoic "I won't."
    hide vriska with slideoutleft

    show vriska_paren sad onlayer talksprites at right with slideinright
    VRISKA_paren "..."
    hide vriska_paren with slideoutright


    show vriska adult uncomfortable onlayer talksprites at left with slideinleft
    VRISKA adult "I can't."
    show vriska adult uncomfortable:



        linear 0.1 xzoom -1.0 xcenter 0.5 xoffset -100
    pause 0.25
    hide vriska with slideoutleftslow
    stop music fadeout 3.0

    show white with Dissolve(3.0)
    pause 3.5
    play music "chapters/6/audio/vrisbeach-dreamy.ogg" fadein 1.0 volume 0.5 loop


<div class="beach">
    <img class="beach_bg" src="./images/6/images/Vriska_Beach.png"
        alt="Vriska sits on the familiar beach outside her hive, exactly back where she started. A herd of horses slowly runs past.">
    <img class="beach_horses" role="presentation" src="./images/6/images/horses.png">
</div>

    scene bg vris_beach with Dissolve(2.0)
    show horses onlayer talksprites with Dissolve(2.0):
        yoffset 440
        xalign 0.1
        linear 50.0 xalign 1.5
    pause

    stop music fadeout 3.0
    show white onlayer talksprites with Dissolve(3.0)
    hide horses
    return
