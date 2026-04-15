from backend.database import query_one

print(query_one(
    'SELECT name FROM sqlite_master WHERE type="table"', 
    ()
))

''' 
HOW TO RUN (Windows / PowerShell)
-- From the project root (NOT inside demo/): -- 

python -m demo.test_db


-- If import fails, try: --

ren .\database\db..py db.py

'''