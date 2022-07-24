def read_song_info(filename):
    song_list = []
    
    input_file = open("/Users/nan/Projects/fsd/max/Songs5.txt", "r")
    songs = input_file.readlines()
    input_file.close()

    for song in songs:
        list = song.split(',')
        list[2] = int(list[2])
        tup = tuple(list)
        song_list.append(tup)

    return song_list

print(read_song_info("Songs5.txt"))