def create_song_dictionary(song_list):
    dict = {}
    titles = []
    artist = ""
    for songst in song_list:
        song = songst.split(',')
        if song[1] in dict.keys():
            dict.get(song[1]).append((song[0], song[2]))
        else:
            artist = song[1]
            titles = [(song[0], song[2])]
            dict[artist] = titles

    return dict


songs = ["See You Again,Wiz Khalifa,229", "Uptown Funk,Mark Ronson,270", "Something New,Wiz Khalifa,200", "New Face,PSY,190", "Gangnam Style,PSY,219"]
songs_dict = create_song_dictionary(songs)
for key in sorted(songs_dict):
    print(key, sorted(songs_dict[key]))
print(type(songs_dict))
print(type(songs_dict['Wiz Khalifa']))
print(type(songs_dict['Wiz Khalifa'][0]))

for key in sorted(songs_dict):
    print(key, sorted(songs_dict[key]))
