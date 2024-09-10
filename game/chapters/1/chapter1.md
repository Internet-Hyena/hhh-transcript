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

# chapter1


$ quick_menu = True

if renpy.confirm("Would you like to skip to the chapter select menu?"):
$ MainMenu(confirm=False)()





scene bg tavroscliff with Dissolve(2.0)

"You are now Vriska, and like any good Main Character, you find yourself on the precipice of an all too familiar cliff." (sfx=None)

play music "chapters/1/audio/c1.mp3" fadein 1.0 loop

show vriska gt onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: Wow, hell was right.</p>

<p class="vriska">VRISKA: You h8 to see it.</p>
hide vriska with slideoutleft


box "What will you do?"


show vriska gt angry onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA (gt angry): What do you MEAN what will I do????????</p>

<p class="vriska">VRISKA: Davepeta, is that you?</p>

<p class="vriska">VRISKA (gt thinking): ...</p>

<p class="vriska">VRISKA (gt smug): Wow once again it falls to me to figure all this shit out in any sort of meaningful way.</p>

<p class="vriska">VRISKA (gt idle): ...</p>

<p class="vriska">VRISKA (gt angry): And why the fuck is Tavros here!!!!!!!!</p>
hide vriska with slideoutleft


show tavros onlayer talksprites at right with slideinright

<p class="tavros">TAVROS: i PROBABLY DON'T, uHH, WANT TO QUESTION, yOUR METHODS</p>

<p class="tavros">TAVROS (nervous): aND MAYBE, iF THERE WERE A BRAVER VERSION, oF ME, hERE, HE MIGHT SAY, tHAT UM, iT'S BECAUSE USUALLY, tHAT MAKES YOU MAD</p>

<p class="tavros">TAVROS: bUT SINCE THERE ISN'T, a VERSION OF ME LIKE THAT HERE, i GUESS IT'S BECAUSE I, uHH</p>

<p class="tavros">TAVROS (smiling): lIVE HERE MOSTLY,</p>
hide tavros with slideoutright


show vriska gt onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: Shut the fuck up Tavros!</p>

<p class="vriska">VRISKA (gt thinking): This is o8viously some sort of trial.</p>

<p class="vriska">VRISKA: Cleeeeeeeearly I'm 8eing faced with the ghosts of my past and I have to \"sort it out\" or some horse shit.</p>

<p class="vriska">VRISKA: Thanks for the guidance, Nepadave, or whoever the literal hell.</p>

<p class="vriska">VRISKA (gt smug): 8ut I got it all figured out already!</p>

<p class="vriska">VRISKA (gt thinking): I'm going to speedrun enlightenment and save this horri8le fake universe from imploding in on itself.</p>

<p class="vriska">VRISKA (gt smug): You're welcome.</p>
hide vriska with slideoutleft


show tavros onlayer talksprites at right with slideinright

<p class="tavros">TAVROS: oK WELL, i WILL PRETEND THAT, uHH</p>

<p class="tavros">TAVROS: iF I WAS SOMEONE, wHO DIDN'T UNDERSTAND, wHAT YOU WERE SAYING,</p>

<p class="tavros">TAVROS (nervous): bECAUSE, i'M FEELING PRETTY ALIVE FOR THE MOST PART, i THINK</p>

<p class="tavros">TAVROS: tHAT PERSON, tHAT I'M PRETENDING TO BE, mIGHT ASK</p>

<p class="tavros">TAVROS (smiling): wHY, yOU THINK THAT IM A GHOST,</p>
hide tavros with slideoutright


show vriska gt onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: You still have legs, for one.</p>
hide vriska with slideoutleft


show tavros onlayer talksprites at right with slideinright

<p class="tavros">TAVROS: oH THANK YOU,</p>

<p class="tavros">TAVROS: tHAT IS A NORMAL THING, fOR YOU TO SAY, aBOUT GHOSTS,</p>

<p class="tavros">TAVROS (smiling): i SEE UM, yOU ALSO, hAVE LEGS</p>

<p class="tavros">TAVROS (nervous): wHICH MIGHT BE A GHOST THING, tHAT I AM MOSTLY, uNAWARE OF</p>

<p class="tavros">TAVROS: sO, mAYBE, wE ARE BOTH GHOSTS,</p>

<p class="tavros">TAVROS (smiling): }:)</p>
hide tavros with slideoutright


show vriska gt thinking onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA (gt thinking): I've already done this, though.</p>

