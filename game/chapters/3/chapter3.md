init python:
build.archive("chapter3", "all")
build.classify('game/chapters/3/**', 'chapter3')

image bg spidermom_pit:
size (950,650) yalign 0.5 xalign 0.5
"chapters/3/images/spidermom_pit.png"

image bg web:
size (950,650) yalign 0.5 xalign 0.5
"chapters/3/images/web.png"

image bg level_complete_3:
size (950,650) yalign 0.5 xalign 0.5
"chapters/3/images/level_complete_1.png"
pause 0.05
"chapters/3/images/level_complete_2.png"
pause 0.05
"chapters/3/images/level_complete_3.png"
pause 0.05
repeat

label chapter3_prologue:

scene black

show white with Dissolve(1.0)

"YEAR 4" (window_yalign=0.5, window_yoffset=0, window_xsize=150, window_ysize=75, window_ypos=0.5)

scene bg vriskaroom with Dissolve(3.0)

play music "chapters/3/audio/nana.wav" fadein 1.0 volume 0.5 loop

show nannasprite neutral onlayer talksprites at right with slideinright
NANNASPRITE "Oh there you are!"
NANNASPRITE "Feeling like you're getting your lucky mojo back again?"
hide nannasprite with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
VRISKA "Not really. ::::/"
VRISKA "8ut everyone has 8een trying so hard to cheer me up, I thought I'd give it another try."
hide vriska with slideoutleft


show nannasprite neutral onlayer talksprites at right with slideinright
NANNASPRITE "Tell Nanna about it, you know how I love a good bit of girl talk."
hide nannasprite with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
VRISKA "I don't want to 8ore you, it's just the same pro8lem as always."
VRISKA adult sad "Finally I get my sea legs and figured out what this whole process is a8out, 8reeze through Eridan and John and Kanaya, only to get stuck all over again on HER."
hide vriska with slideoutleft


show nannasprite neutral onlayer talksprites at right with slideinright
NANNASPRITE "Well I am sure there is some common thread, every trial you face is designed to better prepare you for the next."
hide nannasprite with slideoutright


show vriska adult sad onlayer talksprites at left with slideinleft
VRISKA "I'm not so sure........she's different from the rest of them. And no matter how I approach this, I can't figure out what the hell she wants."
hide vriska with slideoutleft


show nannasprite neutral onlayer talksprites at right with slideinright
NANNASPRITE "You'll figure it out sooner than you expect, deary! I have the utmost faith in you."
hide nannasprite with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
VRISKA "Thanks Nannasprite! Honestly having you and Nannasprite 2 here has made this whole experience way more 8earable."
hide vriska with slideoutleft


show nannasprite giggle onlayer talksprites at right with slideinright
NANNASPRITE "You know what they say, flattery will get you all the cookies two lovely aged blue ladies can fit in one oven."
hide nannasprite with slideoutright


show vriska adult smiling onlayer talksprites at left with slideinleft
VRISKA "Hell yeeeeeeees!!!!!!!!"
VRISKA "It's funny thinking 8ack on it, John and I actually had a conversation a8out you sweeps ago."
VRISKA adult smiling "We kind of 8onded over how, past our cultural differences, we shared this same experience of connecting to our predecessors through their writings."
VRISKA "I'm glad he finally got to meet you. I hope he appreci8ted every minute of it!"
hide vriska with slideoutleft


show nannasprite giggle onlayer talksprites at right with slideinright
NANNASPRITE "Oh ho, I'd like to think so!"
NANNASPRITE neutral "I miss that boy, he could be such a pill at times but we had some lovely chats. Always sung his heart out during our little “jam seshs,” too."
hide nannasprite with slideoutright


show vriska adult smiling onlayer talksprites at left with slideinleft
VRISKA "Doooooooork! Can you 8elieve he has his own little progeny now, strutting his shit in that same oddly secure, self-assured way?"
VRISKA "I wonder how those kids are doing right now........"
VRISKA "What exactly do humans get out of these familial prim8 relationships, anyway?"
VRISKA "Is it a chemical manipulation thing?"
hide vriska with slideoutleft


