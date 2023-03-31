class Person:
    def __init__(self, name, friends, watchlist, watched):
        self.name = name
        self.friends = friends
        self.watchlist = watchlist
        self.watched = watched
    
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    def add_to_watchlist(self, new_movie):
        if new_movie not in self.watchlist:
            self.watchlist.append(new_movie)
    
    def watch_movie(self, movie):
        if movie in self.watchlist:
            self.watchlist.remove(movie) 

        if movie not in self.watched:
            self.watched.append(movie)  
