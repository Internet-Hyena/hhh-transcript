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

# chapter2


<p class="vriska">VRISKA: ........</p>
<p class="tavros">TAVROS: oH,</p>
<p class="tavros">TAVROS: hI VRISKA,</p>
<p class="vriska">VRISKA: Sigh.</p>
<p class="vriska">VRISKA: Hi Tavros.</p>
<p class="tavros">TAVROS: ,,,,,</p>
<p class="vriska">VRISKA: ........</p>
<p class="tavros">TAVROS: sHOULD I, bE WORRIED ABOUT THE FACT THAT YOU, aRE NOT TALKING,</p>
<p class="tavros">TAVROS: wHEN THAT IS, uHH, yOUR FAVORITE THING TO DO, uSUALLY,</p>
<p class="vriska">VRISKA: May8e.</p>
<p class="vriska">VRISKA: Who cares.</p>
<p class="tavros">TAVROS: oKAY, tHEN,</p>
<p class="tavros">TAVROS: sHOULD I MAYBE DO, oR SAY SOMETHING,</p>
<p class="vriska">VRISKA: It doesn't matter. We can do whatever you want.</p>
<p class="tavros">TAVROS: iS THIS, a TRICK,,, i CAN NEVER TELL,</p>
<p class="vriska">VRISKA: No, Tavros, I've already tried tricking you. It doesn't work.</p>

<p class="vriska">VRISKA (angry): I've apologized, I've killed you, you've killed me, you've paralyzed me, disfigured me, we traveled the world together.</p>
<p class="vriska">VRISKA: We 8uilt you an army, had several revolutions, you got to do your little dance a thousand times over.</p>
<p class="tavros">TAVROS: wOAH,</p>

<p class="tavros">TAVROS (smirk): bADASS,</p>
<p class="vriska">VRISKA: Not that you remem8er any of it, asshole.</p>
<p class="vriska">VRISKA: And even worse, none of it was what I was supposed to do, apparently!</p>
<p class="vriska">VRISKA: Now I'm too tired to try and fix this anymore.</p>
<p class="vriska">VRISKA: I think it's time we face the music.</p>

<p class="vriska">VRISKA (sad): You 8roke me, Pupa.</p>
<p class="tavros">TAVROS: oH,</p>
<p class="tavros">TAVROS: mY BAD,</p>
<p class="tavros">TAVROS: aND ALSO MY BAD, fOR NOT REMEMBERING THINGS, tHAT DIDN'T ACTUALLY HAPPEN,</p>
<p class="tavros">TAVROS: ,,,</p>
<p class="tavros">TAVROS: sO, dO YOU REALLY MEAN IT,</p>
<p class="vriska">VRISKA: Mean what?</p>
<p class="tavros">TAVROS: pARTICIPATING IN AN ACTIVITY, oF,,, mY OWN CHOOSING,</p>
<p class="vriska">VRISKA: Sure, why the hell not? What do you want to do?</p>
<p class="tavros">TAVROS: wELL, iF YOU ARE, BEING HONEST, AND NOT LYING,</p>
<p class="tavros">TAVROS: tHEN, i,</p>
<p class="tavros">TAVROS: wANT,,,,</p>
<p class="vriska">VRISKA: ........</p>
<p class="tavros">TAVROS: tO PLAY A GAME, }:),</p>
<p class="vriska">VRISKA (jaw drop): THAT'S what you want to do? Actually?</p>
<p class="tavros">TAVROS: iT'S WHAT I ALWAYS WANT TO DO,</p>
<p class="tavros">TAVROS: i CAN GO, sET EVERYTHING UP,</p>

<p class="tavros">TAVROS (neutral): uNLESS YOU WERE DOING THAT THING, wHERE YOU TELL ME A THING, tHAT IS UNTRUE,</p>
<p class="tavros">TAVROS: AGAIN,</p>
box "What will you do?"


<p class="vriska">VRISKA: Fiiiiiiiine.</p>

<p class="vriska">VRISKA (neutral): I'm already here, might as well knock another option off the list I GUESS.</p>
menu:
"{plain}[pick] {/plain}[command]":
<p class="tavros">TAVROS: yAY!</p>
<p class="vriska">VRISKA: I won........</p>
<p class="tavros">TAVROS: tHAT,</p>

