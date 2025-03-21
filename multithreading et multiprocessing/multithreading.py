import threading
import time
from concurrent.futures import ThreadPoolExecutor


def main() -> None:
    print('classic usage ............')
    thread1: threading.Thread = threading.Thread(target=print_numbers, args=([1, 2, 3, 4, 5],))
    thread2: threading.Thread = threading.Thread(target=print_letters)

    start: float = time.time()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'Finished classic usage {time.time() - start} ............')

    # with the help of thread pool
    print('With the help of thread pool')
    start: float = time.time()

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(print_number, [i for i in range(1, 18)])

    print(f'finished with the help of thread pool: {time.time() - start}')


def print_numbers(numbers: list[int]) -> None:
    for i in numbers:
        time.sleep(1)
        print(f'Number: {i}', end='\n')

def print_letters() -> None:
    for letter in 'abcde':
        time.sleep(1)
        print(f'Letter: {letter}', end='\n')

def print_number(number: int) -> None:
    time.sleep(1)
    print(f'Number: {number}', end='\n')

if __name__ == '__main__':
    main()
