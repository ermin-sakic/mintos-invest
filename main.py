#!/usr/bin/python3
import table_parser
import math
import collections

from config import config as cfg

# Amount
RATIO_PRIMARY = 1-cfg["RATIO_INVEST_INTO_SECONDARY"]

# Fetch ratings
p2p_exp_ratings = table_parser.get_p2p_explore_ratings()
p2p_anl_ratings = table_parser.get_p2p_anlage_ratings()

# Exclude LOs
if cfg["EXCLUDE_SUSPENDED_LOS"]:
    ratings_filtered = {i: p2p_exp_ratings[i] for i in p2p_exp_ratings if i not in cfg["EXCLUDE_LOs"] and 'suspended' not in i}
else:
    ratings_filtered = {i: p2p_exp_ratings[i] for i in p2p_exp_ratings if i not in cfg["EXCLUDE_LOs"]}


if cfg["USE_P2P_ANLAGE"]:
    print("\nAdjusting the ratings based on P2P Anlage ratings...")

# Compute adjusted ratings per-LO
for i in ratings_filtered:
    # Add extra points if positive in P2P Anlage ratings
    if cfg["USE_P2P_ANLAGE"]:
        if i in p2p_anl_ratings:
            extra_points = (p2p_anl_ratings[i] - cfg["P2P_ANLAGE_MAX_POINTS"] / 2.0) / cfg["P2P_ANLAGE_MAX_POINTS"] * cfg["THRSH_P2P_ANLAGE_BONUS"]
            ratings_filtered[i] += extra_points
            print('P2PAnlage: Updating rating for {} by {:1.2f}'.format(i, extra_points))

    if ratings_filtered[i] > cfg["THRSH_BONUS_RATING"]:
        print("Updating rating by {}x".format(cfg["BONUS_WEIGHT_MULTIPLIER"]))
        ratings_filtered[i] = cfg["BONUS_WEIGHT_MULTIPLIER"]*ratings_filtered[i]

    print('Aggregate rating {:25}: {:1.2f}'.format(i, ratings_filtered[i]))
   
# Remove all LOs whose rating exceed the threshold bounds 
ratings_filtered = {i: ratings_filtered[i] for i in ratings_filtered if (cfg["THRSH_LOWER_CUTOFF_RATING"] <= ratings_filtered[i] <= cfg["THRSH_UPPER_CUTOFF_RATING"])}

# Compute amount to invest per LO givent rating
sum_ratings = math.fsum(ratings_filtered.values())
ratings_processed = {i: cfg["TOTAL_AMOUNT_INVEST"]*ratings_filtered[i] / sum_ratings for i in ratings_filtered}
ratings_processed = collections.OrderedDict(sorted(ratings_processed.items(), key=lambda x: x[1], reverse=True))

print("\nFinal ratings for {} unique LOs: {} \n".format(len(ratings_processed), ratings_filtered))
print("\n\nOutput investment strategy in EUR:\n")

# Compute amount to invest into prim/sec market per LO given overall investment and prim/sec weight
ctr = 1
for lo in ratings_processed:
    if lo in cfg["EXCLUDE_SECONDARY"]:
        print("[{:2}] PRI {:25}: {:10.2f}".format(ctr+1, lo, round(ratings_processed[lo], 2)))
        print("[{:2}] SEC {:25}: {:10.2f}".format(ctr+2, lo, 0))
    else:
        print("[{:2}] PRI {:25}: {:10.2f}".format(ctr+1, lo, RATIO_PRIMARY*round(ratings_processed[lo], 2)))
        print("[{:2}] SEC {:25}: {:10.2f}".format(ctr+2, lo, cfg["RATIO_INVEST_INTO_SECONDARY"]*round(ratings_processed[lo], 2)))
    ctr += 2

print("\nInvesting a total amount of {:.2f} EUR.".format(math.fsum(ratings_processed.values())))
print("\nAll done!")
