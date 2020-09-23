import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = 'user-top-read' #how much we are allowed to see from user

# these should be delted and instead added to ENV VARs
client_id = 'eb9a37f93d5148e28e113134d65d6c08'
client_secret = '29d3cde540304c43b72e8b344c605f63'
redirect_uri = 'project-songbird-login://callback'


def getGenreCounts(user_genres):
    genre_counts = {}
    for genre in user_genres:
        for item in genre:
            if item in genre_counts:
                genre_counts[item] += 1
            else:
                genre_counts[item] = 1
    return genre_counts


# authenticate use
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri))



#Get dataframe info (artist name, genres, popularity, link to artist spotify page)

top_artists = sp.current_user_top_artists(25, time_range='long_term')
top_tracks = sp.current_user_top_tracks(50, time_range='short_term')
top_genres = [item['genres'] for item in top_artists['items']]


songs = [item['name'] for item in top_tracks['items']]
#print(songs)

artists = [item['name'] for item in top_artists['items']]
genres = [item['genres'] for item in top_artists['items']]

genre_counts1 = getGenreCounts(genres)




#sp = spotipy.Spotify(auth="BQC0QKIE5rrwvFLfBB3mLxT4CSvyL-nX-idKfuXS_VYt_KRdNs2yYgKyjSCtHJJAF8XKlCA7DA1EKzRcznxWlePqYK_HIq9tRns9rlXSUk3zalsIhJL__0_l50yaSERoJdbdnYhaj7WR1awTgYEC")
sp = spotipy.Spotify(auth="BQCJzuIk7cIv6IJW__FOLeQrfyXsLYu5TH-9_Sv5muk9wpTKWYGBIJj07zHQIrAv8Gb2w1gjhDxaz5PpZbgeTPW0Ma3bMfWSFHX7eYtQojU8GTYGzBv6oCx2UgR70l1oC1FrrmWafhXEKDsMhu9vvC9OpDruJRg")
top_artists2 = sp.current_user_top_artists(25, time_range="long_term")

genres2 = [item['genres'] for item in top_artists2['items']]

genre_counts2=getGenreCounts(genres2)





popularity = [item['popularity'] for item in top_artists['items']]
urls = [item['external_urls']['spotify'] for item in top_artists['items']]

# create pandas dataframe of above data
df_data = {'Artists': artists, 'Genres': genres, 'Popularity': popularity, 'URLs': urls}
df = pd.DataFrame(df_data)
df.set_index('Artists', inplace=True)


# def musicCompScore(df1, df2):
#     total_score = getCompScore(df1('Artists'), df2('Artists'))
#


def getGenreScore(user1, user2):
    points = 0
    for item in user1:
        if item in user2:
            if user1[item] > 10 and user2[item]>10:
                points+=10
            elif user1[item] > 5 and user2[item] > 5:
                points+=7
            else:
                points+=5
    return points


print('alex genres: ',genre_counts1)
print('justin genres: ',genre_counts2)

print('genre score: ',getGenreScore(genre_counts1,genre_counts2))
