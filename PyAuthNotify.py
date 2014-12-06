import prowlpy
from os import system

prowl = prowlpy.Prowl("a14760eb4526b54081ddd233ae9f819ff523000f")

# prowl.post("AuthNotify", "test!")
AUTHLOG = open("/var/log/auth.log", "r")
BACKUPLOG = open("/root/backups/authbackup.txt", "a")

def checkFails():
    for line in AUTHLOG:
        BACKUPLOG.write(line)
        if "authentication failure" in line:
            prowl.post("CF30",
                       "LOGIN FAILURE",
                       "Unsuccessful login attempt",
                       "1")
        if "user unknown" in line:
            prowl.post("CF30",
                       "USER UNKNOWN",
                       "Possible bruteforce attempt",
                       "2")
        else:
            continue

checkFails()
AUTHLOG.close()
BACKUPLOG.close()
system("> /var/log/auth.log")
exit()
