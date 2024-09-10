init offset = -2









init python:
    d_height = 650
    d_width = 950
    gui.init(d_height, d_width)
    if 'pc' in config.variants:
        config.physical_width = d_width
        config.physical_height = d_height
    config.screen_width = d_width
    config.screen_height = d_height
    config.splashscreen_suppress_overlay = False

    def force_resolution(width, height):
        return (d_width, d_height)
    def new_force_resolution(width, height):
        if width < d_width or height < d_height:
            if "small" not in config.variants:
                config.variants = ["small", "pc", None]
            
            ratio = min(1.0 * width / d_width, 1.0 * height / d_height)
            view_width = max(int(d_width * ratio), 1)
            view_height = max(int(d_height * ratio), 1)
            
            
            
            return (view_width, view_height)
        else:
            return (d_width, d_height)

define config.reload_menu = False
define config.adjust_view_size = new_force_resolution


define config.check_conflicting_properties = True


define config.nearest_neighbor = True

define config.font_hinting = {None: None}





init python:
    def say_callback(char, *args, **kwargs):
        if not kwargs["interact"]:
            return
        
        if "sfx" in kwargs:
            sfx = kwargs["sfx"]
        
        elif getattr(char, 'name', None) == "box":
            sfx = "audio/X.mp3"
        
        else:
            sfx = "audio/next.mp3"
        
        renpy.sound.play(sfx, channel='sound', relative_volume=0.75)
        
        return args, kwargs

define config.say_arguments_callback = say_callback

define slideinleft = MoveTransition(.1, enter=offscreenleft, enter_time_warp=_warper.easein)
define slideoutleft = MoveTransition(.1, leave=offscreenleft, leave_time_warp=_warper.easeout)
define slideoutleftslow = MoveTransition(0.5, leave=offscreenleft, leave_time_warp=_warper.easeout)
define slideinright = MoveTransition(.1, enter=offscreenright, enter_time_warp=_warper.easein)
define slideoutright = MoveTransition(.1, leave=offscreenright, leave_time_warp=_warper.easein)





define config.detached_layers += [ "talksprites" ]




















define gui.accent_color = '#005682'


define gui.idle_color = '#888888'



define gui.idle_small_color = '#aaaaaa'


define gui.hover_color = '#0080BF'



define gui.selected_color = '#ffffff'


define gui.insensitive_color = '#8888887f'



define gui.muted_color = '#41A6D9'
define gui.hover_muted_color = '#49bAF2'


define gui.text_color = '#000000'
define gui.interface_text_color = '#ffffff'




define gui.text_font = "gui/fonts/courbd.ttf"
define gui.text_hinting = "auto"

define gui.text_shaper = "harfbuzz"


define gui.name_text_font = "gui/fonts/courbd.ttf"


define gui.interface_text_font = "gui/fonts/verdana.ttf"


define gui.text_size = 18


define gui.name_text_size = 14


define gui.interface_text_size = 18


define gui.label_text_size = 18


define gui.notify_text_size = 14


define gui.title_text_size = 38





define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"






define gui.textbox = Frame("gui/textbox.png", left=9, top=9)


define gui.textbox_height = 125
define gui.textbox_width = 600






define gui.textbox_yalign = 1.0




define gui.dialogue_xpos = 20
define gui.dialogue_ypos = 15



define gui.dialogue_width = 560



define gui.dialogue_text_xalign = 0.0
define gui.dialogue_text_yalign = 0.0



define gui.name_xpos = 0
define gui.name_ypos = 0



define gui.name_xalign = 0.5



define gui.namebox_width = None
define gui.namebox_height = None



define gui.namebox_borders = Borders(5, 5, 5, 5)



define gui.namebox_tile = False







define gui.button_width = None
define gui.button_height = None


define gui.button_borders = Borders(4, 4, 4, 4)



define gui.button_tile = False


define gui.button_text_font = gui.interface_text_font


define gui.button_text_size = gui.interface_text_size


define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color



define gui.button_text_xalign = 0.0








define gui.radio_button_borders = Borders(18, 4, 4, 4)

