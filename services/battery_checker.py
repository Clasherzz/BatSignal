import psutil
import winsound
import time


def play_alert_sound(duration_ms):
    freq = 1000
    winsound.Beep(freq, duration_ms)

def monitor_battery(config):
    low_triggered = False
    high_triggered = False

    try:
        while True:
            battery = psutil.sensors_battery()
            percent = battery.percent
       # plugged = battery.power_plugged

            if percent <= config["low_threshold"] :
                if config["repeat"]=="No" and not low_triggered:
                    play_alert_sound(config["beep_duration"])
                    low_triggered = True
                elif config["repeat"]=="Yes":   
                    play_alert_sound(config["beep_duration"])
                else:
                    break
                

            else:
                low_triggered = False

            if percent >= config["high_threshold"]:
                if not high_triggered:
                    play_alert_sound(config["beep_duration"])
                    high_triggered = True
            else:
                high_triggered = False

        time.sleep(60)
    except:
        print("Error: Unable to monitor battery. Please check your system.")
        time.sleep(60)