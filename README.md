# moneydance-py
Useful Python scripts for Moneydance

These scripts have been developed for Moneydance 2017.

# Contents
## change-security-cusip.py
Reset the link between a security in your Moneydance file and an Online Banking security, and optionally move that link to a new security.

I developed this script because I accidentally selected the wrong security on the initial import from an Online Banking account. You may also need it if your bank updates the CUSIP, you roll your account over to a new broker, etc.

You will have to edit the security names in the script.
* `move_from` is the security whose information will be copied and wiped.
* `move_to` is the security to which the copied information will be written. Use `None` to just wipe the `move_from` security.

It would be really cool to build an extension that fires this script when a security is removed from a brokerage account, thus resetting the Online Banking link.