import pandas as pd

class TaskManager:
    def __init__(self):
        veri = {
            "id": [],
            "title": [],
            "status": []
        }  
        self.db = pd.DataFrame(veri)

    def showData(self):
        if self.db.empty:
            return None
        
        return self.db
    
    def addTask(self,id,title,status):
        ilksatir = {
            "id": id,
            "title": title,
            "status": status
        }

        self.db.loc[len(self.db)] = ilksatir

    def findTaskByStatus(self,status):
        if self.db.empty:
            return None
        
        status = status.lower()
        
        return self.db[self.db["status"].str.lower() == status]
        
    def findTaskById(self,id):
        if self.db.empty:
            return None
        
        sonuc = self.db[self.db["id"] == id]
        if sonuc.empty:
            return None
        else:
            return sonuc.iloc[0]
        
    def updateTaskStatus(self,id,newstatus):
        newstatus = newstatus.lower()

        sonuc = self.db[self.db["id"] == id]

        index = sonuc.index[0]

        if sonuc.empty:
            return None
        else:
            self.db.loc[index,"status"] = newstatus
            return self.db.loc[index]
    
        

