#!/usr/bin/env python3

import json
import pprint

f = open('tasks.json')
data = json.load(f)
f.close()

for task in data:
    # print(i)
    # pprint.pprint(task)
    prov = data[task]['task']['provisionerId']
    wt = data[task]['task']['workerType']
    print(f"{task}: {prov}/{wt}")
