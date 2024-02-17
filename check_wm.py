import os

def get_wm_name():
    stream = os.popen('wmctrl -m | grep Name')
    output = stream.read()
    return output.split(": ")[1].strip()

if __name__ == "__main__":
    print("wm name:", repr(get_wm_name()))
