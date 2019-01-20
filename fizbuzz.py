#! /bin/env python3.6

def fizzbuzz():
    for i in range(0, 100):
        if i % 5 == 0:
            print(f"{i} Buz")

        elif i % 3 == 0:
            print(f"{i} Fiz")

        elif i % 5 and i % 3:
            print(f"{i} FizBuzz")


def fizzbuzz_2():
    def is_fiz(num):
        return num % 5 == 0

    def is_buz(num):
        return num % 3 == 0

    def is_fizzbuzz(num):
        return (is_fiz(num) and is_buz(num))

    for num in range(0, 100):
        if is_buz(num):
            print(f"{num} Buz")

        elif is_fiz(num):
            print(f"{num} Fiz")

        elif is_fizzbuzz(num):
            print(f"{num} FizBuzz")


fizzbuzz()
fizzbuzz_2()
