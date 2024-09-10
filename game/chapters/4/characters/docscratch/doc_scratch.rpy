init python:
    def doc_callback(event, interact=True, **kwargs):
        if not interact:
            return
        if event=="begin" or event == "show":
            renpy.sound.play("chapters/4/audio/typingloop.ogg", channel='sound', relative_volume=0.5, loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()


define DOC_SCRATCH = Character("DOC_SCRATCH",
                              what_color='#FFFFFF',
                              image="doc_scratch",
                              window_xoffset=-165,
                              window_yoffset=-10,
                              what_slow_cps=18,
                              what_outlines=[ ( 3, "#003700", 0, 0) ],
                              what_line_overlap_split=2,
                              what_line_leading=4,
                              callback=doc_callback)
define DOC_SCRATCH_center = Character("DOC_SCRATCH_center", kind=DOC_SCRATCH,
                                     what_outlines=[ ( 3, "#2ed73a", 0, 0) ],
                                     window_xoffset=0,
                                     window_yoffset=0,
                                     what_line_overlap_split=1,
                                     what_xalign=0.5,
                                     window_xalign=0.5,
                                     window_yalign=0.05,
                                     what_textalign=0.5,
                                     what_text_align=0.5,
)
define DOC_SCRATCH_end = Character("DOC_SCRATCH_center", kind=DOC_SCRATCH_center,
                                     window_yalign=0.5,
                                     what_size=30,
)

image doc_scratch:
    "chapters/4/characters/docscratch/scratch_1.png"
    pause 10.0
    "chapters/4/characters/docscratch/scratch_2.png"
    pause 0.05
    "chapters/4/characters/docscratch/scratch_3.png"
    pause 0.05
    "chapters/4/characters/docscratch/scratch_4.png"
    pause 0.05
    "chapters/4/characters/docscratch/scratch_5.png"
    pause 5.0
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
