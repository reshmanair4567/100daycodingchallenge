class Bucket:
    def __init__(self):
        self.bucket=[]

    def update(self,val):
        found=False
        for i,k in enumerate(self.bucket):
            if val==k:
                self.bucket[i]=val
                found=True
                break
        if not found:
            self.bucket.append(val)
    
    def get(self,key):
        for k in self.bucket:
            if key==k:
                return True
        return False

    def remove(self,key):
        for i,v in enumerate(self.bucket):
            if key==v:
                del self.bucket[i]

class Hashset:
    def __init__(self):
        self.key_space = 2096
        self.hash_table=[Bucket() for i in range(self.key_space)]

    def add(self,key):
        hashkey=key%self.key_space
        self.hash_table[hashkey].update(key)

    def remove(self,key):
        hashkey=key%self.key_space
        self.hash_table[hashkey].remove(key) 

    def contains(self,key):
        hashkey=key%self.key_space
        return self.hash_table[hashkey].get(key)


ob = Hashset()
ob.add(1)
ob.add(3)
print(ob.contains(1))
print(ob.contains(2))
ob.add(2)
print(ob.contains(2))
ob.remove(2)
print(ob.contains(2))
# print(ob)

