#!/usr/bin/python
import subprocess
from typing import final
import status_bar_date
import time
import sys
import kb_layout
import os
import battery_charge
import volume


def render():
    date = status_bar_date.date_for_status_bar()
    current_kblayout = kb_layout.get_kbdlayout()
    content = " | "
    content += current_kblayout.upper()
    content += " | "
    s = battery_charge.get_battery_charge()
    if s:
        content += "B " + s + "%"
        content += " | "
    v = volume.current()
    if v:
        content += f"V {v}% | "
    content += date
    content += " | "
    subprocess.run(["xsetroot", "-name", content])


def is_loop_runned():
    ps = os.popen("ps aux").readlines()
    c = 0
    for p in ps:
        if "status_bar.py loop" in p:
            c += 1
    return c > 1


def loop():
    if is_loop_runned():
        print("status bar loop alredy runned!")
        return
    while True:
        try:
            render()
        except:
            pass
        finally:
            time.sleep(1)


if __name__ == "__main__":
    if sys.argv[1] == "render":
        render()
    elif sys.argv[1] == "loop":
        loop()
    else:
        print("need command: render | loop")
