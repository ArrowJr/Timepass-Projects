import os
import time
import random
print('Welcome to Movie Picker.')
towatch=list()

##for i in range(len(os.listdir('D://Movies'))):
##    movie=os.listdir('D://Movies')[i]
##    towatch.append(movie)


def ScanAgain():    
    file=open("UnWatchedMovies.txt","w")
    for j in range(len(os.listdir('D://Movies'))):
        file.write(os.listdir('D://Movies')[j]+"\n")   
    file.close()

#def EditMovies():
    
def MoviePicker():
    print('Hold on while we fetch your movie list')
    for i in range(len(os.listdir('D://Movies'))):
        movie=os.listdir('D://Movies')[i]
        towatch.append(movie)
##    file=open("UnWatchedMovies.txt","r")
##    for i in towatch:
##        print(i)
##        if i not in file:
##            towatch.remove(i)
##        else:continue
##    file.close()
    for a in range(len(towatch)):print(towatch[a])
    number=random.randint(1,len(towatch)-1)
    time.sleep(2)
    movie=towatch[number]
    print('And the movie of today is:\n',movie)


MoviePicker()    
##ScanAgain()
