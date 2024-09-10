init python:
    build.archive("chapter2", "all")
    build.classify('game/chapters/2/**', 'chapter2')

    renpy.music.register_channel("sfx", mixer="sfx")

image bg lomat:
    size (950,650) yalign 0.5 xalign 0.5
    "chapters/2/images/lomat.png"

image bg questcocoon:
    size (950,650) yalign 0.5 xalign 0.5
    "chapters/2/images/questcocoon.png"

image c2p1:
    xalign 0.0 yalign 0.0
    "chapters/2/images/panel1.png"

image c2p2:
    xalign 0.0 yalign 0.0
    "chapters/2/images/panel2.png"

image c2p3:
    xalign 0.0 yalign 0.0
    "chapters/2/images/panel3.png"

image bg level_complete_2:
    size (950,650) yalign 0.5 xalign 0.5
    "chapters/2/images/level_complete_1.png"
    pause 0.05
    "chapters/2/images/level_complete_2.png"
    pause 0.05
    "chapters/2/images/level_complete_3.png"
    pause 0.05
    repeat

label chapter2:


    $ command = "{{Select \"FLARP BOOK\"}"

    play music "chapters/1/audio/c1.mp3" fadein 1.0 volume 0.5 loop
    scene bg tavroscliff with Dissolve(2.0)


    show vriska sad onlayer talksprites at left with slideinleft
    VRISKA "........"
    hide vriska with slideoutleft


    show tavros smiling onlayer talksprites at right with slideinright
    TAVROS "oH,"
    TAVROS "hI VRISKA,"
    hide tavros with slideoutright


    show vriska sad onlayer talksprites at left with slideinleft
    VRISKA "Sigh."
    VRISKA "Hi Tavros."
    hide vriska with slideoutleft


    show tavros neutral onlayer talksprites at right with slideinright
    TAVROS ",,,,,"
    hide tavros with slideoutright


    show vriska sad onlayer talksprites at left with slideinleft
    VRISKA "........"
    hide vriska with slideoutleft


    show tavros nervous onlayer talksprites at right with slideinright
    TAVROS "sHOULD I, bE WORRIED ABOUT THE FACT THAT YOU, aRE NOT TALKING,"
    TAVROS "wHEN THAT IS, uHH, yOUR FAVORITE THING TO DO, uSUALLY,"
    hide tavros with slideoutright


    show vriska sad onlayer talksprites at left with slideinleft
    VRISKA "May8e."
    VRISKA "Who cares."
    hide vriska with slideoutleft


    show tavros nervous onlayer talksprites at right with slideinright
    TAVROS "oKAY, tHEN,"
    TAVROS "sHOULD I MAYBE DO, oR SAY SOMETHING,"
    hide tavros with slideoutright


    show vriska sad onlayer talksprites at left with slideinleft
    VRISKA "It doesn't matter. We can do whatever you want."
    hide vriska with slideoutleft


    show tavros nervous onlayer talksprites at right with slideinright
    TAVROS "iS THIS, a TRICK,,, i CAN NEVER TELL,"
    hide tavros with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "No, Tavros, I've already tried tricking you. It doesn't work."

    VRISKA angry "I've apologized, I've killed you, you've killed me, you've paralyzed me, disfigured me, we traveled the world together."
    VRISKA "We 8uilt you an army, had several revolutions, you got to do your little dance a thousand times over."
    hide vriska with slideoutleft


    show tavros neutral onlayer talksprites at right with slideinright
    TAVROS "wOAH,"

    TAVROS smirk "bADASS,"
    hide tavros with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "Not that you remem8er any of it, asshole."
    VRISKA "And even worse, none of it was what I was supposed to do, apparently!"
    VRISKA "Now I'm too tired to try and fix this anymore."
    VRISKA "I think it's time we face the music."

    VRISKA sad "You 8roke me, Pupa."
    hide vriska with slideoutleft


    show tavros neutral onlayer talksprites at right with slideinright
    TAVROS "oH,"
    TAVROS "mY BAD,"
    TAVROS "aND ALSO MY BAD, fOR NOT REMEMBERING THINGS, tHAT DIDN'T ACTUALLY HAPPEN,"
    TAVROS ",,,"
    TAVROS "sO, dO YOU REALLY MEAN IT,"
    hide tavros with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "Mean what?"
    hide vriska with slideoutleft


    show tavros neutral onlayer talksprites at right with slideinright
    TAVROS "pARTICIPATING IN AN ACTIVITY, oF,,, mY OWN CHOOSING,"
    hide tavros with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "Sure, why the hell not? What do you want to do?"
    hide vriska with slideoutleft


    show tavros nervous onlayer talksprites at right with slideinright
    TAVROS "wELL, iF YOU ARE, BEING HONEST, AND NOT LYING,"
    TAVROS "tHEN, i,"
    TAVROS "wANT,,,,"
    hide tavros with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "........"
    hide vriska with slideoutleft


    show tavros smiling onlayer talksprites at right with slideinright
    TAVROS "tO PLAY A GAME, }:),"
    hide tavros with slideoutright


    show vriska smiling onlayer talksprites at left with slideinleft
    VRISKA jaw drop "THAT'S what you want to do? Actually?"
    hide vriska with slideoutleft


    show tavros smiling onlayer talksprites at right with slideinright
    TAVROS "iT'S WHAT I ALWAYS WANT TO DO,"
    TAVROS "i CAN GO, sET EVERYTHING UP,"

    TAVROS neutral "uNLESS YOU WERE DOING THAT THING, wHERE YOU TELL ME A THING, tHAT IS UNTRUE,"
    TAVROS "AGAIN,"
    hide tavros with slideoutright


    box "What will you do?"


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "Fiiiiiiiine."

    VRISKA neutral "I'm already here, might as well knock another option off the list I GUESS."
    hide vriska with slideoutleft



    $ command = "{{Play game.}"
    menu:
        "{plain}[pick] {/plain}[command]":
            show black with Dissolve(2.0)
            hide black with Dissolve(2.0)

    show tavros pupa smiling onlayer talksprites at right with slideinright
    TAVROS "yAY!"
    hide tavros with slideoutright


    show vriska scared onlayer talksprites at left with slideinleft
    VRISKA "I won........"
    hide vriska with slideoutleft


    show tavros pupa neutral onlayer talksprites at right with slideinright
    TAVROS "tHAT,"

    TAVROS pupa smiling "wAS AWESOME!"
    TAVROS "mY CHARACTER EARNED SO MUCH XP,"
    TAVROS "hEHEHE,"
    hide tavros with slideoutright


    show vriska scared onlayer talksprites at left with slideinleft
    VRISKA "8ut I won. Why hasn't this place spit me out yet?"
    hide vriska with slideoutleft


    show tavros pupa smiling onlayer talksprites at right with slideinright
    TAVROS "wHILE YOU WAIT, fOR WHATEVER YOU SEEM TO THINK WILL HAPPEN,"
    TAVROS "lETS PLAY ANOTHER SESSION,"
    hide tavros with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "No offense, dude, 8ut that was incredi8ly easy for me. Do you reeeeeeeeally think you stand a chance at winning the next game?"
    hide vriska with slideoutleft


    show tavros pupa neutral onlayer talksprites at right with slideinright
    TAVROS "uGH, mAYBE NOT,"
    TAVROS "bUT, i DON'T CARE THAT MUCH ABOUT lOSING,"

    TAVROS pupa smiling "i JUST WANT TO PLAY,"
    TAVROS "iN THAT WAY, iTS LIKE, wE ARE BOTH WINNERS,"
    hide tavros with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "No we are not. I won."
    VRISKA "You didn't, and you have to accept that."
    hide vriska with slideoutleft


    show tavros pupa smiling onlayer talksprites at right with slideinright
    TAVROS "oKAY, bUT, i DON'T,"

    TAVROS pupa neutral "oR, i GUESS I DO, bUT, nOT IN THE WAY YOU WANT ME TO,"
    hide tavros with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "In that c8se, let's play another session! Let's just keep playing sessions over and over again and never stop!!!!!!!!!"
    VRISKA "And for the rest of forever, you will lose every single one of them."
    VRISKA "How does that m8ke you feel, you still “ok8y” with that?"
    hide vriska with slideoutleft


    show tavros pupa smiling onlayer talksprites at right with slideinright
    TAVROS "wELL, tHOUGH IT WOULD BE EXCITING TO WIN,"
    TAVROS "iF WE PLAY, aND I COULD LOSE IN A NEW, dIFFERENT WAY,"
    TAVROS "tHAT IS ALSO PRETTY EXCITING, sTILL,"
    TAVROS pupa smiling eyesclosed "lIKE AN ADVENTURE, };),"
    hide tavros with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "Damn."
    VRISKA "That is quite possi8ly the gayest thing I have ever heard someone say, Nitram."
    hide vriska with slideoutleft


    show tavros pupa nervous onlayer talksprites at right with slideinright
    TAVROS "wHAT DOES THAT, uHH, eVEN MEAN,"
    hide tavros with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "I don't know! It's a human word Dave would repeat all the time 8efore I started using it against him."

    VRISKA smiling "They tried expl8ning the context a few times, but honestly none of it made any sense. It was just only a 8unch of made up crap from a dead alien culture."
    hide vriska with slideoutleft


    show tavros pupa neutral onlayer talksprites at right with slideinright
    TAVROS "dAVE, wHAT?"
    hide tavros with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "Who cares, essentially it's just what you call people after they say something incredi8ly inane and need to shut up."
    hide vriska with slideoutleft


    show tavros pupa neutral onlayer talksprites at right with slideinright
    TAVROS "oKAY,"

    TAVROS pupa smiling "wELL THEN, vRISKA, i THINK YOU, aRE gAY TOO,"
    hide tavros with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "Tavros, you can't just call me gay when I haven't said anything stupid, that's not how this works!"
    hide vriska with slideoutleft


    show tavros pupa smirk onlayer talksprites at right with slideinright
    TAVROS "yOU AND I, aRE BOTH STUPID GAY,"
    TAVROS "nOW BASED OFF THE RULES OF GAY, wE HAVE TO SHUT UP AND GAME,"
    hide tavros with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "I'm not gay, stop saying I'm gaaaaaaaay!!!!!!!!"
    VRISKA "I swear you're more 8ullheaded than Karkat sometimes."
    VRISKA "At least he concedes to 8eing pissed off and giving a shit."

    VRISKA smug "Come on, you can 8e honest with me for once. It 8others you right, always 8eing too weak to fight, always getting dealt a 8ad h8nd?"
    hide vriska with slideoutleft


    show tavros pupa neutral onlayer talksprites at right with slideinright
    TAVROS "mAYBE?"
    TAVROS "bUT ALSO, iF SOMEONE DIDN'T LOSE, fOLLOWING ALL THESE RULES WOULDN'T BE VERY AMUSING,"

    TAVROS pupa smiling "sO REALLY, lOSING IS ACTUALLY A FINE AND NORMAL THING TO HAPPEN,"
    hide tavros with slideoutright


    show vriska jaw drop onlayer talksprites at left with slideinleft
    VRISKA "What is your fucking pro8lem m8n!"
    hide vriska with slideoutleft


    show tavros pupa nervous onlayer talksprites at right with slideinright
    TAVROS "lITERALLY, nOTHING?"
    TAVROS "yOU ARE REALLY, uHH, cONCERNING YOURSELF HERE, wITH ME LOSING,"
    hide tavros with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "8ecause it's frustrating! You act completely unaware of the fact that the world is working against you!"
    hide vriska with slideoutleft


    show tavros pupa neutral onlayer talksprites at right with slideinright
    TAVROS "i, dON'T BELIEVE THAT'S NECESSARILY TRUE,"
    hide tavros with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "You couldn't even fit in your own recuperacoon 8ecause of your horns, what kind of sick joke is THAT?"
    hide vriska with slideoutleft


    show tavros pupa neutral onlayer talksprites at right with slideinright
    TAVROS "yES, tHAT IS UNFORTUNATE,"
    TAVROS "bUT, nOT A BIG DEAL,"
    hide tavros with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "Ok sure, that was a weak example and at this point of your life nothing 8ad had happened yet, 8ut it was coming!"

    VRISKA angry "You could dream of cavalreapers all you wanted, 8ut whether it was on or off planet, you weren't going to sk8 8y forever."

    VRISKA sad "You were doomed, Tavros, and you didn't even care."
    hide vriska with slideoutleft


    show tavros pupa neutral onlayer talksprites at right with slideinright
    TAVROS "bUT,"
    TAVROS "i WASN'T,"
    TAVROS "aLTERNIA WAS,"
    TAVROS "aND, tHE ONLY PERSON THAT EVER KILLED ME,"
    TAVROS "wAS YOU, vRISKA,"
    hide tavros with slideoutright


    show vriska smug onlayer talksprites at left with slideinleft
    VRISKA "Ah HA, so y8u DO remem8er everyth8ng, you 8ig li8r!"
    hide vriska with slideoutleft


    show tavros pupa neutral onlayer talksprites at right with slideinright
    TAVROS "hMM,"

    TAVROS pupa smiling "nO,"
    hide tavros with slideoutright


    show bg at hpunch
    show vriska jaw drop onlayer talksprites at left with slideinleft
    VRISKA "W-Wh8?"

    VRISKA breaking point "WH8T?????????"
    VRISKA "AAAAAAAAAH!"
    VRISKA "God, it's coming back to me so clearly why ex8ctly I h8ed you so much."
    VRISKA "You're like a moo8east walking up to the 8olt gun, out of its own volition."

    VRISKA smug "Like, what is it? Do you h8 yourself so much trying to survive was a h8ssle for you?"
    hide vriska with slideoutleft


    show tavros pupa smiling onlayer talksprites at right with slideinright
    TAVROS "i DON'T THINK THAT THOUGHT, eVER, cROSSED MY MIND!"
    hide tavros with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "Well it should h8ve!!!!!!!!"
    VRISKA "You know, fine, you weren't good enough to live, 8ut you could've had the decency to 8e afraid."
    hide vriska with slideoutleft


    show tavros pupa nervous onlayer talksprites at right with slideinright
    TAVROS "i GUESS, i CAN'T SAY, tHESE IDEAS DON'T MAKE SENSE,"
    TAVROS "tO SOMEONE THAT'S NOT ME,"

    TAVROS pupa neutral "yET, aPPLIED TO ME, aS MY OWN THOUGHTS,"
    TAVROS "tHEY ARE, cOMPLETELY MAKE BELIEVE,"
    TAVROS "i, dON'T UNDERSTAND WHERE THEY ARE COMING FROM,"
    TAVROS "iT IS, aS IF, yOU ARE CONFUSING ME, wITH THE, uHH, fEELINGS OF SOMEBODY ELSE,"
    TAVROS "oR,"

    TAVROS pupa surprise "!"
    hide tavros with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "Shut up."
    hide vriska with slideoutleft


    show tavros pupa smirk onlayer talksprites at right with slideinright
    TAVROS "aRE YOU, tHE SOMEBODY ELSE, vRISKA,"
    hide tavros with slideoutright


    show vriska sad onlayer talksprites at left with slideinleft
    VRISKA "........"
    hide vriska with slideoutleft


    show tavros pupa smiling onlayer talksprites at right with slideinright
    TAVROS "hUH,"
    TAVROS "wHAT WORD, iF THERE WAS ONE, wOULD BE USED FOR THIS PHENOMENON,"
    hide tavros with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "........"

    VRISKA sad "I think if a certain uppity human was here, she'd call it “projecting.”"
    hide vriska with slideoutleft


    show tavros pupa neutral onlayer talksprites at right with slideinright
    TAVROS "tRUE, yOU DO TREAT ME LIKE A PROJECT,"
    TAVROS "tHERE IS, i THINK, a MUCH BETTER WAY TO PUT IT,"

    TAVROS pupa smirk "iT'S AS IF, i'M YOUR RUFIOH,"
    hide tavros with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "No."
    hide vriska with slideoutleft


    show tavros pupa smiling onlayer talksprites at right with slideinright
    TAVROS "uHHH, yES,"
    TAVROS "bUT INSTEAD OF BEING YOUR BEST PAL WITH HIGH SELF ESTEEM, i, rEMIND YOU OF ALL YOUR FEARS,"
    TAVROS "aND, bAD THOUGHTS,"
    TAVROS "aND, aM VERY REAL,"
    hide tavros with slideoutright


    show vriska smug onlayer talksprites at left with slideinleft
    VRISKA "Nope. A8solutely not."
    hide vriska with slideoutleft


    show tavros pupa smiling onlayer talksprites at right with slideinright
    TAVROS "i THINK, i AM MOST DEFINITELY, hITTING THE NAIL ON THE HEAD, hERE,"
    hide tavros with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "Wrong! Wrong! Wrong! Wrong! Wrong! Wrong! WRONG! WRONG!"
    hide vriska with slideoutleft


    show tavros pupa smiling onlayer talksprites at right with slideinright
    TAVROS "nO NEED TO BE ASHAMED, oF YOUR INSANE DELUSIONS,"
    hide tavros with slideoutright


    show vriska breaking point onlayer talksprites at left with slideinleft
    VRISKA "WROOOOOOOONG!!!!!!!!"
    hide vriska with slideoutleft


    show tavros pupa smirk onlayer talksprites at right with slideinright
    TAVROS "i LOVE NOW KNOWING, tHAT YOU HAVE PROBLEMS,"
    TAVROS "aND, i THINK YOU ARE, aCTUALLY, bEING INCREDIBLY SMART,"

    TAVROS pupa neutral "pERHAPS, rUFIOH WAS TOO FAKE FOR AN IMAGINARY FRIEND, aND, tHAT'S WHY MY SELF ESTEEM NEVER IMPROVED,"

    TAVROS pupa smiling "wHAT I MEAN IS, wE BOTH, cOULD BE PROJECTS, fOR EACH OTHER,"
    hide tavros with slideoutright


    show vriska sad onlayer talksprites at left with slideinleft
    VRISKA "Noooooooo."
    hide vriska with slideoutleft


    show tavros pupa smirk onlayer talksprites at right with slideinright
    TAVROS "yEEEEEEEES,"
    hide tavros with slideoutright


    show vriska sad onlayer talksprites at left with slideinleft
    VRISKA ">::::("
    hide vriska with slideoutleft


    show tavros pupa smiling eyesclosed onlayer talksprites at right with slideinright
    TAVROS pupa smiling eyesclosed "i FEEL, sO VERY INSPIRED RIGHT NOW, i COULD DO A LITTLE DANCE,"
    hide tavros with slideoutright


    show vriska sad onlayer talksprites at left with slideinleft
    VRISKA "Don't."
    hide vriska with slideoutleft


    show tavros pupa smiling onlayer talksprites at right with slideinright
    TAVROS "oK THEN CONSIDER,"
    TAVROS "iN OUR NEXT CAMPAIGN, tHE BOY SKYLARK,,, bECOMES HIS OWN, uH, bLUE FAIRY,"
    hide tavros with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "You're not 8lue Tavros. Don't start pretending to 8e 8lue."
    hide vriska with slideoutleft


    show tavros pupa neutral onlayer talksprites at right with slideinright
    TAVROS "i WON'T,"

    TAVROS pupa smirk "i WILL, iNSTEAD, bE THE MUCH RARER BRONZE FAIRY, wHO COMMANDS BEAST WITH HER RESPLENDENT SONG, bUT, iS ACTUALLY USING HER PSYCHIC POWERS,"
    TAVROS "aND, sHE WILL BE SUPER NICE, aND SOFT, aND AWESOME BECAUSE, eVERYONE LIKES HER,"
    TAVROS pupa smiling eyesclosed "cONTRARY, tO HER EVIL FAIRY FRIEND, wHO EVERYONE HATES, fOR BEING A BIG ASSHOLE,"
    hide tavros with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "........"
    hide vriska with slideoutleft


    show tavros pupa smiling onlayer talksprites at right with slideinright
    TAVROS "sORRY,"
    hide tavros with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "No you're not, you're totally proud of yourself!!!!!!!!"
    hide vriska with slideoutleft


    show tavros pupa neutral onlayer talksprites at right with slideinright
    TAVROS "oKAY, i'M NOT,"

    TAVROS pupa smirk "hEHEHEHEHEHEHEHE,"
    hide tavros with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "Fuck it, what other choice do I have 8ut 8e on 8oard with this whole trainwreck."

    VRISKA smiling "Let's play some games for girls."
    VRISKA "I'll get the character sheets, where did you put them?"
    hide vriska with slideoutleft


    show tavros pupa nervous onlayer talksprites at right with slideinright
    TAVROS "oH, tHAT WAS, uHH, pRETTY EASY,"
    TAVROS "i WAS, mOSTLY JOKING,"
    hide tavros with slideoutright


    show vriska smug onlayer talksprites at left with slideinleft
    VRISKA "Were you? Were you really?"
    hide vriska with slideoutleft


    show tavros pupa nervous onlayer talksprites at right with slideinright
    TAVROS "uHHHHHHHH,"
    TAVROS "i THINK I NEED SOME TIME, tO THINK ON THAT,"
    hide tavros with slideoutright


    show vriska smiling onlayer talksprites at left with slideinleft
    VRISKA "You know what I realized, Tavros? This might 8e the first time I ever seriously sat down and 8othered to listen to you."
    VRISKA "And for the first time it's hitting me. You're kind of nuts."
    hide vriska with slideoutleft


    show tavros pupa smiling onlayer talksprites at right with slideinright
    TAVROS "tHAT'S FUNNY TO HEAR, cOMING FROM YOU, oF ALL PEOPLE,"
    hide tavros with slideoutright


    show vriska smiling onlayer talksprites at left with slideinleft
    VRISKA "You're right, it is funny."
    VRISKA "This whole time I thought I was supposed to 8e pushing you."

    VRISKA neutral "It's soooooooo o8vious now, that was pretty fucking stupid of me. There was nothing I could have done to change your mind, huh?"
    hide vriska with slideoutleft


    show aradiabot shadowed onlayer talksprites at right with slideinright
    ARADIABOT "exactly"
    ARADIABOT "y0ure finally starting t0 get it"
    hide aradiabot with slideoutright



    $ command = "{{==>}"
    menu:
        "{plain}[pick] {/plain}[command]":
            stop music fadeout 1.0
            show black with Dissolve(2.0)
            scene bg lomat with Dissolve(3.0)
            pause 0.5
            play music "chapters/2/audio/ch2.flac" fadein 0.5 volume 0.5 loop
            hide black with Dissolve(2.0)




    show vriska jaw drop onlayer talksprites at shake, left with slideinleft
    VRISKA "!!!!!!!!"
    VRISKA "Where the hell am I?"
    VRISKA "Tavros????????"
    VRISKA "Aradia… 8ot?"

    VRISKA neutral "... LOMAT."
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "im n0t g0ing t0 kill y0u"
    ARADIABOT "in case y0u were w0ndering"
    hide aradiabot with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "Yeah, that was going to 8e my next question."
    VRISKA "Are you... aware of the situation? Does this mean I finally cleared Tavros and you're the next level of helltier?"
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "i w0uldnt say that"
    ARADIABOT "m0re accurately this is the b0ss fight t0 drive the p0int h0me"
    hide aradiabot with slideoutright


    show vriska smug onlayer talksprites at left with slideinleft
    VRISKA "Team Charge as a package deal, how is that allowed?"
    hide vriska with slideoutleft


    show aradiabot neutral onlayer talksprites at right with slideinright
    ARADIABOT "because shut up"
    ARADIABOT "shut up is h0w"
    hide aradiabot with slideoutright


    show vriska smug onlayer talksprites at left with slideinleft
    VRISKA "Ruuuuuuuude. 8ut honestly, I'm so happy to see a new face that I'm not even mad a8out it."
    hide vriska with slideoutleft


    box "What will you do?"

    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "That said... if I was confused 8efore, now I'm really lost."
    VRISKA "Shouldn't we 8e 8ack at your hive, with me on my knees telling you I wished I never killed you or something?"
    VRISKA "Take my eternity with those ghostly dead jerks on the chin, and let you live out your life."
    hide vriska with slideoutleft


    show aradiabot shadowed onlayer talksprites at right with slideinright
    ARADIABOT "after everything that has happened y0u still think the p0int of all this is m0re punishment?"
    hide aradiabot with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "It's not........?"
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "weve d0ne that already it d0esnt w0rk"
    hide aradiabot with slideoutright


    show vriska smug onlayer talksprites at left with slideinleft
    VRISKA "8ut you felt 8etter the first time, right? Remem8er how good this moment was, taking life into your own hands and getting the last fist in this cycle of revenge?"
    VRISKA "You got me soooooooo good, you can't go 8ack and say killing me was meaningless now!"
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "yes i can"
    ARADIABOT "im a r0b0t"
    ARADIABOT "i d0nt feel g00d 0r bad 0r justified"
    ARADIABOT "i just d0 my j0b"
    hide aradiabot with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "Come on!!!!!!!! Even while piloting that hunk of tin, you have to admit it was a little satisfying."
    hide vriska with slideoutleft


    show aradiabot neutral onlayer talksprites at right with slideinright
    ARADIABOT "maybe f0r y0u"
    hide aradiabot with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "Excuse me?"
    hide vriska with slideoutleft


    stop music fadeout 2.0

    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "what i mean is y0u g0t exactly what y0u wanted"
    ARADIABOT "y0u were ex0nerated vriska thats what its always been ab0ut"
    hide aradiabot with slideoutright


    show vriska sad onlayer talksprites at left with slideinleft
    VRISKA "Don't say that! I worked my ass off to m8ke things right!"
    VRISKA "I never once asked to 8e f8rgiven for free, I always paid the price!"
    VRISKA "Would it kill you to notice that? To see how hard I'm trying?"
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "pr0bably"
    ARADIABOT "d0es it even matter"
    ARADIABOT "wh0 can aff0rd t0 care when they kn0w y0ure g0ing t0 hurt them again?"
    hide aradiabot with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "I WON'T!"
    hide vriska with slideoutleft


    show aradiabot shadowed onlayer talksprites at right with slideinright
    ARADIABOT "y0u will"
    hide aradiabot with slideoutright


    show vriska breaking point onlayer talksprites at left with slideinleft
    VRISKA "FINE!!!!!!!!"
    VRISKA "8ut what am I supp8sed to do then? Get 8eaten and 8ruised and mutil8ed and h8 myself forever, knowing n8ne of it will ever 8e enough?"
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "sure"
    ARADIABOT "thats h0w y0u like it anyways"
    ARADIABOT "always taking"
    ARADIABOT "never c0mpr0mising"
    hide aradiabot with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "That's h8w you see me????????"

    VRISKA smug "8h8h8h8h8h8h8h8h, you... you 8lue 8looded trash c8n!"

    VRISKA mind control "Who cares what you think then! None of this is real anyw8ys."

    VRISKA mind control "And that means the usual rules don't 8pply right? Who needs to sit around arguing when I can M8KE YOU C8RE!"
    hide vriska with slideoutleft






    show aradiabot shadowed onlayer talksprites at right with slideinright
    ARADIABOT "why are y0u hesitating?"
    hide aradiabot with slideoutright

    box "What will you do?" with Shake((0, 0, 0, 0), 1.0, dist=5)

    show aradiabot shadowed onlayer talksprites at right with slideinright
    ARADIABOT "this is the 0nly way right?"
    hide aradiabot with slideoutright

    bigBox "What will you do?" with Shake((0, 0, 0, 0), 1.3, dist=10)

    show aradiabot shadowed onlayer talksprites at right with slideinright
    ARADIABOT "this is h0w y0u win"
    hide aradiabot with slideoutright

    biggerBox "What will you do?" with Shake((0, 0, 0, 0), 1.5, dist=20)

    show aradiabot shadowed onlayer talksprites at right with slideinright
    ARADIABOT "d0 it"
    hide aradiabot with slideoutright


    biggestBox "WHAT WILL YOU DO?" with Shake((0, 0, 0, 0), 2.0, dist=30)


    play sfx "chapters/2/audio/break.mp3" volume 0.75 noloop
    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "D8MN IT!"
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "g00d j0b"
    hide aradiabot with slideoutright


    play music "chapters/2/audio/ch2.flac" fadein 1.0 volume 0.5 loop
    show vriska breaking point onlayer talksprites at left with slideinleft
    VRISKA "Sh8t 8p!!!!!!!!"
    VRISKA "I thought you said you wer8n't going to punish me anym8re!"
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "im n0t"
    ARADIABOT "that was a test"
    ARADIABOT "and y0u passed"
    hide aradiabot with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "Gr8, glad to hear 8t!"
    VRISKA "Can y8u tell m8 how to get 8ut of here now?"
    VRISKA sad "I me8n........ what do I have t8 do to finally redeem myself."
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "y0ure n0t here t0 be redeemed vriska y0ure here t0 gr0w up"
    hide aradiabot with slideoutright


    show vriska breaking point onlayer talksprites at left with slideinleft
    VRISKA "........ WH8T THE H8LL DOES TH8T MEAN?"
    hide vriska with slideoutleft


    show aradiabot palm face onlayer talksprites at right with slideinright
    ARADIABOT "y0u are very g00d at saying s0rry"
    ARADIABOT "pr0bably because y0ure c0nstantly creating situati0ns y0u have t0 say s0rry f0r"
    ARADIABOT "why is that"
    hide aradiabot with slideoutright


    show vriska smug onlayer talksprites at left with slideinleft
    VRISKA "Uhhhhhhhh, 8ecause I'm a 8ig idiot who sucks?"
    hide vriska with slideoutleft


    show aradiabot neutral onlayer talksprites at right with slideinright
    ARADIABOT "0k"
    hide aradiabot with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "8ut I have to 8e this way!"
    VRISKA "When everyone else starts slacking off and getting compl8cent I'm the 8ossy 8road that shakes everything up and puts them 8ack on track."
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "thats kind 0f sad"
    hide aradiabot with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "No it's not, it's awesome!"
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "d0 y0u even want t0 be that b0ssy br0ad?"
    hide aradiabot with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "Of course I do!!!!!!!!"
    VRISKA "If I wasn't, what good would I 8e to anyone? What would even 8e the point of keeping me around? Of 8eing alive????????"
    hide vriska with slideoutleft


    show aradiabot palm face onlayer talksprites at right with slideinright
    ARADIABOT "see what i mean that is a very sad thing t0 say"
    ARADIABOT speak "i d0nt think its true either"
    ARADIABOT "i think that even at y0ur m0st useless self there is a place in the w0rld f0r y0u"
    ARADIABOT "and pe0ple in it that want t0 share a life with y0u if y0ud let them"
    hide aradiabot with slideoutright


    show vriska jaw drop onlayer talksprites at left with slideinleft
    VRISKA "Y-you can't mean that?"
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "i d0"
    hide aradiabot with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "Aradia ........"
    VRISKA "Am I the pro8lem?"
    hide vriska with slideoutleft


    show aradiabot neutral onlayer talksprites at right with slideinright
    ARADIABOT "0o0"
    ARADIABOT "i am g0ing t0 expl0de again"
    hide aradiabot with slideoutright


    show vriska sad onlayer talksprites at left with slideinleft
    VRISKA "I'm 8eing serious! If I hear you out, take all this crap seriously, do you actually think I could change?"
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "0f c0urse!"
    ARADIABOT "y0u already have"
    hide aradiabot with slideoutright


    show vriska jaw drop onlayer talksprites at left with slideinleft
    VRISKA "I have????????"
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "yes"
    ARADIABOT "alternia and the game and the mete0r and everything else y0uve lived thr0ugh have made y0u incrementally different than y0u were bef0re"
    ARADIABOT "y0u are in c0nstant m0ti0n every m0ment y0ure alive"
    hide aradiabot with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "Oh. I wasn't expecting you to say that, that's actually kind of nice to hear!"
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "thats why stagnati0n and cycles are s0 danger0us"
    ARADIABOT "y0u get c0mf0rtable with their r0utine"
    ARADIABOT "all the while ign0rant t0 the c0rrupti0n c0nsistently layering 0n t0p 0f itself"
    ARADIABOT "sl0wly making y0u w0rse"
    ARADIABOT "and w0rse"
    ARADIABOT shadowed "and w0rse"
    ARADIABOT neutral "until n0thing is left"
    hide aradiabot with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "Jeeze."
    VRISKA "There it is, there is that fucking Megido-patented 8ummer."
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "yeah"
    hide aradiabot with slideoutright


    show vriska sad onlayer talksprites at left with slideinleft
    VRISKA "I don't completely get it, honestly."
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "that aligns with y0ur aspect"
    ARADIABOT "light players define themselves by their direct acti0ns and understanding"
    ARADIABOT "the unique privilege 0f being a time player is 0ur intrinsic kn0wledge 0f h0w it all keeps happening"
    hide aradiabot with slideoutright


    show vriska smug onlayer talksprites at left with slideinleft
    VRISKA "So cooooooool."
    hide vriska with slideoutleft


    show aradiabot palm face onlayer talksprites at right with slideinright
    ARADIABOT ">.>"
    hide aradiabot with slideoutright


    show vriska neutral onlayer talksprites at left with slideinleft
    VRISKA "Fine, may8e you've got a point. MAY8E there is some8ody out there still w8ing for me, even after all my fum8ling."
    VRISKA sad "It's something, I guess."
    VRISKA "Can I ask one more question?"
    hide vriska with slideoutleft


    show aradiabot neutral onlayer talksprites at right with slideinright
    ARADIABOT "0k"
    hide aradiabot with slideoutright


    show vriska sad onlayer talksprites at left with slideinleft
    VRISKA "Not to 8eat a dead ro8ot, 8ut despite everything that happened, could we have ever 8een friends?"
    hide vriska with slideoutleft


    show aradiabot speak onlayer talksprites at right with slideinright
    ARADIABOT "y0u mean if y0u had put in the time and w0rked 0n wh0 y0u are and bec0me ultimately the best versi0n 0f y0urself?"
    ARADIABOT "hmm"
    ARADIABOT "n0"
    hide aradiabot with slideoutright


    show vriska jaw drop onlayer talksprites at left with slideinleft
    VRISKA "!!!!!!!!"
    VRISKA "C-can I 8sk why????????"
    VRISKA "D8 you h8 me that much?"
    hide vriska with slideoutleft


    show aradiabot neutral onlayer talksprites at right with slideinright
    ARADIABOT "i d0nt hate y0u"
    ARADIABOT "but i d0nt want to spend my time 0n y0u either"
    hide aradiabot with slideoutright


    show vriska breaking point onlayer talksprites at left with slideinleft
    VRISKA "8ut!!!!!!!!"
    hide vriska with slideoutleft


    show aradiabot shadowed onlayer talksprites at right with slideinright
    ARADIABOT shadowed "V.V"
    hide aradiabot with slideoutright


    show vriska angry onlayer talksprites at left with slideinleft
    VRISKA "........"
    VRISKA sad "........ ok."
    VRISKA neutral "Ok."
    hide vriska with slideoutleft

    show black with Dissolve(1.0)
    scene c2p1 with Dissolve(3.0)


    $ command = "{{Vriska: Take Aradia's hand.}"
    menu:
        "{plain}[pick] {/plain}[command]":
            show black with Dissolve(2.0)
            scene bg questcocoon with Dissolve(3.0)



    $ command = "{{==>}"
    menu:
        "{plain}[pick] {/plain}[command]":
            show c2p2 with Dissolve(3.0)


    VRISKA_center "I know it doesn't change anything, 8ecause it already happened and also you two aren't even real."
    VRISKA_center "8ut I am actually sorry. For everything."


    TAVROS_center "yOURE RIGHT, iT'S DEFINITELY POINTLESS TO SAY, bUT, iT IS AN APPRECI8TED GESTURE };)"


    $ command = "{{==>}"
    menu:
        "{plain}[pick] {/plain}[command]":
            show c2p3 with Dissolve(3.0)


    VRISKA_center "And, it's not going to 8e the same again."
    VRISKA_center "I'll stick with it this time. I promise."


    ARADIA_center "we kn0w"
    ARADIA_center "y0u have t0"
    ARADIA_center "n0 0ne else is g0ing t0 save y0u n0w"


    VRISKA_center "8ecause it's just me left?"


    ARADIA_center "yes"
    ARADIA_center "its just y0u"
    ARADIA_center "g00d luck vriska"
    ARADIA_center "i h0pe y0u get better s00n"


    $ command = "{{Level Complete!}"
    menu:
        "{plain}[pick] {/plain}[command]":
            show white with Dissolve(2.0)
            play sfx "audio/vris_level.wav" volume 0.75 noloop 
            scene bg level_complete_2 with Dissolve(1.0)
            pause
            show white with Dissolve(1.0)
            $ multipersist.chapter2_complete= True
            $ multipersist.save()
            stop music fadeout 3.0
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
