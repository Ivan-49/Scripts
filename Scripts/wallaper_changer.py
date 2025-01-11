from random import randint
import ctypes
import os
from keyboard import add_hotkey, wait, call_later
from asyncio import run


def change_wallpaper():
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDWININICHANGE = 0x02

    directory = "C:/Users/remne/Pictures/wallaper"
    files = os.listdir(directory)
    i = randint(0, len(files) - 1)
    image_path = os.path.join(directory, files[i])

    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE
    )


# async def main():
#     add_hotkey("alt+f6", lambda: call_later(change_wallpaper, args=()))

#     wait()


# if __name__ == "__main__":
#     run(main())
