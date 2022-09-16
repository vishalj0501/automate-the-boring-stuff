import pyinputplus as inp
import random
import time

for i in range(10):
    try:
        a=random.randint(0,9)
        b=random.randint(0,9)
        
        ans=inp.inputInt("%s x %s = "%(a,b),limit=3,timeout=8)

        if(ans==a*b):
            print("Correct!")
            time.sleep(3)
        else:
            print("Wrong answer!")

    except TimeoutError:
        print("Time Out, Exceeded 8 seconds")