show nannasprite neutral onlayer talksprites at right with slideinright
NANNASPRITE "Some would say so, and of course there is some truth to that."
NANNASPRITE "That said, it's hardly the whole story... People are much too concerned with trying to boil down these kinds of marvelous profundities to cold hard facts."
NANNASPRITE giggle "I'd go blue in the face trying to lay out every rhyme and flimsy whimsy a person could have for baking up a brood, hoo hoo!"
hide nannasprite with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
VRISKA "You prolifer8ed yourself though, right? Why?"
hide vriska with slideoutleft


show nannasprite neutral onlayer talksprites at right with slideinright
NANNASPRITE "Hm. There was a beautiful sense of novelty to it, I suppose."
NANNASPRITE "Like both John and you, my role model was my own tome of japes, left behind by my dearly departed adoptive father."
NANNASPRITE "It never sat right with me, how limited my experience with actual humans was."
NANNASPRITE "I couldn't exactly bring that man back from the dead, but I could put myself in his shoes and do the bang up job he never had the opportunity to do. Not to mention, I like babies! :B"
hide nannasprite with slideoutright



show vriska adult smiling onlayer talksprites at left with slideinleft
VRISKA "That's it?"
VRISKA adult angry "I don't know, couldn't you have done anything else? What's so special a8out 8a8ies? I saw one in passing and they're weird as hell! Rose told me they even pee their damn pants!"
hide vriska with slideoutleft


show nannasprite giggle onlayer talksprites at right with slideinright
NANNASPRITE "They sure do! Sometimes, they'll even pee on you too."
hide nannasprite with slideoutright


show vriska adult jaw drop onlayer talksprites at left with slideinleft
VRISKA "They pee ON people!"
VRISKA " What........"
VRISKA adult neutral "That sounds like a nightmare."
hide vriska with slideoutleft


show nannasprite giggle onlayer talksprites at right with slideinright
NANNASPRITE "It is! One time my son laughed at me as it was happening!"
hide nannasprite with slideoutright


show vriska adult angry onlayer talksprites at left with slideinleft
VRISKA "Uuuuuuuugh!!!!!!!!"
hide vriska with slideoutleft


show nannasprite giggle onlayer talksprites at right with slideinright
NANNASPRITE "He was right, though. It was funny."
hide nannasprite with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
VRISKA "So that was it? There wasn't anything else you wanted in life? You were fine with pee?"
hide vriska with slideoutleft


show nannasprite neutral onlayer talksprites at right with slideinright
NANNASPRITE "Well I was fairly enamored of the idea of getting even, once upon a time."
NANNASPRITE "So many nights spent plotting that awful woman's downfall and making her pay for all the indignities of my childhood. For always making me feel like I was powerless to do anything. "
NANNASPRITE "For a while I even thought it was my fate!"
hide nannasprite with slideoutright


show vriska adult angry smiling onlayer talksprites at left with slideinleft
VRISKA "Yessssssss! That's what I'm fucking talking a8out!"
hide vriska with slideoutleft


show nannasprite neutral onlayer talksprites at right with slideinright
NANNASPRITE "Hush up now, none of that! Fantasizing about all that even after my own death and resurrection is absurd!"
NANNASPRITE "Not to mention that now, after seeing what my younger self has gotten up to in this realm, I clearly underestimated the depth of my own desires."
hide nannasprite with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
VRISKA "C'mon, we're not doing this again. You can't keep comparing yourself to her! She's a freak and you're like the least freakish person I've ever met."
hide vriska with slideoutleft


show nannasprite serious onlayer talksprites at right with slideinright
NANNASPRITE "I'm not trying to get down on myself, deary, it's simply a fact of reality. I'll never know if any of my schemes coming to fruition would have left me satisfied, and now I highly doubt it!"
NANNASPRITE serious "The past is always going to be the past."
hide nannasprite with slideoutright


