import random
import time
import threading

# lock = threading.Lock()
class Bank():
    def __init__(self, balance):
        self.balance = int(balance)
        self.lock = threading.Lock()
    def deposit(self):
        for i in range(1,101):
            adding = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
                # print(f'Сумма {adding} принята к пополнению, счет разблокирован {self.lock.locked()}')
            self.balance += adding
            print(f'Пополнение: {adding}. Баланс: {self.balance}')
            time.sleep(0.001)
    def take(self):
        for i in range(1, 101):
            withdrawal = random.randint(50, 500)
            if withdrawal <= self.balance:
                self.balance -= withdrawal
                print(f'Снятие: {withdrawal}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()
                # print(f'Сумма {withdrawal} превышает баланс счета, счет заблокирован {self.lock.locked()}')
            time.sleep(0.001)


bk = Bank(0)
# bk.deposit()
# bk.take()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

