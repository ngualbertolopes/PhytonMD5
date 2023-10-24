import hashlib
h="apple"
my_hash = hashlib.sha256(h.encode('utf-8')).hexdigest()
print(my_hash)