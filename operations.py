import json


class Operations:
    def __init__(self):
        try:
            with open("database.json", "r") as db:
                data = json.load(db)
                if len(data["Operations"])>0:
                    self.curr_id = list(data["Operations"].keys())[-1]
                else:
                    self.curr_id = -1
        except:
            detail = {"Operations" : {}}
            with open("database.json",  "w") as db:
                json.dump(detail, db, indent=4)

    def get_operations(self):
        with open("database.json", "r") as db:
            operations = json.load(db)
            return list(operations["Operations"].values())

    def set_operations(self, set_op):
        with open("database.json", "r+") as db:
            operations = json.load(db)
            operations["Operations"][int(self.curr_id) + 1] = set_op
            db.seek(0)
            json.dump(operations, db, indent=4)

    def delete_operations(self, key=""):
        with open("database.json", "r+") as db:
            operations = json.load(db)
            if key != "":
                del operations["Operations"][int(key)]
            else:
                del operations["Operations"][int(self.curr_id)]
            db.seek(0)
            json.dump(operations, db, indent=4)

op = Operations()
op.set_operations("Total matches won by a specific team (by default all years, or in particular range of years)")
print(op.get_operations())