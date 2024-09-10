init python:

    import math
    class Shaker(object):
        
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
        
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            
            self.start = [ self.anchors.get(i, i) for i in start ]  
            self.dist = dist    
            self.child = child
        
        def __call__(self, t, sizes):
            
            
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x
            
            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
            
            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            
            return (int(nx), int(ny), 0, 0)

    def _Shake(start, time, child=None, dist=100.0, **properties):
        
        move = Shaker(start, child, dist)
        return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

    def _ShakeObj(time, child=None, dist=100.0, **properties):
        
        move = Shaker(start=None, child=child, dist=dist)
        return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)


    Shake = renpy.curry(_Shake)
    sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    ShakeObj = renpy.curry(_ShakeObj)


style box is window
style box:
    yalign 0.5
    xalign 0.5
    yoffset 0
    xsize gui.textbox_width
    ysize gui.textbox_height

style big_box is box
style big_box:
    xsize int(gui.textbox_width * 1.1)
    ysize int(gui.textbox_height * 1.1)

style bigger_box is box
style bigger_box:
    xsize int(gui.textbox_width * 1.6)
    ysize int(gui.textbox_height * 1.6)

style biggest_box is box
style biggest_box:
    xsize int(gui.textbox_width * 1.6)
    ysize int(gui.textbox_height * 1.6)

define box = Character("box", color='#000000', what_color='#000000', what_xalign=0.5, what_yalign=0.5, what_textalign = 0.5, window_style="box")

define bigBox = Character("box", kind=box, window_style="big_box", what_size=(25))

define biggerBox = Character("box", kind=box, window_style="bigger_box", what_size=(30))

define biggestBox = Character("box", kind=box, window_style="biggest_box", what_size=(50))

transform tremble:
    alpha 1.0 yoffset 0
    choice:
        block:
            ease_bounce 0.05 xoffset 2
            ease_bounce 0.05 xoffset -2
            repeat 2
        block:
            choice:
                ease_bounce 0.05 xoffset 2
                ease_bounce 0.05 xoffset -2
                repeat 2
            choice:
                ease_bounce 0.05 xoffset 2
                ease_bounce 0.05 xoffset -2
                ease_bounce 0.05 xoffset 2
                repeat
    ease_bounce 0.3 yoffset 0
    repeat

transform jerkTopRight:

    pause 0.01
    xalign 0.5 yalign 1.0
    easeout 0.2 xalign 1.5 yalign -1.0
    pause 0.1
    easeout 0.1 xalign 0.5 yalign 1.0

transform jerkTopLeft:
    xalign 0.5 yalign 1.0
    easeout 0.2 xalign -0.5 yalign -1.0
    pause 0.1
    easeout 0.1 xalign 0.5 yalign 1.0

transform jerkTopMiddle:
    xalign 0.5 yalign 1.0
    easeout 0.1 yalign -1.0
    pause 0.1
    easeout 0.07 yalign 1.0

transform knightMoveRight:
    xalign 0.5 yalign 1.0
    easeout 0.1 xalign 1.0
    pause 0.1
    easeout 0.1 yalign -1.1
    pause 0.1
    easeout 0.07 xalign 0.5 yalign 1.0

transform knightMoveLeft:
    xalign 0.5 yalign 1.0
    easeout 0.1 xalign 0.0
    pause 0.1
    easeout 0.1 yalign -1.1
    pause 0.1
    easeout 0.07 xalign 0.5 yalign 1.0

transform moveAllOver(s=0.1, r=100):

    choice:
        easeout s xalign 0.9 yalign 0.7
        pause 0.01
        easeout s xalign 0.2 yalign 0.2
        pause 0.01
    choice:
        easeout s xalign 0.5 yalign -1.0
        pause 0.01
        easeout s xalign 0.0 yalign 0.0
        pause 0.01
    choice:
        easeout s xalign 0.0 yalign 1.0
        pause 0.01
        easeout s xalign 0.8 yalign -0.7
        pause 0.01
    pause 0.1
    repeat r
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
