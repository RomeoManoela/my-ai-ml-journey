import multiprocessing
import time

def main() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5]

    p1: multiprocessing.Process = multiprocessing.Process(target=print_squares, args=(numbers,))
    p2: multiprocessing.Process = multiprocessing.Process(target=print_cubes, args=(numbers,))
    start: float = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    end: float = time.time() - start
    print(f"Temps d'exécution: {end}")


def print_squares(numbers: list[int]) -> None:
    for number in numbers:
        print(f"Square: {number ** 2}")
        time.sleep(1)


def print_cubes(numbers: list[int]) -> None:
    for number in numbers:
        print(f"Cube: {number ** 3}")
        time.sleep(1.5)


if __name__ == "__main__":
    main()