<p class="vriska">VRISKA (gt smug): I reconciled with Tavros days ago.</p>

<p class="vriska">VRISKA: I'm completely in the clear! He forgave me already.</p>
hide vriska with slideoutleft


show tavros nervous onlayer talksprites at right with slideinright

<p class="tavros">TAVROS (nervous): fOR WHAT,</p>
hide tavros with slideoutright


show vriska gt thinking onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA (gt thinking): It couldn't 8e that easy, could it?</p>

<p class="vriska">VRISKA: Hey. Tavros.</p>
hide vriska with slideoutleft


show tavros smiling onlayer talksprites at right with slideinright

<p class="tavros">TAVROS (smiling): hI THAT'S ME, i THINK,</p>
hide tavros with slideoutright


show vriska gt onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: I'm sorry I killed you.</p>
hide vriska with slideoutleft


show tavros onlayer talksprites at right with slideinright

<p class="tavros">TAVROS: dID YOU DO THAT,</p>
hide tavros with slideoutright


box "What will you do?"


show vriska gt idle onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA (gt idle): </p>

<p class="vriska">VRISKA (gt neutral): ... damn.</p>

<p class="vriska">VRISKA (gt smug): Well I guess it wouldn't 8e worth anything if it were that simple.</p>
hide vriska with slideoutleft


show tavros nervous onlayer talksprites at right with slideinright

<p class="tavros">TAVROS (nervous): uM VRISKA DID-</p>
hide tavros with slideoutright


show vriska gt angry onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA (gt angry): Ugh!!!!!!!!</p>

<p class="vriska">VRISKA (gt thinking): What did they mean \"sort it out,\" then? I feel fine a8out killing Tavros, and he's certainly ok with it now. The situation's sorted!</p>
hide vriska with slideoutleft


show tavros smiling onlayer talksprites at right with slideinright

<p class="tavros">TAVROS (smiling): iS THAT TRUE,</p>
hide tavros with slideoutright


show vriska gt onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: It's completely sorted!</p>

<p class="vriska">VRISKA: Damn, it could have 8een any num8er of things.</p>

<p class="vriska">VRISKA (gt smug): I did a lot of things wrong.</p>

<p class="vriska">VRISKA: Hey Tavros, I'm sorry I made you an accomplice to a really awesome assassination that I got my ass kicked for, 8ut then I 8ecame a god so 8asically it was the right thing to do.</p>
hide vriska with slideoutleft


show tavros smiling eyesclosed onlayer talksprites at right with slideinright

<p class="tavros">TAVROS (smiling eyesclosed): ...</p>
hide tavros with slideoutright


box "What will you do?"


show vriska gt thinking onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA (gt thinking): No dice, huh? Okay, try this one on for size!</p>

<p class="vriska">VRISKA: I'm sorry I kissed you and then used mind control to make you try and love me that one time. That one's on me.</p>
hide vriska with slideoutleft


show tavros smiling onlayer talksprites at right with slideinright

<p class="tavros">TAVROS (smiling): ...</p>
hide tavros with slideoutright


box "What will you do?"


show vriska gt onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: Fuck, that was a good one... this character growth shit is hard.</p>
hide vriska with slideoutleft

$ command = "{{Hours later, but not many.}"
menu:
"{plain}[pick] {/plain}[command]":
show black with Dissolve(2.0)
hide black with Dissolve(2.0)


show vriska gt sad onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA (gt sad): ...I'm sorry I said your lusus \"smelled like tears\".</p>
hide vriska with slideoutleft


box "What will you do?"

show vriska gt angry onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA (gt angry): FUCK!!!!!!!!</p>

<p class="vriska">VRISKA (gt thinking): I'm really scraping the 8ottom of the 8arrel here...</p>

<p class="vriska">VRISKA: and I'm 8eing sincere a8out at least 80%% of these!</p>
hide vriska with slideoutleft


show tavros nervous onlayer talksprites at right with slideinright

<p class="tavros">TAVROS (nervous): aS MUCH FUN, aS I THINK YOU MAYBE THINK WE ARE MUTUALLY HAVING</p>

<p class="tavros">TAVROS: aND, i DON'T WANT TO RUIN THAT, bY</p>

<p class="tavros">TAVROS: bEING MY USUAL SELF, lIKE YOU ARE ALWAYS TELLING ME IS BAD,</p>

