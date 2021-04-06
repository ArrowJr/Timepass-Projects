import time
import pyttsx3 as pt
eng=pt.init()

##print('Enter your rep time tempo for a set: ',end='\n')
##time_tempo=input()
##time_tempo=time_tempo.split(' ')
##time_tempo=[int(i) for i in time_tempo]
while True:
    print('''What exercise will you perform today?\n
                    Press 1 for your dumbell and barbell
                    Press 2 for pushups of all variations
                    Press 3 for bench press and hex press
                    Press 4 for cutomization

            ''')
    t=input()
    if t == '1':time_tempo=[2,2,4,1]
    elif t == '2':time_tempo=[2,2,1]
    elif t == '3':time_tempo=[2,4,3]
    else:
        print('Enter your rep time tempo for a set: ',end='\n')
        time_tempo=input()
        time_tempo=time_tempo.split(' ')
        time_tempo=[int(i) for i in time_tempo]

    time.sleep(1)
    print('Now starting tempo count. GET READY!!!!!!')
    time.sleep(2)
    set_reps=input('How many reps?: ')
    reps=0
    while True:
        if reps == int(set_reps):break
        print('Number of reps completed: ',reps)
        reps+=1
        for phase in time_tempo:
            j=1
            while j <= phase:
                eng.say(j)
                time.sleep(1)
                j+=1
                eng.runAndWait()







##    for phase in time_tempo:
##        while phase!=0:
##            print(phase)
##            eng.say(phase)
##            time.sleep(1)
##            phase-=1
##            eng.runAndWait()

    

