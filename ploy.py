class india:
    def capital(self):
        print("india")

class usa:
    def capital(self):
        print("usa")

obj_ind=india()
obj_usa=usa()

for country in(obj_ind,obj_usa):
    country.capital()