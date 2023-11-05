"""Import "os" to help Python recognize filepaths independent from the operating system.
   Import "time" so that the program can run a timer.
   Import "keyboard" to detect specific keystrokes."""
import os
import time
import keyboard

# These keys must all be different.
PAUSE_RESUME_KEY = "down"
NOTE_KEY = "Shift"
DISPLAY_TIME_KEY = "ctrl"
QUIT_KEY = "q"


def seconds_to_h_m_s(seconds):
    """This method converts a time in seconds to a time in hours, minutes and seconds."""
    hours = seconds // 3600
    seconds -= (hours * 3600)
    minutes = seconds // 60
    seconds -= (minutes * 60)
    return hours, minutes, seconds


def h_m_s_to_seconds(hours, minutes, seconds):
    """This method converts a time in hours, minutes and seconds to a time in seconds."""
    return (hours * 3600) + (minutes * 60) + seconds


def timestamp_to_h_m_s(timestamp):
    """This method converts a timestamp in the format "HH:MM:SS" to hours, minutes and seconds"""
    first_colon = timestamp.find(":")
    second_colon = timestamp.find(":", first_colon + 1)
    hours = int(timestamp[:first_colon])
    minutes = int(timestamp[first_colon + 1:second_colon])
    seconds = int(timestamp[second_colon + 1:])
    return hours, minutes, seconds


def h_m_s_to_timestamp(hours, minutes, seconds):
    """This method converts a time in hours, minutes and
    seconds to a timestamp in the format 'HH:MM:SS'"""
    result = ""
    if hours < 10:
        result += "0"
    result += f"{int(hours)}:"
    if minutes < 10:
        result += "0"
    result += f"{int(minutes)}:"
    if seconds < 10:
        result += "0"
    result += f"{int(seconds)}"
    return result


def h_m_s_to_words(hours, minutes, seconds):
    """
    This method converts a time in hours, minutes and
    seconds to words that can be inserted into a sentence.
    Different examples of inputs and their corresponding outputs are:
    h_m_s_to_words(0, 0, 0) -> "0 seconds"
    h_m_s_to_words(0, 2, 17) -> "2 minutes and 17 seconds"
    h_m_s_to_words(1, 0, 0) -> "1 hour"
    h_m_s_to_words(2, 0, 1) -> "2 hours and 1 second"
    h_m_s_to_words(2, 3, 4) -> "2 hours, 3 minutes and 4 seconds"
    """
    output = ""
    if not (hours or minutes or seconds):
        output += "0 seconds"
    else:
        if hours != 0:
            output += f"{hours} hour"
            if hours > 1:
                output += "s"
        if minutes != 0:
            if hours != 0:
                if seconds != 0:
                    output += ", "
                else:
                    output += " and "
            output += f"{minutes} minute"
            if minutes > 1:
                output += "s"
        if seconds != 0:
            if hours != 0 or minutes != 0:
                output += " and "
            output += f"{seconds} second"
            if seconds > 1:
                output += "s"
    return output


def total_seconds_actual(start_minus_offset, paused_time):
    """This method returns the actual number of seconds that have passed when factoring
    in the timer's initial offset and the total amount of time spent paused."""
    return time.perf_counter() - start_minus_offset - paused_time


def seconds_to_timestamp(seconds):
    """This method generates a timestamp based on the provided number of seconds."""
    cur_hours, cur_minutes, cur_seconds = seconds_to_h_m_s(seconds)
    timestamp = h_m_s_to_timestamp(cur_hours, cur_minutes, cur_seconds)
    return timestamp


print("\nEnter the name of the output file where you "\
        "would like your annotations to be saved. "\
        "You will most likely want to write to a file whose name ends in \".txt\". "\
        "If no file exists with the name you entered, "\
        "a new file will be created with that name.\n")
OUTPUT_FILE_CHOSEN = False

