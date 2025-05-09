import psutil
import winsound
import time

def play_alert_sound(duration_ms):
    freq = 1000
    winsound.Beep(freq, duration_ms)

def monitor_battery(config):
    low_triggered = False
    high_triggered = False

    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = battery.power_plugged

        if not plugged and percent <= config["low_threshold"]:
            if not low_triggered:
                play_alert_sound(config["beep_duration"])
                low_triggered = True
        else:
            low_triggered = False

        if plugged and percent >= config["high_threshold"]:
            if not high_triggered:
                play_alert_sound(config["beep_duration"])
                high_triggered = True
        else:
            high_triggered = False

        time.sleep(60)
