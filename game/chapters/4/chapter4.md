image bg parlor:
size (950,650) yalign 0.5 xalign 0.5
"chapters/4/images/scratchsparlor.png"

image bg chessboard:
size (950,650) yalign 0.5 xalign 0.5
"chapters/4/images/chessboard.png"

image bg chessboard_vrisgone:
size (950,650) yalign 0.5 xalign 0.5
"chapters/4/images/chessboard_vrisgone.png"

image bg chessboard_glitch:
size (950,650) yalign 0.5 xalign 0.5
"chapters/4/images/chessboard.png"
pause 0.2
choice:
glitch("bg chessboard", offset=60, chroma=True, randomkey=413)
choice:
glitch("bg chessboard", offset=60, chroma=True, randomkey=0)
choice:
glitch("bg chessboard", offset=60, chroma=True, randomkey=2202)
choice:
glitch("bg chessboard", offset=60, chroma=True, randomkey=8888)
pause 0.1
"chapters/4/images/chessboard.png"
repeat 5

image bg chessboard_vrisgone_glitch:
size (950,650) yalign 0.5 xalign 0.5
"chapters/4/images/chessboard_vrisgone.png"
pause 0.2
choice:
glitch("bg chessboard_vrisgone", offset=60, chroma=True, randomkey=413)
choice:
glitch("bg chessboard_vrisgone", offset=60, chroma=True, randomkey=2202)
choice:
glitch("bg chessboard_vrisgone", offset=60, chroma=True, randomkey=0)
choice:
glitch("bg chessboard_vrisgone", offset=60, chroma=True, randomkey=8888)
pause 0.1
"chapters/4/images/chessboard_vrisgone.png"
repeat

image bg level_complete_4:
size (950,650) yalign 0.5 xalign 0.5
"chapters/4/images/level_complete_1.png"
pause 0.05
"chapters/4/images/level_complete_2.png"
pause 0.05
"chapters/4/images/level_complete_3.png"
pause 0.05
"chapters/4/images/level_complete_4.png"
pause 0.05
repeat

image glitch_box:
size (950,650) yalign 0.5 xalign 0.5
"chapters/4/images/glitch_box_00000.png"
pause 0.067
"chapters/4/images/glitch_box_00001.png"
pause 0.067
"chapters/4/images/glitch_box_00002.png"
pause 0.067
"chapters/4/images/glitch_box_00003.png"
pause 0.067
"chapters/4/images/glitch_box_00004.png"
pause 0.067
"chapters/4/images/glitch_box_00005.png"
pause 0.067
"chapters/4/images/glitch_box_00006.png"
pause 0.067
"chapters/4/images/glitch_box_00007.png"
pause 0.067
"chapters/4/images/glitch_box_00008.png"
pause 0.067
"chapters/4/images/glitch_box_00009.png"
pause 0.067
"chapters/4/images/glitch_box_00010.png"
pause 0.067
"chapters/4/images/glitch_box_00011.png"
pause 0.067
"chapters/4/images/glitch_box_00012.png"
pause 0.067
"chapters/4/images/glitch_box_00013.png"
pause 0.067
"chapters/4/images/glitch_box_00014.png"
pause 0.067
"chapters/4/images/glitch_box_00015.png"
pause 0.1
"chapters/4/images/glitch_box_00016.png"
pause 0.067
"chapters/4/images/glitch_box_00017.png"

