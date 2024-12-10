# Characters are defined and given a color
define s = Character("Sabine", color="#F86983")                   
define pov = Character("[povname]", color= "#145480")

#Game Starts
label start:
    
    # Screen 1 
    scene bg coffeeshop           

    # Allows python support.   
    python:
        # Player name is entered as input.
        povname = renpy.input("What is your name?", length=32)      
        povname = povname.strip() #removes extra spaces

        # If no name is assigned, default is given.
        if not povname:                                             
            povname = "Andrea"

    pov "My name is [povname]!"

    #Dialogue starts
    "It's a beautiful day in Brighton..."
    "Sabine and [povname] have agreed to meet in their nearest coffee shop to talk about a subject they love..."
    "THE WIZARD OF OZ!"

    #Shows Character
    show sabine happy
    s "Hey, [povname]. I'm so glad you came!"

    #Changes atrribute of character
    show sabine eyesclosed 
    s "I was starting to think that maybe you weren't so interesed."

    show sabine happy
    s "Well, let's go inside and not waste any more time!"

    # Screen 2
    scene bg coffeeshopinside 
    show sabine happy at right 
    with fade
    s "I've been doing a lot of research lately..."
    s "And I was right..." 
    s "The WIZARD OF OZ movie has so many intricate details that are so easy to overlook."

    #Identifies a program point 
    label the_question:                                    
        "Would you like me to start with some context or go straight to the nitty-gritty?"

        #Presents choices to player
        menu:                                             
            "Context":  
                pov "I want some context first."                          
                jump context

            "Start right away":                             
                jump the_tarot
                pov "Let's get into it."  

    # Screen 3
    label context:
        s "Gotcha!"
        show thewizardcover at left 
        with dissolve
        s "'The Wonderful Wizard of Oz' is a children's novel written by American author L. Frank Baum."
        s "It became very popular at the start of the last century, where it captivated the imagination of millions of kids."
        hide thewizardcover 
        with dissolve
        show dorothy at left 
        with dissolve
        s "It tells the story of Dorothy, a farm girl from Kansas that gets swept away by a tornado into the magical land of Oz."
        hide dorothy at left 
        with dissolve
        show judygarland at left 
        with dissolve
        s "The book has many adaptations. The most popular of them being the 1939 film 'The Wizard Of Oz' starring Judy Garland as Dorothy."
        s "I'm guessing you've seen it!"
        s "It's a fascinating tale that hides many wonderful secrets behind it's fairly simple narrative."
        s "NOW, let's start with my first finding!"
        s "Let's take a seat..."   
        jump the_tarot

    # Screen 4
    label the_tarot:
        scene bg coffeeshoptable
        show sabine happy at right
        with fade
        s "I was looking through my old tarot deck..."
        s "And look at what I found..."
        show thefool at left 
        with dissolve
        
        s "This is 'The Fool', the first card of the tarot..."
        "Does it remind you of anything?"

        menu the_tarot_menu:                                             
            "I don't get it":                           
                s "Look very closely"
                jump the_tarot_menu

            "Wait a minute...I've seen this before!": 
                call answerselector

            "Give me a hint, please":
                s "The Fool represents an adventurous figure at the beggining of its journey..."
                s "But they are not traveling alone..."
                s "Do you see who is right beside them?"
                jump the_tarot_menu
                    

            
            
    