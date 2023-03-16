# This app makes a connection to EXISTING PostgreSQL DB
# and print all data to a file each 5 seconds

import time
import sys
from example_package import example

sec_to_sleep =  5
original_stdout = sys.stdout # Save a reference to the original standard output

with open('db_out.log', 'w+') as f:
    sys.stdout = f # Change the standard output to the file we created.
    
    for i in range(600):
        print(example.print_db())
        time.sleep(sec_to_sleep)
    
    sys.stdout = original_stdout # Reset the standard output to its original value