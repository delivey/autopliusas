import beepy as beep
import webbrowser


def open_url(url):
    webbrowser.open(url)


def make_beep():
    for i in range(3):
        beep.beep(1)


def notify(url):
    make_beep()
    open_url(url)


if __name__ == "__main__":
    notify("https://autoplius.lt")
