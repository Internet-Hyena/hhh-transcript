



init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.psd', None)
    build.classify('**.ai', None)
    build.classify('**.html', None)
    build.classify('.git/**', None)
    build.classify('formatter/**', None)
    build.classify('private/**', None)
    build.classify('.vscode/**', None)
    build.classify("**.rpy", None)
    build.classify("saves/**", None)
    build.classify("utils/**", None)
    build.classify("cache/**", None)

    build.archive("audio", "all")
    build.archive("images", "all")
    build.archive("gui", "all")
    build.archive("scripts", "all")

    build.classify('game/audio/**', 'audio')
    build.classify('game/fonts/**', 'fonts')
    build.classify('game/gui/**', 'gui')
    build.classify('game/*.rpyc', 'scripts')
    build.classify('game/images/**', 'images')









    build.documentation('*.html')
    build.documentation('*.txt')










    build.archive('chapter1', 'all')
    build.archive('chapter2', 'all')
    build.archive('chapter3', 'all')
    build.archive('chapter4', 'all')


    build.classify('game/chapters/1/**', 'chapter1')
    build.classify('game/chapters/2/**', 'chapter2')
    build.classify('game/chapters/3/**', 'chapter3')
    build.classify('game/chapters/4/**', 'chapter4')


    build.classify('game/chapters/*/**', None)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
