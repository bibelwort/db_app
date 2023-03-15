# This app makes a connection to EXISTING PostgreSQL DB
# and print all data to the screen each 5 seconds

import time
from example_package import example

sec_to_sleep =  5
while True:
    example.print_db()
    time.sleep(sec_to_sleep)