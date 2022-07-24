
song_list = [('See You Again', 'Wiz Khalifa', 229), ('We Own It', 'Wiz Khalifa', 227), ('Gangnam Style', 'PSY', 219)]

def durDict(song_list):
    dict = {}
    duration = 0
    artist = ""
    for song in song_list:
        if artist == song[1]:
            duration += song[2]
        else:
            artist = song[1]
            duration = song[2]
            
        dict[artist] = duration

    return dict

def titleDict(song_list):
    dict = {}
    titles = []
    artist = ""
    for song in song_list:
        if artist == song[1]:
            titles.append(song[0])
        else:
            artist = song[1]
            titles = [song[0]]
            
        dict[artist] = titles

    return dict

print(durDict(song_list))
print(titleDict(song_list))