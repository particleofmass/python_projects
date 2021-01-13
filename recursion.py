def factorial(number):
    return number * factorial(number - 1) if number > 1 else 1


def fibo(posinfibo):
    if posinfibo > 2:
        return fibo(posinfibo - 1) + fibo(posinfibo - 2)
    else:
        return 1

