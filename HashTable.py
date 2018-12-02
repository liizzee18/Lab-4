class HashTableNode:
    def __init__(self, word, next):
        self.word = word
        self.next = next


class HashTable:


    def __init__(self, size):
        self.table = []
        for i in range(size):
            self.table.append([])

    def hash(self, k):
        index = 0
        temp = ord('a')
        for i in range(len(k)):
            base = ord(k[i]) - temp
            index += base * pow(26, (len(k)-1)-i)
        return index % len(self.table)

    def hash2(self, k):# turns indvidual letter to a int value and then adds it together
        num = ''.join(str(ord(a))for a in k)
        return int(num) % len(self.table)



    def insert(self, k):
        index = self.hash(k)
        list = self.table[index]
        node = HashTableNode(k, list)
        list.append(node)


    def search(self,k):
        pos = self.hash(k)
        list = self.table[pos]
        if k == list:
            return k
        else:
            return None


    