from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
# visit all rooms at least once end result visit all rooms shortest route possible
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# ----- Adding code ----- #

explored = {}  # create an empty dictionary to save all explored rooms

backtrack = []  # empty list to save backtracking path, in order to back track when needed

# all possible directions saved as keys, and exit (opposite direction) saved as values direction:opposite
move_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# Save Room Number (current_room) in explored as a key, with each possible exit direction as values
explored[player.current_room.id] = player.current_room.get_exits()

while len(explored) < len(room_graph):  # while all the rooms hav not been explored
    if player.current_room.id not in explored:  # if current room hasn't been explored
        # saves room & all exits in explored
        explored[player.current_room.id] = player.current_room.get_exits()
        # previous room is saved as last direction in backtracking path
        prevRoom = backtrack[-1]
       # print('Previous Room: ', prevRoom, 'Backtracking Path: ', backtrack, 'Current Room of Player: ',
              #player.current_room.id)  # print previous room, backtracking path and current room of player
        # remove direction coming from as possible exit
        explored[player.current_room.id].remove(prevRoom)
    # otherwise if the current room has no unused exits, pick one and check it off
    elif len(explored[player.current_room.id]) > 0:
        # nextRoom = the last of current_room exits
        nextRoom = explored[player.current_room.id][-1]
       # print('Next Room: ', nextRoom, 'Backtracking Path: ', backtrack,
             # 'Current Room of Player: ', player.current_room.id)
        # remove it from the explored path
        explored[player.current_room.id].pop()
        traversal_path.append(nextRoom)  # add next room to traversal path
        # add the move to backtracking path
        backtrack.append(move_direction[nextRoom])
        player.travel(nextRoom)  # go to next room
        #print('Going to the: ', nextRoom)
    # if current room has no exits, go back
    elif len(explored[player.current_room.id]) == 0:
        # previous room is saved as last direction in backtracking path
        prevRoom = backtrack[-1]
        #print('Previous Room: ', prevRoom, 'Backtracking Path: ', backtrack, 'Current Room of Player: ',
              #player.current_room.id)
        backtrack.pop()  # remove the direction from backtracking path
        # add the previous room to the traversal path
        traversal_path.append(prevRoom)
        player.travel(prevRoom)  # go back to the previous room
        #print('Going back to: ', prevRoom)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