image exactly:
"chapters/4/images/Exactly_0000.png"
pause 0.045
"chapters/4/images/Exactly_0001.png"
pause 0.045
"chapters/4/images/Exactly_0002.png"
pause 0.045
"chapters/4/images/Exactly_0003.png"
pause 0.045
"chapters/4/images/Exactly_0004.png"
pause 0.045
"chapters/4/images/Exactly_0005.png"
pause 0.045
"chapters/4/images/Exactly_0006.png"
pause 0.045
"chapters/4/images/Exactly_0007.png"
pause 0.045
"chapters/4/images/Exactly_0008.png"
pause 0.045
"chapters/4/images/Exactly_0009.png"
pause 0.045
"chapters/4/images/Exactly_0010.png"
pause 0.045
"chapters/4/images/Exactly_0011.png"
pause 0.045
"chapters/4/images/Exactly_0012.png"
pause 0.045
"chapters/4/images/Exactly_0013.png"
pause 0.045
"chapters/4/images/Exactly_0014.png"
pause 0.045
"chapters/4/images/Exactly_0015.png"
pause 0.045
"chapters/4/images/Exactly_0016.png"
pause 0.045
"chapters/4/images/Exactly_0017.png"
pause 0.045
"chapters/4/images/Exactly_0018.png"
pause 0.045
"chapters/4/images/Exactly_0019.png"
pause 0.045
"chapters/4/images/Exactly_0020.png"
pause 0.045
"chapters/4/images/Exactly_0021.png"
pause 0.045
"chapters/4/images/Exactly_0022.png"
pause 0.045
"chapters/4/images/Exactly_0023.png"
pause 0.045
repeat

image umber = Solid("#a15000")
image burgandy = Solid("#a10000")
image teal = Solid("#008282")
image red = Solid("#ff0000")
image purple = Solid("#4200b0")
image blue = Solid("#0022cf")
image green = Solid("#008141")

transform stop_move:
xoffset 0

transform jerkRight:
ease 1.0 xalign 1.0
transform jerkLeft:
ease 1.0 xalign 0.0
transform jerkHalfLeft:
ease 0.5 xalign 0.0

transform returnToCenter:
ease 0.5 xalign 0.5 yalign 1.0

transform returnToCenterSlow:
xoffset 0
ease 2.0 xalign 0.5 yalign 1.0

transform lightshake:
linear 0.05 xoffset 10
linear 0.05 xoffset -10
repeat 2

transform shrink:
ease 0.5 xalign 0.2
easeout 1.5 xoffset 100 zoom 0 alpha 0

transform unshrink:
alpha 1.0
zoom 1.0

image vriska_glow:
xoffset 20
"chapters/4/characters/vriska/vriska_sullen_crying_eye.png"
matrixcolor BrightnessMatrix(1.0)

transform pulse:
alpha 0.0
block:
ease 1.0 alpha 0.0
ease 2.5 alpha 1.0


# chapter4_prologue
$ scratch = False
scene black

scene bg vriskaroom with Dissolve(3.0)
play music "chapters/4/audio/erisol.wav" fadein 1.0 volume 0.5 loop


show vriska adult neutral onlayer talksprites at left with slideinleft
<p class="vriska">VRISKA: Whew.</p>
<p class="vriska">VRISKA: Long day.</p>
hide vriska with slideoutleft


show gcatav mischievous onlayer talksprites at right with slideinright
<p class="gcatav">GCATAV: mAYBE, yOU SHOULD TAKE A BREAK, fROM ALL THE TOTALLY AWESOME PERSONAL BREAKTHROUGHS YOU ARE HAVING,</p>
<p class="gcatav">GCATAV: aND KICK IT WITH ME AND ERISOL FOR A WHILE,</p>
hide gcatav with slideoutright


show erisolsprite neutral onlayer talksprites at right with slideinright
<p class="erisolsprite">ERISOLSPRITE: yeah, you kiinda look liike 2hiit.</p>
hide erisolsprite with slideoutright


show vriska adult smiling onlayer talksprites at left with slideinleft
<p class="vriska">VRISKA: Says Scarfshades McLopsided.</p>
hide vriska with slideoutleft


show erisolsprite neutral onlayer talksprites at right with slideinright
<p class="erisolsprite">ERISOLSPRITE: 2ay2 the bu2ted a22 biitch wweariin the 2ame raggedy jacket 2he2 wworn 2iince wwe wwere liike fiivve.</p>
hide erisolsprite with slideoutright


show vriska adult smiling onlayer talksprites at left with slideinleft
<p class="vriska">VRISKA: Says the guy who literally can't change his clothes.</p>
hide vriska with slideoutleft


show erisolsprite neutral onlayer talksprites at right with slideinright
<p class="erisolsprite">ERISOLSPRITE: ii cant be held accountable for my dii2cordant cla22-2wwag diichotomy, but here you are a 2wweep and a half deep iin a per2onally taiilored realm of 2elf-reflectiion and you 2tiill choo2e twwo look liike thii2.</p>
hide erisolsprite with slideoutright


