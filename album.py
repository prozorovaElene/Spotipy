from song import Song

class Album:
    def __init__(self, title, releaseYear):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__songs = []

    def getTitle (self):
        return self.__title
    def getReleaseYear (self):
        return self.__releaseYear
    def getSongs (self):
        return self.__songs


    def addSongs (self, *newSongs):
        counter = 0
        for i in newSongs:
            while (self.__songs == []):
                counter = counter + 1
                self.__songs.append(i)
                continue
            sign = True
            for j in self.__songs:
                if not ((i.getTitle() != j.getTitle()) or (i.getReleaseYear() != j.getReleaseYear()) or (i.getDuration() != j.getDuration())):
                    sign = False
            if sign == True:
                counter = counter + 1
                self.__songs.append(i)
        return counter

    def sortBy(self, byKey, reverse):
        return self.__songs.sort(key=byKey, reverse=reverse)
    def sortByName(self, reverse):
        return self.sortBy(lambda x: x.getTitle(), reverse)
    def sortByPopularity(self, reverse):
        return self.sortBy(lambda x: x.getLikes(), reverse)
    def sortByDuration(self, reverse):
        return self.sortBy(lambda x: x.getDuration(), reverse)
    def sortByReleaseYear(self, reverse):
        return self.sortBy(lambda x: x.getReleaseYear(), reverse)

    def helperAlbumLikes(self):
        likes = 0
        for i in self.__songs:
            likes+=i.getLikes()
        return likes


    def __str__(self):
            string_Album = '{'
            for i in self.__songs:
                string_Album+=str(i) + '|'
            if self.__songs==[]:
                string_Album = "{}"
            return f'Title:{self.__title},Release year:{self.__releaseYear},songs:{string_Album[:-1]+"}"}'

    
