#%%
schema = "Nombre,Apellido,Edad,Mail"
row = "Brian,Marquez,27,bmarquez@test.com"

class Str2Dic(object):
    def __init__(self, schemaStr, separator=","):
        self.schema = schemaStr.split(separator)
        self.separator = separator

    def convert(self,row):
        temp = row.split(self.separator)
        if len(temp) == len(self.schema):
            i = 0
            dic = {}
            while i < len(temp):
                key = self.schema[i]
                value = temp[i]
                dic[key] = value
                i = i + 1
            return dic
        

o = Str2Dic(schema)
d = o.convert(row)
print(d)

#%%
class Str2Doc(object):
    def __init__(self, keysStr, separator =","):
        self.separator = separator
        self.keys = keysStr.split(separator)
    
    def convert(self, line):
        values = line.split(self.separator)

        if len(values) == len(self.keys):
            dic = {}
            i = 0
            while i < len(values):
                key = self.keys[i]
                val = values[i]

                dic[key] = val
                i += 1
            return dic


s2d = Str2Doc("nombre,mail,telefono,edad")
print(s2d.keys)
print(s2d.convert("brian,g@mailcom,228jk989,2a8"))