show vriska adult smiling onlayer talksprites at left with slideinleft
<p class="vriska">VRISKA: Heh.</p>
hide vriska with slideoutleft


show erisolsprite smirking onlayer talksprites at right with slideinright
<p class="erisolsprite">ERISOLSPRITE: heh.</p>
<p class="erisolsprite">ERISOLSPRITE (neutral): anyway, come chiill.</p>
hide erisolsprite with slideoutright


show gcatav mischievous onlayer talksprites at right with slideinright
<p class="gcatav">GCATAV: oR, iNSTEAD OF CHILLING,</p>
<p class="gcatav">GCATAV (mischievous): wE COULD THROW AROUND A BALL OF YARN, oR SOMETHING ELSE VISUALLY STIMULATING, tHAT MIMICS MY PREFERRED QUARRY OF SMALL ANIMALS I COULD KILL FOR FUN AND NOT EAT,</p>
<p class="gcatav">GCATAV (mischievous): aND I COULD CHASE IT WITH MY LEGS,</p>
<p class="gcatav">GCATAV (mischievous): tHAT AREN'T LEGS, aND ARE ACTUALLY A GHOST TAIL,</p>
<p class="gcatav">GCATAV (mischievous): wHICH REALLY HAS NO BEARING ON MY ABILITY TO MOVE AT ALL,</p>
<p class="gcatav">GCATAV (mischievous): aNYWAY,</p>
<p class="gcatav">GCATAV (mischievous): tHE IMPORTANT THING, iS THAT YOU SHOULD PROBABLY GET SOME R AND R,</p>
<p class="gcatav">GCATAV (mischievous): aND ALSO HAVE A VERY VIGOROUS PLAYTIME SESH, wITH THE BOYS,</p>
<p class="gcatav">GCATAV (mischievous): aND MAYBE GET WICKED PRANKED ON,</p>
<p class="gcatav">GCATAV (mischievous): sO YOU DON'T BURN OUT,</p>
<p class="gcatav">GCATAV (mischievous): }:3</p>
<p class="gcatav">GCATAV (sneeze): aCHOO!</p>
hide gcatav with slideoutright


show erisolsprite neutral onlayer talksprites at right with slideinright
<p class="erisolsprite">ERISOLSPRITE: dude, 2neeze iintwwo your fuckin 2houlder or 2omethiing.</p>
<p class="erisolsprite">ERISOLSPRITE (neutral): arent you done beiin allergiic twwo your2elf?</p>
hide erisolsprite with slideoutright


show gcatav mischievous onlayer talksprites at right with slideinright
<p class="gcatav">GCATAV: i MEAN,</p>
<p class="gcatav">GCATAV (mischievous): *sNIFF*</p>
<p class="gcatav">GCATAV (mischievous): i FEEL LIKE i'M DOING PRETTY GOOD, oN THE NOT BEING ALLERGIC TO MYSELF FRONT,</p>
<p class="gcatav">GCATAV (mischievous): cOMPARED TO BEFORE,</p>
<p class="gcatav">GCATAV (mischievous): cONSIDERING THAT i HAVE A BUILT-IN MAGICAL AUTOIMMUNE DISORDER WHICH i HAVE NEVERTHELESS MOSTLY TRIUMPHED OVER, dUE TO MY VAST WILLPOWER, aND ALSO BECAUSE EVERYONE YELLED AT ME,</p>
<p class="gcatav">GCATAV (sneeze): aCHOO!</p>
hide gcatav with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
<p class="vriska">VRISKA: As tempting as it sounds to stick around and shoot the shit for a while, I think...</p>
<p class="vriska">VRISKA: I think I need to keep going.</p>
<p class="vriska">VRISKA (adult smiling): I'm kind of on a roll here. Gotta strike while the iron is hot!</p>
hide vriska with slideoutleft


show gcatav subdued onlayer talksprites at right with slideinright
<p class="gcatav">GCATAV: iS THE IRON, iN THE FIRE,</p>
hide gcatav with slideoutright


show vriska adult angry smiling onlayer talksprites at left with slideinleft
<p class="vriska">VRISKA: You fucking know it is!</p>
hide vriska with slideoutleft


