init python:
    build.archive("chapter1", "all")
    build.classify('game/chapters/1/**', 'chapter1')

image c1p1f1:
    size (950,650)
    xalign 0.5 yalign 0.0
    nearest True
    "chapters/1/images/panel1_1.png"

image c1p1f2:
    size (950,650)
    xalign 0.5 yalign 0.0
    nearest True
    "chapters/1/images/panel1_2.png"

image c1p1:
    contains:
        "c1p1f1"
    contains:
        "c1p1f2"
        alpha 0.0
        linear 0.25 alpha 1.0
        linear 0.25 alpha 0.0
        repeat
image c1p2:
    xalign 0.0 yalign 0.0
    "chapters/1/images/panel2_1.png"
    pause (0.05)
    "chapters/1/images/panel2_2.png"
    pause (0.05)
    repeat
image c1p3:
    xalign 1.0 yalign 1.0
    "chapters/1/images/panel3.png"
image c1p4:
    zoom 1.5
    nearest True
    xalign 0.5 yalign 1.0
    "chapters/1/images/panel4.png"
image c1p5:
    zoom 1.5
    nearest True
    xalign 0.5 yalign 1.0
    "chapters/1/images/panel5.png"
image c1p6:
    zoom 1.5
    nearest True
    yoffset -50
    xalign 0.5 yalign 0.0
    "chapters/1/images/panel6.png"

image c1end:
    yalign 0.0
    "chapters/1/images/end.png"

