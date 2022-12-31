
def songs_and_is_liked_or_not(all_songs,user):
    liked_list = list()
    for song in all_songs:
            try:
                user.songs.get(pk=song.id)
                liked_list.append(1)
            except:
                liked_list.append(0)
    return zip(all_songs, liked_list)