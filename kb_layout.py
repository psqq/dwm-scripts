import os
import time
import sys


def get_kbdlayout():
    stream = os.popen("setxkbmap -query | grep -oP 'layout:\\s*\\K([\\w,]+)'")
    output = stream.read()
    return output.strip()


def set_kbdlayout(layout):
    stream = os.popen("setxkbmap " + layout)


def cycle_kbdlayouts(layouts: list):
    current_layout = get_kbdlayout()
    index = layouts.index(current_layout)
    index += 1
    if index >= len(layouts):
        index = 0
    set_kbdlayout(layouts[index])


def test():
    current_layout = get_kbdlayout()
    print("current get_kbdlayout:", repr(current_layout))
    layout = "ru"
    set_kbdlayout(layout)
    time.sleep(0.1)
    print(layout, "get_kbdlayout:", repr(get_kbdlayout()))
    set_kbdlayout(current_layout)


if __name__ == "__main__":
    if sys.argv[1] == "set":
        set_kbdlayout(sys.argv[2])
    elif sys.argv[1] == "circle":
        cycle_kbdlayouts(sys.argv[2:])
    else:
        print("need command: set | circle")
