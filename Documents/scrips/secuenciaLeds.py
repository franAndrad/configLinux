from os import system
from time import sleep

while 1 :
    system("echo 1 >| /sys/class/leds/input7::capslock/brightness")
    system("echo 1 >| /sys/class/leds/input7::numlock/brightness")
    sleep(1)
    system("echo 0 >| /sys/class/leds/input7::capslock/brightness")
    system("echo 0 >| /sys/class/leds/input7::numlock/brightness")
    sleep(1)