label chapter1:


    $ quick_menu = True

    if renpy.confirm("Would you like to skip to the chapter select menu?"):
        $ MainMenu(confirm=False)()





    scene bg tavroscliff with Dissolve(2.0)

    "You are now Vriska, and like any good Main Character, you find yourself on the precipice of an all too familiar cliff." (sfx=None)

    play music "chapters/1/audio/c1.mp3" fadein 1.0 loop

    show vriska gt onlayer talksprites at left with slideinleft

    VRISKA "Wow, hell was right."

    VRISKA "You h8 to see it."
    hide vriska with slideoutleft


    box "What will you do?"


    show vriska gt angry onlayer talksprites at left with slideinleft

    VRISKA gt angry "What do you MEAN what will I do????????"

    VRISKA "Davepeta, is that you?"

    VRISKA gt thinking "..."

    VRISKA gt smug "Wow once again it falls to me to figure all this shit out in any sort of meaningful way."

    VRISKA gt idle "..."

    VRISKA gt angry "And why the fuck is Tavros here!!!!!!!!"
    hide vriska with slideoutleft


    show tavros onlayer talksprites at right with slideinright

    TAVROS "i PROBABLY DON'T, uHH, WANT TO QUESTION, yOUR METHODS"

    TAVROS nervous "aND MAYBE, iF THERE WERE A BRAVER VERSION, oF ME, hERE, HE MIGHT SAY, tHAT UM, iT'S BECAUSE USUALLY, tHAT MAKES YOU MAD"

    TAVROS "bUT SINCE THERE ISN'T, a VERSION OF ME LIKE THAT HERE, i GUESS IT'S BECAUSE I, uHH"

    TAVROS smiling "lIVE HERE MOSTLY,"
    hide tavros with slideoutright


    show vriska gt onlayer talksprites at left with slideinleft

    VRISKA "Shut the fuck up Tavros!"

    VRISKA gt thinking "This is o8viously some sort of trial."

    VRISKA "Cleeeeeeeearly I'm 8eing faced with the ghosts of my past and I have to \"sort it out\" or some horse shit."

    VRISKA "Thanks for the guidance, Nepadave, or whoever the literal hell."

    VRISKA gt smug "8ut I got it all figured out already!"

    VRISKA gt thinking "I'm going to speedrun enlightenment and save this horri8le fake universe from imploding in on itself."

    VRISKA gt smug "You're welcome."
    hide vriska with slideoutleft


    show tavros onlayer talksprites at right with slideinright

    TAVROS "oK WELL, i WILL PRETEND THAT, uHH"

    TAVROS "iF I WAS SOMEONE, wHO DIDN'T UNDERSTAND, wHAT YOU WERE SAYING,"

    TAVROS nervous "bECAUSE, i'M FEELING PRETTY ALIVE FOR THE MOST PART, i THINK"

    TAVROS "tHAT PERSON, tHAT I'M PRETENDING TO BE, mIGHT ASK"

    TAVROS smiling "wHY, yOU THINK THAT IM A GHOST,"
    hide tavros with slideoutright


    show vriska gt onlayer talksprites at left with slideinleft

    VRISKA "You still have legs, for one."
    hide vriska with slideoutleft


    show tavros onlayer talksprites at right with slideinright

    TAVROS "oH THANK YOU,"

    TAVROS "tHAT IS A NORMAL THING, fOR YOU TO SAY, aBOUT GHOSTS,"

    TAVROS smiling "i SEE UM, yOU ALSO, hAVE LEGS"

    TAVROS nervous "wHICH MIGHT BE A GHOST THING, tHAT I AM MOSTLY, uNAWARE OF"

    TAVROS "sO, mAYBE, wE ARE BOTH GHOSTS,"

    TAVROS smiling "}:)"
    hide tavros with slideoutright


    show vriska gt thinking onlayer talksprites at left with slideinleft

    VRISKA gt thinking "I've already done this, though."

    VRISKA gt smug "I reconciled with Tavros days ago."

    VRISKA "I'm completely in the clear! He forgave me already."
    hide vriska with slideoutleft


    show tavros nervous onlayer talksprites at right with slideinright

    TAVROS nervous "fOR WHAT,"
    hide tavros with slideoutright


    show vriska gt thinking onlayer talksprites at left with slideinleft

    VRISKA gt thinking "It couldn't 8e that easy, could it?"

    VRISKA "Hey. Tavros."
    hide vriska with slideoutleft


    show tavros smiling onlayer talksprites at right with slideinright

    TAVROS smiling "hI THAT'S ME, i THINK,"
    hide tavros with slideoutright


    show vriska gt onlayer talksprites at left with slideinleft

    VRISKA "I'm sorry I killed you."
    hide vriska with slideoutleft


    show tavros onlayer talksprites at right with slideinright

    TAVROS "dID YOU DO THAT,"
    hide tavros with slideoutright


    box "What will you do?"


    show vriska gt idle onlayer talksprites at left with slideinleft

    VRISKA gt idle ""

    VRISKA gt neutral "... damn."

    VRISKA gt smug "Well I guess it wouldn't 8e worth anything if it were that simple."
    hide vriska with slideoutleft


    show tavros nervous onlayer talksprites at right with slideinright

    TAVROS nervous "uM VRISKA DID-"
    hide tavros with slideoutright


    show vriska gt angry onlayer talksprites at left with slideinleft

    VRISKA gt angry "Ugh!!!!!!!!"

    VRISKA gt thinking "What did they mean \"sort it out,\" then? I feel fine a8out killing Tavros, and he's certainly ok with it now. The situation's sorted!"
    hide vriska with slideoutleft


    show tavros smiling onlayer talksprites at right with slideinright

    TAVROS smiling "iS THAT TRUE,"
    hide tavros with slideoutright


    show vriska gt onlayer talksprites at left with slideinleft

    VRISKA "It's completely sorted!"

    VRISKA "Damn, it could have 8een any num8er of things."

    VRISKA gt smug "I did a lot of things wrong."

    VRISKA "Hey Tavros, I'm sorry I made you an accomplice to a really awesome assassination that I got my ass kicked for, 8ut then I 8ecame a god so 8asically it was the right thing to do."
    hide vriska with slideoutleft


    show tavros smiling eyesclosed onlayer talksprites at right with slideinright

    TAVROS smiling eyesclosed "..."
    hide tavros with slideoutright


    box "What will you do?"


    show vriska gt thinking onlayer talksprites at left with slideinleft

    VRISKA gt thinking "No dice, huh? Okay, try this one on for size!"

    VRISKA "I'm sorry I kissed you and then used mind control to make you try and love me that one time. That one's on me."
    hide vriska with slideoutleft


    show tavros smiling onlayer talksprites at right with slideinright

    TAVROS smiling "..."
    hide tavros with slideoutright


    box "What will you do?"


    show vriska gt onlayer talksprites at left with slideinleft

    VRISKA "Fuck, that was a good one... this character growth shit is hard."
    hide vriska with slideoutleft

    $ command = "{{Hours later, but not many.}"
    menu:
        "{plain}[pick] {/plain}[command]":
            show black with Dissolve(2.0)
            hide black with Dissolve(2.0)


    show vriska gt sad onlayer talksprites at left with slideinleft

    VRISKA gt sad "...I'm sorry I said your lusus \"smelled like tears\"."
    hide vriska with slideoutleft


    box "What will you do?"

    show vriska gt angry onlayer talksprites at left with slideinleft

    VRISKA gt angry "FUCK!!!!!!!!"

    VRISKA gt thinking "I'm really scraping the 8ottom of the 8arrel here..."

    VRISKA "and I'm 8eing sincere a8out at least 80%% of these!"
    hide vriska with slideoutleft


    show tavros nervous onlayer talksprites at right with slideinright

    TAVROS nervous "aS MUCH FUN, aS I THINK YOU MAYBE THINK WE ARE MUTUALLY HAVING"

    TAVROS "aND, i DON'T WANT TO RUIN THAT, bY"

    TAVROS "bEING MY USUAL SELF, lIKE YOU ARE ALWAYS TELLING ME IS BAD,"

    TAVROS nervous "a LOT OF THOSE THINGS, sEEM, uM"

    TAVROS smiling "uNIMPORTANT AND SORT OF, nORMAL,"

    TAVROS nervous "fOR YOU,"
    hide tavros with slideoutright


    show vriska gt thinking onlayer talksprites at left with slideinleft

    VRISKA gt thinking ""

    VRISKA gt smug "You're right."

    VRISKA gt idle "..."

    VRISKA gt idle "..."
    hide vriska with slideoutleft


    box "What will you do?"


    show vriska gt onlayer talksprites at left with slideinleft

    VRISKA "Damn it. Well even if that doesn't solve this puzzle, 8y some happenstantial miracle it's still true."
    hide vriska with slideoutleft


    show tavros onlayer talksprites at right with slideinright

    TAVROS "i THINK IT'S, sOMETIMES ALRIGHT"

    TAVROS "tO JUST STAND, tOGETHER,"

    TAVROS "oUTSIDE OF MY HOUSE, fOR A FEW HOURS, aND,"

    TAVROS nervous "i AM NOT AT ALL"

    TAVROS "fRIGHTENED, tHAT YOU WILL DO SOMETHING,"

    TAVROS smiling "hORRIBLE TO ME,"
    hide tavros with slideoutright


    show vriska gt onlayer talksprites at left with slideinleft

    VRISKA "Incredi8le! Listen to you!"

    VRISKA "You have me here practically groveling at your feet."

    VRISKA "And even after all I put you through, you're still not trying to get your just desserts."

    VRISKA gt sad "All this apologizing and rolling over and exposing my weaknesses isn't solving shit!"

    VRISKA gt smug "It's like I'm always saying, words are meaningless."

    VRISKA "What we need is action."
    hide vriska with slideoutleft


    show tavros nervous onlayer talksprites at right with slideinright

    TAVROS nervous "i THINK MAYBE, tHAT,"

    TAVROS "dOING uHH, \"ACTIONS,\""

    TAVROS "mIGHT BE ONE OF THE THINGS, tHAT YOU FEEL, lIKE YOU DID WRONG"

    TAVROS "aND, mAYBE SOME WORDS, aCTUALLY,"

    TAVROS smiling "cAN BE PRETTY USEFUL, sOMETIMES,"
    hide tavros with slideoutright


    show vriska gt onlayer talksprites at left with slideinleft

    VRISKA "That sounds wrong, so I'm going to completely ignore it."
    hide vriska with slideoutleft


    show tavros onlayer talksprites at right with slideinright

    TAVROS "oH, oK,"
    hide tavros with slideoutright


    show vriska gt onlayer talksprites at left with slideinleft

    VRISKA "8ut sure. Let's try it your way."
    hide vriska with slideoutleft


    show tavros smiling eyesclosed onlayer talksprites at right with slideinright

    TAVROS smiling eyesclosed "oH, oK,"
    hide tavros with slideoutright


    show vriska gt onlayer talksprites at left with slideinleft

    VRISKA "Instead of me taking action, what I need is for you to take action."

    VRISKA gt smug "It was so o8vious that it's stupid, actually."
    hide vriska with slideoutleft


    show tavros onlayer talksprites at right with slideinright

    TAVROS "tHAT'S NOT, wHAT I SAID, aT ALL,"
    hide tavros with slideoutright


    show vriska gt onlayer talksprites at left with slideinleft

    VRISKA "The reason I'm stuck here is 8ecause I don't owe you plac8ing apologies"

    VRISKA "I owe you revenge. It's just that easy!"
    hide vriska with slideoutleft


    show tavros onlayer talksprites at right with slideinright

    TAVROS "bUT-"
    hide tavros with slideoutright


    show vriska gt smug onlayer talksprites at left with slideinleft

    VRISKA gt smug "It's just that easy!"
    hide vriska with slideoutleft


    show tavros idle onlayer talksprites at right with slideinright

    TAVROS idle "..."
    hide tavros with slideoutright


    show vriska gt angry onlayer talksprites at left with slideinleft

    VRISKA gt angry "IT'S J-"
    hide vriska with slideoutleft


    show tavros onlayer talksprites at right with slideinright

    TAVROS "bUT WHAT IF, sOMEONE WERE TO SAY, hYPOTHETICALLY SPEAKING,"

    TAVROS "i DON'T THINK THATS THE THING I WANT TO, uMM, bE DOING"

    TAVROS nervous "aT ALL, oR, eVEN SORT OF,,"

    TAVROS "aND THAT I STILL THINK IT WAS WRONG BUT I FORGIVE YOU FOR DOING THOSE THINGS THAT YOU SAID YOU DID, tO ME EARLIER,"
    hide tavros with slideoutright


    show vriska gt onlayer talksprites at left with slideinleft

    VRISKA "No. You deserve revenge. Action 8egets action. This makes perfect sense to anyone who's 8een paying attention."

    VRISKA gt thinking ""

    VRISKA gt neutral "You have to throw me off this cliff."

    VRISKA "Then we'll 8e completely squared away."
    hide vriska with slideoutleft


    show tavros nervous onlayer talksprites at right with slideinright

    TAVROS nervous "uHH I DON'T THINK-"
    hide tavros with slideoutright


    show vriska gt smug onlayer talksprites at left with slideinleft

    VRISKA gt smug "I'm praaaaaaaactically an expert on this revenge thing. Trust me."
    hide vriska with slideoutleft


    show tavros onlayer talksprites at right with slideinright

    TAVROS "vRISKA I DON'T WANT TO DO A REVENGE ON YOU"

    TAVROS "fOR CRIMES, yOU HAVEN'T REALLY DONE, aND MAYBE SOME YOU DID,"

    TAVROS "aND THIS MAY, uHH, sEEM COUNTERPRODUCTIVE, tO YOUR IDEA"

    TAVROS nervous "bUT IT SOUNDS LIKE, bEING THROWN OFF A CLIFF MIGHT NOT BE A HEALTHY COPING MECHANISM,"
    hide tavros with slideoutright


    show vriska gt onlayer talksprites at left with slideinleft

    VRISKA "It's fine! Kill me, get your revenge, and I'll finally 8e on my way."

    VRISKA gt smug "Out of your life forever! Never to torment you again!"

    VRISKA "And whatever version of you this is can go on living your little life playing with your little monster dolls or whatever!"

    VRISKA gt sad "Here on Alternia."

    VRISKA gt sad "8efore everything goes wrong."

    VRISKA "You can kill me now 8efore it's too late for you."

    VRISKA gt sad "8efore I screw your life up."

    VRISKA gt smug "It's perfect!"
    hide vriska with slideoutleft


    show tavros onlayer talksprites at right with slideinright

    TAVROS nervous "nO I DON'T WANT TO DO THAT,"
    hide tavros with slideoutright


    show vriska gt onlayer talksprites at left with slideinleft

    VRISKA "I know you have it in you. I've seen it."

    VRISKA gt angry "God damn it Tavros, if you don't kill me I can't move on."

    VRISKA gt neutral "You'd 8e doing me a favor."

    VRISKA "Go on."
    hide vriska with slideoutleft


    show tavros nervous onlayer talksprites at right with slideinright

    TAVROS nervous "uHH,"
    hide tavros with slideoutright


    show vriska gt onlayer talksprites at left with slideinleft

    VRISKA "Kill me."
    hide vriska with slideoutleft


    show tavros nervous onlayer talksprites at right with slideinright

    TAVROS nervous "nO,"
    hide tavros with slideoutright


    show vriska gt angry onlayer talksprites at left with slideinleft

    VRISKA gt angry "Hey get 8ack here!"
    hide vriska with slideoutleft


    show tavros nervous onlayer talksprites at right with slideinright

    TAVROS nervous "nO!"
    show tavros nervous idle:
        linear .1 xzoom -1.0
    pause .25
    hide tavros with slideoutright


    show vriska gt angry onlayer talksprites at left with slideinleft

    VRISKA gt angry "Stop running!"
    hide vriska with slideoutleft



    TAVROS "nO, i LOVE TO RUN AND, i DO NOT PLAN ON STOPPING, aNY TIME SOON," (window_xoffset=0)


    show vriska gt angry onlayer talksprites at left with slideinleft

    VRISKA gt angry "You kill me right this instant!"

    VRISKA "Damn it, I forgot how fast he used to 8e."
    hide vriska with slideoutleft



    TAVROS "nO!" (window_xoffset=0)


    show vriska gt smug onlayer talksprites at left with slideinleft

    VRISKA gt smug "Man, doing the right thing sure is hard work."

    VRISKA "I didn't want to do this, Tavros, 8ut you're forcing my hand here. I won't make the same mistake again."
    hide vriska with slideoutleft

    $ command = "{{Thief: Do the right thing.}"
    menu:
        "{plain}[pick] {/plain}[command]":
            show c1p1 with Dissolve(1.0)

    $ command = "{{It's really for the 8est.}"
    menu:
        "{plain}[pick] {/plain}[command]":

            show c1p2 with Dissolve(1.0)
            show c1p3 with Dissolve(1.0)


    VRISKA "Good luck." (what_xalign=0.5, what_yalign=0.5, what_textalign=0.5, window_xoffset=0)

    $ command = "{{Adios, Toreador.}"
    menu:
        "{plain}[pick] {/plain}[command]":
            scene c1p4 with Dissolve(1.0)
            pause 0.5

    stop music fadeout 2.0

    $ command = "{{==>}"
    menu:
        "{plain}[pick] {/plain}[command]":
            play sound "chapters/1/audio/stabbed.mp3" volume 0.5
            hide c1p4
            show c1p5 at shake
            pause 0.5

    $ command = "{{==>}"
    menu:
        "{plain}[pick] {/plain}[command]":
            scene black with Dissolve(1.0)
            play sound "chapters/1/audio/you_died.mp3"
            show c1p6 with Dissolve(3.0)
            pause 0.5


    TAVROS "uHH, oH SHUCKS, bYE VRISKA," (what_xalign=0.5, what_yalign=0.5, what_textalign=0.5, window_xoffset=0)

    $ command = "{{==>}"
    menu:
        "{plain}[pick] {/plain}[command]":
            show white with Dissolve(3.0)
            scene bg mspa
            show c1end
            show white
            hide white with Dissolve(3.0)
            pause 0.5

    "You are now Vriska, and like any good Main Character, you find yourself on the precipice of an all too familiar Beach.\n\nWhat will you do?"

    $ multipersist.chapter1_complete = True
    $ multipersist.save()
    jump chapter1_end