show vriska adult sad onlayer talksprites at left with slideinleft
VRISKA "..."
hide vriska with slideoutleft


show nannasprite neutral onlayer talksprites at right with slideinright
NANNASPRITE "It's all a bit embarrassing, really... All that said, watching your progress these past few years has inspired me to frame the whole debacle a bit differently."
hide nannasprite with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
VRISKA "Oh?"
hide vriska with slideoutleft


show nannasprite serious onlayer talksprites at right with slideinright
NANNASPRITE "I had always wanted Betty Crocker to know what a mistake it was to steal my life, my potential, from me."
NANNASPRITE serious "But the real issue was that not once during my childhood did I ever feel particularly wanted, or welcomed, into the world. I only had my brother, and even he ran off on me!"
NANNASPRITE "Yet despite that fact, and the anger and the disappointment, I still raised someone who knew what it was like to be loved."
NANNASPRITE "I never once questioned choosing my son over some run of the mill escapade or rousing romp. And while in my twilight years of retired spritehood, I have often pondered the “could be.”"
NANNASPRITE neutral "Seeing that choice isn't innate to every iteration of Jane Crocker has assured me that I did indeed fulfill a path of potential to its fullest degree. I'm grateful to her for that... marginally."
hide nannasprite with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
VRISKA "I guess that makes sense. Weren't you worried, though? That you weren't following the right path, or living up to your destiny?"
hide vriska with slideoutleft


show nannasprite giggle onlayer talksprites at right with slideinright
NANNASPRITE "I never even considered that, hoo hoo!"
NANNASPRITE neutral "Is that how you kids think these days? My lord, no wonder none of you go outside anymore."
hide nannasprite with slideoutright


show vriska adult angry onlayer talksprites at left with slideinleft
VRISKA "Don't p8tronize me, old lady! Destiny's the found8tion of my godhood!"
hide vriska with slideoutleft


show nannasprite neutral onlayer talksprites at right with slideinright
NANNASPRITE "True. I am only a simple elderly woman, stand-mixed with the unknowable secrets of the universe and a one-armed clown doll. But from experience, I would still argue that destiny mostly fulfills itself."
NANNASPRITE wink "There are many more important things you should focus on, such as getting the heck out of here!"
hide nannasprite with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
VRISKA "Wow, I've 8een pep-talked and I didn't even realize it. You have a point, though... It's not like I have any other plan 8ut to keep trying."
VRISKA adult sad "Also, sorry for getting snippy there. <::::("
hide vriska with slideoutleft


show nannasprite neutral onlayer talksprites at right with slideinright
NANNASPRITE "Don't fret over it dear, a blue gentlewoman appreciates a bit of bite to her compeers."
hide nannasprite with slideoutright


show vriska adult smiling onlayer talksprites at left with slideinleft
VRISKA "See Nannasprite, you're the only one that gets it. You're a real one."
hide vriska with slideoutleft


show nannasprite giggle onlayer talksprites at right with slideinright
NANNASPRITE "DAMN right I am."
hide nannasprite with slideoutright

show vriska adult smiling onlayer talksprites at left with slideinleft
VRISKA "Woah, getting crazy now."
hide vriska with slideoutleft

show nannasprite giggle onlayer talksprites at right with slideinright
NANNASPRITE "Tee hee! <;B"
hide nannasprite with slideoutright

show vriska adult proud onlayer talksprites at left with slideinleft
VRISKA "<33333333"
hide vriska with slideoutleft

$ command = "{{Choose Mindfang's Journal.}"
menu:
"{plain}[pick] {/plain}[command]":
show white with Dissolve(2.0)
stop music fadeout 3.0
pause 0.5
jump chapter3

label chapter3:
$ command = "{{????????}"
menu:
"{plain}[pick] {/plain}[command]":
show black with Dissolve(2.0)
scene bg web with Dissolve(2.0)
pause 0.5

