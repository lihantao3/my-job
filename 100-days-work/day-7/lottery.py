#双色球选号
from random import randrange, randint, sample


def select_balls():
    selected = [x for x in sample(range(1, 34), 6)]
    selected.sort()
    selected.append(randint(1, 16))
    return selected


def display_balls(balls):
    for index, ball in enumerate(balls):
        if index < len(balls) - 1:
            print(ball, end=' ')
        else:
            print('|', end=' ')
            print(ball)


def main():
    n = int(input('机选几注： '))
    for _ in range(n):
        display_balls(select_balls())


if __name__ == '__main__':
    main()
