from util import Stack, Queue
import random
import math


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:  # if same id
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # friend or user id is in the other frind or user id
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)  # add user id to frined
            self.friendships[friend_id].add(user_id)  # add friend id to user

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.

        Code by: Beej
        """
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        random.shuffle(possible_friendships)
        #x = 0
        for i in range(0, math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        q = Queue()  # breadth first traversal (BFT)

        q.enqueue([user_id])  # add user_id to queue as starting path list

        while q.size() > 0:  # while the Q is not empty
            cur_path = q.dequeue()  # dequeue current path

            cur_node = cur_path[-1]  # node is very last in cur path list

            if cur_node not in visited:  # if node has not been visited
                visited[cur_node] = cur_path  # update the path

                # get cur node's friendships
                friends = self.friendships[cur_node]

                for f in friends:  # go thru friends
                    # add friend to cur path of cur node (append)
                    f_path = cur_path + [f]
                    q.enqueue(f_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print('Friends: ', sg.friendships)
    connections = sg.get_all_social_paths(1)
    print('Paths: ', connections)
