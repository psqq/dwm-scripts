import sys
import os
import re


def up():
    stream = os.popen("pactl set-sink-volume @DEFAULT_SINK@ +5%")


def down():
    stream = os.popen("pactl set-sink-volume @DEFAULT_SINK@ -5%")


def current(first_only=True):
    stream = os.popen("pactl get-sink-volume @DEFAULT_SINK@")
    output = stream.read().strip()
    all_unique_with_percent = list(set(re.findall(r"\d+%", output)))
    volumes = []
    for v in all_unique_with_percent:
        volumes.append(int(v[:-1]))
    if first_only:
        return volumes[0]
    return volumes


if __name__ == "__main__":
    if sys.argv[1] == "up":
        up()
    elif sys.argv[1] == "down":
        down()
    elif sys.argv[1] == "current":
        print(current())
    else:
        print("need command: up | down | current")
