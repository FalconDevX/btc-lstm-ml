import os

for file in os.listdir('GOLD'):
    if file.endswith('.txt'):
        os.remove(os.path.join('GOLD', file))