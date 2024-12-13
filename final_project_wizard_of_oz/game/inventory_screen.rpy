init python:
    # Assigns an image to item
    inventory_icon = ["images/1.png", "images/2.png", "images/3.png", "images/4.png", "images/5.png"]

    # Item is assigned a name
    item_name = {
        "images/1.png": "The Fool",
        "images/2.png": "Plato",
        "images/3.png": "Locked Item",
        "images/4.png": "Mystery Book",
        "images/5.png": "Emerald Tablet"
    }

    # Description of the items
    description = {
        "images/1.png": "The Fool is the archetype of the adventurer, both corageous and unexperienced. They start their journey to find themselves.",
        "images/2.png": "Plato is known for his theory of Forms. He believed that for every material thing, there was an ideal counterpart.",
        "images/3.png": "You haven't unlocked this item yet.",
        "images/4.png": "A book Sabine found.",
        "images/5.png": "The Emerald Tablet is an ancient book that is worth investigating."
    }   

    # Name of the item (variable)
    name_item = ""

    story_name_item = ""

    # Shows description (variable)
    show_description = ""

    # Shows the item selected (variable)
    show_item = ""

    # Checks if the inventory is open
    open_inventory = False
    

screen inventory_screen():
    # invetory_screen becomes main screen
    modal True
    # background
    add "images/inventory_bg.png"
    # creates a grid
    grid 3 2:
        xalign 0.3
        yalign 0.4
        # for each item in list:
        for item in inventory_icon:
                    #open a frame which will display items as icons and allow a description to be shown if cliked on.
                    frame:
                        imagebutton idle item action [SetVariable("name_item", (item_name.get(item))), SetVariable("show_description", (description.get(item))), SetVariable("show_item", item), ToggleVariable("open_inventory", True)]
    # Show the item description if open_inventory is True
    if open_inventory == True:
        frame:
            background "#ca0b35a9"
            xfill True
            xalign 0.5
            yalign 0.9
            padding (50,40)
            vbox:
                for item in inventory_icon:
                    if item in show_item:
                        text name_item
                        image item
                        text show_description
                        
    textbutton "Close Inventory" action [Hide("inventory_screen"), Show("inventory_button"), ToggleVariable("open_inventory", False)] xalign 0.98 yalign 0.0
