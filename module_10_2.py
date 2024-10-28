import threading
import time
class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = int(power)

    def fight(self, name, power):
        global fight_time
        enemies = 100
        day_begin = time.time()
        while enemies:
            time.sleep(1)
            enemies -= power
            day_finish = time.time()
            print(f'{name} сражается {int(day_finish - day_begin)} день(дня), осталось {enemies} воинов')
        victory = time.time()
        fight_time = int(victory - day_begin)


    def run(self):
        print(f'{self.name}, на нас напали')
        self.fight(self.name, self.power)
        print(f'{self.name} одержал победу спустя {fight_time} дней(дня)!')

thread_1 = Knight('Sir Lancelot', 10)
thread_2 = Knight("Sir Galahad", 20)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()