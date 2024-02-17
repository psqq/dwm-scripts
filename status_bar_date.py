import os


def date_for_status_bar():
    stream = os.popen('LC_ALL=ru_RU.UTF-8 date +"%a %d %b %H:%M:%S"')
    output = stream.read()
    return output.strip()


if __name__ == "__main__":
    print("date_for_status_bar:", repr(date_for_status_bar()))