<p class="tavros">TAVROS (pupa smiling): wAS AWESOME!</p>
<p class="tavros">TAVROS: mY CHARACTER EARNED SO MUCH XP,</p>
<p class="tavros">TAVROS: hEHEHE,</p>
<p class="vriska">VRISKA: 8ut I won. Why hasn't this place spit me out yet?</p>
<p class="tavros">TAVROS: wHILE YOU WAIT, fOR WHATEVER YOU SEEM TO THINK WILL HAPPEN,</p>
<p class="tavros">TAVROS: lETS PLAY ANOTHER SESSION,</p>
<p class="vriska">VRISKA: No offense, dude, 8ut that was incredi8ly easy for me. Do you reeeeeeeeally think you stand a chance at winning the next game?</p>
<p class="tavros">TAVROS: uGH, mAYBE NOT,</p>
<p class="tavros">TAVROS: bUT, i DON'T CARE THAT MUCH ABOUT lOSING,</p>

<p class="tavros">TAVROS (pupa smiling): i JUST WANT TO PLAY,</p>
<p class="tavros">TAVROS: iN THAT WAY, iTS LIKE, wE ARE BOTH WINNERS,</p>
<p class="vriska">VRISKA: No we are not. I won.</p>
<p class="vriska">VRISKA: You didn't, and you have to accept that.</p>
<p class="tavros">TAVROS: oKAY, bUT, i DON'T,</p>

<p class="tavros">TAVROS (pupa neutral): oR, i GUESS I DO, bUT, nOT IN THE WAY YOU WANT ME TO,</p>
<p class="vriska">VRISKA: In that c8se, let's play another session! Let's just keep playing sessions over and over again and never stop!!!!!!!!!</p>
<p class="vriska">VRISKA: And for the rest of forever, you will lose every single one of them.</p>
<p class="vriska">VRISKA: How does that m8ke you feel, you still “ok8y” with that?</p>
<p class="tavros">TAVROS: wELL, tHOUGH IT WOULD BE EXCITING TO WIN,</p>
<p class="tavros">TAVROS: iF WE PLAY, aND I COULD LOSE IN A NEW, dIFFERENT WAY,</p>
<p class="tavros">TAVROS: tHAT IS ALSO PRETTY EXCITING, sTILL,</p>
<p class="tavros">TAVROS (pupa smiling eyesclosed): lIKE AN ADVENTURE, };),</p>
<p class="vriska">VRISKA: Damn.</p>
<p class="vriska">VRISKA: That is quite possi8ly the gayest thing I have ever heard someone say, Nitram.</p>
<p class="tavros">TAVROS: wHAT DOES THAT, uHH, eVEN MEAN,</p>
<p class="vriska">VRISKA: I don't know! It's a human word Dave would repeat all the time 8efore I started using it against him.</p>

<p class="vriska">VRISKA (smiling): They tried expl8ning the context a few times, but honestly none of it made any sense. It was just only a 8unch of made up crap from a dead alien culture.</p>
<p class="tavros">TAVROS: dAVE, wHAT?</p>
<p class="vriska">VRISKA: Who cares, essentially it's just what you call people after they say something incredi8ly inane and need to shut up.</p>
<p class="tavros">TAVROS: oKAY,</p>

<p class="tavros">TAVROS (pupa smiling): wELL THEN, vRISKA, i THINK YOU, aRE gAY TOO,</p>
<p class="vriska">VRISKA: Tavros, you can't just call me gay when I haven't said anything stupid, that's not how this works!</p>
<p class="tavros">TAVROS: yOU AND I, aRE BOTH STUPID GAY,</p>
<p class="tavros">TAVROS: nOW BASED OFF THE RULES OF GAY, wE HAVE TO SHUT UP AND GAME,</p>
<p class="vriska">VRISKA: I'm not gay, stop saying I'm gaaaaaaaay!!!!!!!!</p>
<p class="vriska">VRISKA: I swear you're more 8ullheaded than Karkat sometimes.</p>
<p class="vriska">VRISKA: At least he concedes to 8eing pissed off and giving a shit.</p>