<p class="tavros">TAVROS (nervous): a LOT OF THOSE THINGS, sEEM, uM</p>

<p class="tavros">TAVROS (smiling): uNIMPORTANT AND SORT OF, nORMAL,</p>

<p class="tavros">TAVROS (nervous): fOR YOU,</p>
hide tavros with slideoutright


show vriska gt thinking onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA (gt thinking): </p>

<p class="vriska">VRISKA (gt smug): You're right.</p>

<p class="vriska">VRISKA (gt idle): ...</p>

<p class="vriska">VRISKA (gt idle): ...</p>
hide vriska with slideoutleft


box "What will you do?"


show vriska gt onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: Damn it. Well even if that doesn't solve this puzzle, 8y some happenstantial miracle it's still true.</p>
hide vriska with slideoutleft


show tavros onlayer talksprites at right with slideinright

<p class="tavros">TAVROS: i THINK IT'S, sOMETIMES ALRIGHT</p>

<p class="tavros">TAVROS: tO JUST STAND, tOGETHER,</p>

<p class="tavros">TAVROS: oUTSIDE OF MY HOUSE, fOR A FEW HOURS, aND,</p>

<p class="tavros">TAVROS (nervous): i AM NOT AT ALL</p>

<p class="tavros">TAVROS: fRIGHTENED, tHAT YOU WILL DO SOMETHING,</p>

<p class="tavros">TAVROS (smiling): hORRIBLE TO ME,</p>
hide tavros with slideoutright


show vriska gt onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: Incredi8le! Listen to you!</p>

<p class="vriska">VRISKA: You have me here practically groveling at your feet.</p>

<p class="vriska">VRISKA: And even after all I put you through, you're still not trying to get your just desserts.</p>

<p class="vriska">VRISKA (gt sad): All this apologizing and rolling over and exposing my weaknesses isn't solving shit!</p>

<p class="vriska">VRISKA (gt smug): It's like I'm always saying, words are meaningless.</p>

<p class="vriska">VRISKA: What we need is action.</p>
hide vriska with slideoutleft


show tavros nervous onlayer talksprites at right with slideinright

<p class="tavros">TAVROS (nervous): i THINK MAYBE, tHAT,</p>

<p class="tavros">TAVROS: dOING uHH, \"ACTIONS,\"</p>

<p class="tavros">TAVROS: mIGHT BE ONE OF THE THINGS, tHAT YOU FEEL, lIKE YOU DID WRONG</p>

<p class="tavros">TAVROS: aND, mAYBE SOME WORDS, aCTUALLY,</p>

<p class="tavros">TAVROS (smiling): cAN BE PRETTY USEFUL, sOMETIMES,</p>
hide tavros with slideoutright


show vriska gt onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: That sounds wrong, so I'm going to completely ignore it.</p>
hide vriska with slideoutleft


show tavros onlayer talksprites at right with slideinright

<p class="tavros">TAVROS: oH, oK,</p>
hide tavros with slideoutright


show vriska gt onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: 8ut sure. Let's try it your way.</p>
hide vriska with slideoutleft


show tavros smiling eyesclosed onlayer talksprites at right with slideinright

<p class="tavros">TAVROS (smiling eyesclosed): oH, oK,</p>
hide tavros with slideoutright


show vriska gt onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: Instead of me taking action, what I need is for you to take action.</p>

<p class="vriska">VRISKA (gt smug): It was so o8vious that it's stupid, actually.</p>
hide vriska with slideoutleft


show tavros onlayer talksprites at right with slideinright

<p class="tavros">TAVROS: tHAT'S NOT, wHAT I SAID, aT ALL,</p>
hide tavros with slideoutright


show vriska gt onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: The reason I'm stuck here is 8ecause I don't owe you plac8ing apologies</p>

<p class="vriska">VRISKA: I owe you revenge. It's just that easy!</p>
hide vriska with slideoutleft


show tavros onlayer talksprites at right with slideinright

<p class="tavros">TAVROS: bUT-</p>
hide tavros with slideoutright


show vriska gt smug onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA (gt smug): It's just that easy!</p>
hide vriska with slideoutleft


show tavros idle onlayer talksprites at right with slideinright

<p class="tavros">TAVROS (idle): ...</p>
hide tavros with slideoutright


show vriska gt angry onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA (gt angry): IT'S J-</p>
hide vriska with slideoutleft


show tavros onlayer talksprites at right with slideinright

