# -*- coding: utf-8 -*-
# author: supegg.rao
# mail: supegg.rao@gmail.com
'''
subscribe messages
'''

import time, redis, json

if __name__ == "__main__":
    print(f'Burn, burn, burn them all...')

    with open("server.json", 'r') as f:
        server = json.load(f)
    with open("client.json", 'r') as f:
        client = json.load(f)

    rc = redis.StrictRedis(server['ip'], server['port'],
                           server['db'], server['passport'], decode_responses=True)
    
    ps = rc.pubsub()
    ps.subscribe([v['channel'] for v in client.values()])
    
    for item in ps.listen():
        if item['type'] == 'message':
            data = json.loads(item['data'])
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(data['ts']))}] [{item['channel']}] [{data['author']}]: {data['message']}")
            