<p class="vriska">VRISKA (smug): Come on, you can 8e honest with me for once. It 8others you right, always 8eing too weak to fight, always getting dealt a 8ad h8nd?</p>
<p class="tavros">TAVROS: mAYBE?</p>
<p class="tavros">TAVROS: bUT ALSO, iF SOMEONE DIDN'T LOSE, fOLLOWING ALL THESE RULES WOULDN'T BE VERY AMUSING,</p>

<p class="tavros">TAVROS (pupa smiling): sO REALLY, lOSING IS ACTUALLY A FINE AND NORMAL THING TO HAPPEN,</p>
<p class="vriska">VRISKA: What is your fucking pro8lem m8n!</p>
<p class="tavros">TAVROS: lITERALLY, nOTHING?</p>
<p class="tavros">TAVROS: yOU ARE REALLY, uHH, cONCERNING YOURSELF HERE, wITH ME LOSING,</p>
<p class="vriska">VRISKA: 8ecause it's frustrating! You act completely unaware of the fact that the world is working against you!</p>
<p class="tavros">TAVROS: i, dON'T BELIEVE THAT'S NECESSARILY TRUE,</p>
<p class="vriska">VRISKA: You couldn't even fit in your own recuperacoon 8ecause of your horns, what kind of sick joke is THAT?</p>
<p class="tavros">TAVROS: yES, tHAT IS UNFORTUNATE,</p>
<p class="tavros">TAVROS: bUT, nOT A BIG DEAL,</p>
<p class="vriska">VRISKA: Ok sure, that was a weak example and at this point of your life nothing 8ad had happened yet, 8ut it was coming!</p>

<p class="vriska">VRISKA (angry): You could dream of cavalreapers all you wanted, 8ut whether it was on or off planet, you weren't going to sk8 8y forever.</p>

<p class="vriska">VRISKA (sad): You were doomed, Tavros, and you didn't even care.</p>
<p class="tavros">TAVROS: bUT,</p>
<p class="tavros">TAVROS: i WASN'T,</p>
<p class="tavros">TAVROS: aLTERNIA WAS,</p>
<p class="tavros">TAVROS: aND, tHE ONLY PERSON THAT EVER KILLED ME,</p>
<p class="tavros">TAVROS: wAS YOU, vRISKA,</p>
<p class="vriska">VRISKA: Ah HA, so y8u DO remem8er everyth8ng, you 8ig li8r!</p>
<p class="tavros">TAVROS: hMM,</p>

<p class="tavros">TAVROS (pupa smiling): nO,</p>
<p class="vriska">VRISKA: W-Wh8?</p>

<p class="vriska">VRISKA (breaking point): WH8T?????????</p>
<p class="vriska">VRISKA: AAAAAAAAAH!</p>
<p class="vriska">VRISKA: God, it's coming back to me so clearly why ex8ctly I h8ed you so much.</p>
<p class="vriska">VRISKA: You're like a moo8east walking up to the 8olt gun, out of its own volition.</p>

<p class="vriska">VRISKA (smug): Like, what is it? Do you h8 yourself so much trying to survive was a h8ssle for you?</p>
<p class="tavros">TAVROS: i DON'T THINK THAT THOUGHT, eVER, cROSSED MY MIND!</p>
<p class="vriska">VRISKA: Well it should h8ve!!!!!!!!</p>
<p class="vriska">VRISKA: You know, fine, you weren't good enough to live, 8ut you could've had the decency to 8e afraid.</p>
<p class="tavros">TAVROS: i GUESS, i CAN'T SAY, tHESE IDEAS DON'T MAKE SENSE,</p>
<p class="tavros">TAVROS: tO SOMEONE THAT'S NOT ME,</p>

<p class="tavros">TAVROS (pupa neutral): yET, aPPLIED TO ME, aS MY OWN THOUGHTS,</p>
<p class="tavros">TAVROS: tHEY ARE, cOMPLETELY MAKE BELIEVE,</p>
<p class="tavros">TAVROS: i, dON'T UNDERSTAND WHERE THEY ARE COMING FROM,</p>
<p class="tavros">TAVROS: iT IS, aS IF, yOU ARE CONFUSING ME, wITH THE, uHH, fEELINGS OF SOMEBODY ELSE,</p>
<p class="tavros">TAVROS: oR,</p>