play music "chapters/3/audio/ch3.wav" fadein 0.2 volume 1.5 loop



show mindmom blue silhouette onlayer talksprites at right with slideinright
MINDMOM "The girl was thrown into emptiness."
MINDMOM "Despite the darkness, the space wasn't foreign. The way the moons hung in the sky, the sound of the waves as they crashed, the 8reeze, these were all familiar sens8tions."
MINDMOM "As was the figure 8efore her. Though she had only ever seen it 8ehind her eyes, its form was shaped 8y words."
hide mindmom with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
VRISKA "You can drop the ominous 8uild up, I already know the twist."
hide vriska with slideoutleft


show mindmom mindfang neutral onlayer talksprites at right with slideinright
MINDMOM "Oh? Had the thief 8een here 8efore?"
hide mindmom with slideoutright


show vriska adult stoic onlayer talksprites at left with slideinleft
VRISKA "Yep! In 8rief summary, at least once a week for the last 2 years."
VRISKA "8roaching every kind of chit chat that goes a8solutely nowhere."
VRISKA "The whole endeavor usually ends with me either killing you or... feeding myself to you."
VRISKA angry smiling "And for some reason, you talk like a 8ook. Which is a huge head8che, 8y the way!"
hide vriska with slideoutleft


show mindmom mindfang back onlayer talksprites at right with slideinright
MINDMOM "Well she was a 8ook, our esteemed narr8tor. That's how Vriska knew her, at any r8te. And unlike a certain someone, she knew the value of showmanship."
hide mindmom with slideoutright


show vriska adult angry smiling onlayer talksprites at left with slideinleft
VRISKA "Yeah, you really shook me the first time around."
VRISKA "You were all like, “Surprise, 8itch. I'm 8oth the Marquise, and your lusus!” And I fell str8 on my ass, flipping the fuck out like a 8ig tool."
VRISKA stoic "8ut FYI, after the last hundred or so reveals, it just comes off as trying waaaaaaaay too hard."
hide vriska with slideoutleft


show mindmom mindfang thinking annoyed onlayer talksprites at right with slideinright
MINDMOM "Hmph!"
hide mindmom with Dissolve(0.5)









show bg at Shake((0,0,0,0), 3.0, dist=10)

play sfx "chapters/3/audio/squelch.mp3" noloop
scene bg spidermom_pit with Dissolve(3.0)

show vriska adult stoic onlayer talksprites at left with slideinleft
VRISKA "Hi Momfang."
VRISKA "It's 8een a 8it. How are you?"
hide vriska with slideoutleft


show mindmom mindfang back onlayer talksprites at right with slideinright
MINDMOM "The spider did not pause to find an answer; she already had one."
MINDMOM momfang back "“HUNGRY. KILL. EAT. SHIT. DEATH.”"
hide mindmom with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
VRISKA "So same as usual! Awesome. Glad to hear it."
VRISKA "So what's on the agenda this time? Do NOT say revisiting how I found that old journal, or my first feeding."
hide vriska with slideoutleft


show mindmom mindfang thinking annoyed onlayer talksprites at right with slideinright
MINDMOM "Would the spiderling prefer returning to the day she got stuck in this we8 and had to eat her way out?"
hide mindmom with slideoutright


show vriska adult angry onlayer talksprites at left with slideinleft
VRISKA "No!!!!!!!! I do NOT want to 8e a kid again, period."
hide vriska with slideoutleft


show mindmom holding spider head onlayer talksprites at right with slideinright
MINDMOM "What a8out the day her lusus died?"
hide mindmom with slideoutright


show vriska adult angry onlayer talksprites at left with slideinleft
VRISKA "Done that! Sick of it! I always almost drown in 8lood, and it makes the whole canyon smell terri8le."
VRISKA "It's 8ad enough 8eing stuck 8ack in this place. If you go down memory lane again, I'm jumping."
hide vriska with slideoutleft


