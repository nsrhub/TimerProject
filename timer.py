import subprocess
import time

class Timer:
    """
    Timer class used to create a countdown based on the provided hours, minutes, and seconds.
    
    Attributes:
        hours (int): Number of hours for the timer.
        minutes (int): Number of minutes for the timer.
        seconds (int): Number of seconds for the timer.
        isTimer (bool): A flag indicating if the timer is set to a specific time.
    """
    
    def __init__(self, hours=0, minutes=0, seconds=0):
        """
        Initializes the Timer instance with the given hours, minutes, and seconds.

        Args:
            hours (int): The number of hours. Default is 0.
            minutes (int): The number of minutes. Default is 0.
            seconds (int): The number of seconds. Default is 0.
        """
        # Check if the timer is set to a specific time
        self.isTimer = True if hours or minutes or seconds else False
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        

    @property
    def minutes(self):
        """
        Getter for minutes. Returns the stored minute value.
        """
        return self._minutes


    @minutes.setter
    def minutes(self, value):
        """
        Setter for minutes. Updates the minute value and converts excess minutes into hours.

        Args:
            value (int): New minute value.
        """
        if value >= 60:
            self.hours += value // 60  # Convert excess minutes into hours
            self._minutes = value % 60  # Store the remaining minutes
        else:
            self._minutes = value


    @property
    def seconds(self):
        """
        Getter for seconds. Returns the stored second value.
        """
        return self._seconds


    @seconds.setter
    def seconds(self, value):
        """
        Setter for seconds. Updates the second value and converts excess seconds into minutes.

        Args:
            value (int): New second value.
        """
        if value >= 60:
            self.minutes += value // 60  # Convert excess seconds into minutes
            self._seconds = value % 60  # Store the remaining seconds
        else:
            self._seconds = value


    def countdown(self):
        """
        Executes the countdown and displays the remaining time in HH:MM:SS format.
        """
        # Iterate through the remaining hours, minutes, and seconds
        for _ in range(self.hours + 1):
            for _ in range(self.minutes + 1):
                for _ in range(self.seconds + 1):
                    # Print the remaining time on the same line
                    print(f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}', end='\r')
                    time.sleep(1)  # Wait for 1 second
                    self.seconds -= 1  # Decrement seconds
                self.minutes -= 1  # Decrement minutes when seconds are done
                self.seconds = 59  # Reset seconds to 59
            self.minutes = 59  # Reset minutes to 59 when hours change
            self.hours -= 1  # Decrement hours when minutes are done
        if self.isTimer:
            self.sound()  # Play sound when the countdown ends


    def sound(self):
        """
        Plays a sound using the `paplay` command when the countdown ends.
        """
        subprocess.run(['paplay', 'sound.wav'])  # Play the sound
            





if __name__ == '__main__':
    # Create a Timer object and set it to 1 hour and 1 minute
    timer = Timer(0, 60, 60)
    timer.countdown()  # Start the countdown
