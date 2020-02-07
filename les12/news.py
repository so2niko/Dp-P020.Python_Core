import time
from datetime import date

class News:
    def __init__(self, li):
        print("Создание новой записи:\n")
        self.__nonstruct = []
        self.__headers = li[0]#(input("Введите заголовок новости:\n")).upper()
        self.__tags = li[2]#input("Введите хештеги через пробел:\n")
        self.__pub_date = li[1]#time.gmtime()
        self.__published = []
        self.__record = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'#input("Введите запись:\n")

    @property
    def headers(self):
        return(self.__headers)
        
    @property
    def tags(self):
        hashtags = []
        hashtags_mass = self.__tags.split()
        for each in hashtags_mass:
            hashtag = "#"+each
            hashtags.append(hashtag)
            self.__tags = " ".join(hashtags)
        return(self.__tags)

    @property    
    def pub_date(self):
        pub_time = self.__pub_date
        self.__pub_date = [str(pub_time[0]), str(pub_time[1]), str(pub_time[2])]
        return(self.__pub_date)

    @property
    def record(self):
        return(self.__record)

    def published(self):
        
        c_time = time.gmtime()
        #c = date(c_time[0], c_time[1], c_time[2])
        c = date(2020,2,2)
        p = date(int(self.__pub_date[0]), int(self.__pub_date[1]), int(self.__pub_date[2]))
        
        diff = (c - p).days
        if diff == 0:
            return("Posted today")
        elif diff > 7:
            publ = [self.__pub_date[2], self.__pub_date[1], self.__pub_date[0]]
            return(f"Posted {'.'.join(publ)}")
        else:
            return(f"Posted {diff} days ago")
            
    def print(self):
        print("-" * 30)
        print(f"\n - - - - - {self.__headers} - - - - - " )
        print(f"\n{self.published()}\n")
        print("-" * 30)
        print(f"\n{self.__record}")
        print(f"\n{self.tags}")


try:   
    newsList = []
    file = open('data2.csv', 'r')
    for line in file.readlines():
        newsList.append(News(line.split(',')))

    print(pe)
except:
    print('Error. What do we do?')






