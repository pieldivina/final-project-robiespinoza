screen emerald_button():
    # Creates a button that has an image
    imagebutton:
        xalign 0.5
        yalign 0.5
        # Calls all images with emerald_button in their name (idle, hover and pushed)
        # Button will dissapear when actioned and jump to label book_reveal
        auto "emerald_button_%s.png" action [ToggleScreen("emerald_button"), Jump("book_reveal")]