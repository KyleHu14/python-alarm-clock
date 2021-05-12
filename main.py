def alarm(input_time):
    return None

def print_title() -> None:
    print('#' * 26)
    print('#' + '{:^24s}'.format("Alarm Clock App") + '#')
    print('#' * 26)
    print()


def main():
    print_title()
    print('Enter Time in the Following Format : [Hours:Minutes:Seconds]')
    print('Example (5 hours, 5 minutes, 60 seconds) : [5:5:60]\n')
    user_input_time = input('Enter Time: ')

    alarm(user_input_time)

main()