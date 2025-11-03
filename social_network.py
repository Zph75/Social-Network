class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):

        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"{name} already exists in the network!")

    def add_friendship(self, person1_name, person2_name):

        if person1_name not in self.people or person2_name not in self.people:
            print(f"Friendship not created. {person1_name} or {person2_name} doesn't exist!")
            return
        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):

        for person in self.people.values():
            friend_names = [friend.name for friend in person.friends]
            print(f"{person.name} is friends with: {', '.join(friend_names)}")



network = SocialNetwork()


network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")


network.add_person("Alex")

network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny")  
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

network.print_network()


"""
Graphs are an ideal structure for representing social networks because they naturally model the relationships between individuals as nodes (Person objects) and edges (friendships). Unlike lists, which are linear and inefficient for representing complex relationships, or trees, which enforce hierarchical constraints, graphs allow for bidirectional and non-hierarchical relationships. This makes it possible to efficiently query who a person is friends with and to expand the network dynamically.

Using a dictionary to store Person objects provides fast access to nodes by name, which is crucial for operations like adding friends or checking if a user exists. The adjacency list representation (each Person maintaining a list of friends) allows the network to efficiently handle sparse connections without wasting memory, as would occur with adjacency matrices for large networks.

In testing, adding friends requires checking for existence and avoiding duplicates, which adds minor overhead but ensures network integrity. Printing the network scales linearly with the number of users and friendships, providing a clear view of the social graph. The main trade-off observed is that deep network queries (e.g., finding connections of friends-of-friends) require additional traversal algorithms, but for the purposes of managing direct friendships, the current design is efficient and intuitive.

Overall, this approach models a real-world social network effectively, maintains data integrity, and provides clear performance characteristics for adding users and friendships.
"""