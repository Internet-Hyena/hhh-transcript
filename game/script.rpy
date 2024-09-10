






define multipersist = MultiPersistent("hyperbolic-helltier-chamber.beyondcanon.com")

define narrator = Character("", color='#000000', what_color='#000000', what_xalign=0.5, what_yalign=0.5, what_textalign = 0.5, window_yoffset=-25, window_ysize=150)

init python:
    pick = "{color=#000000}>{/color}"
    quick_menu = True

image black = Solid("#000000")
image white = Solid("#FFFFFF")

image bg mspa = Composite(
    (950,650),
    (0,0), Solid("#C6C6C6"),
    (150, 0), Solid("#EEEEEE"),
    (800, 0), Solid("#C6C6C6"))
image bg vriskaroom:
    xalign 0.5
    yalign 0.5
    Image("images/vriskaroom.png")
image bg tavroscliff:
    size (950,650) yalign 0.5 xalign 0.5
    "images/tavroscliff.png"

transform shake:
    xalign 0.5
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    xoffset 0 xalign 0.5
    repeat 3

label after_load:
    $ renpy.set_physical_size((950, 650))

label splashscreen:
    $ quick_menu = True
    scene bg mspa

    jump chapter1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
