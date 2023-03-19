# This app makes a connection to EXISTING PostgreSQL DB
# and print all data to a file each second

import time
import sys
from db_package import db_reader

sec_to_sleep =  1
original_stdout = sys.stdout

for i in range(60):
    with open('app.log', 'w') as f:
        sys.stdout = f
        print(db_reader.read())
        sys.stdout = original_stdout
    time.sleep(sec_to_sleep)