label chapter1_end:

    show white with Dissolve(3.0)

    "YEAR 2" (window_yalign=0.5, window_yoffset=0, window_xsize=150, window_ysize=75, window_ypos=0.5)

    scene bg vriskaroom with Dissolve(3.0)

    play music "chapters/1/audio/c1end.mp3" volume 0.5 loop

    show davepeta roleplay onlayer talksprites at right with slideinright

    DAVEPETASPRITE "*dp pads through the underbrush of the forest, leaving paw prints after themselves in the freshly fallen snow*"
    DAVEPETASPRITE "*their ears twitch cutely with every step they take beclaws as perfect a creature as they are cats are still too fucking stupid to invent proper p33ts protectors*"
    DAVEPETASPRITE "*they will probably need to get these silly little beans amputated after walking through all this white shit but whatever its fine, at the end of this tail is an important furiend*" (what_size=16)
    hide davepeta with slideoutright


    show vriska idle onlayer talksprites at left with slideinleft

    VRISKA "..."
    hide vriska with slideoutleft


    show davepeta roleplay onlayer talksprites at right with slideinright

    DAVEPETASPRITE "every year farmers and freaks alike crowd around this curious critter wringing their sweaty boring human hands all nervously hoping for winters end"
    DAVEPETASPRITE "but this overhyped moles shadow offurs a symbolic appouncement for the spider instead"
    hide davepeta with slideoutright


    show vriska idle onlayer talksprites at left with slideinleft

    VRISKA "........"
    hide vriska with slideoutleft


    show davepeta roleplay onlayer talksprites at right with slideinright

    DAVEPETASPRITE "the breaking of cycles, dissolution of the self, whatever other philosophical rhetoric bill murray said in that one meowvie"
    DAVEPETASPRITE "its all up to you, spider, to grab this guy by the furry haunches bend him over and nonsexually spank him into submewssion"

    DAVEPETASPRITE neutral "what will you do vriska?"
    hide davepeta with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft

    VRISKA "*The spider doesn't do anything, 8ecause spiders don't have 8rains to make good choices. Instead, we're doomed to crawl around on our 8ellies like idiots, w8ing to 8e crushed under the giant furry ass of an animal so pathetic humans had to make up reasons to care a8out it, and with her luck she'll spend eternity 8uried alive under poop pellets du88ed the pharaoh of trash assholes and praying to die.*" (what_size=13)
    hide vriska with slideoutleft


    show davepeta thinking onlayer talksprites at right with slideinright

    DAVEPETASPRITE "vriskers not to ask an obvious question but"
    DAVEPETASPRITE "are you good?"

    DAVEPETASPRITE uncomfortable "you s33m... depressed"
    hide davepeta with slideoutright


    show vriska onlayer talksprites at left with slideinleft

    VRISKA "What are you talking a8out?"
    VRISKA "Isn't it o8vious how excited I am?"
    VRISKA "8anging my head against a wall for several hours is practically my daily medit8tion now."

    VRISKA angry "\"Purrhaps\" today will 8e the day I finally give myself a deep enough pan lesion that my neurons will reset and I can finally understand what I'm supposed to 8e doing here."
    VRISKA "Finally moving on FROM THIS 8ORING M8ND NUM8ING SHIIIIIIITTY PUNISHM8NT PIT."
    hide vriska with slideoutleft


    show davepeta pokerface onlayer talksprites at right with slideinright

    DAVEPETASPRITE "wrow"
    hide davepeta with slideoutright


    show vriska sad onlayer talksprites at left with slideinleft

    VRISKA "Sigh."
    VRISKA "Can you please tell me what to do? And not in some coy, rounda8out way like you have 8een."

    VRISKA neutral "You're supposed to 8e guiding me, 8ut instead sweeps of my life are 8eing w8sted here when I could 8e doing so much more out there."
    hide vriska with slideoutleft


    show davepeta embarrassed onlayer talksprites at right with slideinright

    DAVEPETASPRITE "trust me im trying!!"
    DAVEPETASPRITE "my advice is just... a litter bit limited"

    DAVEPETASPRITE thinking "ask me about mechanics or some dank catnip or even how to stunt down the stairs without breaking every bone in your body and i can chitter your ear off for another couple years" (what_size=16)
    DAVEPETASPRITE "but countless cool dudes and kitty girls cant inform much on how to handle those classic serket problems"

    DAVEPETASPRITE pokerface "feel me?"
    hide davepeta with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft

    VRISKA "Soooooooo what you are saying is you can't help 8ecause you are the Ultimate Winged Weener and can't relate to 8eing a huge 8itch like me?"
    hide vriska with slideoutleft


    show davepeta onlayer talksprites at right with slideinright

    DAVEPETASPRITE "ha he"

    DAVEPETASPRITE pokerface "w33ner"

    DAVEPETASPRITE cute "but yeah thats pretty much how it is"

    DAVEPETASPRITE neutral "you know what they say theres purrppets and then theres pawppet33rs"
    DAVEPETASPRITE "and both mew selves rather be on the yarn strings"
    DAVEPETASPRITE "so alot of my thoughts on how to come back from all your bullshit begins and ends at \"i simply would not have done that in the first place\""

    DAVEPETASPRITE pokerface "no judgment of course"

    DAVEPETASPRITE thinking "see if you had watched the damn groundhog movie youd have all the relatable advice youd n33d"
    hide davepeta with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft

    VRISKA "I will never ever watch that stupid groundhog movie!"
    VRISKA "This is such 8ullshit. Like you're some softy, hurt-no8ody housecat! You literally defe8ed Lord English and kill wild animals with your 8are h8nds!!!!!!!!"
    hide vriska with slideoutleft


    show davepeta pokerface onlayer talksprites at right with slideinright

    DAVEPETASPRITE "ok hunting is way different"
    DAVEPETASPRITE "blood and guts and broken wrists and fractured tailbones"
    DAVEPETASPRITE "thats nature and instinct it doesnt have to be mean"
    DAVEPETASPRITE roleplay "*the fearsome gender neutral lionesster pins down its prey but instead of getting down to business growls out how the prey deserves this for being a big disappointing pussy*" (what_size=16)

    DAVEPETASPRITE uncomfortable "s33 very weird"

    DAVEPETASPRITE cute "i might have to eat a guy but that doesnt mean i cant respect them"
    hide davepeta with slideoutright


    show vriska sad onlayer talksprites at left with slideinleft

    VRISKA "8ut what if the natural order is exactly what's working against me here?"

    VRISKA angry "Wh8t am I supposed to do then????????"
    hide vriska with slideoutleft


    show davepeta thinking onlayer talksprites at right with slideinright

    DAVEPETASPRITE "sure hope thats not true..."

    DAVEPETASPRITE cute "or well be here furrever!"
    hide davepeta with slideoutright

    stop music fadeout 3.0

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