<p class="tavros">TAVROS (pupa surprise): !</p>
<p class="vriska">VRISKA: Shut up.</p>
<p class="tavros">TAVROS: aRE YOU, tHE SOMEBODY ELSE, vRISKA,</p>
<p class="vriska">VRISKA: ........</p>
<p class="tavros">TAVROS: hUH,</p>
<p class="tavros">TAVROS: wHAT WORD, iF THERE WAS ONE, wOULD BE USED FOR THIS PHENOMENON,</p>
<p class="vriska">VRISKA: ........</p>

<p class="vriska">VRISKA (sad): I think if a certain uppity human was here, she'd call it “projecting.”</p>
<p class="tavros">TAVROS: tRUE, yOU DO TREAT ME LIKE A PROJECT,</p>
<p class="tavros">TAVROS: tHERE IS, i THINK, a MUCH BETTER WAY TO PUT IT,</p>

<p class="tavros">TAVROS (pupa smirk): iT'S AS IF, i'M YOUR RUFIOH,</p>
<p class="vriska">VRISKA: No.</p>
<p class="tavros">TAVROS: uHHH, yES,</p>
<p class="tavros">TAVROS: bUT INSTEAD OF BEING YOUR BEST PAL WITH HIGH SELF ESTEEM, i, rEMIND YOU OF ALL YOUR FEARS,</p>
<p class="tavros">TAVROS: aND, bAD THOUGHTS,</p>
<p class="tavros">TAVROS: aND, aM VERY REAL,</p>
<p class="vriska">VRISKA: Nope. A8solutely not.</p>
<p class="tavros">TAVROS: i THINK, i AM MOST DEFINITELY, hITTING THE NAIL ON THE HEAD, hERE,</p>
<p class="vriska">VRISKA: Wrong! Wrong! Wrong! Wrong! Wrong! Wrong! WRONG! WRONG!</p>
<p class="tavros">TAVROS: nO NEED TO BE ASHAMED, oF YOUR INSANE DELUSIONS,</p>
<p class="vriska">VRISKA: WROOOOOOOONG!!!!!!!!</p>
<p class="tavros">TAVROS: i LOVE NOW KNOWING, tHAT YOU HAVE PROBLEMS,</p>
<p class="tavros">TAVROS: aND, i THINK YOU ARE, aCTUALLY, bEING INCREDIBLY SMART,</p>

<p class="tavros">TAVROS (pupa neutral): pERHAPS, rUFIOH WAS TOO FAKE FOR AN IMAGINARY FRIEND, aND, tHAT'S WHY MY SELF ESTEEM NEVER IMPROVED,</p>

