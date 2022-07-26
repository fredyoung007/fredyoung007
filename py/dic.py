def update_albums_dictionary(album_dictionary, album_name, song_list):
    if album_name in album_dictionary.keys():
        album_dictionary[album_name] += song_list
    else: 
        album_dictionary[album_name] = song_list

    album_dictionary[album_name] = list(set(album_dictionary[album_name]))
    album_dictionary[album_name].sort()

albums = {
    "Live at the Bedford": ["Fall"]
}

songs = ["Wake Me Up", "Homeless", "Homeless"]
update_albums_dictionary(albums, "Live at the Bedford", songs)
update_albums_dictionary(albums, "New album", songs)
update_albums_dictionary(albums, "New album", ["Anothre song"])

for key in sorted(albums.keys()):
    print(key, albums[key])