show gcatav subdued onlayer talksprites at right with slideinright
<p class="gcatav">GCATAV: tHAT'S COOL,</p>
<p class="gcatav">GCATAV (subdued): iT'S JUST THAT eRISOL AND i HAVE BEEN SORT OF TALKING IT OVER,</p>
<p class="gcatav">GCATAV (subdued): aND IT KIND OF FEELS LIKE THE FIRE IS ABOUT TO GET REALLY REALLY HOT,</p>
<p class="gcatav">GCATAV (subdued): aND MAYBE SPENDING TOO MUCH TIME IN THE FIRE IS GOING TO MAKE YOUR IRON KIND OF MELTED AND FLACCID AND SHITTY, iNSTEAD OF USEFUL, iN THE BLACKSMITHING SENSE THAT'S RELEVANT TO THIS METAPHOR,</p>
<p class="gcatav">GCATAV (subdued): *sNIFF*</p>
hide gcatav with slideoutright


show erisolsprite neutral onlayer talksprites at right with slideinright
<p class="erisolsprite">ERISOLSPRITE: yeah.</p>
hide erisolsprite with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
<p class="vriska">VRISKA: Whaaaaaaaat?</p>
<p class="vriska">VRISKA (adult neutral): No way.</p>
<p class="vriska">VRISKA (adult smiling): These irons are always, always fired.</p>
hide vriska with slideoutleft


show gcatav subdued onlayer talksprites at right with slideinright
<p class="gcatav">GCATAV: wELL, yEAH,</p>
<p class="gcatav">GCATAV (subdued): aND HISTORICALLY SPEAKING-</p>
hide gcatav with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
<p class="vriska">VRISKA: Oh 8lah 8lah 8lah, don't 8e such a pussy.</p>
hide vriska with slideoutleft


show gcatav subdued onlayer talksprites at right with slideinright
<p class="gcatav">GCATAV: i LITERALLY CAN'T NOT BE A CAT,</p>
hide gcatav with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
<p class="vriska">VRISKA: You know what I mean.</p>
<p class="vriska">VRISKA (adult smiling): I've just gotta get in there and make this shit happen.</p>
<p class="vriska">VRISKA (adult proud): I pretty much AM the fire!</p>
<p class="vriska">VRISKA (adult neutral): How 8ad could it even 8e?</p>
hide vriska with slideoutleft


show gcatav subdued still onlayer talksprites at right with slideinright
<p class="gcatav">GCATAV: ,,,</p>
hide gcatav with slideoutright


show erisolsprite neutral still onlayer talksprites at right with slideinright
<p class="erisolsprite">ERISOLSPRITE: ...</p>
hide erisolsprite with slideoutright


show vriska adult neutral still onlayer talksprites at left with slideinleft
<p class="vriska">VRISKA: ........</p>
<p class="vriska">VRISKA (adult neutral): Look, I'm just gonna go ahead and do this thing.</p>
hide vriska with slideoutleft


show erisolsprite neutral onlayer talksprites at right with slideinright
<p class="erisolsprite">ERISOLSPRITE: ok wwell fuck u2 for tryiin ii gue22, havve fun gettiing traumatiized.</p>
hide erisolsprite with slideoutright


show vriska adult angry onlayer talksprites at left with slideinleft
<p class="vriska">VRISKA: I'm not gonna get traumatized!</p>
hide vriska with slideoutleft

$ command = "{{ENTER SCRATCH'S PARLOR}"
menu:
"{plain}[pick] {/plain}[command]":
show white with Dissolve(2.0)
stop music fadeout 3.0
pause 0.5
jump chapter4

# chapter4
$ scratch = True

play music "chapters/4/audio/scrA.ogg" fadein 1.0 volume 0.5 loop
scene bg parlor with Dissolve(3.0)
show doc_scratch onlayer talksprites at right with slideinright
<p class="doc_scratch">DOC_SCRATCH: Well, well.</p>
<p class="doc_scratch">DOC_SCRATCH: Isn't this a perfectly predictable inevitability?</p>
<p class="doc_scratch">DOC_SCRATCH: It certainly has been a while, Vriska. You seem to have blossomed nicely.</p>
<p class="doc_scratch">DOC_SCRATCH: Care for a piece of candy?</p>
hide doc_scratch with slideoutright