<p class="tavros">TAVROS: bUT WHAT IF, sOMEONE WERE TO SAY, hYPOTHETICALLY SPEAKING,</p>

<p class="tavros">TAVROS: i DON'T THINK THATS THE THING I WANT TO, uMM, bE DOING</p>

<p class="tavros">TAVROS (nervous): aT ALL, oR, eVEN SORT OF,,</p>

<p class="tavros">TAVROS: aND THAT I STILL THINK IT WAS WRONG BUT I FORGIVE YOU FOR DOING THOSE THINGS THAT YOU SAID YOU DID, tO ME EARLIER,</p>
hide tavros with slideoutright


show vriska gt onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: No. You deserve revenge. Action 8egets action. This makes perfect sense to anyone who's 8een paying attention.</p>

<p class="vriska">VRISKA (gt thinking): </p>

<p class="vriska">VRISKA (gt neutral): You have to throw me off this cliff.</p>

<p class="vriska">VRISKA: Then we'll 8e completely squared away.</p>
hide vriska with slideoutleft


show tavros nervous onlayer talksprites at right with slideinright

<p class="tavros">TAVROS (nervous): uHH I DON'T THINK-</p>
hide tavros with slideoutright


show vriska gt smug onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA (gt smug): I'm praaaaaaaactically an expert on this revenge thing. Trust me.</p>
hide vriska with slideoutleft


show tavros onlayer talksprites at right with slideinright

<p class="tavros">TAVROS: vRISKA I DON'T WANT TO DO A REVENGE ON YOU</p>

<p class="tavros">TAVROS: fOR CRIMES, yOU HAVEN'T REALLY DONE, aND MAYBE SOME YOU DID,</p>

<p class="tavros">TAVROS: aND THIS MAY, uHH, sEEM COUNTERPRODUCTIVE, tO YOUR IDEA</p>

<p class="tavros">TAVROS (nervous): bUT IT SOUNDS LIKE, bEING THROWN OFF A CLIFF MIGHT NOT BE A HEALTHY COPING MECHANISM,</p>
hide tavros with slideoutright


show vriska gt onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: It's fine! Kill me, get your revenge, and I'll finally 8e on my way.</p>

<p class="vriska">VRISKA (gt smug): Out of your life forever! Never to torment you again!</p>

<p class="vriska">VRISKA: And whatever version of you this is can go on living your little life playing with your little monster dolls or whatever!</p>

<p class="vriska">VRISKA (gt sad): Here on Alternia.</p>

<p class="vriska">VRISKA (gt sad): 8efore everything goes wrong.</p>

<p class="vriska">VRISKA: You can kill me now 8efore it's too late for you.</p>

<p class="vriska">VRISKA (gt sad): 8efore I screw your life up.</p>

<p class="vriska">VRISKA (gt smug): It's perfect!</p>
hide vriska with slideoutleft


show tavros onlayer talksprites at right with slideinright

<p class="tavros">TAVROS (nervous): nO I DON'T WANT TO DO THAT,</p>
hide tavros with slideoutright


show vriska gt onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: I know you have it in you. I've seen it.</p>

<p class="vriska">VRISKA (gt angry): God damn it Tavros, if you don't kill me I can't move on.</p>

<p class="vriska">VRISKA (gt neutral): You'd 8e doing me a favor.</p>

<p class="vriska">VRISKA: Go on.</p>
hide vriska with slideoutleft


show tavros nervous onlayer talksprites at right with slideinright

<p class="tavros">TAVROS (nervous): uHH,</p>
hide tavros with slideoutright


show vriska gt onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: Kill me.</p>
hide vriska with slideoutleft


show tavros nervous onlayer talksprites at right with slideinright

<p class="tavros">TAVROS (nervous): nO,</p>
hide tavros with slideoutright


show vriska gt angry onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA (gt angry): Hey get 8ack here!</p>
hide vriska with slideoutleft


show tavros nervous onlayer talksprites at right with slideinright

<p class="tavros">TAVROS (nervous): nO!</p>
show tavros nervous idle:
linear .1 xzoom -1.0
pause .25
hide tavros with slideoutright


show vriska gt angry onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA (gt angry): Stop running!</p>
hide vriska with slideoutleft



<p class="tavros">TAVROS: nO, i LOVE TO RUN AND, i DO NOT PLAN ON STOPPING, aNY TIME SOON,</p> (window_xoffset=0)


