#most of the code was stolen from here - https://github.com/neuefische/muc-ds-22-3-daily-review/tree/main/pairing
#Andreas, Aljoscha and Evgeny are honest thieves :), thanks Louis!
import random 
import numpy as np
import pandas as pd
import pickle
from pathlib import Path
import time
from math import factorial, floor
import os
from config import LOOKBACK

#calculate the k-th permutations of a list S
def kthperm(S, k):  #  nonrecursive version
    P = []
    while S != []:
        f = factorial(len(S)-1)
        i = int(floor(k/f))
        x = S[i]
        k = k%f
        P.append(x)
        S = S[:i] + S[i+1:]
    return P


#read the member textfile containing one name per row
def read_member_list():
    fle = Path('./pairing/members.txt')
    fle.touch(exist_ok=True)
    try:
        with open (fle) as f:
            file = f.readlines()
        members = [name.strip('\n') for name in file]
        #print(members)
    except: 
        print('CANNOT READ MEMBER LIST')
        members = []
    members = [name.strip('\n') for name in file]
    if len(members) == 0:    
        members = list(range(1,5))
    return members

#read the file where the previous groups are stored
#i made it a pickle, in future i would make it a csv
def read_prev_grps():
    fle = Path('./pairing/prev_pairings.pickle')
    fle.touch(exist_ok=True)
    try: 
        with open('./pairing/prev_pairings.pickle', 'rb') as handle:
            prev_pairs = pickle.load(handle)

    except: 
        'CANNOT READ PREVIOUS GROUPS.'
        prev_pairs = []
    return prev_pairs


#function that accepts a tuple of tuples and returns the co-occurrence matrix
def co_occurrence_matrix(participants_tuple):
    df = pd.DataFrame(participants_tuple) 

    u = (pd.get_dummies(df, prefix='', prefix_sep='')
       .groupby(level=0, axis=1)
       .sum())

    v = u.T.dot(u)
    v.values[(np.r_[:len(v)], ) * 2] = 0

    return v



#create the new pairings from the members with a group size of 'size'
# lookback defines how many previous pairings you compare with the new generated. if lookback > n-1 it will set to n-1
# the smaller the lookback the faster the algorithm but the greater 
# default is lookback = -1 which will set it also to n-1
def new_pairings(size, lookback=-1):

    t=time.time()
    

    #read the member from .txt-file
    members = read_member_list()
    #read the previous pairings from .pickle-file
    prev_pairs = read_prev_grps()

    #How many groups are there?
    n = len(members) #number of member
    num_grp = n // int(size) #group size
    
    if lookback > n-1: 
        lookback = n-1
        print(f'lookback to big: setting it to number of members -1 = {n-1}')
    elif lookback == -1: lookback = n-1
   
    random.seed(len(prev_pairs)) #random seed from length of prev_pairs list
    
    same_pairings = True #bool for checking if one pair exists in the previous pairings
    print('Generating...')
    print()

    while same_pairings == True: #until we have found truly unique pairs
        
        #random number between 0 and n!
        k = random.randint(0,factorial(n))
        # calculate the m-th permutation of the members list
        new_perm = tuple(kthperm(members, k))

        #Split perm in num_grp pairings
        #if it does not add up, the rest are assigned to the other groups automatically
        new_pairings = np.array_split(new_perm,num_grp)
        new_pairings = [tuple(ele.tolist()) for ele in new_pairings] # np array to list of tuples

        same_pairings = False
        if len(prev_pairs) > 0: #if we have previous created groups
            #sort pairs because groups of (person_1,person_2) and (person_2,person_1) should be handled as equal
            new_pairings = [tuple(sorted(pair)) for pair in new_pairings] 

            # check every tuple of pairs of the past
            
            #go back in pairing history and compare new pairings with previous pairings up to 'lookback' steps back
            for go_back in range(-1,-min(len(prev_pairs)+1,lookback),-1):
                old_pairings = [pair for pair in prev_pairs[go_back]]

                if any(new_pair in old_pairings for new_pair in new_pairings):
                    same_pairings = True
                    break
                    
            
                 


    for c, pair in enumerate(new_pairings):
        p = str(pair)[1:-1]
        p = p.replace("'","")
        print(f'{c+1}: {p}')
    
    # create csv with groups
    df_groups = pd.DataFrame(new_pairings)
    df_groups.to_csv('./pairing/groups.csv')
    
    #add new pairs to previous pairings
    prev_pairs.append(tuple(new_pairings))

    df = co_occurrence_matrix(prev_pairs[0])

    for i in range(1,len(prev_pairs)):
        df_new = co_occurrence_matrix(prev_pairs[i])
        df = df.add(df_new)

    #save all previous pairings in pickle file
    try:
        with open('./pairing/prev_pairings.pickle', 'wb') as handle:
            pickle.dump(prev_pairs, handle, protocol=pickle.HIGHEST_PROTOCOL)
            df.to_csv('./pairing/co_occurrence.csv')
    except: print('COULD NOT WRITE THE PICKLE FILE :(')
    print()
    elap_t = time.time()-t
    print(f'Elapsed time was {elap_t:0.2f}s')
    
    return new_pairings, elap_t


#groupsize
size = os.environ.get('LOG_LEVEL')

#lookback: how many previous generations should be compared with the new one
lookback = LOOKBACK
new_pairings(size=size, lookback = lookback)



