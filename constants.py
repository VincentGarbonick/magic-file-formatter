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

# Formats 
FORMAT_MTGO_CSV = "MTGO CSV"
FORMAT_MTGO_DEK = "MTGO DEK"
FORMAT_MOXFIELD = "Moxfield"

# Extensions 
DEK = ".dek"
CSV = ".csv"
XML = ".xml"

# xml
MTGO_CARD_TAG = "Cards"

# Frontend constants
APP_NAME = "MTG File Formatter"
INPUT_FORMATS = [FORMAT_MTGO_DEK, FORMAT_MTGO_CSV]
OUTPUT_FORMATS = [FORMAT_MOXFIELD]
RESULT_FILE_NAME = "result"

# Backend constnats 
SUCCESS_CODE = 0
FAILURE_CODE = 1
PASSTHROUGH_CODE = 10

def join_headers(headers):
    return ",".join(f'"{header}"' for header in headers)
