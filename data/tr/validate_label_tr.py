# Validate and normalize tr (Turkish) transcriptions.
# Returns a cleaned version of the label
# or None if it's invalid.
# SEE: https://github.com/ftyers/commonvoice-utils/blob/main/cvutils/validator.py
# & https://github.com/ftyers/commonvoice-utils/blob/main/cvutils/data/tr/validate.tsv

import re, os, sys, unicodedata

def validate_label(label):
    # For now we can only handle [a-z ']
    if re.search(r"[0-9]|[(<\[\]&*{]", label) is not None:
        return None

	# REPL
    label = label.replace(u'\u0021', " ") # !
    label = label.replace(u'\u0022', " ") # "
    label = label.replace(u'\u0027', " ") # '
    label = label.replace(u'\u002e', " ") # .
    label = label.replace(u'\u002c', " ") # ,

    label = label.replace(u'\u002d', " ") # -
    label = label.replace(u'\u2014', " ") # —
    label = label.replace(u'\u2013', " ") # –
	
    label = label.replace(u'\u003a', " ") # :
    label = label.replace(u'\u003b', " ") # ;
    label = label.replace(u'\u003f', " ") # ?

    label = label.replace(u'\u2018', " ") # ‘
    label = label.replace(u'\u201c', " ") # “
    label = label.replace(u'\u201d', " ") # ”
	# ADDED - REPL
    label = label.replace(u'\u2026', " ") # …
	
	# NORM
    label = label.replace(u'\u2019', u'\u0027') # ’ ->	'
    label = label.replace(u'\u00fb', u'\u0075') # û -> u
    label = label.replace(u'\u0131\u0307', u'\u0069') # î -> i
    label = label.replace(u'\u0049\u0307', u'\u0130') # İ -> İ
	
	# DEL
    label = label.replace(u'\u0307', "") #̇
    label = label.replace(u'\u00ad', "") # All soft hyphens
	
    label = re.sub("  *", " ", label) # multiple consequitive spaces
    label = label.strip()
    label = label.lower()

    return label if label else None
