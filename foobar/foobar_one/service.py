import time


def main():
    print('Starting')
    while True:
        print('Running... one')
        time.sleep(5)
        raise Exception('Lols')
