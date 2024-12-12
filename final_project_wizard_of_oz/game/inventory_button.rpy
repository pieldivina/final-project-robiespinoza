# Creates the inventory button
screen inventory_button:
    frame:
        xalign 0.98
        yalign 0.02
        xsize 380
        ysize 150
        padding (10,10)
        hbox:
            xalign 0.5
            yalign 0.5
            # When pressed (action) inventory will either show or hide
            textbutton "Inventory" action [Show("inventory_screen"), Hide("inventory_button")]
            image "images/basket.png"