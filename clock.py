import datetime
import time
import os

def alarm_clock():
    print("Welcome to the Alarm Clock!")
    alarm_time = input("Enter the alarm time in HH:MM:SS format (24-hour clock): ")
    
    try:
        # Validate input
        alarm_hour, alarm_minute, alarm_second = map(int, alarm_time.split(":"))
        if not (0 <= alarm_hour < 24 and 0 <= alarm_minute < 60 and 0 <= alarm_second < 60):
            raise ValueError
        
        print(f"Alarm set for {alarm_time}. Waiting...")
        
        while True:
            # Get the current time
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            
            # Check if current time matches alarm time
            if current_time == alarm_time:
                print("Wake up! It's time!")
                
                # Optional: Play a sound (on systems with aplay installed)
                try:
                    os.system("echo -e '\a'")  # Beep sound
                except:
                    pass
                
                break
            time.sleep(1)  # Check every second
            
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS (24-hour format).")

# Run the alarm clock
alarm_clock()
