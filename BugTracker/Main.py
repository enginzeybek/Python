import pandas as pd

class BugTracker:
    def __init__(self):
        self.db = pd.DataFrame({
            "id": [],
            "title": [],
            "status": [],
            "priority": []
        })

    def add_bug(self,id,title,status,priority):
        yeni_satir = {
            "id": id,
            "title": title,
            "status": status,
            "priority": priority
        }

        self.db.loc[len(self.db)] = yeni_satir

    def show_bugs(self):
        print(self.db)
        
    def update_status(self,id,new_status):
        self.db.loc[self.db["id"] == id,"status"] = new_status

    def delete_bug(self,id):
        self.db = self.db.loc[self.db["id"] != id]


bug = BugTracker()

bug.add_bug(1,"Login Error","Open","High")
bug.show_bugs()
bug.update_status(1,"Closed")
bug.show_bugs()