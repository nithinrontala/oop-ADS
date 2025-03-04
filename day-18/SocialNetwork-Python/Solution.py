class Person:
    def __init__(self, name, games=None):
        self.name = name
        self.games = games 

    def add_game(self, game):
        if game not in self.games:
            self.games.append(game)
    
    def remove_game(self, game):
        if game in self.games:
            self.games.remove(game)

    def get_favorite_games(self):
        return self.games
    
    def get_name(self):
        return self.name

    def __str__(self):
        return f"Person(name={self.name}, games={self.games})"


class SocialNetwork:
    def __init__(self):
        self.users = []
        self.person = None

    def add_user(self, user):
        for i in self.users:
            if i.get_name() == user.get_name():
                print(f"User with name {user.get_name()} already exists.")
                return
        self.users.append(user)
    
    def remove_user(self, name):
        for user in self.users:
            if user.get_name() == name:
                self.users.remove(user)
                if self.person==user:
                    self.person=None
                return
        print(f"User with name {name} not found.")

    def get_user(self, name):
        for user in self.users:
            if user.get_name() == name:
                return user
        return None

    def update_person(self, person):
        for i in self.users:
            if i.get_name() == person.get_name():
                self.person  = i
                return
        print(f"User {person.name} is not in the network.")
        
    def get_users_who_like(self, game):
        users_who_like = []
        for user in self.users:
            if game in user.get_favorite_games():
                users_who_like.append(user.get_name())
        return users_who_like

    def __str__(self):
        s = ""
        for i in self.users:
            s+=str(i)+", "
        s = s.strip(", ")
        # print("43576890",s.strip(", "))
        return f"SocialNetwork(current person={self.person}, users=[{s}])"
