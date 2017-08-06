import webbrowser
import time
print("This program started on: " + str(time.ctime()) + "\n")
for i in range(0,3):
    time.sleep(5)
    webbrowser.open("https://youtu.be/jCHriYAr6Qw")
    j = i+1
    print("Loop count: " + str(j) + "\nCurrent time: " + str(time.ctime()))

