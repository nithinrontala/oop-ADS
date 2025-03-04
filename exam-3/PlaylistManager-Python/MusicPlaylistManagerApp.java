import java.util.ArrayList;
import java.util.List;

class SongTest {
    public static void runTests() {
        System.out.println("Running Song Tests...");

        // Test Case 1: Create a song and check details string.
        Song s1 = new Song("Imagine", "John Lennon", "Imagine", "Rock", 183);
        String details = s1.displayDetails();
        if (!details.contains("Imagine")) {
            System.out.println("Test Case 1 Failed: Song details should contain the title.");
        } else {
            System.out.println("Test Case 1 Passed.");
        }

        // Test Case 2: Check that artist is correctly assigned.
        if (!s1.artist.equals("John Lennon")) {
            System.out.println("Test Case 2 Failed: Artist name is incorrect.");
        } else {
            System.out.println("Test Case 2 Passed.");
        }

        // Test Case 3: Check album assignment.
        if (!s1.album.equals("Imagine")) {
            System.out.println("Test Case 3 Failed: Album name is incorrect.");
        } else {
            System.out.println("Test Case 3 Passed.");
        }

        // Test Case 4: Check duration is set correctly.
        if (s1.duration != 183) {
            System.out.println("Test Case 4 Failed: Duration is incorrect.");
        } else {
            System.out.println("Test Case 4 Passed.");
        }

        System.out.println("Song Tests Completed.");
        System.out.println("----------------------------------------------------");
    }
}

class PlaylistTest {
    public static void runTests() {
        System.out.println("Running Playlist Tests...");

        Playlist playlist = new Playlist("Favorites");

        // Test Case 1: Add songs and check count.
        Song s1 = new Song("Song A", "Artist1", "Album1", "Pop", 200);
        Song s2 = new Song("Song B", "Artist2", "Album2", "Rock", 240);
        Song s3 = new Song("Song C", "Artist1", "Album3", "Pop", 180);
        Song s4 = new Song("Song D", "Artist3", "Album4", "Jazz", 220);
        playlist.addSong(s1);
        playlist.addSong(s2);
        playlist.addSong(s3);
        playlist.addSong(s4);
        if (playlist.getSongs().size() != 4) {
            System.out.println("Test Case 1 Failed: There should be 4 songs in the playlist.");
        } else {
            System.out.println("Test Case 1 Passed.");
        }

        // Test Case 2: Remove a song and check count.
        boolean removed = playlist.removeSong("Song B");
        if (!removed) {
            System.out.println("Test Case 2 Failed: Song B should be removed.");
        } else if (playlist.getSongs().size() != 3) {
            System.out.println("Test Case 2 Failed: There should be 3 songs left.");
        } else {
            System.out.println("Test Case 2 Passed.");
        }

        // Test Case 3: Filter songs by artist "Artist1".
        List<Song> filteredByArtist = playlist.filterSongs("artist", "Artist1");
        if (filteredByArtist.size() != 2) {
            System.out.println("Test Case 3 Failed: There should be 2 songs by Artist1.");
        } else {
            System.out.println("Test Case 3 Passed.");
        }

        // Test Case 4: Search songs by keyword "Jazz".
        List<Song> searchResults = playlist.searchSongs("Jazz");
        if (searchResults.size() != 1) {
            System.out.println("Test Case 4 Failed: There should be 1 song with Jazz in details.");
        } else {
            System.out.println("Test Case 4 Passed.");
        }

        System.out.println("Playlist Tests Completed.");
        System.out.println("----------------------------------------------------");
    }
}

class PlaylistManagerTest {
    public static void runTests() {
        System.out.println("Running PlaylistManager Tests...");

        PlaylistManager manager = new PlaylistManager();

        // Test Case 1: Create playlists and verify list.
        manager.createPlaylist("Chill");
        manager.createPlaylist("Workout");
        manager.createPlaylist("Party");
        manager.createPlaylist("Study");
        List<String> names = manager.listPlaylists();
        if (names.size() != 4) {
            System.out.println("Test Case 1 Failed: There should be 4 playlists.");
        } else {
            System.out.println("Test Case 1 Passed.");
        }

        // Test Case 2: Get a specific playlist and add a song.
        Playlist chill = manager.getPlaylist("Chill");
        if (chill == null) {
            System.out.println("Test Case 2 Failed: Playlist 'Chill' should exist.");
        } else {
            Song s = new Song("Calm Song", "ArtistX", "AlbumX", "Ambient", 300);
            chill.addSong(s);
            if (chill.getSongs().size() != 1) {
                System.out.println("Test Case 2 Failed: 'Chill' should have 1 song.");
            } else {
                System.out.println("Test Case 2 Passed.");
            }
        }

        // Test Case 3: Delete a playlist and verify deletion.
        boolean deleted = manager.deletePlaylist("Party");
        if (!deleted) {
            System.out.println("Test Case 3 Failed: 'Party' playlist should be deleted.");
        } else if (manager.listPlaylists().size() != 3) {
            System.out.println("Test Case 3 Failed: There should be 3 playlists after deletion.");
        } else {
            System.out.println("Test Case 3 Passed.");
        }

        // Test Case 4: Cross-playlist search.
        // Add songs to different playlists.
        Playlist workout = manager.getPlaylist("Workout");
        workout.addSong(new Song("Energy", "ArtistY", "AlbumY", "Rock", 210));
        Playlist study = manager.getPlaylist("Study");
        study.addSong(new Song("Focus", "ArtistZ", "AlbumZ", "Classical", 260));
        List<Song> crossSearch = manager.crossPlaylistSearch("ArtistY");
        if (crossSearch.size() != 1) {
            System.out.println("Test Case 4 Failed: Cross-search should find 1 song by ArtistY.");
        } else {
            System.out.println("Test Case 4 Passed.");
        }

        System.out.println("PlaylistManager Tests Completed.");
        System.out.println("----------------------------------------------------");
    }
}

