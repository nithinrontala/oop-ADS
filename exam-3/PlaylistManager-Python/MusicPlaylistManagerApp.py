
from Solution import Song, Playlist, PlaylistManager

def test_song():
    print("Running Song Tests...")
    # Test Case 1: Create song and verify details string
    s1 = Song("Imagine", "John Lennon", "Imagine", "Rock", 183)
    details = s1.display_details()
    assert "Imagine" in details, "Test Case 1 Failed: Details should contain the title."
    
    # Test Case 2: Check artist assignment
    assert s1.artist == "John Lennon", "Test Case 2 Failed: Artist is incorrect."
    
    # Test Case 3: Check album assignment
    assert s1.album == "Imagine", "Test Case 3 Failed: Album is incorrect."
    
    # Test Case 4: Check duration
    assert s1.duration == 183, "Test Case 4 Failed: Duration is incorrect."
    
    print("Song Tests Passed.")
    print("----------------------------------------------------")

def test_playlist():
    print("Running Playlist Tests...")
    playlist = Playlist("Favorites")
    
    # Create songs
    s1 = Song("Song A", "Artist1", "Album1", "Pop", 200)
    s2 = Song("Song B", "Artist2", "Album2", "Rock", 240)
    s3 = Song("Song C", "Artist1", "Album3", "Pop", 180)
    s4 = Song("Song D", "Artist3", "Album4", "Jazz", 220)
    
    # Test Case 1: Add songs and check count.
    playlist.add_song(s1)
    playlist.add_song(s2)
    playlist.add_song(s3)
    playlist.add_song(s4)
    assert len(playlist.get_songs()) == 4, "Test Case 1 Failed: There should be 4 songs in the playlist."
    
    # Test Case 2: Remove a song and check count.
    removed = playlist.remove_song("Song B")
    assert removed, "Test Case 2 Failed: Song B should be removed."
    assert len(playlist.get_songs()) == 3, "Test Case 2 Failed: There should be 3 songs after removal."
    
    # Test Case 3: Filter songs by artist "Artist1"
    filtered = playlist.filter_songs("artist", "Artist1")
    assert len(filtered) == 2, "Test Case 3 Failed: There should be 2 songs by Artist1."
    
    # Test Case 4: Search for songs with keyword "Jazz"
    search_results = playlist.search_songs("Jazz")
    assert len(search_results) == 1, "Test Case 4 Failed: There should be 1 song with Jazz in details."
    
    print("Playlist Tests Passed.")
    print("----------------------------------------------------")

def test_playlist_manager():
    print("Running PlaylistManager Tests...")
    manager = PlaylistManager()
    
    # Test Case 1: Create playlists and verify count.
    manager.create_playlist("Chill")
    manager.create_playlist("Workout")
    manager.create_playlist("Party")
    manager.create_playlist("Study")
    assert len(manager.list_playlists()) == 4, "Test Case 1 Failed: There should be 4 playlists."
    
    # Test Case 2: Get a specific playlist and add a song.
    chill = manager.get_playlist("Chill")
    assert chill is not None, "Test Case 2 Failed: Playlist 'Chill' should exist."
    s = Song("Calm Song", "ArtistX", "AlbumX", "Ambient", 300)
    chill.add_song(s)
    assert len(chill.get_songs()) == 1, "Test Case 2 Failed: 'Chill' should have 1 song."
    
    # Test Case 3: Delete a playlist and verify deletion.
    deleted = manager.delete_playlist("Party")
    assert deleted, "Test Case 3 Failed: 'Party' playlist should be deleted."
    assert len(manager.list_playlists()) == 3, "Test Case 3 Failed: There should be 3 playlists remaining."
    
    # Test Case 4: Cross-playlist search.
    workout = manager.get_playlist("Workout")
    workout.add_song(Song("Energy", "ArtistY", "AlbumY", "Rock", 210))
    study = manager.get_playlist("Study")
    study.add_song(Song("Focus", "ArtistZ", "AlbumZ", "Classical", 260))
    cross_results = manager.cross_playlist_search("ArtistY")
    assert len(cross_results) == 1, "Test Case 4 Failed: Cross-search should find 1 song by ArtistY."
    
    print("PlaylistManager Tests Passed.")
    print("----------------------------------------------------")

