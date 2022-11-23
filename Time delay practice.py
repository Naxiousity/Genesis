
from threading import Timer
 
def foo(delay):
    print(f'Feelsgoodman')
 
if __name__ == '__main__':
 
    delay = 10        # in seconds
 
    print('Timer class demo')
 
    # call foo() after 1 second
    t = Timer(delay, foo, [delay])
    t.start()
 
    print('Coming for your booty in 10 sec')