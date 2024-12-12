screen counter_screen():
    #Creates a frame
    frame: 
        #Frame is automatically assigned from GUI folder (I created my own)
        xalign 0.03
        yalign 0.03
        xsize 220
        ysize 100
        padding (30,25)
        #Creates a vertical box
        vbox:
            text "Points: [points]"