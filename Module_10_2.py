import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        enemyes = 100
        day = 0
        print(f'{self.name}, на нас напали!')
        for i in range(enemyes):
            time.sleep(1)
            enemyes -= self.power
            day += 1
            if enemyes < 0:
                break
            print(f'{self.name} сражается {day}, осталось {enemyes} воинов.')

thread1 = Knight('valet', 10)
thread1.start()
thread2 = Knight('shrek', 20)
thread2.start()