show mindmom mindfang neutral onlayer talksprites at right with slideinright
MINDMOM "The girl was 8linded 8y her pup8ed angst. As 8efouled as those we8s were, this gossamer carnage had 8een home, once. Her time here made her who she was."
hide mindmom with slideoutright


show vriska adult stoic onlayer talksprites at left with slideinleft
VRISKA "Is that why we're here, in argua8ly one of my least favorite places to exist?"
VRISKA "Instead of telling me my own origin story, can we skip to the end where I clear this shit once and for all and move on to someone that matters?"
hide vriska with slideoutleft


show mindmom mindfang thinking annoyed onlayer talksprites at right with slideinright
MINDMOM "The Thief's request was denied 8y the narr8tor, who wondered if it would kill the younger Serket to colla8or8. Had she not once intric8ley woven her own daring campaigns? What happened to that thespian vivacity?"
hide mindmom with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
VRISKA "I don't know if it's a f8tal symptom of watching the sweeps go 8y, 8ut FLARPing isn't as fun anymore. A lot of energy and drama for nothing."
hide vriska with slideoutleft


show mindmom mindfang thinking annoyed onlayer talksprites at right with slideinright
MINDMOM "That statement was so un8elieva8le as to 8e almost insulting. Who could deny a little drama? Everyone appreci8ted a good game. Especially the girl."
hide mindmom with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
VRISKA "Ok, yes, I am attached to the struggle. 8ut 8ack then, all that satisf8ction was pretty short lived."
VRISKA adult sad "Every win, I had to share with her. Every moment, I felt her w8ting for me. It feels 8ad, not getting a choice when you do all the fucking work."
hide vriska with slideoutleft


show mindmom mindfang neutral onlayer talksprites at right with slideinright
MINDMOM "When we were sailing the high seas, we did not exhaust our exploits with self indulgent contrition."
MINDMOM "Daily we made 8ets with death, and whichever faulty panlo8es occasionally sparked empathetic were rightly silenced, that we might revel in our winnings undistur8ed. We have always taken what we wanted "

hide mindmom with slideoutright


show vriska adult sad onlayer talksprites at left with slideinleft
VRISKA "Sure, the 8ooty was gr8, up until the point where there was no one left to play with. After that, it was all as good as gar8age."
hide vriska with slideoutleft


show mindmom mindfang back onlayer talksprites at right with slideinright
MINDMOM "That spoke to a pro8lem with the girl's mindset. Trolls died. On a planet 8uilt to 8reed killers, was that such a 8ad thing?"
MINDMOM "Little spider8ite 8eat them all. Not 8ecause she was talented, or smart, or particularly strong, though she was all of those things. It was 8ecause she learned the rules 8efore anyone else did. "

hide mindmom with slideoutright


show vriska adult stoic onlayer talksprites at left with slideinleft
VRISKA "So I'm only alive thanks to you? 8ecause you were just that necessary and important?"
hide vriska with slideoutleft


show mindmom mindfang back onlayer talksprites at right with slideinright
MINDMOM "It was true."
MINDMOM momfang back "“GRU8.”"
hide mindmom with slideoutright


show vriska adult angry smiling onlayer talksprites at left with slideinleft
VRISKA "8ZZZZZZZZT WRONG! I'm not falling for that hoofshit again."
VRISKA "I've already tried respecting you for making me the 8est, 8ut you know what I'm realizing?"
VRISKA "I didn't have to go through aaaaaaaall of THAT to 8e strong. Vrissy didn't!"
VRISKA adult angry "Even growing up in a f8ke world where no one has a spine, and with 8arely any guidance, her powers can do things mine can't."
VRISKA adult angry smiling "So what silver lining is left, honestly?"
hide vriska with slideoutleft


show mindmom mindfang silent onlayer talksprites at right with slideinright
MINDMOM "........"
hide mindmom with slideoutright