show vriska gt angry onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA (gt angry): You kill me right this instant!</p>

<p class="vriska">VRISKA: Damn it, I forgot how fast he used to 8e.</p>
hide vriska with slideoutleft



<p class="tavros">TAVROS: nO!</p> (window_xoffset=0)


show vriska gt smug onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA (gt smug): Man, doing the right thing sure is hard work.</p>

<p class="vriska">VRISKA: I didn't want to do this, Tavros, 8ut you're forcing my hand here. I won't make the same mistake again.</p>
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


<p class="vriska">VRISKA: Good luck.</p> (what_xalign=0.5, what_yalign=0.5, what_textalign=0.5, window_xoffset=0)

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


<p class="tavros">TAVROS: uHH, oH SHUCKS, bYE VRISKA,</p> (what_xalign=0.5, what_yalign=0.5, what_textalign=0.5, window_xoffset=0)

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

# chapter1_end

show white with Dissolve(3.0)

"YEAR 2" (window_yalign=0.5, window_yoffset=0, window_xsize=150, window_ysize=75, window_ypos=0.5)

scene bg vriskaroom with Dissolve(3.0)

play music "chapters/1/audio/c1end.mp3" volume 0.5 loop

show davepeta roleplay onlayer talksprites at right with slideinright

<p class="davepetasprite">DAVEPETASPRITE: *dp pads through the underbrush of the forest, leaving paw prints after themselves in the freshly fallen snow*</p>
<p class="davepetasprite">DAVEPETASPRITE: *their ears twitch cutely with every step they take beclaws as perfect a creature as they are cats are still too fucking stupid to invent proper p33ts protectors*</p>
<p class="davepetasprite">DAVEPETASPRITE: *they will probably need to get these silly little beans amputated after walking through all this white shit but whatever its fine, at the end of this tail is an important furiend*</p> (what_size=16)
hide davepeta with slideoutright


show vriska idle onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: ...</p>
hide vriska with slideoutleft


show davepeta roleplay onlayer talksprites at right with slideinright

<p class="davepetasprite">DAVEPETASPRITE: every year farmers and freaks alike crowd around this curious critter wringing their sweaty boring human hands all nervously hoping for winters end</p>
<p class="davepetasprite">DAVEPETASPRITE: but this overhyped moles shadow offurs a symbolic appouncement for the spider instead</p>
hide davepeta with slideoutright


show vriska idle onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: ........</p>
hide vriska with slideoutleft


show davepeta roleplay onlayer talksprites at right with slideinright

<p class="davepetasprite">DAVEPETASPRITE: the breaking of cycles, dissolution of the self, whatever other philosophical rhetoric bill murray said in that one meowvie</p>
<p class="davepetasprite">DAVEPETASPRITE: its all up to you, spider, to grab this guy by the furry haunches bend him over and nonsexually spank him into submewssion</p>

<p class="davepetasprite">DAVEPETASPRITE (neutral): what will you do vriska?</p>
hide davepeta with slideoutright


show vriska angry onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: *The spider doesn't do anything, 8ecause spiders don't have 8rains to make good choices. Instead, we're doomed to crawl around on our 8ellies like idiots, w8ing to 8e crushed under the giant furry ass of an animal so pathetic humans had to make up reasons to care a8out it, and with her luck she'll spend eternity 8uried alive under poop pellets du88ed the pharaoh of trash assholes and praying to die.*</p> (what_size=13)
hide vriska with slideoutleft


show davepeta thinking onlayer talksprites at right with slideinright

<p class="davepetasprite">DAVEPETASPRITE: vriskers not to ask an obvious question but</p>
<p class="davepetasprite">DAVEPETASPRITE: are you good?</p>

<p class="davepetasprite">DAVEPETASPRITE (uncomfortable): you s33m... depressed</p>
hide davepeta with slideoutright


show vriska onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: What are you talking a8out?</p>
<p class="vriska">VRISKA: Isn't it o8vious how excited I am?</p>
<p class="vriska">VRISKA: 8anging my head against a wall for several hours is practically my daily medit8tion now.</p>

<p class="vriska">VRISKA (angry): \"Purrhaps\" today will 8e the day I finally give myself a deep enough pan lesion that my neurons will reset and I can finally understand what I'm supposed to 8e doing here.</p>
<p class="vriska">VRISKA: Finally moving on FROM THIS 8ORING M8ND NUM8ING SHIIIIIIITTY PUNISHM8NT PIT.</p>
hide vriska with slideoutleft


