# I had to manually do this by trawling cardhoarder, plz clap
class MoxfieldMapper: 
    # we only care about the codes that cause errors
    # I speculate this is an issue with the two letter set codes that MTGO uses, as it seems like scryfall codes "normalize" them into using 3 letter codes
    code_maps = {
        # Mirage 
        "MI": "MIR",
        # Visions
        "VI": "VIS",
        # Portal
        "PO": "POR", #speculative
        # Weatherlight
        "WL": "WTH",
        # Tempest
        "TE": "TMP",
        # Stronghold
        "ST": "STH",
        # Exodus 
        "EX": "EXO",
        # Urza's Saga
        "UZ": "USG",
        # Urza's Legacy
        "UL": "ULG",
        # Urza's Destiny 
        "UD": "UDS",
        # Portal Three Kingdoms
        "PK": "PTK",
        # Mercadian Masques
        "MM": "MMQ",
        # Nemesis 
        "NE": "NEM",
        # Prophecy 
        "PR": "PCY",
        # Invasion 
        "IN": "INV",
        # Planeshift 
        "PS": "PLS",
        # 7th Edition 
        "7E": "7ED",
        # Apocalypse 
        "AP": "APC",
        # Odyssey
        "OD": "ODY",
    }
