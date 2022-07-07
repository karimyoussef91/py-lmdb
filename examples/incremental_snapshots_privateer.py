import lmdb
import json
import sys
import os
import math
import time

file = sys.argv[1]
privateer_base_path = sys.argv[2]
database_name = sys.argv[3]
snapshot_name = sys.argv[4]
db_init = sys.argv[5]

# if db_init == "1":
db = lmdb.open(privateer_base_path=privateer_base_path, db_name=database_name,map_size=1099511627776 * 2, readonly=False,
                   meminit=False, map_async=True, writemap=True)
# else:
#    db = lmdb.open(privateer_base_path=privateer_base_path, db_name=database_name, readonly=False, meminit=False, map_async=True, writemap=True)

txn = db.begin(write=True)

data = []
with open(file) as f:
    for line in f:
        json_line = json.loads(line)
        data.append(json_line)

start = time.time()
for json_line in data:
    comment_id = json_line['id']
    comment_body = json_line['body']
    txn.put(comment_id.encode('utf-8'), comment_body.encode('utf-8'))
txn.commit()

db.copy(snapshot_name)

db.sync()
db.close()

end = time.time()

print("Total Time: " + str(end - start))
print("Total records: " + str(len(data)))
