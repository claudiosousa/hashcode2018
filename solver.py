from math import *
from pprint import pprint
import random
import itertools
from collections import Counter, defaultdict
import sys

PLOT = True
INITIAL_STATES = 50
ENLARGE_VARIANTS = 2


def dist_r(r):
    return abs(r[2] - r[0]) + abs(r[3] - r[1])


def shortest_start(c, r):
    return max(abs(c['pos'][0] - r[0]) + abs(c['pos'][1] - r[1]) + c['t'], r[4])


def run():
    [R, C, F, N, B, T] = map(int, input().split())

    # R – number of rows of the grid (1 ≤ R ≤ 10000)
    # C – number of columns of the grid (1 ≤ C ≤ 10000)
    # F – number of vehicles in the fleet (1 ≤ F ≤ 1000)
    # N – number of rides (1 ≤ N ≤ 10000)
    # B – per-ride bonus for starting the ride on time (1 ≤ B ≤ 10000)
    # T – number of steps in the simulation (1 ≤ T ≤ 10 )

    max_dist = R * C + 1

    #pprint([R, C, F, N, B, T])

    rides = []
    for i in range(N):
        rides.append(list(map(int, input().split())) + [i, 0, 0])

    for r in rides:
        r[7] = dist_r(r)

    # a – the row of the start intersection (0 ≤ a < R)
    # b – the column of the start intersection (0 ≤ b < C)
    # x – the row of the finish intersection (0 ≤ x < R)
    # y – the column of the finish intersection (0 ≤ y < C)
    # s – the earliest start(0 ≤ s < T)
    # f – the latest finish (0 ≤ f ≤ T) , (f ≥ s + |x − a| + |y − b|)

    #pprint(rides)

    cars = [{'id': f, 'rides': [], 't': 0, 'pos': (0, 0)} for f in range(F)]

    i = 0
    while rides:
        i += 1
        sortest_ride = None
        shortest_dist = max_dist
        shortest_t = 0
        for r in rides:
            if r[8]:
                continue
            for c in cars:
                d = shortest_start(c, r)
                t = d + r[7]
                if d < shortest_dist and t <= T and t < r[5]:
                    shortest_dist = d
                    shortest_t = t
                    sortest_ride = (r, c)

        if not sortest_ride:
            break

        sortest_ride[1]['rides'].append(sortest_ride[0][6])
        sortest_ride[1]['pos'] = (sortest_ride[0][2], sortest_ride[0][3])
        sortest_ride[1]['t'] = shortest_t
        sortest_ride[0][8] = 1
        if i % 100 == 0:
            print(i / N, file=sys.stderr)
        rides.remove(sortest_ride[0])

    for c in cars:
        print(' '.join(map(str, [len(c['rides'])] + [r for r in c['rides']])))


if __name__ == '__main__':
    run()