<p class="tavros">TAVROS (pupa smiling): wHAT I MEAN IS, wE BOTH, cOULD BE PROJECTS, fOR EACH OTHER,</p>
<p class="vriska">VRISKA: Noooooooo.</p>
<p class="tavros">TAVROS: yEEEEEEEES,</p>
<p class="vriska">VRISKA: >::::(</p>
<p class="tavros">TAVROS (pupa smiling eyesclosed): i FEEL, sO VERY INSPIRED RIGHT NOW, i COULD DO A LITTLE DANCE,</p>
<p class="vriska">VRISKA: Don't.</p>
<p class="tavros">TAVROS: oK THEN CONSIDER,</p>
<p class="tavros">TAVROS: iN OUR NEXT CAMPAIGN, tHE BOY SKYLARK,,, bECOMES HIS OWN, uH, bLUE FAIRY,</p>
<p class="vriska">VRISKA: You're not 8lue Tavros. Don't start pretending to 8e 8lue.</p>
<p class="tavros">TAVROS: i WON'T,</p>

<p class="tavros">TAVROS (pupa smirk): i WILL, iNSTEAD, bE THE MUCH RARER BRONZE FAIRY, wHO COMMANDS BEAST WITH HER RESPLENDENT SONG, bUT, iS ACTUALLY USING HER PSYCHIC POWERS,</p>
<p class="tavros">TAVROS: aND, sHE WILL BE SUPER NICE, aND SOFT, aND AWESOME BECAUSE, eVERYONE LIKES HER,</p>
<p class="tavros">TAVROS (pupa smiling eyesclosed): cONTRARY, tO HER EVIL FAIRY FRIEND, wHO EVERYONE HATES, fOR BEING A BIG ASSHOLE,</p>
<p class="vriska">VRISKA: ........</p>
<p class="tavros">TAVROS: sORRY,</p>
<p class="vriska">VRISKA: No you're not, you're totally proud of yourself!!!!!!!!</p>
<p class="tavros">TAVROS: oKAY, i'M NOT,</p>

<p class="tavros">TAVROS (pupa smirk): hEHEHEHEHEHEHEHE,</p>
<p class="vriska">VRISKA: Fuck it, what other choice do I have 8ut 8e on 8oard with this whole trainwreck.</p>

<p class="vriska">VRISKA (smiling): Let's play some games for girls.</p>
<p class="vriska">VRISKA: I'll get the character sheets, where did you put them?</p>
<p class="tavros">TAVROS: oH, tHAT WAS, uHH, pRETTY EASY,</p>
<p class="tavros">TAVROS: i WAS, mOSTLY JOKING,</p>
<p class="vriska">VRISKA: Were you? Were you really?</p>
<p class="tavros">TAVROS: uHHHHHHHH,</p>
<p class="tavros">TAVROS: i THINK I NEED SOME TIME, tO THINK ON THAT,</p>
<p class="vriska">VRISKA: You know what I realized, Tavros? This might 8e the first time I ever seriously sat down and 8othered to listen to you.</p>
<p class="vriska">VRISKA: And for the first time it's hitting me. You're kind of nuts.</p>
<p class="tavros">TAVROS: tHAT'S FUNNY TO HEAR, cOMING FROM YOU, oF ALL PEOPLE,</p>
<p class="vriska">VRISKA: You're right, it is funny.</p>
<p class="vriska">VRISKA: This whole time I thought I was supposed to 8e pushing you.</p>

<p class="vriska">VRISKA (neutral): It's soooooooo o8vious now, that was pretty fucking stupid of me. There was nothing I could have done to change your mind, huh?</p>
<p class="aradiabot">ARADIABOT: exactly</p>
<p class="aradiabot">ARADIABOT: y0ure finally starting t0 get it</p>
menu:
"{plain}[pick] {/plain}[command]":
pause 0.5
<p class="vriska">VRISKA: !!!!!!!!</p>
<p class="vriska">VRISKA: Where the hell am I?</p>
<p class="vriska">VRISKA: Tavros????????</p>
<p class="vriska">VRISKA: Aradia… 8ot?</p>

<p class="vriska">VRISKA (neutral): ... LOMAT.</p>
<p class="aradiabot">ARADIABOT: im n0t g0ing t0 kill y0u</p>
<p class="aradiabot">ARADIABOT: in case y0u were w0ndering</p>
<p class="vriska">VRISKA: Yeah, that was going to 8e my next question.</p>
<p class="vriska">VRISKA: Are you... aware of the situation? Does this mean I finally cleared Tavros and you're the next level of helltier?</p>
<p class="aradiabot">ARADIABOT: i w0uldnt say that</p>
<p class="aradiabot">ARADIABOT: m0re accurately this is the b0ss fight t0 drive the p0int h0me</p>
<p class="vriska">VRISKA: Team Charge as a package deal, how is that allowed?</p>
<p class="aradiabot">ARADIABOT: because shut up</p>
<p class="aradiabot">ARADIABOT: shut up is h0w</p>
<p class="vriska">VRISKA: Ruuuuuuuude. 8ut honestly, I'm so happy to see a new face that I'm not even mad a8out it.</p>
box "What will you do?"

<p class="vriska">VRISKA: That said... if I was confused 8efore, now I'm really lost.</p>
<p class="vriska">VRISKA: Shouldn't we 8e 8ack at your hive, with me on my knees telling you I wished I never killed you or something?</p>
<p class="vriska">VRISKA: Take my eternity with those ghostly dead jerks on the chin, and let you live out your life.</p>
<p class="aradiabot">ARADIABOT: after everything that has happened y0u still think the p0int of all this is m0re punishment?</p>
<p class="vriska">VRISKA: It's not........?</p>
<p class="aradiabot">ARADIABOT: weve d0ne that already it d0esnt w0rk</p>
<p class="vriska">VRISKA: 8ut you felt 8etter the first time, right? Remem8er how good this moment was, taking life into your own hands and getting the last fist in this cycle of revenge?</p>
<p class="vriska">VRISKA: You got me soooooooo good, you can't go 8ack and say killing me was meaningless now!</p>
<p class="aradiabot">ARADIABOT: yes i can</p>
<p class="aradiabot">ARADIABOT: im a r0b0t</p>
<p class="aradiabot">ARADIABOT: i d0nt feel g00d 0r bad 0r justified</p>
<p class="aradiabot">ARADIABOT: i just d0 my j0b</p>
<p class="vriska">VRISKA: Come on!!!!!!!! Even while piloting that hunk of tin, you have to admit it was a little satisfying.</p>
<p class="aradiabot">ARADIABOT: maybe f0r y0u</p>
<p class="vriska">VRISKA: Excuse me?</p>
<p class="aradiabot">ARADIABOT: what i mean is y0u g0t exactly what y0u wanted</p>
<p class="aradiabot">ARADIABOT: y0u were ex0nerated vriska thats what its always been ab0ut</p>
<p class="vriska">VRISKA: Don't say that! I worked my ass off to m8ke things right!</p>
<p class="vriska">VRISKA: I never once asked to 8e f8rgiven for free, I always paid the price!</p>
<p class="vriska">VRISKA: Would it kill you to notice that? To see how hard I'm trying?</p>
<p class="aradiabot">ARADIABOT: pr0bably</p>
<p class="aradiabot">ARADIABOT: d0es it even matter</p>
<p class="aradiabot">ARADIABOT: wh0 can aff0rd t0 care when they kn0w y0ure g0ing t0 hurt them again?</p>
<p class="vriska">VRISKA: I WON'T!</p>
<p class="aradiabot">ARADIABOT: y0u will</p>
<p class="vriska">VRISKA: FINE!!!!!!!!</p>
<p class="vriska">VRISKA: 8ut what am I supp8sed to do then? Get 8eaten and 8ruised and mutil8ed and h8 myself forever, knowing n8ne of it will ever 8e enough?</p>
<p class="aradiabot">ARADIABOT: sure</p>
<p class="aradiabot">ARADIABOT: thats h0w y0u like it anyways</p>
<p class="aradiabot">ARADIABOT: always taking</p>
<p class="aradiabot">ARADIABOT: never c0mpr0mising</p>
<p class="vriska">VRISKA: That's h8w you see me????????</p>

<p class="vriska">VRISKA (smug): 8h8h8h8h8h8h8h8h, you... you 8lue 8looded trash c8n!</p>

<p class="vriska">VRISKA (mind control): Who cares what you think then! None of this is real anyw8ys.</p>

<p class="vriska">VRISKA (mind control): And that means the usual rules don't 8pply right? Who needs to sit around arguing when I can M8KE YOU C8RE!</p>
<p class="aradiabot">ARADIABOT: why are y0u hesitating?</p>
box "What will you do?" with Shake((0, 0, 0, 0), 1.0, dist=5)

<p class="aradiabot">ARADIABOT: this is the 0nly way right?</p>
bigBox "What will you do?" with Shake((0, 0, 0, 0), 1.3, dist=10)

<p class="aradiabot">ARADIABOT: this is h0w y0u win</p>
biggerBox "What will you do?" with Shake((0, 0, 0, 0), 1.5, dist=20)

<p class="aradiabot">ARADIABOT: d0 it</p>
biggestBox "WHAT WILL YOU DO?" with Shake((0, 0, 0, 0), 2.0, dist=30)


<p class="vriska">VRISKA: D8MN IT!</p>
<p class="aradiabot">ARADIABOT: g00d j0b</p>
<p class="vriska">VRISKA: Sh8t 8p!!!!!!!!</p>
<p class="vriska">VRISKA: I thought you said you wer8n't going to punish me anym8re!</p>
<p class="aradiabot">ARADIABOT: im n0t</p>
<p class="aradiabot">ARADIABOT: that was a test</p>
<p class="aradiabot">ARADIABOT: and y0u passed</p>
<p class="vriska">VRISKA: Gr8, glad to hear 8t!</p>
<p class="vriska">VRISKA: Can y8u tell m8 how to get 8ut of here now?</p>
<p class="vriska">VRISKA (sad): I me8n........ what do I have t8 do to finally redeem myself.</p>
<p class="aradiabot">ARADIABOT: y0ure n0t here t0 be redeemed vriska y0ure here t0 gr0w up</p>
<p class="vriska">VRISKA: ........ WH8T THE H8LL DOES TH8T MEAN?</p>
<p class="aradiabot">ARADIABOT: y0u are very g00d at saying s0rry</p>
<p class="aradiabot">ARADIABOT: pr0bably because y0ure c0nstantly creating situati0ns y0u have t0 say s0rry f0r</p>
<p class="aradiabot">ARADIABOT: why is that</p>
<p class="vriska">VRISKA: Uhhhhhhhh, 8ecause I'm a 8ig idiot who sucks?</p>
<p class="aradiabot">ARADIABOT: 0k</p>
<p class="vriska">VRISKA: 8ut I have to 8e this way!</p>
<p class="vriska">VRISKA: When everyone else starts slacking off and getting compl8cent I'm the 8ossy 8road that shakes everything up and puts them 8ack on track.</p>
<p class="aradiabot">ARADIABOT: thats kind 0f sad</p>
<p class="vriska">VRISKA: No it's not, it's awesome!</p>
<p class="aradiabot">ARADIABOT: d0 y0u even want t0 be that b0ssy br0ad?</p>
<p class="vriska">VRISKA: Of course I do!!!!!!!!</p>
<p class="vriska">VRISKA: If I wasn't, what good would I 8e to anyone? What would even 8e the point of keeping me around? Of 8eing alive????????</p>
<p class="aradiabot">ARADIABOT: see what i mean that is a very sad thing t0 say</p>
<p class="aradiabot">ARADIABOT (speak): i d0nt think its true either</p>
<p class="aradiabot">ARADIABOT: i think that even at y0ur m0st useless self there is a place in the w0rld f0r y0u</p>
<p class="aradiabot">ARADIABOT: and pe0ple in it that want t0 share a life with y0u if y0ud let them</p>
<p class="vriska">VRISKA: Y-you can't mean that?</p>
<p class="aradiabot">ARADIABOT: i d0</p>
<p class="vriska">VRISKA: Aradia ........</p>
<p class="vriska">VRISKA: Am I the pro8lem?</p>
<p class="aradiabot">ARADIABOT: 0o0</p>
<p class="aradiabot">ARADIABOT: i am g0ing t0 expl0de again</p>
<p class="vriska">VRISKA: I'm 8eing serious! If I hear you out, take all this crap seriously, do you actually think I could change?</p>
<p class="aradiabot">ARADIABOT: 0f c0urse!</p>
<p class="aradiabot">ARADIABOT: y0u already have</p>
<p class="vriska">VRISKA: I have????????</p>
<p class="aradiabot">ARADIABOT: yes</p>
<p class="aradiabot">ARADIABOT: alternia and the game and the mete0r and everything else y0uve lived thr0ugh have made y0u incrementally different than y0u were bef0re</p>
<p class="aradiabot">ARADIABOT: y0u are in c0nstant m0ti0n every m0ment y0ure alive</p>
<p class="vriska">VRISKA: Oh. I wasn't expecting you to say that, that's actually kind of nice to hear!</p>
<p class="aradiabot">ARADIABOT: thats why stagnati0n and cycles are s0 danger0us</p>
<p class="aradiabot">ARADIABOT: y0u get c0mf0rtable with their r0utine</p>
<p class="aradiabot">ARADIABOT: all the while ign0rant t0 the c0rrupti0n c0nsistently layering 0n t0p 0f itself</p>
<p class="aradiabot">ARADIABOT: sl0wly making y0u w0rse</p>
<p class="aradiabot">ARADIABOT: and w0rse</p>
<p class="aradiabot">ARADIABOT (shadowed): and w0rse</p>
<p class="aradiabot">ARADIABOT (neutral): until n0thing is left</p>
<p class="vriska">VRISKA: Jeeze.</p>
<p class="vriska">VRISKA: There it is, there is that fucking Megido-patented 8ummer.</p>
<p class="aradiabot">ARADIABOT: yeah</p>
<p class="vriska">VRISKA: I don't completely get it, honestly.</p>
<p class="aradiabot">ARADIABOT: that aligns with y0ur aspect</p>
<p class="aradiabot">ARADIABOT: light players define themselves by their direct acti0ns and understanding</p>
<p class="aradiabot">ARADIABOT: the unique privilege 0f being a time player is 0ur intrinsic kn0wledge 0f h0w it all keeps happening</p>
<p class="vriska">VRISKA: So cooooooool.</p>
<p class="aradiabot">ARADIABOT: >.></p>
<p class="vriska">VRISKA: Fine, may8e you've got a point. MAY8E there is some8ody out there still w8ing for me, even after all my fum8ling.</p>
<p class="vriska">VRISKA (sad): It's something, I guess.</p>
<p class="vriska">VRISKA: Can I ask one more question?</p>
<p class="aradiabot">ARADIABOT: 0k</p>
<p class="vriska">VRISKA: Not to 8eat a dead ro8ot, 8ut despite everything that happened, could we have ever 8een friends?</p>
<p class="aradiabot">ARADIABOT: y0u mean if y0u had put in the time and w0rked 0n wh0 y0u are and bec0me ultimately the best versi0n 0f y0urself?</p>
<p class="aradiabot">ARADIABOT: hmm</p>
<p class="aradiabot">ARADIABOT: n0</p>
<p class="vriska">VRISKA: !!!!!!!!</p>
<p class="vriska">VRISKA: C-can I 8sk why????????</p>
<p class="vriska">VRISKA: D8 you h8 me that much?</p>
<p class="aradiabot">ARADIABOT: i d0nt hate y0u</p>
<p class="aradiabot">ARADIABOT: but i d0nt want to spend my time 0n y0u either</p>
<p class="vriska">VRISKA: 8ut!!!!!!!!</p>
<p class="aradiabot">ARADIABOT (shadowed): V.V</p>
<p class="vriska">VRISKA: ........</p>
<p class="vriska">VRISKA (sad): ........ ok.</p>
<p class="vriska">VRISKA (neutral): Ok.</p>
menu:
"{plain}[pick] {/plain}[command]":
menu:
"{plain}[pick] {/plain}[command]":
<p class="vriska">VRISKA: I know it doesn't change anything, 8ecause it already happened and also you two aren't even real.</p>
<p class="vriska">VRISKA: 8ut I am actually sorry. For everything.</p>


<p class="tavros">TAVROS: yOURE RIGHT, iT'S DEFINITELY POINTLESS TO SAY, bUT, iT IS AN APPRECI8TED GESTURE };)</p>


menu:
"{plain}[pick] {/plain}[command]":
<p class="vriska">VRISKA: And, it's not going to 8e the same again.</p>
<p class="vriska">VRISKA: I'll stick with it this time. I promise.</p>


<p class="aradia">ARADIA: we kn0w</p>
<p class="aradia">ARADIA: y0u have t0</p>
<p class="aradia">ARADIA: n0 0ne else is g0ing t0 save y0u n0w</p>


<p class="vriska">VRISKA: 8ecause it's just me left?</p>


<p class="aradia">ARADIA: yes</p>
<p class="aradia">ARADIA: its just y0u</p>
<p class="aradia">ARADIA: g00d luck vriska</p>
<p class="aradia">ARADIA: i h0pe y0u get better s00n</p>


menu:
"{plain}[pick] {/plain}[command]":
pause
iled by unrpyc: https://github.com/CensoredUsername/unrpyc
