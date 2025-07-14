import time
# countdown_timer.py
# countdown_timer.py this module implements a countdown timer
def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

if __name__ == "__main__":
    try:
        total_seconds = int(input("Enter the time in seconds for countdown: "))
        countdown_timer(total_seconds)
    except ValueError:
        print("Please enter a valid integer for seconds.")  