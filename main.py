from vectordb import MiniDB
from loader import Loader

if __name__ == "__main__":
    mini_db = MiniDB()
    mini_db.create(Loader("manuals/git.pdf"))
   # print(mini_db.load())


