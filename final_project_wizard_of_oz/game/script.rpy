# Characters are defined and assigned a color
define s = Character("Sabine", color="#F86983")                   
define pov = Character("[povname]", color= "#145480")

# Creates variables that can be changed throughout the game
default dont_get_it = False 
default points = 0  #point counter starts at 0
default correct_answer = False
default centered_menu = False

# Creates a type of animation that can be used at any time. 
transform zoom_in_and_out:
    #Anchors it at the center of the element
    anchor (0.5, 0.5)
    #Position on the screen
    pos (620, 440)
    #Default size
    xzoom 1.0 
    # Over 4 seconds, image will zoom in and out and repeat
    easein 2.0 zoom 0.9
    easein 2.0 zoom 1.1
    repeat

transform static_left:
    anchor (0.5, 0.5)
    pos (620, 440)

transform rotation:
    anchor (0.5, 0.5)
    pos (620, 440)
    xzoom 1.0 
    easein 2.0 xzoom -1.0
    easein 2.0 xzoom 1.0
    repeat

# VISUAL NOVEL STARTS HERE
label start:
    
    # SCENE 1 
    scene bg coffeeshop           

    # Allows python support
    python:
        # Player name is entered as input
        povname = renpy.input("What is your name?", length=32)      
        povname = povname.strip() #removes extra spaces

        # If no name is assigned, default is given
        if not povname:                                             
            povname = "Andrea"

    pov "My name is [povname]!"

    # Dialogue starts
    "It's a beautiful day in Brighton..."
    "Sabine and [povname] have agreed to meet in their nearest coffee shop to talk about a subject they love..."
    "THE WIZARD OF OZ!"

    # Shows character
    show sabine happy
    # with fade animation
    with fade
    s "Hey, [povname]. I'm so glad you came!"

    # Changes atrribute of character
    show sabine eyesclosed 
    s "I was starting to think that maybe you weren't so interesed."

    show sabine happy
    s "Well, let's go inside and not waste any more time!"

    # SCENE 2
    scene bg coffeeshopinside 
    show sabine happy at right # establishes placement
    with fade
    s "I've been doing a lot of research lately..."
    s "And I was right..." 
    s "The WIZARD OF OZ movie has so many intricate details that are so easy to overlook."

    # Identifies a program point 
    label the_question:                                    
        s "Would you like me to start with some context or go straight to the nitty-gritty?"

        #Presents choices to player
        menu:                                             
            "Context":  
                pov "I want some context first."                          
                # moves to next section
                jump context

            "Start right away": 
                show sabine wink                            
                pov "Let's get into it."  
                jump the_tarot
                

    # SCENE 3
    label context:
        show sabine wink
        s "Gotcha!"
        scene bg wizardbook
        with fade
        s "'The Wonderful Wizard of Oz' is a children's novel written by American author L. Frank Baum."
        s "It became very popular at the start of the last century, where it captivated the imagination of millions of kids."
        scene bg wizardbook2
        with fade
        s "It tells the story of Dorothy, a farm girl from Kansas that gets swept away by a tornado into the magical land of Oz."
        scene bg wizardfilm
        with fade
        s "The book has many adaptations. The most popular of them being the 1939 film 'The Wizard Of Oz' starring Judy Garland as Dorothy."
        s "I'm guessing you've seen it!"
        scene bg coffeeshopinside 
        show sabine happy at right 
        with fade
        s "It's a fascinating tale that hides many wonderful secrets behind its fairly simple narrative."
        s "Now, let's start with my first finding!"
        s "Let's take a seat..."   
        jump the_tarot

    # SCENE 4
    label the_tarot:
        scene bg coffeeshoptable
        show sabine happy at right
        with fade
        s "I was looking through my old tarot deck..."
        s "And look at what I found..."
        show the_fool_yeah at zoom_in_and_out 
        with dissolve
        
        s "This is 'The Fool', the first card of the tarot..."
        "Does it remind you of anything?"

        menu the_tarot_menu:                                             
            "I don't get it":
                # Variable is set to True
                $ dont_get_it = True 
                #calls a label
                call hint
                jump the_tarot_menu
            "Wait a minute...I've seen this before!": 
                jump seen_this_before
            # If player doesn't get it, third option appears in menu
            "It's a dog!" if dont_get_it:
                jump its_a_dog 

    label hint:
        s "I'll give you a hint..."
        s "The Fool represents an adventurous figure at the beginning of its journey..."
        s "But they are not travelling alone..."
        s "Do you see who's right beside them?"
        return 

    label seen_this_before:   
        s "Please tell me"
        s "Who does this remind you of?"
        $ answer = renpy.input("It reminds me of:")
        $ answer = answer.strip()
        # If user answers correcty, correct_answer variable is changed to 'True' and they advance to next screen
        if answer == "Dorothy":
            $ correct_answer = True
            jump correct_answer
        elif answer == "dorothy":
            $ correct_answer = True
            jump correct_answer
        # If user answers incorrectly, they are asked to try again
        else:
            "Please try again"
            "I'll give you another hint..."
            "It starts with a D..."
            jump seen_this_before

    label its_a_dog:
        s "Yes! It's a dog."
        s "Which dog does this remind you of?"
        $ answer = renpy.input("It reminds me of:")
        $ answer = answer.strip()
        # If user answers correcty, correct_answer variable is changed to 'True' and they advance to next screen
        if answer == "Toto":
            $ correct_answer = True
            jump correct_answer
        elif answer == "toto":
            $ correct_answer = True
            jump correct_answer
        # If user answers incorrectly, they are asked to try again
        else:
            "Please try again"
            "I'll give you another hint..."
            "It starts with a T..."
            jump its_a_dog

    label correct_answer:
        # If answer is correct, 1 point is added to the counter
        if correct_answer == True:
            $ points =+ 1
        s "Very Nice!"
        s "I have something to show you."
        hide the_fool_yeah 
        # Hides dialogue window temporarily
        window hide
        # Points are shown on screen
        show screen points_screen 
        # Actions are paused for 3 seconds to allow user to read the screen text box.
        $ renpy.pause (3.0)
        
        # Returns dialogue window to normal functionality (automatic hide/show)
        window auto 
        show sabine eyesclosed  
        s "You are very bright."
        hide screen points_screen
        show screen counter_screen
        show sabine happy
        s "You can now see your points in the top left corner of the screen."
        s "If you earn 5 points I may give you a reward..."
        s "Let's continue."
        s "As I was saying..."
        s "Dorothy is, in fact, The Fool."
        show dorothy_thefool at rotation
        with dissolve
        s "When we first meet her, she's at the begginning of her journey."
        s "An adventurer, both brave and innocent."
        s "She's been dragged into this world that is very different from hers. "
        s "These are, in fact, two different worlds."
        jump plato_world_of_ideas
    
    label plato_world_of_ideas:
        scene bg plato
        with fade
        s "Do you happen to know this guy?"
        # Applies special centered menu created in screen.rpy file (line 211)
        $ centered_menu = True
        menu centered_menu:                                             
            "Yes":  
                jump plato_yes
            "No": 
                jump plato_no   

    label plato_yes:
        s "Who would this be?"


    label plato_no:
        s "That's OK!"
        s "Please open this book to find out"






        s "She has to walk down the yellow brick road in order to meet the powerful Wizard of Oz."
        s "She has to find her way back home..."
        s "Or in other words..."
        s "She has to "

    

