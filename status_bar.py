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


def render(display):
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
    xsetrootEnv = os.environ.copy()
    if display:
        xsetrootEnv["DISPLAY"] = display
    subprocess.run(["xsetroot", "-name", content], env=xsetrootEnv)


def is_loop_runned(display):
    ps = os.popen("ps aux").readlines()
    c = 0
    cmdForSearch = "status_bar.py loop"
    if display:
        cmdForSearch += " " + display
    for p in ps:
        if cmdForSearch in p:
            c += 1
    return c > 1


def loop(display):
    if is_loop_runned(display):
        print("status bar loop alredy runned!")
        return
    while True:
        try:
            render(display)
        except:
            pass
        finally:
            time.sleep(1)


if __name__ == "__main__":
    if sys.argv[1] == "render":
        render()
    elif sys.argv[1] == "loop":
        display = sys.argv[2] if 2 < len(sys.argv) else ""
        loop(display)
    else:
        print("need command: render | loop")
