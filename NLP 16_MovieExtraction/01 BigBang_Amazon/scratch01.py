from tqdm import tqdm
import time
outer_count = 10
inner_count = 5
# for i in tqdm(range(outer_count), desc="Outer", position=0, colour = 'blue'):
#     for j in tqdm(range(inner_count), desc="Inner", position=1, leave=False, colour = 'green'):
#         # your code
#         time.sleep(0.5)

def outer_tqdm():
    for i in tqdm(range(outer_count), desc="Outer", colour = '#1b487b'):
        inner_tqdm()

def inner_tqdm():
    for j in tqdm(range(inner_count), desc="Inner", leave=False, colour = 'blue'):
        # your code
        time.sleep(0.1)

outer_tqdm()
