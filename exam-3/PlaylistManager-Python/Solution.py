class Song:
    def __init__(self,title,artist,album,genre,duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.duration  = duration
        self.list = []

    def display_details(self):
        return f"Title: {self.title}, Artist: {self.artist}, Album: {self.album}, Genre: {self.genre}, Duration: {self.duration}"
    
class Playlist:
    def __init__(self,name):
        self.name = name
        self.list = []

    def add_song(self,song):
        self.list.append(song)
        # print("b",self.list)
        
    def remove_song(self,song):
        for i in self.list:
            if i.title == song:
                self.list.remove(i)
                # print("a",self.list)
                return True
        return False
    def get_songs(self):
        return  self.list
    
    def filter_songs(self,criteria,value):
        filtered = []
        if criteria == "artist":
            for i in self.list:
                if i.artist == value:
                    filtered.append(i)
            return filtered
        
        if criteria == "genre":
            for i in self.list:
                if i.genre == value:
                    filtered.append(i)
            return filtered
        
        
        if criteria == "title":
            for i in self.list:
                if i.title == value:
                    filtered.append(i)
            return filtered
        

        if criteria == "album":
            for i in self.list:
                if i.album == value:
                    filtered.append(i)
            return filtered
        

                    
            
    def search_songs(self,keyword):
        key = []
        for i in self.list:
            if keyword.lower() in i.title.lower() or keyword.lower() in i.artist.lower() or keyword.lower() in  i.album.lower() or keyword.lower() in  i.genre.lower():
                key.append(i)
        # print(key)
        return key
    
    
class PlaylistManager:
    def __init__(self):
        self.palylists = []

    def create_playlist(self,name):
        self.palylists.append(Playlist(name))
            
            # print(self.palylists)
        
    def delete_playlist(self,name):
        for i in self.palylists:
            if i.name == name:
                self.palylists.remove(i)
                return True
        return False
    
    def get_playlist(self,name):
        # print(len(self.palylists))
        for i in self.palylists:
            if i.name == name:
                return i
        return None
    
    def list_playlists(self):
        return self.palylists
    
    def cross_playlist_search(self,keyword):
        songs = []
        # print(keyword)

        for i in self.palylists:
            s = i.search_songs(keyword)
            # print(s)
            songs.extend(s)
            # print(songs)
        return songs
    


