from multiprocessing import Pool
import time
def read_info(name):
    all_data = []
    with open(name, 'r', encoding='UTF-8') as  file:
        for line in file:
            all_data.append(file.readline())

    # print(all_data)
list_of_files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
#Линейное вычисление
# start_time = time.time()
# for name in list_of_files:
#     read_info(name)
# end_time = time.time()
# print(f"Время линейного вычисления {end_time - start_time}")

# Многопроцессный
if __name__ == '__main__':
    start_time = time.time()
    with Pool(processes=4) as pool:
        pool.map(read_info, list_of_files)
    end_time = time.time()
    print(f"Время многопроцессного вычисления {end_time - start_time}")

