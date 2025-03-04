import java.util.ArrayList;
import java.util.List;

class Song {
    String title;
    String artist;
    String album;
    String genre;
    String duration;
    List<Song> list;

    public Song(String title, String artist, String album, String genre, String duration) {
        this.title = title;
        this.artist = artist;
        this.album = album;
        this.genre = genre;
        this.duration = duration;
        this.list = new ArrayList<>();
    }

    public String displayDetails() {
        return "Title: " + this.title + ", Artist: " + this.artist + ", Album: " + this.album + ", Genre: " + this.genre + ", Duration: " + this.duration;
    }
}

class Playlist {
    String name;
    List<Song> list;

    public Playlist(String name) {
        this.name = name;
        this.list = new ArrayList<>();
    }

    public void addSong(Song song) {
        this.list.add(song);
    }

    public boolean removeSong(String songTitle) {
        for (Song song : this.list) {
            if (song.title.equals(songTitle)) {
                this.list.remove(song);
                return true;
            }
        }
        return false;
    }

    public List<Song> getSongs() {
        return this.list;
    }

    public List<Song> filterSongs(String criteria, String value) {
        List<Song> filtered = new ArrayList<>();
        for (Song song : this.list) {
            switch (criteria) {
                case "artist":
                    if (song.artist.equals(value)) {
                        filtered.add(song);
                    }
                    break;
                case "genre":
                    if (song.genre.equals(value)) {
                        filtered.add(song);
                    }
                    break;
                case "title":
                    if (song.title.equals(value)) {
                        filtered.add(song);
                    }
                    break;
                case "album":
                    if (song.album.equals(value)) {
                        filtered.add(song);
                    }
                    break;
            }
        }
        return filtered;
    }

    public List<Song> searchSongs(String keyword) {
        List<Song> key = new ArrayList<>();
        for (Song song : this.list) {
            if (song.title.toLowerCase().contains(keyword.toLowerCase()) ||
                song.artist.toLowerCase().contains(keyword.toLowerCase()) ||
                song.album.toLowerCase().contains(keyword.toLowerCase()) ||
                song.genre.toLowerCase().contains(keyword.toLowerCase())) {
                key.add(song);
            }
        }
        return key;
    }
}

class PlaylistManager {
    List<Playlist> playlists;

    public PlaylistManager() {
        this.playlists = new ArrayList<>();
    }

    public void createPlaylist(String name) {
        this.playlists.add(new Playlist(name));
    }

    public boolean deletePlaylist(String name) {
        for (Playlist playlist : this.playlists) {
            if (playlist.name.equals(name)) {
                this.playlists.remove(playlist);
                return true;
            }
        }
        return false;
    }

    public Playlist getPlaylist(String name) {
        for (Playlist playlist : this.playlists) {
            if (playlist.name.equals(name)) {
                return playlist;
            }
        }
        return null;
    }

    public List<Playlist> listPlaylists() {
        return this.playlists;
    }

    public List<Song> crossPlaylistSearch(String keyword) {
        List<Song> songs = new ArrayList<>();
        for (Playlist playlist : this.playlists) {
            List<Song> s = playlist.searchSongs(keyword);
            songs.addAll(s);
        }
        return songs;
    }
}

