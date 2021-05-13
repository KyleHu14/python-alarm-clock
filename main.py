import time 
import datetime

def print_title() -> None:
    # Prints the title / welcome string when you open the app
    print('#' * 26)
    print('#' + '{:^24s}'.format("Alarm Clock App") + '#')
    print('#' * 26)
    print()


def take_input() -> str:
    # Takes the input from the user and checks if the input is correct
    print('Enter Time in the Following Format : [Hours:Minutes:Seconds]')
    print('Example (5 hours, 5 minutes, 60 seconds) : 5:5:60\n')
    user_input_time = input('Enter Time: ')

    while not _check_input(user_input_time):
        print('[ERROR] : Incorrect input detected, please re-enter the time.')
        user_input_time = input('Enter Time : ')
        print()
    
    return user_input_time


def _check_input(input_time : str) -> bool:
    # When given a string, checks if the input fulfills the int:int:int format
    if input_time.count(':') >= 4:
        return False 
    
    if input_time.isalpha():
        return False 
        
    if ':' in input_time:
        for x in input_time.split(':'):
            if x.isalpha():
                return False 
    
    return True


def convert_time(input_time : str) -> int:
    # Converts the input time in the format hour:min:sec and converts it to seconds

    hours = int(input_time.split(':')[0])
    minute = int(input_time.split(':')[1])
    sec = int(input_time.split(':')[2])

    return (hours * 60 * 60) + (minute * 60) + sec


def countdown(secs : int) -> None:
    while secs > 0:
        print(datetime.timedelta(seconds=secs), end='\r')
        time.sleep(1)
        secs -= 1


def main() -> None:
    print_title()
    final_time = convert_time(take_input())
    countdown(final_time)

main()