show vriska adult angry smiling onlayer talksprites at left with slideinleft
VRISKA "8ut that's the point, right?"
VRISKA "There is no p8sitive spin, no learning to appreci8 you, 8ecause even 8y Alternian st8ndards you sucked!"
VRISKA adult angry "You weren't a cust8dian, you were a responsi8ility."
VRISKA "I protected you, I c8red for you, and you would have happily killed me the moment things didn't go your w8y."
hide vriska with slideoutleft


show mindmom mindfang thinking annoyed onlayer talksprites at right with slideinright
MINDMOM "And?"
hide mindmom with slideoutright


show vriska adult jaw drop onlayer talksprites at left with slideinleft
VRISKA "Th8t's not fucking norm8l!!!!!!!"
hide vriska with slideoutleft


show mindmom holding mindfangs head onlayer talksprites at right with slideinright
MINDMOM "It was for a spider."
hide mindmom with slideoutright


show vriska adult sad onlayer talksprites at left with slideinleft
VRISKA "God, you're insuffera8le!!!!!!!!"
VRISKA "I had one place I was supposed to feel safe."
VRISKA adult angry "Why did you h8ve to 8e everything wrong with the w8rld, rolled into one terri8le monster?"
hide vriska with slideoutleft


show mindmom holding mindfangs head onlayer talksprites at right with slideinright
MINDMOM "The spider has no answer to that. She has never once thought of her own n8ture. She has only ever lived and devoured."
MINDMOM momfang back "\"HUNGRY. KILL. FUCK. EAT. FEED.\""
hide mindmom with slideoutright


show vriska adult angry onlayer talksprites at left with slideinleft
VRISKA "I KN8W YOU'RE HUNGRY! What a8out me? My entire gru8hood, I gave and you took. F8r once, what a8out what I w8nt?!"
hide vriska with slideoutleft


show mindmom momfang thinking annoyed onlayer talksprites at right with slideinright
MINDMOM "She has never considered this."
MINDMOM momfang thinking annoyed "And wasn't considering it now, to 8e clear."
MINDMOM momfang thinking annoyed "8ut the narr8tor was curious, what DID the spiderling want from the monster?"
MINDMOM momfang thinking annoyed "To hear her say “THANK YOU” for the young girl's service, for her to 8e “SORRY\"?"
hide mindmom with slideoutright


show vriska adult angry onlayer talksprites at left with slideinleft
VRISKA "What I w8nt is for you to go 8ack in time and pr8tect that fucking kid, like you were supposed to!!!!!!!!"
VRISKA "If you did, may8e I'd 8e a8le to relax and let my f8cking guard down for ONCE, instead of const8ntly ruining things and thinking everyone is going to turn around and kill me!"
VRISKA adult neutral "Oh my god."
VRISKA adult angry "Tavros was right!!!!!!!!"
hide vriska with slideoutleft


show mindmom momfang back onlayer talksprites at right with slideinright
MINDMOM "\"FOOD?\""
hide mindmom with slideoutright


show vriska adult angry onlayer talksprites at left with slideinleft
VRISKA "Sh8t the f8ck up!!!!!!!!"
VRISKA "Now I get why talking to all my friends finally led up to you."
VRISKA "Y8u're the reason why I could never trust any8ody!"
VRISKA adult sad "Even h8r!!!!!!!! Especi8lly her."
VRISKA "I was so terrified of getting it wrong, so I'm stuck following in the footsteps 8f the M8rquise."
hide vriska with slideoutleft


show mindmom mindfang thinking annoyed onlayer talksprites at right with slideinright
MINDMOM "And what, thought our intrepid narr8tor, was so 8ad a8out that? She'd always seen herself a comfort to the young troll."
MINDMOM momfang thinking annoyed "She taught her descendant so much, and in such lurid detail."
hide mindmom with slideoutright


show vriska adult angry onlayer talksprites at left with slideinleft
VRISKA "It was 80%% smut!!!!!!!!"
hide vriska with slideoutleft


