PyAuthNotify
============

Prowl integrated failed authentication script wirtten in python.

PyAuthNotify is a simple python script written for integration with Prowl that checks the Auth.log every minute for multiple types of failed authentications. If it finds one, it sends a notification to prowl. After checking the log, the script backs it up and clears the log. This script reqiures the prowlpy library which I have included.


Do the following to add the script to you crontab as root

~# sudo nano /etc/crontab

add this line at the bottom:

*/1 * * * * root python <PATH TO PyAuthNotify.py>


This script includes the prowlpy library which I have included.