show vriska adult angry onlayer talksprites at left with slideinleft
<p class="vriska">VRISKA (adult): Oh fuck your stupid candy, you glo8e-headed little freak.</p>
hide vriska with slideoutleft


show doc_scratch onlayer talksprites at right with slideinright
<p class="doc_scratch">DOC_SCRATCH: I know for a fact you'd enjoy it, but suit yourself.</p>
hide doc_scratch with slideoutright


show vriska adult stoic onlayer talksprites at left with slideinleft
<p class="vriska">VRISKA (adult): Ugh. I had a feeling ages ago that I'd 8e seeing your smug ass again.</p>
hide vriska with slideoutleft


show doc_scratch onlayer talksprites at right with slideinright
<p class="doc_scratch">DOC_SCRATCH: The feeling was mutual.</p>
<p class="doc_scratch">DOC_SCRATCH: Although it was less the wary hunch of a scared little girl than the delightful certainty that you'd come crawling back to me, sooner or later.</p>
<p class="doc_scratch">DOC_SCRATCH: Care to tell me how you've been?</p>
hide doc_scratch with slideoutright


show vriska adult angry jaw drop onlayer talksprites at left with slideinleft
<p class="vriska">VRISKA (adult): What, like you don't know?</p>
hide vriska with slideoutleft


show doc_scratch onlayer talksprites at right with slideinright
<p class="doc_scratch">DOC_SCRATCH: Of course I know. I'm always watching you.</p>
<p class="doc_scratch">DOC_SCRATCH: I just figured I'd lend a little weight to the charade of our reintroduction, and allow you a chance to greet me on your own terms.</p>
<p class="doc_scratch">DOC_SCRATCH: It's only polite.</p>
hide doc_scratch with slideoutright


show vriska adult angry smiling onlayer talksprites at left with slideinleft
<p class="vriska">VRISKA (adult): You know what?</p>
<p class="vriska">VRISKA (adult angry smiling): I've 8een pretty damn good.</p>
<p class="vriska">VRISKA (adult angry smiling): 8een losing track of the sweeps I've spent in here fixing pretty much everything other than the thing I actually came in here to fix, 8ut it's paying off!</p>
hide vriska with slideoutleft


show doc_scratch onlayer talksprites at right with slideinright
<p class="doc_scratch">DOC_SCRATCH: There's a convenient timer for the express purpose of tracking that.</p>
hide doc_scratch with slideoutright


show vriska adult angry onlayer talksprites at left with slideinleft
<p class="vriska">VRISKA (adult): Yeah, and I never look at it 8ecause it pisses me off!</p>
<p class="vriska">VRISKA (adult angry smiling): 8ut it's fine.</p>
<p class="vriska">VRISKA (adult angry smiling): It just means I've had a lot of time to think stuff over.</p>
<p class="vriska">VRISKA (adult angry smiling): Stuff that was holding me 8ack, throwing me off-course.</p>
<p class="vriska">VRISKA (adult angry smiling): Things way more consequential than the 8a8y gru8shit pan-games you used to play with me.</p>
<p class="vriska">VRISKA (adult angry smiling): Honestly, I should 8e surprised to even see you here!</p>
<p class="vriska">VRISKA (adult angry smiling): Really, all you were doing is sticking your stupid flat face into my REAL 8aggage.</p>
hide vriska with slideoutleft


show doc_scratch onlayer talksprites at right with slideinright
<p class="doc_scratch">DOC_SCRATCH: I like to think that I'm far and away the most prolific contributor to your baggage.</p>
hide doc_scratch with slideoutright


show vriska adult angry onlayer talksprites at left with slideinleft
<p class="vriska">VRISKA (adult): You wish!</p>
<p class="vriska">VRISKA (adult angry smiling): Man, I figured may8e this place was working up to something really intense, 8ut instead all I get is Glo8ehead the Gru8toucher playing puppetmaster again.</p>
show vriska at tremble, left
<p class="vriska">VRISKA (adult angry smiling): What a joke!</p>
<p class="vriska">VRISKA (adult angry smiling): You fucked with a 8unch of little kids and 8lew up, then you LOST.</p>
<p class="vriska">VRISKA (adult angry smiling): You could 8arely handle me when I was six, I'm supposed to 8e scared of you NOW?</p>
hide vriska with slideoutleft


