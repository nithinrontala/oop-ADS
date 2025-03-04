
from Solution import Person, SocialNetwork

def main():
    print("=== Testing Person class ===")
    # Create a Person instance.
    john = Person("John", ["The Movie: The Game", "The Legend of Corgi"])
    print("Initial games for John:", john.get_favorite_games())
    print("John's name:", john.get_name())

    # Test add_game method.
    john.add_game("New Adventure")
    print("After adding 'New Adventure':", john.get_favorite_games())
    # Attempt to add duplicate game.
    john.add_game("New Adventure")
    print("After attempting to add 'New Adventure' again:", john.get_favorite_games())

    # Test remove_game method.
    john.remove_game("The Movie: The Game")
    print("After removing 'The Movie: The Game':", john.get_favorite_games())

    print("\n=== Testing SocialNetwork class ===")
    network = SocialNetwork()

    # Test add_user.
    network.add_user(john)
    alice = Person("Alice", ["Dinosaur Diner", "The Movie: The Game"])
    bob = Person("Bob", ["The Legend of Corgi", "Dinosaur Diner"])
    network.add_user(alice)
    network.add_user(bob)
    print("Users in network after adding John, Alice, Bob:")
    print(network)

    # Test get_user method.
    retrieved_alice = network.get_user("Alice")
    print("Retrieved user:", retrieved_alice)

    # Test update_person method.
    network.update_person(alice)
    print("After updating current person to Alice, current person:", network.person)

    # Test get_users_who_like method.
    dinosaur_fans = network.get_users_who_like("Dinosaur Diner")
    print("Users who like 'Dinosaur Diner':", dinosaur_fans)
    corgi_fans = network.get_users_who_like("The Legend of Corgi")
    print("Users who like 'The Legend of Corgi':", corgi_fans)

    # Test remove_user method.
    network.remove_user("Alice")
    print("After removing Alice from network:")
    print(network)

    # Test remove_user on a non-existing user.
    network.remove_user("NonExistent")

    # Test update_person with a non-existent user.
    network.update_person(alice)

    # Further test: Attempt to add a user that already exists.
    network.add_user(bob)


if __name__ == '__main__':
    main()
