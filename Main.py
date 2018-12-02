from HashTable import HashTable

#This method creates the table with the words 
def create_table(file, hashtable):
    with open(file) as file:
        for line in file:
            items= line.split(" ")
            if items[0][0].isalpha():
                word = line.split(" ")[1]  
                hashtable.insert(word)

    return hashtable

#Computing the load factor: measures how full the hashtable 
def load_factor(self):
    num_elements = 0
    for i in range(len(self.table)):
        temp = self.table[i]
        for temp in self.table[i]:
            num_elements += 1
    return num_elements / len(self.table)


def number_comparisons(self):
        total_elem = 0
        num_occupied = 0
        for i in range(len(self.table)):
            temp = self.table[i]
            if temp is not None:
                num_occupied +=1

            for temp in self.table[i]:
                total_elem +=1
                temp = temp.next

        return total_elem/num_occupied

def main():
    file = "file.txt"
    table = HashTable(700)
    create_table(file, table)
    print(" [ Load factor ] ",load_factor(table))
    print("[ Number of comparisons ]  ", number_comparisons(table))

main()