show davepeta pokerface onlayer talksprites at right with slideinright

<p class="davepetasprite">DAVEPETASPRITE: wrow</p>
hide davepeta with slideoutright


show vriska sad onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: Sigh.</p>
<p class="vriska">VRISKA: Can you please tell me what to do? And not in some coy, rounda8out way like you have 8een.</p>

<p class="vriska">VRISKA (neutral): You're supposed to 8e guiding me, 8ut instead sweeps of my life are 8eing w8sted here when I could 8e doing so much more out there.</p>
hide vriska with slideoutleft


show davepeta embarrassed onlayer talksprites at right with slideinright

<p class="davepetasprite">DAVEPETASPRITE: trust me im trying!!</p>
<p class="davepetasprite">DAVEPETASPRITE: my advice is just... a litter bit limited</p>

<p class="davepetasprite">DAVEPETASPRITE (thinking): ask me about mechanics or some dank catnip or even how to stunt down the stairs without breaking every bone in your body and i can chitter your ear off for another couple years</p> (what_size=16)
<p class="davepetasprite">DAVEPETASPRITE: but countless cool dudes and kitty girls cant inform much on how to handle those classic serket problems</p>

<p class="davepetasprite">DAVEPETASPRITE (pokerface): feel me?</p>
hide davepeta with slideoutright


show vriska angry onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: Soooooooo what you are saying is you can't help 8ecause you are the Ultimate Winged Weener and can't relate to 8eing a huge 8itch like me?</p>
hide vriska with slideoutleft


show davepeta onlayer talksprites at right with slideinright

<p class="davepetasprite">DAVEPETASPRITE: ha he</p>

<p class="davepetasprite">DAVEPETASPRITE (pokerface): w33ner</p>

<p class="davepetasprite">DAVEPETASPRITE (cute): but yeah thats pretty much how it is</p>

<p class="davepetasprite">DAVEPETASPRITE (neutral): you know what they say theres purrppets and then theres pawppet33rs</p>
<p class="davepetasprite">DAVEPETASPRITE: and both mew selves rather be on the yarn strings</p>
<p class="davepetasprite">DAVEPETASPRITE: so alot of my thoughts on how to come back from all your bullshit begins and ends at \"i simply would not have done that in the first place\"</p>

<p class="davepetasprite">DAVEPETASPRITE (pokerface): no judgment of course</p>

<p class="davepetasprite">DAVEPETASPRITE (thinking): see if you had watched the damn groundhog movie youd have all the relatable advice youd n33d</p>
hide davepeta with slideoutright


show vriska angry onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: I will never ever watch that stupid groundhog movie!</p>
<p class="vriska">VRISKA: This is such 8ullshit. Like you're some softy, hurt-no8ody housecat! You literally defe8ed Lord English and kill wild animals with your 8are h8nds!!!!!!!!</p>
hide vriska with slideoutleft


show davepeta pokerface onlayer talksprites at right with slideinright

<p class="davepetasprite">DAVEPETASPRITE: ok hunting is way different</p>
<p class="davepetasprite">DAVEPETASPRITE: blood and guts and broken wrists and fractured tailbones</p>
<p class="davepetasprite">DAVEPETASPRITE: thats nature and instinct it doesnt have to be mean</p>
<p class="davepetasprite">DAVEPETASPRITE (roleplay): *the fearsome gender neutral lionesster pins down its prey but instead of getting down to business growls out how the prey deserves this for being a big disappointing pussy*</p> (what_size=16)

<p class="davepetasprite">DAVEPETASPRITE (uncomfortable): s33 very weird</p>

<p class="davepetasprite">DAVEPETASPRITE (cute): i might have to eat a guy but that doesnt mean i cant respect them</p>
hide davepeta with slideoutright


show vriska sad onlayer talksprites at left with slideinleft

<p class="vriska">VRISKA: 8ut what if the natural order is exactly what's working against me here?</p>

<p class="vriska">VRISKA (angry): Wh8t am I supposed to do then????????</p>
hide vriska with slideoutleft


show davepeta thinking onlayer talksprites at right with slideinright

<p class="davepetasprite">DAVEPETASPRITE: sure hope thats not true...</p>

<p class="davepetasprite">DAVEPETASPRITE (cute): or well be here furrever!</p>
hide davepeta with slideoutright

stop music fadeout 3.0

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
