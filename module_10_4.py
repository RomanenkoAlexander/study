import threading
import random
import time
from queue import Queue

class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        
        for guest in guests:
            # print(guest)
            try:

                table  = [table for table in self.tables if table.guest == None]
                # print(table)
                table[0].guest = guest
                guest.start()
                print(f'{guest.name} сел(-а) за стол номер {table[0].number}')
            except IndexError:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

                if not self.queue.empty() and table.guest is None:
                    new_guest = self.queue.get()
                    table.guest = new_guest
                    new_guest.start()
                    print(f'{new_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')



tables = [Table(number) for number in range(1, 6)]


guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)

cafe.guest_arrival(*guests)

cafe.discuss_guests()