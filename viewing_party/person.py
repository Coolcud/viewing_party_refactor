class Person:
    def __init__(self, name, friends, watchlist):
        self.name = name
        self.friends = friends
        self.watchlist = watchlist
    
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    def add_to_watchlist(self, new_movie):
        if new_movie not in self.watchlist:
            self.watchlist.append(new_movie)
