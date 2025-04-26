import progressbar
from time import sleep

def intro():
    print('='*100)
    print('F I L E  E D I T O R  T E R M I N A L'.center(100,' '))
    print('='*100)


def shutdown():
    print('='*100)
    print('S H U T D O W N'.center(100, ' '))
    print('-'*100)
    for i in progressbar.progressbar(range(100)):
        sleep(0.01)
    print('='*100)