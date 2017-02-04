#!/usr/bin/env python3
"""Reset the link between a security in your Moneydance file and an Online Banking security,
and optionally move that link to a new security.
The canonical source for this package is https://github.com/finitemobius/moneydance-py"""

import re

__author__ = "Finite Mobius, LLC"
__credits__ = ["Jason R. Miller"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Finite Mobius, LLC"
__email__ = "jason@finitemobius.com"
__status__ = "Development"


# You will need to edit these two variables

# The security for which we want the BREAK the link
move_from = 'Security to Break Link'

# The security TO which we want to MOVE the link
# Use None to just break the old link
move_to = 'Security to Link'
# move_to = None  # To only wipe the move_from security

# Init
book = moneydance.getCurrentAccountBook()
currs = book.getCurrencies()

# Put a list here so it's easier to maintain
schemes_to_reset = ['CUSIP', 'OTHER', 'CUSIP-broken']
# Build a dict from the above list, with None as values
schemes = {}
for key in schemes_to_reset:
    schemes[key] = None

# First, find the security we need to move the link away from
ss = re.compile(move_from, re.IGNORECASE)
for curr in currs:
    if ss.match(curr.getName()):
        print(curr.getName() + ':')
        print('- removing: ' + str.join(', ', schemes.keys()))
        # Populate the list of elements to be copied
        for s in schemes.keys():
            # Copy the old value to our dict
            schemes[s] = curr.getIDForScheme(s)
            # Wipe the old value
            curr.setIDForScheme(s, None)

print(schemes)

# Next, find the security we want to link to
if move_to is not None:
    ss = re.compile(move_to, re.IGNORECASE)
    for curr in currs:
        if ss.match(curr.getName()):
            print(curr.getName() + ':')
            # Paste the elements we copied earlier
            for s in schemes.keys():
                # Skip any values that were None before.
                # This mostly prevents accidentally running this script twice and blowing this one away, too.
                if schemes[s] is not None:
                    print('- ' + s + ' changing from ' + str(curr.getIDForScheme(s)) + ' to ' + schemes[s])
                    curr.setIDForScheme(s, schemes[s])
