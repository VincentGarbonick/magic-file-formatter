# Moxfield
MOXFIELD_HEADERS = [
    "Count",
    "Name",
    "Edition",
    "Condition",
    "Language", 
    "Foil",
    "Collector Number",
    "Alter",
    "Playtest Card",
    "Purchase Price"
]

# Moxfield Defaults
MOXFIELD_DEFAULT_CONDITION = "M"
MOXFIELD_DEFAULT_PRICE = "0"
# We are just defaulting to english for everything, for now
MOXFIELD_DEFAULT_LANGUAGE = "en"
MOXFIELD_FALSE = "FALSE"
MOXFIELD_TRUE = "TRUE"

# CSV Formats 
FORMAT_MTGO_CSV = "MTGO"
FORMAT_MOXFIELD = "Moxfield"

def join_headers(headers):
    return ",".join(f'"{header}"' for header in headers)
