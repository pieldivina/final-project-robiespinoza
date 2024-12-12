#Creates a screen
screen points_screen():
    #Creates a frame
    frame: 
        #Frame is automatically assigned from GUI folder (I created my own)
        xalign 0.25
        yalign 0.5
        xsize 500
        ysize 300
        padding (50,40)
        #Creates a vertical box
        vbox:
            if points == 1:
                text "You now have [points] point!"
                text ""
                text "Each time you answer a question correctly, you earn points."
            else:
                text "You now have [points] points!"
                text ""
                text "Congratulations!"