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
            day += 1
            time.sleep(1)
            enemyes -= self.power
            print(f'{self.name} сражается {day} дней, осталось {enemyes} воинов.')

            if enemyes <= 0:
                break

        print(f"{self.name} одержал победу спустя {day} дней(дня)!")

thread1 = Knight('valet', 10)
thread1.start()
thread2 = Knight('shrek', 20)
thread2.start()



