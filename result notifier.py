import bs4,requests
from plyer import notification as nf
import time as t


#http://www.mumresults.in/

def search(dd,prgno):
    page = requests.get("http://www.mumresults.in/")
    data = bs4.BeautifulSoup(page.text, 'html.parser')
    #data = data.select('.counterthree')
    date = [str(i)[76:86] for i in list(data.select('.rslt_date'))]
    prg = [str(i)[71:79].replace("<","") for i in list(data.select('.prgno'))]

    for i,j in zip(date,prg):
        if i[3:] == dd and j == prgno:
            return True


def tell_me():

    title = 'Result Arrived'
    message= 'Results are out!'
    nf.notify(title= title,message= message,app_icon = None,timeout= 10,toast=False)

print('For example: Month will be 08/2022 and Exam No. is 1T01028')
month = input('Enter in the following format only: MM/YYYY:  ')
prog_id = input('Enter your Exam No. printed on your hall ticket:  ')
minutes = int(input("Enter the time interval in between to check your results in minutes"))
wait_time = minutes * 60
print('\n')


while True:
    a = search(month,prog_id)
    if a == True:
        tell_me()
        break
    print("Result not out yet! Will keep checking.")
    t.sleep(wait_time)


