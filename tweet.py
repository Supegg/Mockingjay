# -*- coding: utf-8 -*-
# author: supegg.rao
# mail: supegg.rao@gmail.com
'''
tweet message to Mockingjay
'''

import sys, json, time, redis

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('usage: python tweet.py chatter message')
        exit()

    if len(sys.argv) == 2:
        print(f"say something {sys.argv[1]}")
        exit()

    print(f'Burn, burn, burn them all...')

    with open("server.json", 'r') as f:
        server = json.load(f)
    with open("client.json", 'r') as f:
        client = json.load(f)

    chatters = client.keys()
    chatter = sys.argv[1]
    message = sys.argv[2]
    if chatter not in chatters:
        print(f'add {chatter} in client.json')
        exit()
    chatter = client[chatter]

    bird = {"author":chatter['nickname'],
    "channel":chatter['channel'],
    "message":message,
    "ts":int(time.time())
    }

    rc = redis.StrictRedis(server['ip'], server['port'],
                           server['db'], server['passport'], decode_responses=True)
        
    rc.lpush(server['bird'], json.dumps(bird))
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(bird['ts']))}] [{bird['channel']}] [{bird['author']}]: {bird['message']}")
