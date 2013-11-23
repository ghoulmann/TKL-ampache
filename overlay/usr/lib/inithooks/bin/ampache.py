#!/usr/bin/python
"""Set Ampache admin password

Option:
--pass= unless provided, will ask interactively
--email= unless provided, will ask interactively
"""

import sys
import getopt

import subprocess

from dialog_wrapper import Dialog

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h", ['help', 'pass=', 'email='])
    except getopt.GetoptError, e:
        usage(e)

    email = ""
    password = ""
    adduser="/var/www/ampache/bin/install/ampache_user.sh"

    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

 
    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Ampache Password",
            "Enter new password for the Ampache 'admin' account.")

    if not email:
        d = Dialog('TurnKey Linux - First boot configuration')
        email = d.get_email(
            "Admin Email",
            "Enter an email address for the Ampache 'admin' account.",
            "admin@example.com")

    subprocess.call(["php", "/var/www/ampache/bin/install/add_user.inc", "-u admin", "-l admin", "-p " + password, "-e " + email])


if __name__ == "__main__":
    main()
