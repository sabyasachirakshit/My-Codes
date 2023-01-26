# Get height and width of console window

# Program-

import fcntl
import termios
import struct


def size():
    th, tw, hp, wp = struct.unpack('HHHH', fcntl.ioctl(
        0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
    return th, tw


print("Number of rows and columns:", size())
