import random
import os
from sys import argv
from datetime import datetime

# Set group size
size = argv[1] if len(argv) > 1 else 2

# Get date of today and seed for random shuffling
date = datetime.now().strftime("%Y_%m_%d")
seed = datetime.now().strftime("%m%d")
#seed = 1

# Store list of groupwork pairings
list_of_pairings = []

# Define function for generating pairings
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i : i + n]


# List of course attendees
n = [
    "Name1",
    "Name2",
    "Name3",
    "Name4",
]

random.Random(seed).shuffle(n)

# Call function and store result in variable pairings
pairings = list(chunks(n, int(size)))

# Store list in new file
with open("groups.txt", "w") as f:
    f.write(str(pairings))
files = [x for x in os.listdir() if os.path.isfile(x)]
if not os.path.exists("groups"):
    os.makedirs("groups")
for i in files:
    if i.endswith(".txt"):
        os.rename(i, "groups/" + date + "_" + i)

# Print groups
for i, x in enumerate(pairings):
    print(i + 1, ":", x)