class IntegrationTest {
    public static void runIntegrationTests() {
        System.out.println("Running Extended Integration Tests...");

        // Create a new manager and several playlists.
        PlaylistManager manager = new PlaylistManager();
        manager.createPlaylist("Road Trip");
        manager.createPlaylist("Relaxation");
        manager.createPlaylist("Workout");

        // Retrieve playlists.
        Playlist roadTrip = manager.getPlaylist("Road Trip");
        Playlist relaxation = manager.getPlaylist("Relaxation");
        Playlist workout = manager.getPlaylist("Workout");

        // Add songs to Road Trip playlist.
        roadTrip.addSong(new Song("Highway Tune", "Greta Van Fleet", "Anthem of the Road", "Rock", 210));
        roadTrip.addSong(new Song("Life is a Highway", "Tom Cochrane", "Mad Mad World", "Rock", 250));
        roadTrip.addSong(new Song("Drive", "Incubus", "Make Yourself", "Alternative", 260));

        // Add songs to Relaxation playlist.
        relaxation.addSong(new Song("Ocean Eyes", "Billie Eilish", "Don't Smile", "Pop", 200));
        relaxation.addSong(new Song("Weightless", "Marconi Union", "Ambient", "Ambient", 500));

        // Add songs to Workout playlist.
        workout.addSong(new Song("Stronger", "Kanye West", "Graduation", "Hip Hop", 312));
        workout.addSong(new Song("Eye of the Tiger", "Survivor", "Eye of the Tiger", "Rock", 245));

        // Scenario 1: Verify filtering within the Road Trip playlist.
        List<Song> roadTripRock = roadTrip.filterSongs("genre", "Rock");
        if (roadTripRock.size() != 2) {
            System.out.println("Integration Test Scenario 1 Failed: Road Trip should have 2 Rock songs.");
        } else {
            System.out.println("Integration Test Scenario 1 Passed.");
        }

        // Scenario 2: Extended search in Road Trip playlist (by partial keyword).
        List<Song> searchDrive = roadTrip.searchSongs("drive");
        if (searchDrive.size() != 1) {
            System.out.println("Integration Test Scenario 2 Failed: Should find 1 song with 'drive' in the details.");
        } else {
            System.out.println("Integration Test Scenario 2 Passed.");
        }

        // Scenario 3: Cross-playlist search (multiple matches).
        List<Song> crossSearch = manager.crossPlaylistSearch("Rock");
        if (crossSearch.size() != 3) {
            System.out.println("Integration Test Scenario 3 Failed: Cross-search for 'Rock' should find 3 songs.");
        } else {
            System.out.println("Integration Test Scenario 3 Passed.");
        }

        // Scenario 4: Delete a song from a playlist and re-run search/filter tests.
        boolean removed = roadTrip.removeSong("Life is a Highway");
        if (!removed) {
            System.out.println("Integration Test Scenario 4 Failed: 'Life is a Highway' should be removed.");
        } else if (roadTrip.getSongs().size() != 2) {
            System.out.println("Integration Test Scenario 4 Failed: Road Trip should now have 2 songs.");
        } else {
            System.out.println("Integration Test Scenario 4 Passed.");
        }

        // Scenario 5: Delete a playlist and check the overall playlist list.
        boolean deletedPlaylist = manager.deletePlaylist("Workout");
        if (!deletedPlaylist) {
            System.out.println("Integration Test Scenario 5 Failed: Workout playlist should be deleted.");
        } else if (manager.listPlaylists().size() != 2) {
            System.out.println("Integration Test Scenario 5 Failed: There should be 2 playlists remaining.");
        } else {
            System.out.println("Integration Test Scenario 5 Passed.");
        }

        // Scenario 6: Verify addition of songs to a new playlist after deletion.
        manager.createPlaylist("Party");
        Playlist party = manager.getPlaylist("Party");
        party.addSong(new Song("Uptown Funk", "Bruno Mars", "Uptown Special", "Funk", 270));
        if (party.getSongs().size() != 1) {
            System.out.println("Integration Test Scenario 6 Failed: Party should have 1 song.");
        } else {
            System.out.println("Integration Test Scenario 6 Passed.");
        }

        System.out.println("Integration Tests Completed.");
        System.out.println("----------------------------------------------------");
    }
}

// -----------------------
// Main Application Class
// -----------------------

public class MusicPlaylistManagerApp {
    public static void main(String[] args) {
        System.out.println("Welcome to the Music Playlist Manager!");

        // Run individual tests
        SongTest.runTests();
        PlaylistTest.runTests();
        PlaylistManagerTest.runTests();

        // Extended integration testing
        System.out.println("Running Complete Extended Integration Test...");
        IntegrationTest.runIntegrationTests();

        System.out.println("All tests completed successfully.");
    }
}