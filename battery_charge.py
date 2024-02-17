#!/usr/bin/python


def get_battery_charge():
    try:
        with open("/sys/class/power_supply/BAT1/capacity", "r") as f:
            return f.read().strip()
    except:
        pass


if __name__ == "__main__":
    print(get_battery_charge())
