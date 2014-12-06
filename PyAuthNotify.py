import prowlpy
from os import system

prowl = prowlpy.Prowl("<API KEY GOES HERE>")              # replace with your prowl API key

AUTHLOG = open("/var/log/auth.log", "r")                  # log location
BACKUPLOG = open("/root/backups/authbackup.txt", "a")     # log backup location

def checkFails():                                         # function to check for failed logins               
    for line in AUTHLOG:
        BACKUPLOG.write(line)
        if "authentication failure" in line:              # checks for specific text in logfile
            prowl.post("PyAuthNotify",                    # notification content, change to anything
                       "LOGIN FAILURE",
                       "Unsuccessful login attempt",
                       "1")                               # notification priority
        if "user unknown" in line:
            prowl.post("PyAuthNotify",
                       "USER UNKNOWN",
                       "Nonexsistent user login attempt",
                       "2")
        else:
            continue

checkFails()
AUTHLOG.close()
BACKUPLOG.close()
system("> /var/log/auth.log")                             # clears log
exit()
