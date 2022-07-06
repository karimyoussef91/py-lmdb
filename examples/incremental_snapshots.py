import lmdb
import json
import sys
import os
import math

file = sys.argv[1]
database_path = sys.argv[2]
snapshot_name = sys.argv[3]

db = lmdb.open(database_path, map_size=1099511627776 * 2, readonly=False,
                   meminit=False, map_async=True, writemap=True)

txn = db.begin(write=True)

data = []
with open(file) as f:
    for line in f:
        json_line = json.loads(line)
        comment_id = json_line['id']
        comment_body = json_line['body']
        txn.put(comment_id.encode('utf-8'), comment_body.encode('utf-8'))

txn.commit()

os.mkdir(snapshot_name)

db.copy(snapshot_name, compact=True, txn=txn)

db.sync()
db.close()
