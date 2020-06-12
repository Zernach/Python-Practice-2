from room import Room
from player import Player
from item import Item

# Instantiate All Rooms
outside = Room("Outside Cave Entrance",
                """"North of you, the cave mount beckons. 
                Or, head south to go back home 
                to the real world.
                    """)

foyer = Room("Foyer", """Dim light filters in from the south. 
                        Dusty passages run north and east.
                        It's spooky in here.
                         """)

overlook =  Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. 
                                    Ahead to the north, a light flickers in the distance, 
                                    but there is no way across the chasm.
                                      """)

narrow = Room("Narrow Passage", """The narrow passage bends here from west
                                    to north. The smell of gold 
                                    permeates the air.
                                    """)

treasure_room = Room("Treasure Chamber", """Alas! 
                                    You've found the long-lost 
                                    treasure chamber!
                                       """)

home = Room('Home', """Enough adventure time -- 
                go back home to the real world! 
                Game over for now.
                """)

# Instantiate All Items, and Add Items to Rooms
key = Item('key')
overlook.items.append(key)
gold = Item('gold')
treasure_room.items.append(gold)
lantern = Item('lantern')

# Instantiate Player, who is Starting in the Outside Room
player1 = Player('Ryan', outside, items = [lantern])

# Movement Handling
def movement(choice):
    # Room linkage declarations, which change based on items in inventory
    outside.n_to = foyer
    foyer.s_to = outside
    foyer.n_to = overlook
    foyer.e_to = narrow
    overlook.s_to = foyer
    narrow.w_to = foyer
    treasure_room.s_to = narrow
    outside.s_to = home
    home.n_to = outside
    # If the player is in the narrow passage, check if key is in player's inventory
    if player1.room.name == 'Narrow Passage':
        if key in player1.items:
            print('You unlock the door with your golden key...')
            narrow.n_to = treasure_room
        else:
            print('What is that keyhole for?')
            narrow.n_to = narrow

    # N, S, E, W movement handling
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed (if method doesn't exist)
    if choice == 'n':
        try:
            player1.room = (player1.room).n_to
        except:
            print('Invalid choice. There is no room to the NORTH.')
    elif choice == 's':
        try:
            player1.room = (player1.room).s_to
        except:
            print('Invalid choice. There is no room to the SOUTH.')
    elif choice == 'e':
        try:
            player1.room = (player1.room).e_to
        except:
            print('Invalid choice. There is no room to the EAST.')
    elif choice == 'w':
        try:
            player1.room = (player1.room).w_to
        except:
            print('Invalid choice. There is no room to the WEST.')


### MAP OF ROOMS
### ------------
### Ov     Tr
###  ^      ^
### Fo --> Na
###  ^
### Ou
###  ^
## Home

def status_check():

    print(f"\nYour current location is: {player1.room.name}")
    print(f"Description of location: {player1.room.description}")

    # Items in Player's Inventory
    if len(player1.items) == 0:
        print("\nItems in Inventory: \nn/a")
    else:
        print("Items in your inventory: ")
        for item_in_inventory in player1.items:
            print(item_in_inventory.name)
    
    # Items in Room
    if len(player1.room.items) == 0:
        print("\nItems in Room: \nn/a")
    else:
        print("\nItems in Room: ")
        for item_in_room in player1.room.items:
            print(item_in_room.name)

def pickup_item():
    try:
        item = input('Which item would you like to pickup: ')
        for item_in_list in player1.room.items:
            if item_in_list.name == item:
                item = item_in_list
                try:
                    player1.items.append(item)
                    print(f'You have added {item} to your inventory.')
                    player1.room.items.remove(item)
                except:
                    print('Invalid choice. There is nothing here to pickup.')
            else:
                pass
    except:
        print('Invalid choice. There is nothing here to pickup.')

def drop_item():
    try:
        item = input('Which item would you like to drop: ')
        for item_in_list in player1.items:
            if item_in_list.name == item:
                item = item_in_list
                try:
                    player1.room.items.append(item)
                    print(f'You have removed {item} from your inventory.')
                    player1.items.remove(item)
                except:
                    print('Invalid choice. That item is not in your inventory.')
            else:
                pass
    except:
        print('Invalid choice. That item is not in your inventory.')


# Infinite Loop until Player presses q for quit:
# Prints the current room name
# Prints the current description (the textwrap module might be useful here).
# Waits for user input and decides what to do.
while True:
    print("———————————————————————————————————————————————")

    if player1.room.name == 'Home':
        if gold in player1.items:
            print('CONGRATULATIONS! YOU HAVE BROUGHT HOME THE GOLD! THE END\n')
            break
        else:
            pass
    else:
        pass

    status_check()

    choice = input("""
    n = north
    s = south
    e = east
    w = west
    p = to pickup an item
    d = to drop an item
    q = quit

    Make your choice: """)
    
    if choice == 'q': # q for quit
        break

    elif choice == 'p': # p for pickup item
        pickup_item()

    elif choice == 'd': # d for drop item
        drop_item()

    elif choice in ['n', 'e', 's', 'w']: # n, s, e, w for directional movement
        movement(choice)

    else:
        print("\n**********\nI'm not sure what that choice means...\n**********")

