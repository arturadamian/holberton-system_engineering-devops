# Postmortem for Web Debugging

## Issue Summary:

The server was returning a 500 error. It was unable to process a request or an error has occurred in the processing of a request. the reason why it happened was a typo in an extension of a configuration file.

## Timeline:

2:00 pm: Got a 500 error and started debugging process
2:20 pm: Tryed to use strace for debugging and found out the reason
2:30 pm: Made a puppet file that rename the file and ran the command
2:40 pm: Sent a request to the server and got 200 OK

## Root Cause and Resolution: 

The root cause of the error was a typo in the extension of the configuration file in the /var/www/html/wp-settings.php. The exxtension of the class-wp-locale file was".phpp" instead of ".php". To resolve the problem I just rename the file (sed, puppet) and restart the server.

## Corrective and preventative measures:

Need to pay more attention for testing code before deployment. Only senior engineers should have access to write code for config files. Need to improve our monitoring system for prevent such errors.