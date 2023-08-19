from song import *
from album import *
from artist import *
class SpotiPy:
    def __init__(self):
        self.__artists = []

    def getArtists(self):
        return self.__artists

    def addArtists(self, *newArtist):
        for j in newArtist:
            if self.__artists == []:
                self.__artists.append(j)
                continue

            sign = True
            for i in self.__artists:
                if not ((i.getFirstName() != j.getFirstName()) or (i.getLastName() != j.getLastName()) 
                or  (i.getBirthYear() != j.getBirthYear())):
                    sign = False
            if sign:
                self.__artists.append(j)



    def getTopTrendingArtist(self):
        topArtist = 0
        for artists in self.__artists:
            if artists.totalLikes() >= topArtist:
                topArtist = artists.totalLikes()

        for artist in self.__artists:
            if artist.totalLikes() == topArtist:
                return (artist.getFirstName(), artist.getLastName())
            


    def getTopTrendingAlbum(self):
        popularAlbumLikes = []
        mostLike = 0
        if self.__artists != []:
            for artists in self.__artists:
                for albums in artists.getAlbums():
                    popularAlbumLikes.append(albums.helperAlbumLikes())
            popularAlbumLikes.sort()
            mostLike = popularAlbumLikes[-1]

            for artist in self.__artists:
                for album in artist.getAlbums():
                    if album.helperAlbumLikes() == mostLike:
                        return album
        else:
            return None
            



    def getTopTrendingSong(self):
        album_popular_song = 0
        album_likes = []
        for i in self.__artists:
            for j in i.getAlbums():
                for l in j.getSongs():
                    album_likes.append(l.getLikes())
        for k in album_likes:
            if k >= album_popular_song:
                album_popular_song = k


        single_popular_song = 0
        single_likes = []
        for i in self.__artists:
            for j in i.getSingles():
                single_likes.append(j.getLikes())

        for k in single_likes:
            if k >= single_popular_song:
                single_popular_song = k

        
        most_popular_song = 0
        if album_popular_song >= single_popular_song:
            most_popular_song = album_popular_song
        else:
            most_popular_song = single_popular_song

        for i in self.__artists:
            if i.getAlbums() != []:
                for i in i.getAlbums():
                    for j in i.getSongs():
                        if j.getLikes() == most_popular_song:
                            return j


        for a in self.__artists:
            for b in a.getSingles():
                if b.getLikes() == most_popular_song:
                    return b


    def loadFromFiles(self):
        pass






