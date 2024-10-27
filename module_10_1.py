import threading
import time

# start_time = None
# end_time = None
# print(time.thread_time())

def write_words(word_count, file_name):
    # По какой-то причине у меня не сработала функция time.threadtime, пришлось воспользоваться функцикй time
    start_time = time.time()
    # print(start_time)
    with open(file_name, 'w', encoding='UTF-8') as  file:
        for i in range(1,word_count+1):
            file.write(f'Какое-то слово № {i} \n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
    end_time = time.time()
    # print(end_time)
    print(f"Время выполнения потока {end_time - start_time}")


write_words(10, 'example1.txt')
write_words(20, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
thred_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thred_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thred_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thred_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thred_1.start()
thred_1.join()
thred_2.start()
thred_2.join()
thred_3.start()
thred_3.join()
thred_4.start()
thred_4.join()
# print(threading.currentThread())