# This loop asks the user to name the output file.
while not OUTPUT_FILE_CHOSEN:

    # The user enters the name of their output file.
    output_file_name = input("Output file name: ")
    print()
    output_path = os.path.join(output_file_name)

    # The program figures out whether the user specified an absolute or relative file path.
    if not os.path.isabs(output_path):
        output_path = os.path.join(os.path.dirname(__file__), output_file_name)

    # If the specified file name is actually a directory, this will not be accepted.
    if os.path.isdir(output_path):
        print(f"\"{output_path}\" is a directory. You must specify a file name.\n")
        continue
    file_directory = os.path.split(output_path)[0]
    if os.path.exists(file_directory):

        if os.path.exists(output_path):

            # If a file already exists with the entered output file name, the user will
            # be asked whether they are sure that they would like to make this their
            # output file. New notes will be appended to the end of the file.
            print(f"\"{output_path}\" already exists. Would you like to write to this "\
                "file anyway? Don't worry, your new notes will be added to the end of "\
                "this file and your previous work will not be erased.\n")
            while True:
                response = input("Confirm existing output file (y/n): ").lower()

                # If the user confirms that they would like to append to an
                # output file that already exists, the loop will terminate
                # and the program will move onto the next question.
                if response in ('y', "yes"):
                    print(f"\nThe output will be saved at \"{output_path}\"...")
                    OUTPUT_FILE_CHOSEN = True
                    break

                # If the user decides not to append to an output file that already exists,
                # the program will ask the user for the name of an output file again.
                if response in ('n', "no"):
                    print()
                    break

                # The program will prompt the user for a response again if they did
                # not reply with either "y"/"yes" or "n"/"no" in response to the question
                # of whether they would like to append their output to an already existing file.
                print("\nI couldn't quite understand that. Please respond "\
                "with either \"y\"/\"yes\" or \"n\"/\"no\".\n")

        # If the user specified a file that does not exist yet, the file will be created.
        else:
            print(f"\"{output_path}\" does not exist yet. This file will be created...")
            OUTPUT_FILE_CHOSEN = True

    # If the user specified a file in a directory that does
    # not exist, the program will reject their response.
    else:
        print(f"\"{file_directory}\" is not an existing directory. "\
            "You must create this directory first.\n")
print()

# The user chooses what time the timer should be at when it starts.
START_TIME_STR = None
print("Enter a start time in the format HH:MM:SS, or simply press "\
    "\"Enter\" for a start time of 00:00:00. For example, to start the "\
    "timer at two minutes and 15 seconds, enter \"00:02:15\".\n\nStart time: ", end="")
while not START_TIME_STR:

    # The user specifies their desired start time.
    START_TIME_STR = input()

    # If the user does not provide any input, the start time will be set to 0.
    if START_TIME_STR == "":
        START_TIME_STR = "00:00:00"
        start_hours, start_minutes, start_seconds = timestamp_to_h_m_s(START_TIME_STR)

    # The program tries to figure out what starting time the user has entered.
    else:

        # The program tries to interpret the user's input in the HH:MM:SS format.
        try:
            time.strptime(START_TIME_STR, "%H:%M:%S")

        # The program will not accept a time that is not in the HH:MM:SS format.
        except ValueError:
            START_TIME_STR = None
            print("\nPlease use the following format: HH:MM:SS\n\nStart time: ", end="")

        # If the user entered a valid time in the HH:MM:SS format, the loop
        # will terminate and the program will move onto the next question.
        else:
            start_hours, start_minutes, start_seconds = timestamp_to_h_m_s(START_TIME_STR)

            # The minutes and seconds portions of the timer cannot be greater than 60.
            if start_minutes >= 60 or start_seconds >= 60:
                START_TIME_STR = None
                print("\nYou cannot set the number of minutes or seconds "\
                    "to greater than 60.\n\nStart time: ", end="")

# The program informs the user of the start time they have entered.
hms_words = h_m_s_to_words(start_hours, start_minutes, start_seconds)
print(f"\nThe start time is set to {hms_words}...\n")

# The start time is converted to seconds so that the
# start time is easier for the program to interpret.
start_offset = h_m_s_to_seconds(start_hours, start_minutes, start_seconds)

# The program converts the start time to a timestamp.
starting_timestamp = h_m_s_to_timestamp(start_hours, start_minutes, start_seconds)

# The program provides instructions to the user.
print("-----INSTRUCTIONS-----\n")
print(f"MARK CURRENT TIME: {DISPLAY_TIME_KEY}\n")
print(f"CREATE NOTE: {NOTE_KEY} ", end="")
print("(note will be timestamped with the time you started your note)\n")
print("SAVE NOTE: Enter\n")
print(f"PAUSE/RESUME: {PAUSE_RESUME_KEY} ", end="")
print("(you can even write notes while paused)\n")
print(f"QUIT: {QUIT_KEY}\n")
print("Annotations will be saved in the output file you specified.\n")
print(f"Ready? To start the timer, press {PAUSE_RESUME_KEY}.\n")

# The program waits for the user to start the timer.
while True:

    #if keyboard.is_pressed(' '):
    if keyboard.is_pressed(PAUSE_RESUME_KEY):

        # The program starts the timer.
        start_raw = time.perf_counter()
        break

start_raw_minus_start_offset = start_raw - start_offset