show doc_scratch onlayer talksprites at right with slideinright
<p class="doc_scratch">DOC_SCRATCH: Well, you're shaking.</p>
hide doc_scratch with slideoutright

show vriska adult angry onlayer talksprites at shake, left with slideinleft
<p class="vriska">VRISKA: THE F8CK I AM!!!!!!!!</p>
<p class="vriska">VRISKA (adult angry smiling): Shaking with excitement to get you in my rear-view, may8e!</p>
<p class="vriska">VRISKA (adult angry smiling): What is it YOU'RE supposed to teach me?</p>
<p class="vriska">VRISKA (adult angry smiling): How to 8e a creepy little pedophile?</p>
<p class="vriska">VRISKA (adult angry smiling): How to dress and talk like a fucking tool?</p>
<p class="vriska">VRISKA (adult stoic): C'mon!</p>
<p class="vriska">VRISKA (adult stoic): Teach me a lesson!</p>
<p class="vriska">VRISKA (adult angry): F8cking 8RING IT, you 8ald-ass 8ITCH!!!!!!!!</p>
hide vriska with slideoutleft


show doc_scratch onlayer talksprites at right with slideinright
<p class="doc_scratch">DOC_SCRATCH: Exquisite.</p>
<p class="doc_scratch">DOC_SCRATCH: I missed that fumbling braggadocio. It's heartening to know that this place hasn't cured you of it yet.</p>
<p class="doc_scratch">DOC_SCRATCH: It makes you so much fun to play with.</p>
hide doc_scratch with slideoutright

stop music fadeout 0.5
show vriska adult angry onlayer talksprites at center, shrink with slideinleft
play music "chapters/4/audio/scrB.ogg" fadein 0.5 volume 0.5 loop

pause
hide vriska



menu:
"{color=#2CFF4B}{{o} ==>{/color}":
show black with Dissolve(2.0)
scene bg chessboard with Dissolve(2.0)
pause 0.5


$ smol_textbox = True

VRISKA_center "Hey, what the fuck?!"


DOC_SCRATCH_center "There we are."
DOC_SCRATCH_center "Now then, why don't we have ourselves a little game?"


box "{color=#2CFF4B}WHAT WILL YOU DO{/color}{w=0.1}"
scene bg chessboard_glitch
play sfx "chapters/4/audio/whatwillyoudo-scr.ogg" noloop
show glitch_box onlayer talksprites

pause 2.0
scene bg chessboard

hide glitch_box
DOC_SCRATCH_center "Oh no. We won't be needing that."
DOC_SCRATCH_center "Let's get you into your uniform."



show vriska v4 disgusted onlayer talksprites at center, unshrink
scene bg chessboard_vrisgone
VRISKA_center "........"

DOC_SCRATCH_center "Ah, and there she is. My favorite piece."

show vriska v4 frustrated onlayer talksprites at shake, center
VRISKA_center "I'm not your piece!"


DOC_SCRATCH_center "We'll start with a variation of the King's Pawn opening."
DOC_SCRATCH_center "Thief to E4; Thief takes Page."


show vriska v4 frustrated onlayer talksprites at jerkHalfLeft
pause 0.50001
show umber onlayer screens
play sfx "chapters/4/audio/blood-impact1.ogg" noloop
show vriska v4 exploded blood1 at lightshake
pause 0.01
hide umber onlayer screens with Dissolve(1.0)


VRISKA_center "Fuck you!"


DOC_SCRATCH_center "Thief to F5; Thief takes Maid."



show vriska v4 exploded blood1 onlayer talksprites at jerkRight
pause 1.00001
show burgandy onlayer screens
play sfx "chapters/4/audio/blood-impact1.ogg" noloop
show vriska v4 exploded blood2 at lightshake
pause 0.01
hide burgandy onlayer screens with Dissolve(1.0)

VRISKA_center "Stop it!"

DOC_SCRATCH_center "Thief to Z8; Thief takes Seer."



