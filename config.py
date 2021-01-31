config = {
    # General Settings
    "USE_P2P_ANLAGE": True,
    "P2P_ANLAGE_URL": 'http://p2p-anlage.de/2020/10/mintos-analyse-auswirkungen-der-corona-krise-auf-kreditgeber-bei-mintos-102020/',
    
    "USE_P2P_EXPLORE": True,
    "P2P_EXPLORE_URL": "https://explorep2p.com/mintos-lender-ratings/",

    "USE_MINTOS_RATINGS": False,

    # Investment settings, invests (1-ratio)*100% into primary market for the LO
    "TOTAL_AMOUNT_INVEST": 2000,
    "RATIO_INVEST_INTO_SECONDARY": 0.4,

    # Exclude LOs - not to be invested into 
    "EXCLUDE_LOs": ['Creditter', 'Kredit24', 'Pinjam Yuk', 'Swiss Capital', 'EcoFinance' ,'DanaRupiah', 'AlfaKredyt', 'Stikcredit', 'Capitalia', 'Kredit Pintar', 'Creditstar', 'TASCredit', 'Stickcredit', 'Julo', 'Extra Finance', 'Acema', 'Finclusion', 'Aasa', 'ITF Group', 'Akulaku', 'Alex Credit', 'Mwananchi', 'BB Finance Group', 'ID Finance Spain', 'Dziesiątka Finanse', 'Fireof', 'Watu Credit', 'Finko (Sebo, Moldova)'],

    # Exclude LOs for secondary market assignment 
    "EXCLUDE_SECONDARY":['Mozipo Group', 'Credius', 'CashCredit', 'Everest Finanse', 'Revo Technology', 'Mikro Kapital Belarus', 'Dozarplati', 'Credissimo', 'Dineo Credito', 'Sun Finance Latvia', 'Novaloans', 'Kviku', 'Lime Zaim', 'Sun Finance Denmark', 'Evergreen', 'GFM', 'Zenka', 'Sun Finance Poland', 'SOS Credit', 'Rapicredit'],

    # Exclude suspended LOs
    "EXCLUDE_SUSPENDED_LOS": True,
    
    # Rating parametrization - cut-off points (exclude LOs above / below these points)
    "THRSH_LOWER_CUTOFF_RATING": 50,
    "THRSH_UPPER_CUTOFF_RATING": 200,

    # Rating Parametrization - invests *BONUS_WEIGHT_MULITPLIER as much if LO exceeds threshold rating
    "THRSH_BONUS_RATING": 71,
    "BONUS_WEIGHT_MULTIPLIER": 2,    

    # P2P-Anlage Specific Settings
    "P2P_ANLAGE_MAX_POINTS": 25,
    "THRSH_P2P_ANLAGE_BONUS": 10,
}
