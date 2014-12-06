PyAuthNotify
============

Prowl integrated failed authentication script wirtten in python.

PyAuthNotify is a simple python script written for integration with Prowl that checks the Auth.log every minute for multiple types of failed authentications. If it finds one, it sends a notification to prowl. After checking the log, the script backs it up and clears the log.

To run this script you need to get the ProwlPy library from here: https://github.com/jacobb/prowlpy
