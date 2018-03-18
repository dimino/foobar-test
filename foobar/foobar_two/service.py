import time


def main():
    print('Starting')
    while True:
        print('Running... two')
        time.sleep(5)
        raise Exception('Lols')
