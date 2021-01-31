# Mintos-Invest - A helper tool for your Mintos investments

## What is it?

- `mintos-invest` is a helper tool for computing weight-adjusted investments for Mintos loan originators.

- The user can then adjust per-LO investment strategies for both primary and secondary markets according to computed investment assignments.

- `mintos-invest` thus helps minimize the risk exposure for individual LOs. It is fully configurable.

## How does it work?

1) The script crawls the latest per-LO ratings from Mintos-external websites and considers them in the aggreagete per-LO score.
2) The script adjusts the per-LO investments for both primary and secondary markets, given the aggregate ratings and user preference.
 
Currently, `mintos-invest` crawls the latest per-LO ratings from the following sources: 
- [Explore P2P] (www.ExploreP2P.com)
- [P2P-Anlage] (www.P2P-Anlage.de)


## Show me an example!

python3 is required to execute the ``main.py``:
```python
python3 main.py
```

Exemplary output after using default configuration:

```
Output investment strategy in EUR:

[ 2] PRI Placet Group             :     117.19
[ 3] SEC Placet Group             :      78.12
[ 4] PRI DelfinGroup              :     112.09
[ 5] SEC DelfinGroup              :      74.72
[ 6] PRI IuteCredit               :     110.96
[ 7] SEC IuteCredit               :      73.97
[ 8] PRI Wowwo                    :     102.18
[ 9] SEC Wowwo                    :      68.12
[10] PRI Credissimo               :     169.36
[11] SEC Credissimo               :       0.00
[12] PRI Credius                  :     168.42
[13] SEC Credius                  :       0.00
[14] PRI Esto                     :      46.85
[15] SEC Esto                     :      31.23
[16] PRI Creamfinance             :      45.01
[17] SEC Creamfinance             :      30.00
[18] PRI Revo Technology          :      69.58
[19] SEC Revo Technology          :       0.00
[20] PRI Everest Finanse          :      69.58
[21] SEC Everest Finanse          :       0.00
[22] PRI Dineo Credito            :      67.22
[23] SEC Dineo Credito            :       0.00
[24] PRI CashCredit               :      66.05
[25] SEC CashCredit               :       0.00
[26] PRI Sun Finance Latvia       :      64.87
[27] SEC Sun Finance Latvia       :       0.00
[28] PRI Mikro Kapital Belarus    :      63.92
[29] SEC Mikro Kapital Belarus    :       0.00
[30] PRI Mogo                     :      38.21
[31] SEC Mogo                     :      25.48
[32] PRI Mikro Kapital Moldova    :      38.21
[33] SEC Mikro Kapital Moldova    :      25.48
[34] PRI Mikro Kapital Russia     :      37.51
[35] SEC Mikro Kapital Russia     :      25.00
[36] PRI Dozarplati               :      61.09
[37] SEC Dozarplati               :       0.00
[38] PRI Novaloans                :      60.15
[39] SEC Novaloans                :       0.00
[40] PRI Kviku                    :      59.44
[41] SEC Kviku                    :       0.00

Investing a total amount of 2000.00 EUR.

All done!
```

Above investments was assigned according to aggregate ratings:
```
Final ratings for 20 unique LOs: {'Credissimo': 143.6, 'Mogo': 54.0, 'Placet Group': 165.6, 'IuteCredit': 156.8, 'DelfinGroup': 158.4, 'Creamfinance': 63.6, 'Revo Technology': 59, 'Wowwo': 144.4, 'Dozarplati': 51.8, 'Dineo Credito': 57, 'Sun Finance Latvia': 55, 'Credius': 142.8, 'Esto': 66.2, 'Mikro Kapital Russia': 53, 'Mikro Kapital Belarus': 54.2, 'Mikro Kapital Moldova': 54, 'Kviku': 50.4, 'Everest Finanse': 59.0, 'CashCredit': 56, 'Novaloans': 51} 
```

## Investment and rating preferences

To compute the above assignments, following configurable parameters were considered:
- ``"TOTAL_AMOUNT_INVEST": 2000``
- ``"RATIO_INVEST_INTO_SECONDARY": 0.4``
- ``"EXCLUDE_SUSPENDED_LOS": True``
 
A number of LOs were excluded using the `EXCLUDE_LO` parameter:
 - ``"EXCLUDE_LOs": ['Creditter', ... ,'Finko (Sebo, Moldova)']``

A number of LOs were excluded from secondary market assignment:
 - ``"EXCLUDE_SECONDARY":['Mozipo Group', ... ,'Rapicredit']``

 Rating cut-off points were used to exclude LOs above / below these points:
 - ``"THRSH_LOWER_CUTOFF_RATING": 50``
 - ``"THRSH_UPPER_CUTOFF_RATING": 100``

Particular LOs can be preferred using the mulitplier (applied only if an LO exceeds threshold rating):
 - ``"THRSH_BONUS_RATING": 71``,
 - ``"BONUS_WEIGHT_MULTIPLIER": 2``

## Final remarks

Please feel free to adjust the configuration according in ``config.py`` to your preferences!
