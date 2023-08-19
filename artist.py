from song import *
from album import *
class Artist:
    def __init__(self, firstName, lastName, birthYear):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__birthYear = birthYear
        self.__albums = []
        self.__singles = []

    def getFirstName (self):
        return self.__firstName
    def getLastName (self):
        return self.__lastName
    def getBirthYear (self):
        return self.__birthYear
    def getAlbums (self):
        return self.__albums
    def getSingles (self):
        return self.__singles

    def singles_Adder(self, *newSingle): 
        for j in newSingle:
            if self.__singles == []:
                self.__singles.append(j)
                continue

            sign = True
            for i in self.__singles:
                if not ((i.getTitle() != j.getTitle()) or (i.getReleaseYear() != j.getReleaseYear()) or (i.getDuration() != j.getDuration()) or i.getLikes() != j.getLikes()):
                    sign = False
                    break
            if sign:
                self.__singles.append(j) 


    def album_Adder(self, *newSongs):
        for i in newSongs:
            if self.__albums==[]:
                self.__albums.append(i)
                continue
            sign=True
            for j in self.__albums:
                if not((j.getTitle() != i.getTitle()) or (j.getReleaseYear()!=i.getReleaseYear())):
                    sign=False

            if sign == True:
                self.__albums.append(i)


    def mostLikedSong(self):
        likes = []
        for i in self.__albums:
            for j in i.getSongs():
                likes.append(j.getLikes())
        likes.sort()
        if likes != []:
            albumLikes = likes[-1]
        

        likesOfSingles = []
        for i in self.__singles:
            likesOfSingles.append(i.getLikes())
        likesOfSingles.sort()
        if likesOfSingles != []:
            singleLikes = likesOfSingles[-1]
            
        if likes != [] and likesOfSingles != []:
            if albumLikes >= singleLikes:
                leastLiked = albumLikes
            else:
                leastLiked = singleLikes

        if likes != [] and likesOfSingles == []:
            leastLiked = albumLikes
        if likes == [] and likesOfSingles != []:
            leastLiked = singleLikes
    
        if self.__albums != []:
            for albums in self.__albums:
                for songs in albums.getSongs():
                    if songs.getLikes() == leastLiked:
                        return songs

        if self.__singles != []:
            for song in self.__singles:
                if song.getLikes() == leastLiked:
                    return song

    def leastLikedSong(self):
        global albumLikes
        likes = []
        for i in self.__albums:
            for j in i.getSongs():
                likes.append(j.getLikes())
        likes.sort()
        if likes != []:
            albumLikes = likes[0]
            

        global singleLikes
        likesOfSingles = []
        for i in self.__singles:
            likesOfSingles.append(i.getLikes())
        likesOfSingles.sort()
        if likesOfSingles != []:
            singleLikes = likesOfSingles[0]
    
        if self.__albums != []:
            for albums in self.__albums:
                for songs in albums.getSongs():
                    if songs.getLikes() == albumLikes:
                        return songs

        if self.__singles != []:
            for song in self.__singles:
                if song.getLikes() == singleLikes:
                    return song


    def totalLikes(self):
        global total_likes
        totalAlbumLikes = []
        likes = 0
        for i in self.__albums:
            for j in i.getSongs():
                totalAlbumLikes.append(j.getLikes())
        likes+=sum(totalAlbumLikes)
        
        totalSingleLikes = []
        singlesLikes = 0
        for i in self.__singles:
                totalSingleLikes.append(i.getLikes())
        singlesLikes+=sum(totalSingleLikes)
        total_likes = likes + singlesLikes
        return total_likes



    def __str__(self):
        global total_likes
        totalAlbumLikes = []
        likes = 0
        for i in self.__albums:
            for j in i.getSongs():
                totalAlbumLikes.append(j.getLikes())
        likes+=sum(totalAlbumLikes)
        
        totalSingleLikes = []
        singlesLikes = 0
        for i in self.__singles:
                totalSingleLikes.append(i.getLikes())
        singlesLikes+=sum(totalSingleLikes)
        total_likes = likes + singlesLikes

        
        return f'Name: {self.__firstName} {self.__lastName},Birth year:{self.__birthYear},Total likes:{total_likes}'





    
