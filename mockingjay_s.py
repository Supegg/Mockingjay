# -*- coding: utf-8 -*-
# author: supegg.rao
# mail: supegg.rao@gmail.com
'''
publish messages from queue
'''

import redis
import time
import json

if __name__ == "__main__":
    print(f'Burn, burn, burn them all...')

    with open("server.json", 'r') as c:
        server = json.load(c)
    rc = redis.StrictRedis(server['ip'], server['port'],
                           server['db'], server['passport'], decode_responses=True)

    while(True):
        bird = rc.rpop(server['bird'])
        if bird:
            channel = json.loads(bird)['channel']
            rc.publish(channel, bird)
        else:
            time.sleep(1)
            print('sleepy bird...')
