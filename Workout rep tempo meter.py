import time
import pyttsx3 as pt
eng=pt.init()

print('Enter your rep time tempo for a set:',end='\n')
time_tempo=input()
time_tempo=time_tempo.split(' ')
time_tempo=[int(i) for i in time_tempo]
time.sleep(1)
print('Now starting tempo count. GET READY!!!!!!')
time.sleep(2)
reps=0
while True:
    if reps == 15:break
    print('Number of reps completed: ',reps)
    reps+=1
    for phase in time_tempo:
        while phase!=0:
            ##print(phase)
            eng.say(phase)
            time.sleep(1)
            phase-=1
            eng.runAndWait()

    