with open(output_path, "a+", encoding="utf-8") as output_file:

    # The program records the initial starting time.
    starting_lines = f"##############################\n[{starting_timestamp}] -----TIMER START-----"
    print(starting_lines)
    output_file.write(f"{starting_lines}\n")

    TOTAL_PAUSED_TIME = 0.0
    IS_PAUSED = False
    LAST_RECORDED_SECOND = 0
    PAUSED_TIME_PRINTED = False
    time_of_pause = time.perf_counter()
    total_seconds = total_seconds_actual(start_raw_minus_start_offset, TOTAL_PAUSED_TIME)

    while keyboard.is_pressed(PAUSE_RESUME_KEY):
        pass

    # This loop listens for user input and responds accordingly.
    while True:

        # If the timer IS paused, the time that the timer is currently paused at will be printed.
        if IS_PAUSED:
            if not PAUSED_TIME_PRINTED:
                cur_timestamp = seconds_to_timestamp(total_seconds)
                print(f"\r{cur_timestamp}   ", end="")
                PAUSED_TIME_PRINTED = True

        # If the timer IS NOT paused, the program calculates and
        # displays the total amount of seconds that have passed.
        else:
            total_seconds = total_seconds_actual(start_raw_minus_start_offset, TOTAL_PAUSED_TIME)
            NEAREST_CURRENT_SECOND = int(total_seconds)
            if (NEAREST_CURRENT_SECOND != LAST_RECORDED_SECOND) and \
                (abs(total_seconds - NEAREST_CURRENT_SECOND) < 0.001):
                cur_timestamp = seconds_to_timestamp(total_seconds)
                print(f"\r{cur_timestamp}   ", end="")
                LAST_RECORDED_SECOND = NEAREST_CURRENT_SECOND
                PAUSED_TIME_PRINTED = False

        # If the user presses NOTE_KEY, a new note will be recorded.
        if keyboard.is_pressed(NOTE_KEY):
            cur_timestamp = seconds_to_timestamp(total_seconds)
            print(f"\r[{cur_timestamp}] ", end="")
            new_note = input()
            output_file.write(f"[{cur_timestamp}] {new_note}\n")
            PAUSED_TIME_PRINTED = False

        # If the user presses PAUSE_RESUME_KEY, the timer will be either paused or unpaused,
        # depending on whether the timer is currently paused or unpaused.
        elif keyboard.is_pressed(PAUSE_RESUME_KEY):

            # If the timer is currently paused, the timer will be unpaused and the total amount of
            # time spent paused will be calculated so that it can be discounted from the timer.
            if IS_PAUSED:
                time_of_unpause = time.perf_counter()
                TOTAL_PAUSED_TIME += (time_of_unpause - time_of_pause)
                total_seconds = \
                    total_seconds_actual(start_raw_minus_start_offset, TOTAL_PAUSED_TIME)
                cur_timestamp = seconds_to_timestamp(total_seconds)
                resumed_time_line = f"[{cur_timestamp}] -----RESUME-----"
                print(f"\r{resumed_time_line}")
                output_file.write(f"{resumed_time_line}\n")
                IS_PAUSED = False

            # If the timer is currently unpaused, the timer will be paused.
            else:
                time_of_pause = time.perf_counter()
                cur_timestamp = seconds_to_timestamp(total_seconds)
                paused_time_line = f"[{cur_timestamp}] -----PAUSE-----"
                print(f"\r{paused_time_line}")
                output_file.write(f"{paused_time_line}\n")
                IS_PAUSED = True

            PAUSED_TIME_PRINTED = False
            while keyboard.is_pressed(PAUSE_RESUME_KEY):
                pass

        # If the user presses DISPLAY_TIME_KEY, the timer's current time will be displayed.
        elif keyboard.is_pressed(DISPLAY_TIME_KEY):
            cur_timestamp = seconds_to_timestamp(total_seconds)
            cur_time_line = f"[{cur_timestamp}] -----CURRENT TIME-----"
            print(f"\r{cur_time_line}")
            output_file.write(f"{cur_time_line}\n")
            PAUSED_TIME_PRINTED = False
            while keyboard.is_pressed(DISPLAY_TIME_KEY):
                pass

        # If the user presses QUIT_KEY, the timer will stop and the program will exit.
        elif keyboard.is_pressed(QUIT_KEY):
            cur_timestamp = seconds_to_timestamp(total_seconds)
            quit_time_line = f"[{cur_timestamp}] -----QUITTING-----"
            print(f"\r{quit_time_line}")
            output_file.write(f"{quit_time_line}\n")
            break
