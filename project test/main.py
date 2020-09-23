import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = 'user-top-read' #how much we are allowed to see from user

# these should be delted and instead added to ENV VARs
client_id = 'eb9a37f93d5148e28e113134d65d6c08'
client_secret = '29d3cde540304c43b72e8b344c605f63'
redirect_uri = 'project-songbird-login://callback'

# turn list of lists into dictionary with number of times each item appears in list
def getGenreCounts(user_genres):
    genre_counts = {}
    for genre in user_genres:
        for item in genre:
            if item in genre_counts:
                genre_counts[item] += 1
            else:
                genre_counts[item] = 1
    return genre_counts


#get genre compatability score
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



# authenticate user1 (alex)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri))



#Get dataframe info for user1 (artist name, genres, popularity, link to artist spotify page)

top_artists = sp.current_user_top_artists(25, time_range='long_term')
top_tracks = sp.current_user_top_tracks(50, time_range='short_term')
top_genres = [item['genres'] for item in top_artists['items']]

#Turn dataframe info into arrays containing only necessary information
songs = [item['name'] for item in top_tracks['items']]
artists = [item['name'] for item in top_artists['items']]
genres = [item['genres'] for item in top_artists['items']]


#get genre counts for user1
genre_counts1 = getGenreCounts(genres)



#uncomment whoevers auth token you want to use and comment the other out

#justin auth token
#sp = spotipy.Spotify(auth="BQC0QKIE5rrwvFLfBB3mLxT4CSvyL-nX-idKfuXS_VYt_KRdNs2yYgKyjSCtHJJAF8XKlCA7DA1EKzRcznxWlePqYK_HIq9tRns9rlXSUk3zalsIhJL__0_l50yaSERoJdbdnYhaj7WR1awTgYEC")

#jason auth token
sp = spotipy.Spotify(auth="BQCJzuIk7cIv6IJW__FOLeQrfyXsLYu5TH-9_Sv5muk9wpTKWYGBIJj07zHQIrAv8Gb2w1gjhDxaz5PpZbgeTPW0Ma3bMfWSFHX7eYtQojU8GTYGzBv6oCx2UgR70l1oC1FrrmWafhXEKDsMhu9vvC9OpDruJRg")

#get top artists user2
top_artists2 = sp.current_user_top_artists(25, time_range="long_term")

genres2 = [item['genres'] for item in top_artists2['items']]

#get genre counts for user2
genre_counts2=getGenreCounts(genres2)



# TO DO
# def musicCompScore(df1, df2):
#     total_score = getCompScore(df1('Artists'), df2('Artists'))
#



print('alex genres: ',genre_counts1)
print('justin genres: ',genre_counts2)

print('genre score: ',getGenreScore(genre_counts1,genre_counts2))