show vriska v4 exploded blood2 onlayer talksprites at jerkLeft
pause 1.00001
show teal onlayer screens
play sfx "chapters/4/audio/blood-impact1.ogg" noloop
show vriska v4 exploded blood3 at lightshake
pause 0.01
hide teal onlayer screens with Dissolve(1.0)

VRISKA_center "Fucking ST8P 8T!!!!!!!!"
VRISKA_center "Z8 ISN'T EVEN A F8CKING P8SITION, YOU HACK!!!!!!!"


DOC_SCRATCH_center "All the world's my board."
DOC_SCRATCH_center "Thief to ∫40; Thief takes pawn."



show vriska v4 exploded blood3 onlayer talksprites at jerkRight
pause 1.00001
show purple onlayer screens
play sfx "chapters/4/audio/blood-impact2.ogg" noloop
show vriska v4 exploded blood4 at lightshake
pause 0.01
hide purple onlayer screens with Dissolve(1.0)

VRISKA_center "ST8P IT!"


DOC_SCRATCH_center "Thief to µ22; Thief takes pawn."


show vriska v4 exploded blood4 onlayer talksprites at jerkLeft
pause 1.00001
show blue onlayer screens
play sfx "chapters/4/audio/blood-impact2.ogg" noloop
show vriska v4 exploded blood5 at lightshake
pause 0.01
hide blue onlayer screens with Dissolve(1.0)

VRISKA_center "F8CK YOU!"


DOC_SCRATCH_center "Thief to α612; Thief takes pawn."



show vriska v4 exploded blood5 onlayer talksprites at jerkRight
pause 1.00001
show green onlayer screens
play sfx "chapters/4/audio/blood-impact3.ogg" noloop
show vriska v4 exploded blood6 at lightshake
pause 0.01
hide green onlayer screens with Dissolve(1.0)


VRISKA_center "I'LL F8CKING K8LL YOU!"

DOC_SCRATCH_center "Thief to Ω413; Thief takes pawn. Check."


show vriska v4 exploded blood6 onlayer talksprites at jerkLeft
pause 1.00001
show red onlayer screens
play sfx "chapters/4/audio/blood-impact3.ogg" noloop
show vriska v4 exploded blood7 at lightshake
pause 0.01
hide red onlayer screens with Dissolve(1.0)
VRISKA_center "YOU'LL 8E SORRY FOR THIS!"
VRISKA_center "YOU'LL 8E F8CKING SORRY!"
VRISKA_center "YOU'RE A CHEAP FUCKING KARMA GHOST,"
VRISKA_center "THIS IS A STUPID FUCKING CHARADE,"
VRISKA_center "NONE OF THIS MEANS SHIT,"
VRISKA_center "AND I'M NEVER GOING TO 8E CAUGHT UP IN YOUR FUCKING G8MES EVER AGAIN!!!!!!!!"



show vriska v4 exploded blood7 at tremble
DOC_SCRATCH_center "Of course you will."
DOC_SCRATCH_center "You think you're better than me? Better than fate?"
DOC_SCRATCH_center "Vriska, I am going to put you in situations where you have the potential to do terrible things."
DOC_SCRATCH_center "I am going to make things ugly."
DOC_SCRATCH_center "I am going to corner you."
DOC_SCRATCH_center "I am going to pressure you."
DOC_SCRATCH_center "And no matter how much “better” you claim to be, all I have to do is catch you at the wrong moment."
DOC_SCRATCH_center "You're one bad turn from burning all your quaint little progress to the ground."
DOC_SCRATCH_center "One lapse away from being mine again."

show vriska v4 sullen at stop_move
VRISKA_center "Get me out of here."
VRISKA_center v4 sullen crying "I want a do-over."


DOC_SCRATCH_center "Oh, please."
DOC_SCRATCH_center "You of all people should know that you don't *get* do-overs."
DOC_SCRATCH_center "The rest of these frivolous little vision quests may feel like sparing you the effort of getting things right the first time around, but the real world doesn't work that way."
DOC_SCRATCH_center "No, you'll just have to endure it. This won't take long."
DOC_SCRATCH_center "You had a good run out there, flying solo and swashbuckling around as if Light itself were yours to command. "
DOC_SCRATCH_center "It'd be wise to remember that it's a borrowed blessing."
DOC_SCRATCH_center "You flourish at its whim."
DOC_SCRATCH_center "Continue to spit in its face and take it for granted, and it will abandon you once again, perhaps for good."

