# Characters are defined and assigned a color
define s = Character("Sabine", color="#F86983")                   
define pov = Character("[povname]", color= "#145480")

# Creates variables that can be changed throughout the game
default dont_get_it = False
default points = 0  # Point counter starts at 0
default correct_answer = False # Answer for first question is incorrect by default
default centered_menu = False # Menus are placed below the center by default
default inventory_icon = ["images/1.png", "images/2.png", "images/3.png", "images/4.png", "images/5.png"] # Default icons in the inventory

# Creates a type of animation that can be used at any time
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

# Creates an inventory to display on screen


# VISUAL NOVEL STARTS HERE

label start:
    # Background music
    play music "audio/Wet_Land_ST.mp3" volume 1.0
    
    # SCENE 1 
    scene bg coffeeshop     
    with fade      

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
            $ points += 1
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
    
    # SCENE 4 

    label plato_world_of_ideas:
        scene bg plato
        with fade
        s "Do you happen to know this guy?"
        # Applies special centered menu created in screen.rpy file (line 211)
        $ centered_menu = True
        menu plato_menu:                                             
            "Yes":  
                jump plato_yes
            "No": 
                jump plato_no   

    label plato_yes:
        s "Who would this be?"
        $ answer = renpy.input("It is...")
        $ answer = answer.strip()
        # If user answers correcty, correct_answer variable is changed to 'True' and they advance to next screen
        if answer == "Plato":
            $ correct_answer = True
            jump correct_answer_2
        elif answer == "plato":
            $ correct_answer = True
            jump correct_answer_2
        else:
            "Please try again"
            "I'll give you a hint..."
            "He was a Greek philosopher..."
            "Pl..."
            jump plato_yes    

    label correct_answer_2:
        scene bg coffeeshoptable
        show sabine happy at right
        with fade

        if correct_answer == True:
            $ points += 1   
        window hide

        show screen points_screen 
        $ renpy.pause (3.0)
        window auto
        hide screen points_screen
        s "Very Good!"
        s "I was confident in your answer."
        s "This is Plato."
        s "He is widely attributed the famous Theory of Forms."
        s "Plato suggested that for every thing in the material world, there is a non-physical idea that inhabits the World of Forms."
        s "This is very similar to how The Wizard of Oz portrays Dorothy's world v.s. the Magical land of Oz."      
        show hunk at static_left
        with dissolve
        s "For every person that Dorothy knows in Kansas, there is an abstract version of it in Oz."
        s "For example, Hunk, the farmhand, is the Scarecrow."
        hide hunk at static_left
        with dissolve
        s "Now let me show you another thing..."
        jump inventory_available

    label plato_no:
        s "That's OK!"
        s "This is Plato"
        s "He was a Greek philosopher."
        scene bg coffeeshoptable
        show sabine happy at right
        with fade
        s "He is widely attributed the famous Theory of Forms."
        s "Plato suggested that for every thing in the material world, there is a non-physical idea that inhabits the World of Forms."
        s "This is very similar to how The Wizard of Oz portrays Dorothy's world v.s. the Magical land of Oz."      
        show hunk at static_left
        with dissolve
        s "For every person that Dorothy knows in Kansas, there is an abstract version of it in Oz."
        s "For example, Hunk, the farmhand, is the Scarecrow."
        hide hunk at static_left
        with dissolve
        s "Now let me show you another thing..."
        jump inventory_available

    #SCENE 5 

    label inventory_available:
        window hide
        show screen inventory_button
        $ renpy.pause (3.0)
        # Hides one item from the inventory
        $ inventory_icon.remove("images/4.png")
        $ inventory_icon.remove("images/5.png")
        s "You have unlocked an inventory!"
        s "It's a basket, just like the one Dorothy has."
        s "Click on 'Inventory' to be reminded of what you've learned today. You can close the window by clicking on 'Close Inventory. You can click on the icons too!'"
        s "Everytime you learn something, you'll add an item related to that question to your inventory."
        s "As you've seen, there's still one item you haven't unlocked yet..."
        s "Maybe I can unlock it for you..."
        # Show hidden image again and hides another one
        $ inventory_icon.append("images/4.png")
        $ inventory_icon.remove("images/3.png")
        s "Give it a try..."
        s "That's right... I have some new information!"
        s "Let's head to my library and I'll show you what I found"
        jump library

    # SCENE 6

    label library:
        scene bg roomlibrary
        show sabine happy at right
        with fade
        s "Sorry for the mess."
        s "I got quite lost in my research."
        s "Do you happen to remember the Emerald City?"
        menu emerald_city_menu:                                             
            "Is it a restaurant?":
                $ dont_get_it = True 
                call restaurant_hint
                jump emerald_city_menu
            "It's where the Wizard lives": 
                jump where_wizard_lives
                $ correct_answer == True
            "It's where Dorothy is heading!" if dont_get_it:
                jump where_wizard_lives
                $ correct_answer == True
            
    label restaurant_hint:
        s "LOL, it is."
        s "But it's inspired by one emblematic place in Oz..."
        return 
        
    label where_wizard_lives:
        scene bg roomlibrary
        show sabine happy at right
        if correct_answer == True:
            $ points += 1
        show screen points_screen 
        $ renpy.pause (3.0)
        window auto
        hide screen points_screen
        s "That's right!"
        s "It's the ultimate destination..."
        s "But once Dorothy reaches her goal she realizes she never needed the wizard."
        s "She always had the power to go home by herself. She just had to believe in it."
        s "Now, going back to the book I found..."
        s "It reminds me of Emerald City..."
        hide sabine happy 
        with fade
        s "Click on the following button to find out which book I'm talking about..."
        # Calls emerald_button into the screen
        call screen emerald_button

    label book_reveal:
        scene bg roomlibrary
        show sabine eyesclosed at right
        with fade
        show hermes_book at zoom_in_and_out 
        with dissolve
        show sabine happy at right
        s "It's called The Emerald Tablet by Hermes Trismegistus"
        s "Many people argue the real author remains unknown..."
        $ inventory_icon.append("images/5.png")
        $ inventory_icon.remove("images/4.png")
        s "I have added it to your inventory. Take a look!"
        s "I still haven't read it, so this will be the end of our investigation for today."
        s "Thank you for everything, [povname]!"
        s "Let's do this again sometime."
        jump end_screen

    label end_screen:
        hide screen counter_screen
        hide screen inventory_button
        scene bg ending_screen
        with fade
        $ renpy.pause (10.0)

    # NOVEL ENDS