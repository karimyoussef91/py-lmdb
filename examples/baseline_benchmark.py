import lmdb

db = lmdb.open('/l/ssd/test_db',map_size=1099511627776 * 2, readonly=False,
                   meminit=False, map_async=True, writemap=True)

txn = db.begin(write=True)

txn.put(b'key_1', b'value_1')
txn.put(b'key_2', b'value_2')
txn.put(b'key_3', b'value_3')
txn.put(b'key_4', b'value_4')

txn.commit()

db.copy('/l/ssd/test_db_copy')

db.sync()
db.close()



db = lmdb.open('/l/ssd/test_db_copy')

txn = db.begin(write=True)

val = txn.get(b'key_1')
print(val)
db.close()
