
import os
import re

for filename in os.listdir('.'):
    match = re.match(r'data(\d+)\.csv', filename)
    if match:
        original_number = int(match.group(1))
        if original_number % 2 != 0:
            new_number = original_number + 10
            new_filename = f'dataodd_blabla_{new_number}.csv'
            os.rename(filename, new_filename)
            print(f'Renamed {filename} to {new_filename}')
