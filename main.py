#!/usr/bin/python3
import table_parser
import math
import collections
import sys

from config import config

# Load parameters first

# Amount
MONEY_TO_INVEST = config["TOTAL_AMOUNT_INVEST"]
RATIO_SECONDARY = config["RATIO_INVEST_INTO_SECONDARY"]
RATIO_PRIMARY = 1-RATIO_SECONDARY

# Rating-based
LOWER_CUTOFF_POINT = config["THRSH_LOWER_CUTOFF_RATING"] 
UPPER_CUTOFF_POINT = config["THRSH_UPPER_CUTOFF_RATING"]
UPPER_BONUS_POINT = config["THRSH_BONUS_RATING"]
MULTIPLIER_SEVENTY = config["BONUS_WEIGHT_MULTIPLIER"]

# Consider external ratings + their params
USE_P2P_ANLAGE = config["USE_P2P_ANLAGE"]
P2P_ANLAGE_BONUS = config["THRSH_P2P_ANLAGE_BONUS"]
P2P_ANLAGE_MAX_POINTS = config["P2P_ANLAGE_MAX_POINTS"]

# Set the LOs to exclude
EXCLUDE_LOs = config["EXCLUDE_LOs"] 
EXCLUDE_SUSPENDED = config["EXCLUDE_SUSPENDED_LOS"]
EXCLUDE_SECONDARY = config["EXCLUDE_SECONDARY"]

# Fetch ratings
ratings = table_parser.get_p2p_explore_ratings()
p2p_anlage_ratings = table_parser.get_p2p_anlage_ratings()

# Exclude LOs
if EXCLUDE_SUSPENDED:
    ratings_filtered = {i: ratings[i] for i in ratings if (ratings[i] >= LOWER_CUTOFF_POINT and ratings[i] < UPPER_CUTOFF_POINT and 'suspended' not in i and i not in EXCLUDE_LOs)}
else:
    ratings_filtered = {i: ratings[i] for i in ratings if (ratings[i] >= CUTOFF_POINT and i not in EXCLUDE_LOs)}

if USE_P2P_ANLAGE:
    print("\nAdjusting the ratings based on P2P Anlage ratings...")

# Compute adjusted ratings per-LO
for i in ratings_filtered:
    
    # Add extra points if positive in P2P Anlage ratings
    if USE_P2P_ANLAGE:
        if i in p2p_anlage_ratings:
            extra_points = (p2p_anlage_ratings[i] - P2P_ANLAGE_MAX_POINTS / 2) / P2P_ANLAGE_MAX_POINTS * P2P_ANLAGE_BONUS
            ratings_filtered[i] += extra_points
            print('P2PAnlage: Updating rating for {} by {:1.2f}'.format(i, extra_points))

    print('Final rating {:25}: {:1.2f}'.format(i, ratings_filtered[i]))

    if ratings_filtered[i] > UPPER_BONUS_POINT:
        ratings_filtered[i]=MULTIPLIER_SEVENTY*ratings_filtered[i]

# Compute amount to invest per LO givent rating
sum_ratings = math.fsum(ratings_filtered.values())
ratings_processed = {i: MONEY_TO_INVEST*ratings_filtered[i] / sum_ratings for i in ratings_filtered}
ratings_processed = collections.OrderedDict(sorted(ratings_processed.items(), key=lambda x:x[1], reverse=True))

print("\nFinal ratings for {} unique LOs: {} \n".format(len(ratings_processed), ratings_filtered))
print("\n\nOutput investment strategy in EUR:\n")

# Compute amount to invest into prim/sec market per LO given overall investment and prim/sec weight, outputs invest. strategy
ctr = 1
for lo in ratings_processed:
    if lo in EXCLUDE_SECONDARY:
        ctr +=1
        print("[{:2}] PRI {:25}: {:10.2f}".format(ctr, lo, round(ratings_processed[lo], 2)))
        ctr +=1
        print("[{:2}] SEC {:25}: {:10.2f}".format(ctr, lo, 0))
    else:
        ctr +=1
        print("[{:2}] PRI {:25}: {:10.2f}".format(ctr, lo, RATIO_PRIMARY*round(ratings_processed[lo], 2)))
        ctr +=1
        print("[{:2}] SEC {:25}: {:10.2f}".format(ctr, lo, RATIO_SECONDARY*round(ratings_processed[lo], 2)))

print("\nInvesting a total amount of {:.2f} EUR.".format(math.fsum(ratings_processed.values())))
print("\nAll done!")
