import time
import threading


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):

            file.write(f"Какое-то слово № {i} \n")
            time.sleep(00.1)
    print(f"Завершилась запись в файл {file_name}")


wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

first = threading.Thread(target=wite_words, args= (10, 'example5.txt'))
second = threading.Thread(target=wite_words, args= (30, 'example6.txt'))
third = threading.Thread(target=wite_words, args= (200, 'example7.txt'))
fourh = threading.Thread(target=wite_words, args= (100, 'example8.txt'))

first.start()
second.start()
third.start()
fourh.start()

first.join()
second.join()
third.join()
fourh.join()