init python:
    class glitch(renpy.Displayable):
        """
        `randomkey`
            Follows the rules of the random modume's seed function.
            If not set, a random seed is generated when the transform is applied,
            and stays the same afterwards.
            If you want the effect to be random for each render operation, set to None.

        `chroma`
            Boolean, whether to apply the chromatic aberration effect.

        `minbandheight`
            Minimum height of each slice.

        `offset`
            The offset of each slice will be between -offset and offset pixels.

        `nslices`
            Number of slicings to do (the number of slices will be nslices + 1).
            Setting this to 0 is not supported.
            None (the default) makes it random.
        """
        
        NotSet = object()
        
        def __init__(self, child, *, randomkey=NotSet, chroma=True, minbandheight=1, offset=30, nslices=None, **properties):
            super().__init__(**properties)
            self.child = renpy.displayable(child)
            if randomkey is self.NotSet:
                randomkey = renpy.random.random()
            self.randomkey = randomkey
            self.chroma = chroma
            self.minbandheight = minbandheight
            self.offset = offset
            self.nslices = nslices
        
        def render(self, width, height, st, at):
            child = self.child
            child_render = renpy.render(child, width, height, st, at)
            cwidth, cheight = child_render.get_size()
            if not (cwidth and cheight):
                return child_render
            render = renpy.Render(cwidth, cheight)
            randomobj = renpy.random.Random(self.randomkey)
            chroma = self.chroma and renpy.display.render.models
            offset = self.offset
            minbandheight = self.minbandheight
            nslices = self.nslices
            if nslices is None:
                nslices = min(int(cheight/minbandheight), randomobj.randrange(10, 21))
            
            theights = sorted(randomobj.randrange(cheight+1) for k in range(nslices)) 
            offt = 0 
            fheight = 0 
            while fheight<cheight:
                
                if theights:
                    theight = max(theights.pop(0)-fheight, minbandheight)
                else:
                    theight = cheight-theight
                
                slice_render = child_render.subsurface((0, fheight, cwidth, theight))
                
                if offt and chroma:
                    for color_mask, chponder in (((False, False, True, True), 1.25), ((False, True, False, True), 1.), ((True, False, False, True), .75)):
                        chroma_render = slice_render.subsurface((0, 0, cwidth, theight))
                        chroma_render.add_property("gl_color_mask", color_mask)
                        render.blit(chroma_render, (round(offt*chponder), round(fheight)))
                
                else:
                    render.blit(slice_render, (offt, round(fheight)))
                
                fheight += theight
                if offt:
                    offt = 0
                else:
                    offt = randomobj.randrange(-offset, offset+1)
            
            return render
        
        def visit(self):
            return [self.child]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
