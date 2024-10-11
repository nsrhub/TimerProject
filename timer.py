import subprocess
import time

class Timer:
    """
    Timer class that allows setting a countdown timer based on hours, minutes, and seconds.
    When the countdown ends, a sound is played.
    """

    def __init__(self, hours=0, minutes=0, seconds=0):
        """
        Initialize the Timer with optional hours, minutes, and seconds. 
        Determines if the timer should be set by checking if any time is provided.
        """
        if hours > 0 or minutes > 0 or seconds > 0:
            self.setTimer = True  # Flag indicating if the timer is set
        else:
            self.setTimer = False  # Timer not set

        # Set initial time values
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def minutes(self):
        """
        Get the current minutes value.
        """
        return self._minutes

    @minutes.setter
    def minutes(self, value):
        """
        Set the minutes value and adjust hours if minutes exceed 60.
        """
        if value >= 60:
            self.hours += value // 60  # Add extra hours if minutes exceed 60
            self._minutes = value % 60  # Set remaining minutes
        else:
            self._minutes = value

    @property
    def seconds(self):
        """
        Get the current seconds value.
        """
        return self._seconds

    @seconds.setter
    def seconds(self, value):
        """
        Set the seconds value and adjust minutes if seconds exceed 60.
        """
        if value >= 60:
            self.minutes += value // 60  # Add extra minutes if seconds exceed 60
            self._seconds = value % 60  # Set remaining seconds
        else:
            self._seconds = value

    def countdown(self):
        """
        Starts the countdown based on the provided hours, minutes, and seconds.
        Decrements the time every second until it reaches zero, then plays a sound.
        """
        for _ in range(self.hours + 1):
            for _ in range(self.minutes + 1):
                for _ in range(self.seconds + 1):
                    # Print the current time in HH:MM:SS format
                    print(f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}', end='\r')
                    time.sleep(1)  # Wait for 1 second
                    self.seconds -= 1  # Decrement the seconds
                self.minutes -= 1  # Decrement the minutes
                self.seconds = 59  # Reset seconds to 59 after a full minute
            self.minutes = 59  # Reset minutes to 59 after a full hour
            self.hours -= 1  # Decrement the hours
        self.sound()  # Play sound when countdown ends

    def sound(self):
        """
        Plays a sound when the countdown reaches zero. 
        Plays the sound 3 times.
        """
        if self.hours == -1 and self.setTimer:
            for _ in range(3):
                subprocess.run(['paplay', 'sound.wav'])  # Play sound using 'paplay'





if __name__ == '__main__':
    # Initialize the timer with 0 hours, 60 minutes, and 60 seconds
    timer = Timer(0, 60, 60)
    timer.countdown()  # Start the countdown
