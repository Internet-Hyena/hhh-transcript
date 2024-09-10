define VRISKA = Character("VRISKA", what_color='#005682', image="vriska", what_prefix="VRISKA: ", window_xoffset=165, window_yoffset=-10)

define VRISKA_center = Character("VRISKA", what_color='#005682', image="vriska", what_prefix="VRISKA: ", window_yoffset=-10)

image vriska:
    xoffset -100
    "chapters/1/characters/vriska/vriska_neutral1.png"
    pause 0.25
    "chapters/1/characters/vriska/vriska_neutral2.png"
    pause 0.25
    repeat

image vriska neutral:
    xoffset -100
    Image("chapters/1/characters/vriska/vriska_neutral1.png")
    pause 0.25
    Image("chapters/1/characters/vriska/vriska_neutral2.png")
    pause 0.25
    repeat

image vriska idle:
    xoffset -100
    "chapters/1/characters/vriska/vriska_neutral1.png"

image vriska smiling:
    xoffset -100
    "chapters/1/characters/vriska/vriska_smiling1.png"
    pause 0.25
    "chapters/1/characters/vriska/vriska_smiling2.png"
    pause 0.25
    repeat

image vriska smug:
    xoffset -220
    "chapters/1/characters/vriska/vriska_smug1.png"
    pause 0.25
    "chapters/1/characters/vriska/vriska_smug2.png"
    pause 0.25
    repeat

image vriska angry:
    xoffset -75
    "chapters/1/characters/vriska/vriska_angry1.png"
    pause 0.045
    "chapters/1/characters/vriska/vriska_angry2.png"
    pause 0.045
    "chapters/1/characters/vriska/vriska_angry3.png"
    pause 0.045
    "chapters/1/characters/vriska/vriska_angry4.png"
    pause 0.045
    "chapters/1/characters/vriska/vriska_angry5.png"
    pause 0.045
    "chapters/1/characters/vriska/vriska_angry6.png"
    pause 0.045
    repeat

image vriska sad:
    xoffset -100
    "chapters/1/characters/vriska/vriska_sad1.png"
    pause 1.0
    "chapters/1/characters/vriska/vriska_sad2.png"
    pause 0.25
    "chapters/1/characters/vriska/vriska_sad3.png"
    pause 0.083
    "chapters/1/characters/vriska/vriska_sad4.png"
    pause 0.083
    "chapters/1/characters/vriska/vriska_sad5.png"
    pause 0.083
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
