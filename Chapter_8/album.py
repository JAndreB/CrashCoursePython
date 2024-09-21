def make_album(artist_name, album_title, no_of_songs=''):
    """creates a dictionary with album details"""
    if no_of_songs:
        album = {'artist': artist_name, 'album': album_title, 'no_of_songs': no_of_songs}
    else:
        album = {'artist': artist_name, 'album': album_title}

    return album

list_of_albums = []

while True:
    print("\nGive us the album info!")
    print("Press q to quit at any time")
    name = input("Artist: ")
    if name == 'q':
        break
    alb = input("Album name: ")
    if alb == 'q':
        break

    alb_info = make_album(name.title(), alb.title())
    print(alb_info)
    list_of_albums.append(alb_info)
    print(list_of_albums)