show mindmom mindfang neutral onlayer talksprites at right with slideinright
MINDMOM "It was a well written, one-of-a-kind historical document that mapped out all the swash8uckling majesty of a 8rilliant woman's destiny."
hide mindmom with slideoutright


show vriska adult angry smiling onlayer talksprites at left with slideinleft
VRISKA "Of course you'd s8y that, you wr8te it!"
VRISKA "8ut sure, y8u helped keep me alive, and m8de me a wicked pir8. Unfortun8tely, it made everyone else h8 me!"
VRISKA adult sad "I could have 8een any8ody... and you took that aw8y from me. You made me afraid of it."
hide vriska with slideoutleft


show mindmom momfang back onlayer talksprites at right with slideinright
MINDMOM "“STUPID. STUPID. STUPID. STUPID. STUPID. STUPID. STUPID. STUPID.”"
MINDMOM momfang thinking annoyed "The girl has to 8e reminded, she is not special."
MINDMOM momfang thinking annoyed "She is not the victim of some gr8 tragedy."
MINDMOM momfang thinking annoyed "She is an apex predator. A 8iological, existential threat to all those that cross her path. She thought showing weakness would have solved all her pro8lems? Those irrelevant victims she spent so much time mourning didn't want her companionship."
MINDMOM momfang thinking annoyed "They wanted to make new holes inside of her, to ensure their own survival."
MINDMOM momfang back "“IDIOT.”"
hide mindmom with slideoutright


show vriska adult angry onlayer talksprites at left with slideinleft
VRISKA "Stop it, I don't want to think like that anymore!!!!!!!!"
hide vriska with slideoutleft


show mindmom mindfang neutral onlayer talksprites at right with slideinright
MINDMOM "It was the girl's 8irthright to 8e voracious and awful. Those 8lueprints could not 8e a8andoned. The spider, the narr8tor, the child, they were all looking into the same mirror."
MINDMOM momfang back "“TRAPPED.”"
hide mindmom with slideoutright


show vriska adult angry onlayer talksprites at left with slideinleft
VRISKA "PLEASE!!!!!!!! I kn8w, 8k!?"
VRISKA adult angry "Why didn't you just st8y de8d!!!!!!!! Why didn't I k8ll y8u s88ner!!!!!!!! I should h8ve s8ved myself 8efore it was too l8!!!!!!!!"
hide vriska with slideoutleft


show mindmom mindfang neutral onlayer talksprites at right with slideinright
MINDMOM "8ut even as she said it, the Thief knew that was never an option."
MINDMOM momfang back "Emancip8tion couldn't 8e granted to either party, only mutually assured destruction."
hide mindmom with slideoutright


show vriska adult jaw drop onlayer talksprites at left with slideinleft
VRISKA "........"
VRISKA adult sad "I wish it had 8een different."
hide vriska with slideoutleft


show mindmom holding spider head onlayer talksprites at right with slideinright
MINDMOM "Impossi8le."
hide mindmom with slideoutright


show vriska adult sad onlayer talksprites at left with slideinleft
VRISKA "I wish I was 8orn some8ody else."
hide vriska with slideoutleft


show mindmom holding mindfangs head onlayer talksprites at right with slideinright
MINDMOM "Another dead end."
hide mindmom with slideoutright


show vriska adult angry onlayer talksprites at left with slideinleft
VRISKA "Fine, fuck!"
VRISKA adult angry "JUST LET M8 GET 8UT FROM UNDER Y8U, THEN! L8T ME 8E MY OWN F8CKING PERSON, F8R ONCE!!!!!!!!"
hide vriska with slideoutleft

box "What will you do?"

show vriska adult sad onlayer talksprites at left with slideinleft
VRISKA "........"
hide vriska with slideoutleft


show mindmom momfang back onlayer talksprites at right with slideinright
MINDMOM "“HUNGRY.”"
hide mindmom with slideoutright


show vriska adult sad onlayer talksprites at left with slideinleft
VRISKA "Huh."
hide vriska with slideoutleft


