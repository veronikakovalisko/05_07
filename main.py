import threading
import multiprocessing
import time
import json
import requests


def take(search_str: str):
    answer = requests.get("https://api.pushshift.io/reddit/comment/search/", params={'subreddit': search_str})
    if answer.ok:
        answer.json


def prime(number):
    flag = True
    print(f'start with {number}')
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            flag = False
            break
    print(f'{number = } is prime {flag}')
     NUMBERS = [
        2,  # prime
        1099726899285419,
        1570341764013157,  # prime
        1637027521802551,  # prime
        1880450821379411,  # prime
        1893530391196711,  # prime
        2447109360961063,  # prime
        3,  # prime
        2772290760589219,  # prime
        3033700317376073,  # prime
        4350190374376723,
        4350190491008389,  # prime
        4350190491008390,
        4350222956688319,
        2447120421950803,
        5,  # prime
    ]
    t = time.time()
    prime(NUMBERS[1])
    prime(NUMBERS[2])
    prime(NUMBERS[3])
    prime(NUMBERS[4])
    print(f'zanjalo vremeni - {time.time()-t}')
    ku = []
    for i in NUMBERS[:5]:
         m = multiprocessing.Process(target=prime, args=(i,))
         # m = threading.Thread(target=prime, args=(i,))
         m.start()
         ku.append(m)
    for m in ku:
        m.join()
    print(f'zanjalo vremeni - {time.time() - t}')
    with multiprocessing.Pool() as pool:
        pool.map(prime, NUMBERS[:5])
    print(f'zanjalo vremeni - {time.time() - t}')

if __name__ == '__main__':
   pass