def integration_test():
    print("Running Extended Integration Tests...")
    manager = PlaylistManager()
    manager.create_playlist("Road Trip")
    manager.create_playlist("Relaxation")
    manager.create_playlist("Workout")
    
    road_trip = manager.get_playlist("Road Trip")
    relaxation = manager.get_playlist("Relaxation")
    workout = manager.get_playlist("Workout")
    
    # Add songs to Road Trip playlist
    road_trip.add_song(Song("Highway Tune", "Greta Van Fleet", "Anthem of the Road", "Rock", 210))
    road_trip.add_song(Song("Life is a Highway", "Tom Cochrane", "Mad Mad World", "Rock", 250))
    road_trip.add_song(Song("Drive", "Incubus", "Make Yourself", "Alternative", 260))
    
    # Add songs to Relaxation playlist
    relaxation.add_song(Song("Ocean Eyes", "Billie Eilish", "Don't Smile", "Pop", 200))
    relaxation.add_song(Song("Weightless", "Marconi Union", "Ambient", "Ambient", 500))
    
    # Add songs to Workout playlist
    workout.add_song(Song("Stronger", "Kanye West", "Graduation", "Hip Hop", 312))
    workout.add_song(Song("Eye of the Tiger", "Survivor", "Eye of the Tiger", "Rock", 245))
    
    # --- Extended Testing Scenarios ---
    
    # Scenario 1: Verify filtering within Road Trip playlist for Rock songs.
    road_trip_rock = road_trip.filter_songs("genre", "Rock")
    assert len(road_trip_rock) == 2, "Integration Test Scenario 1 Failed: Road Trip should have 2 Rock songs."
    
    # Scenario 2: Search for a partial keyword in Road Trip.
    search_drive = road_trip.search_songs("drive")
    assert len(search_drive) == 1, "Integration Test Scenario 2 Failed: Should find 1 song with 'drive' in the details."
    
    # Scenario 3: Cross-playlist search for genre "Rock"
    cross_search = manager.cross_playlist_search("Rock")
    # Expected: 2 songs from Road Trip + 1 from Workout = 3 songs total
    assert len(cross_search) == 3, "Integration Test Scenario 3 Failed: Cross-search for 'Rock' should find 3 songs."
    
    # Scenario 4: Delete a song from Road Trip and verify updated count.
    removed = road_trip.remove_song("Life is a Highway")
    assert removed, "Integration Test Scenario 4 Failed: 'Life is a Highway' should be removed."
    assert len(road_trip.get_songs()) == 2, "Integration Test Scenario 4 Failed: Road Trip should now have 2 songs."
    
    # Scenario 5: Delete the Workout playlist and verify the playlist list.
    deleted_playlist = manager.delete_playlist("Workout")
    assert deleted_playlist, "Integration Test Scenario 5 Failed: Workout playlist should be deleted."
    assert len(manager.list_playlists()) == 2, "Integration Test Scenario 5 Failed: There should be 2 playlists remaining."
    
    # Scenario 6: Create a new Party playlist and add a song.
    manager.create_playlist("Party")
    party = manager.get_playlist("Party")
    party.add_song(Song("Uptown Funk", "Bruno Mars", "Uptown Special", "Funk", 270))
    assert len(party.get_songs()) == 1, "Integration Test Scenario 6 Failed: Party should have 1 song."
    
    print("Extended Integration Tests Passed.")
    print("----------------------------------------------------")

def main():
    print("Welcome to the Music Playlist Manager!")
    test_song()
    test_playlist()
    test_playlist_manager()
    integration_test()
    print("All tests completed successfully.")

if __name__ == "__main__":
    main()
