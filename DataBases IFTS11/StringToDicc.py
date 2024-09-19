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