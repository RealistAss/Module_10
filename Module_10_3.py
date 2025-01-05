import random
import threading
import time


class Bank():

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
    def deposit(self):
        trans = 100

        for i in range(trans):
            b = random.randint(50, 500)
            with self.lock:
                self.balance += b

                print(f"Пополнение: {b}. Баланс: {self.balance}")
        time.sleep(0.01)

    def take(self):
        trans = 100

        for i in range(trans):
            b = random.randint(50, 500)
            with self.lock:
                print(f'Запрос на {b}')
                if b <= self.balance:
                    self.balance -= b
                    print(f'Снятие: {b}. Баланс: {self.balance}.')
                else:
                    print("Запрос отклонён, недостаточно средств")
        time.sleep(0.01)

bank = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bank,))
th2 = threading.Thread(target=Bank.take, args=(bank,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bank.balance}')