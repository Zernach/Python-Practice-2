from room import Room, Item
from player import Player

# Declare all the rooms
outside = Room("Outside Cave Entrance",
                """"North of you, the cave mount beckons.
                    Or, head south to go home — adventure time is over.
                    """)

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
                         passages run north and east.
                         """)

overlook =  Room("Grand Overlook", """A steep cliff appears before you, falling
                                      into the darkness. Ahead to the north, a light flickers in
                                      the distance, but there is no way across the chasm.
                                      There is a golden key on the ground.
                                      """, [Item('a golden key')])

narrow = Room("Narrow Passage", """The narrow passage bends here from west
                                    to north. The smell of gold permeates the air.
                                    """)

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
                                       chamber! Sadly, it has already been completely emptied by
                                       earlier adventurers. The only exit is to the south.
                                       """)

home = Room('Home', """Enough adventure time -- go home! Game over for now.""")

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Ryan', outside)

# Movement Handling
def movement(choice):
    # Room linkage declarations, which change based on items in inventory
    outside.n_to = foyer
    outside.s_to = home
    foyer.s_to = outside
    foyer.n_to = overlook
    foyer.e_to = narrow
    overlook.s_to = foyer
    narrow.w_to = foyer
    treasure.s_to = narrow
    # If the player is in the narrow passage, check if key is in player's inventory
    if player1.room.name == 'Narrow Passage':
        try:
            if player1.items[0].name == 'Golden Key':
                print('You unlock the door with your Golden Key...')
                narrow.n_to = treasure
        except:
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
    if player1.items == []:
        pass
    else:
        print(player1.items[i].name for i in range(0, len(player1.items)))




def item_handling(choice):
    try:
        player1.items.append(player1.room.items[0])
        print(f'You have added {player1.room.items[0].name} to your inventory.')
        player1.room.items = []
        try:
            player1.room.description = player1.room.description.replace("a golden key", "nothing")
        except:
            pass
    except:
        print('Invalid choice. There is nothing here to pickup.')


# Infinite Loop until Player presses q for quit:
# Prints the current room name
# Prints the current description (the textwrap module might be useful here).
# Waits for user input and decides what to do.
while True:

    status_check()
    choice = input("Select a direction to move (n, s, e, w), p to pickup items, or q to quit: ")
    
    if choice == 'q':
        break

    elif choice == 'p': # p for pickup items
        item_handling(choice)

    elif choice in ['n', 'e', 's', 'w']:
        movement(choice)

    else:
        print("\nI'm not sure what that choice means...")

