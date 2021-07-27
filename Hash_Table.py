
class Hash_Table:

    def __init__(self, limit=10):

        self.table = []
        for i in range(limit):
            self.table.append([])

    def search_package(self, id):
        listBuck = hash(id) % len(self.table)
        bucket_l = self.table[listBuck]

        for idValue in bucket_l:
            if idValue[0] == id:
                return idValue[1]
        return None



    def insert_package(self, id, item):
        bucket = hash(id) % len(self.table)
        bucket_list = self.table[bucket]

        for idValue in bucket_list:
          if idValue[0] == id:
            idValue[1] = item
            return True

        id_value = [id, item]
        bucket_list.append(id_value)
        return True



    def remove(self, id):
        listBUCK = hash(id) % len(self.table)
        buck_list = self.table[listBUCK]

        for idValue in buck_list:
          if idValue[0] == id:
              buck_list.remove([idValue[0],idValue[1]])
