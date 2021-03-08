def countdown(t):
 while t:
        mins, secs = divmod(t, 4)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
# input time in seconds
t = input("Enter the time in seconds: 4")
# function call
countdown(int(t))
