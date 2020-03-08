import timeit
start = timeit.default_timer()

import random
from multiprocessing import Pool

N = 1000000
process_num = 4

def make_pi(n):
    count_inbound = 0
    for x in range(n):
        the_x = random.random()
        the_y = random.random()
        if((the_x**2 + the_y**2) <= 1):
            count_inbound += 1
    return count_inbound

if __name__ == "__main__":
    #multiprocessing code
    p = Pool(processes = process_num)
    count_in = p.map(make_pi, [int(N/process_num) for x in range(process_num)])
    print(4*sum(count_in)/N)

    #normal code
    #print(4*make_pi(N)/N)

    stop = timeit.default_timer()
    print(stop - start)