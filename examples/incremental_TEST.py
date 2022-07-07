import lmdb
import json
import sys
import os
import math

file = sys.argv[1]
privateer_base_path = sys.argv[2]
snapshot_name = sys.argv[3]

db = lmdb.open(privateer_base_path=privateer_base_path, db_name=snapshot_name)

txn = db.begin(write=True)

data = []
with open(file) as f:
    for line in f:
        json_line = json.loads(line)
        comment_id = json_line['id']
        comment_body = json_line['body']
        comment_body_db = txn.get(comment_id.encode("utf-8")).decode("utf-8")
        if comment_body != comment_body_db:
            print("Error at id: " + comment_id)
            exit(-1)
print("Test Passed!!!")
        
