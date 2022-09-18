def get_total_duration_for_artist(song_dictionary, artist):
    try:
        songs = song_dictionary.get(artist)
    except TypeError:
        print("ERROR: Invalid input!")
        return 0

    if songs is None:
        print("ERROR: " + artist + " is not available.")
        return 0
    
    dur = 0
    for song in songs:
        if len(song)<2:
            print("ERROR: Missing the duration in '" + song[0] + "'.")   
            return dur     
        else:
            dur += song[1] 

    return dur


song_dict = {'Wiz Khalifa': [('Say Yeah',241), ('Something New', 200), ('See You Again', ), ('We Own It',227)], 'Mark Ronson': [('Uptown Funk', 270)], 'PSY': [('Gangnam Style', 219), ('New Face', 190)]}
print(get_total_duration_for_artist(song_dict, 'PSY'))
print(get_total_duration_for_artist(song_dict, 'Taylor Swift'))
print(get_total_duration_for_artist(song_dict, [123]))
print(get_total_duration_for_artist(song_dict, 'Wiz Khalifa'))