#Testfile for creating a lot of groups, can be used to test if the distribution is uniform
#only use for testing. will delete previous pairings file
import os
from rnd_groups import new_pairings
import time
import numpy as np

#delete pickle file
try:
    os.remove('pairing/prev_pairings.pickle')
except: print('NO FILE')
tt = []
t = time.time()


num_runs = 100
for i in range(num_runs):
    _, elap_t = new_pairings(size=2, lookback = -1)
    tt.append(elap_t)

print(f'Total Test Elapsed time was {time.time()-t:0.2f}s')
print(f'Average Elapsed time was {np.mean(tt):0.2f}s')