show vriska v4 sullen crying
VRISKA_center "........"


DOC_SCRATCH_center "Do you remember who you were, before it chose you?"
DOC_SCRATCH_center "The choices you made when luck wasn't on your side?"
DOC_SCRATCH_center "You were such a delectable little victim."
DOC_SCRATCH_center "Poor Vriska, with her voracious lusus."
DOC_SCRATCH_center "With her demanding legacy and her uncooperative, fickle little friends."
DOC_SCRATCH_center "So much was out of your hands, then; how could you help but be my lovely assistant?"

show vriska v4 sullen crying eye
VRISKA_center "You didn't fucking own me."

scene bg chessboard_vrisgone_glitch
play sfx "chapters/4/audio/exactly-scr.ogg" noloop volume 0.75
DOC_SCRATCH_center "{image=exactly}"
stop sfx fadeout 1.0
scene bg chessboard_vrisgone

DOC_SCRATCH_center "But what matters is that I might as well have."
DOC_SCRATCH_center "You let yourself believe you had no option other than to take me up on my hard bargains, again and again."
DOC_SCRATCH_center "For all your talk of independence, all your combative posturing and insistence on your own freedom, you barely bothered to put up any actual resistance to my suggestions."
DOC_SCRATCH_center "You took the easy way out, swearing all the while it was your move."
DOC_SCRATCH_center "What a phenomenal waste of your considerable talents."

VRISKA_center "I don't need your compliments."

DOC_SCRATCH_center "It wasn't a compliment."
DOC_SCRATCH_center "It was an insult, and a warning."
DOC_SCRATCH_center "You're a trump card, Vriska, but your potency is a double-edged sword."
DOC_SCRATCH_center "One you've gotten far too comfortable swinging around, in the past."
DOC_SCRATCH_center "What do you intend to fix, when you leave this place?"
DOC_SCRATCH_center "What, I wonder, will you break?"
DOC_SCRATCH_center "I'd encourage you to be mindful of both."
DOC_SCRATCH_center "Of course, you could always cast aside those pesky trivialities and go with the flow, smashing through circumstance with nary a thought for the consequences."
DOC_SCRATCH_center "It'd be easier."
DOC_SCRATCH_center "We could dance together again, just like old times."
DOC_SCRATCH_center "You choose."
DOC_SCRATCH_center "What'll it be, Vriska? Player, or piece?"
DOC_SCRATCH_center "Thief to ∞108."

show vriska v4 sullen crying eye onlayer talksprites at returnToCenterSlow
pause 0.1

show vriska v4 sullen crying eye onlayer talksprites:
returnToCenterSlow
xalign 0.5 yalign 1.0
show vriska_glow onlayer talksprites:
alpha 0.0
pause 0.5
xalign 0.5 yalign 1.0
pulse


pause 1.5
show white onlayer talksprites:
alpha 0.0
pause 1.5
ease 2.0 alpha 1.0


pause 3.0

DOC_SCRATCH_end "I look forward to finding out."
DOC_SCRATCH_end "Good luck."




hide vriska_glow
hide vriska
stop music fadeout 3.0


$ scratch = False
$ smol_textbox = False
scene bg vriskaroom
hide white with Dissolve(2.0)
play music "chapters/4/audio/erisol.wav" fadein 1.0 volume 0.5 loop
show vriska adult sad onlayer talksprites at left
with Dissolve(3.0)
pause 3.0

show erisolsprite smirking onlayer talksprites at right with slideinright
<p class="erisolsprite">ERISOLSPRITE: oh you totally got traumatiized.</p>

hide vriska with slideoutleft
hide erisolsprite with slideoutright
$ command = "{{Level Complete!}"

menu:
"{plain}[pick] {/plain}[command]":
stop music fadeout 3.0
show white with Dissolve(2.0)
play sfx "audio/vris_level.wav" volume 0.75 noloop 
scene bg level_complete_4 with Dissolve(1.0)
pause
show white with Dissolve(1.0)
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