show mindmom momfang back onlayer talksprites at right with slideinright
MINDMOM "“KILL.”"
hide mindmom with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
VRISKA "You know, every week I come in here trying to figure out what more you could possi8ly want from me, and every week it's the same shit."
VRISKA adult smiling "I really am suuuuuuuuch a moron."
hide vriska with slideoutleft


show mindmom momfang back onlayer talksprites at right with slideinright
MINDMOM "“FEED.”"
hide mindmom with slideoutright


show vriska adult smiling onlayer talksprites at left with slideinleft
VRISKA "Exactly. It was never any deeper than that, the answer was right in front of my face."
VRISKA "Well. I'm not your free meal ticket anymore."
hide vriska with slideoutleft


show mindmom holding spider head onlayer talksprites at right with slideinright
MINDMOM "M8ricide, then?"
hide mindmom with slideoutright


show vriska adult neutral onlayer talksprites at left with slideinleft
VRISKA "Nah."
VRISKA "I never really wanted that either."
hide vriska with slideoutleft


show mindmom momfang thinking annoyed onlayer talksprites at right with slideinright
MINDMOM "Lest the girl forget, there were only two choices."
MINDMOM momfang back "“DIE.”"
hide mindmom with slideoutright


show vriska adult stoic onlayer talksprites at left with slideinleft
VRISKA "8ut that's not true. I'm not a wiggler anymore. Alternia is dead."
VRISKA adult smiling "For once in my life, I have options."
hide vriska with slideoutleft


show mindmom mindfang thinking annoyed onlayer talksprites at right with slideinright
MINDMOM "And just what did the ungrateful little upstart mean 8y that?"
hide mindmom with slideoutright


show vriska adult proud onlayer talksprites at left with slideinleft
VRISKA "I'm glad you asked!"
VRISKA "It means I finally get to walk away from all this. And I'm not going to look 8ack."
hide vriska with slideoutleft


show mindmom holding mindfangs head onlayer talksprites at right with slideinright
MINDMOM "The spider forgot her hunger, for a moment at least, as the reality of such a statement sunk in."
MINDMOM "She was only a spider. She did not fear death, or feel regret, or hold any sadness."
MINDMOM "She never once loved the girl. She did not feel responsi8le."
MINDMOM "That said, the arachnid had grown accustomed to the smaller creature's presence."
MINDMOM "She extended one long, spindly leg 8efore her, towards the young troll."
MINDMOM "As if to say, \"HUG?\""
hide mindmom with slideoutright


show vriska adult stoic onlayer talksprites at left with slideinleft
VRISKA "Oh, a8solutely not."
VRISKA "Hell no."
hide vriska with slideoutleft


show mindmom momfang back onlayer talksprites at right with slideinright
MINDMOM "That proved a good call, as the spider had 100%% planned on eating the girl."
MINDMOM momfang back "Instead, the long lim8 was retracted, placed 8etween the monster's own massive jaws."
stop music fadeout 0.0




play sfx "chapters/3/audio/crunch.mp3" noloop
pause
show mindmom silhouette onlayer talksprites at right with slideinright
MINDMOM "The spider would not notice when the girl turned to leave."
MINDMOM silhouette "And the girl would not turn around to see if she had."
MINDMOM silhouette "The 8ound cover was closed on our trusted narr8tor, as she whispered these final words."
MINDMOM silhouette "“Good luck, Vriska.\n8e assured, you will need it.”"
hide mindmom with slideoutright
play sfx "chapters/3/audio/footsteps.mp3" noloop



$ command = "{{Level Complete!}"
menu:
"{plain}[pick] {/plain}[command]":
show white with Dissolve(2.0)
play sfx "audio/vris_level.wav" volume 0.75 noloop 
scene bg level_complete_3 with Dissolve(1.0)
pause
show white with Dissolve(1.0)
$ multipersist.chapter3_complete= True
$ multipersist.save()
stop music fadeout 3.0
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