define gui.check_button_borders = Borders(18, 4, 4, 4)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(10, 4, 10, 4)

define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 14
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color












define gui.choice_button_width = 700
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(15, 10, 15, 10)
define gui.choice_button_text_font = "gui/fonts/Verdana.ttf"
define gui.choice_button_text_size = 24
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_underline = True
define gui.choice_button_text_idle_color = "#0000FF"
define gui.choice_button_text_hover_color = "#0000FF"
define gui.choice_button_text_insensitive_color = '#0000FF'








define gui.slot_button_width = 205
define gui.slot_button_height = 153
define gui.slot_button_borders = Borders(8, 8, 8, 8)
define gui.slot_button_text_size = 11
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color


define config.thumbnail_width = 190
define config.thumbnail_height = 107


define gui.file_slot_cols = 3
define gui.file_slot_rows = 2









define gui.navigation_xpos = 30


define gui.skip_ypos = 8


define gui.notify_ypos = 34


define gui.choice_spacing = 17


define gui.navigation_spacing = 3


define gui.pref_spacing = 8


define gui.pref_button_spacing = 0


define gui.page_spacing = 0


define gui.slot_spacing = 8


define gui.main_menu_text_xalign = 1.0








define gui.frame_borders = Borders(3, 3, 3, 3)


define gui.confirm_frame_borders = Borders(30, 30, 30, 30)


define gui.skip_frame_borders = Borders(12, 4, 38, 4)


define gui.notify_frame_borders = Borders(12, 4, 30, 4)


define gui.frame_tile = False











define gui.bar_size = 19
define gui.scrollbar_size = 9
define gui.slider_size = 19


define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False


define gui.bar_borders = Borders(3, 3, 3, 3)
define gui.scrollbar_borders = Borders(3, 3, 3, 3)
define gui.slider_borders = Borders(3, 3, 3, 3)


define gui.vbar_borders = Borders(3, 3, 3, 3)
define gui.vscrollbar_borders = Borders(3, 3, 3, 3)
define gui.vslider_borders = Borders(3, 3, 3, 3)



define gui.unscrollable = "hide"







define config.history_length = 250



define gui.history_height = 104


define gui.history_spacing = 0



define gui.history_name_xpos = 116
define gui.history_name_ypos = 0
define gui.history_name_width = 116
define gui.history_name_xalign = 1.0


define gui.history_text_xpos = 127
define gui.history_text_ypos = 2
define gui.history_text_width = 550
define gui.history_text_xalign = 0.0

define gui.history_text_font = "gui/fonts/courbd.ttf"






define gui.nvl_borders = Borders(0, 8, 0, 15)



define gui.nvl_list_length = 6



define gui.nvl_height = 86



define gui.nvl_spacing = 8



define gui.nvl_name_xpos = 320
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 112
define gui.nvl_name_xalign = 1.0


define gui.nvl_text_xpos = 334
define gui.nvl_text_ypos = 6
define gui.nvl_text_width = 438
define gui.nvl_text_xalign = 0.0



define gui.nvl_thought_xpos = 179
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 579
define gui.nvl_thought_xalign = 0.0


define gui.nvl_button_xpos = 334
define gui.nvl_button_xalign = 0.0








define gui.language = "unicode"






init python:



    @gui.variant
    def touch():
        
        gui.quick_button_borders = Borders(30, 11, 30, 0)



    @gui.variant
    def small():
        
        
        gui.text_size = 23
        gui.name_text_size = 27
        gui.notify_text_size = 19
        gui.interface_text_size = 23
        gui.button_text_size = 23
        gui.label_text_size = 26
        
        
        gui.textbox_height = 200
        
        
        gui.dialogue_width = gui.textbox_width - 30
        
        
        gui.slider_size = 27
        
        gui.choice_button_width = 921
        gui.choice_button_text_size = 23
        
        gui.navigation_spacing = 15
        gui.pref_button_spacing = 8
        
        gui.history_height = 142
        gui.history_text_width = 513
        
        gui.quick_button_text_size = 15
        
        
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
