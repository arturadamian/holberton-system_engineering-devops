=Loops, conditions and parsing

## Here is the (non-exhaustive) list of commands & concepts you should master to be verbose with Unix systems:

awk # pattern scanning and processing language
basename # strip directory and suffix from filenames
bg # resumes suspended jobs without bringing them to the foreground
cat # print files
cd # change the shell working directory.
chmod # change file mode
chown # change file owner and group
crontab # maintain crontab files
curl # transfer a URL
cut # remove sections from each line of files
date # display or set date and time
dig # DNS lookup utility
df # report file system disk space usage
diff # compare files line by line
du # estimate file space usage
echo # display a line of text
find # search for files in a directory hierarchy
fg # resumes suspended jobs and bring them to the foreground
grep # print lines matching a pattern
kill # send a signal to a process
less # read file with pagination
ln # create links
ls # list directory contents
lsb_release # print distribution-specific information
lsof # list open files
mkdir # create
mv # move files
nc # arbitrary TCP and UDP connections and listens
netstat # print network connections, routing tables, interface statistics...
nice # execute a utility with an altered scheduling priority
nproc # print the number of processing units available
passwd # change user password
pgrep # look up processes based on name and other attributes
pkill # send signal to processes based on name and other attributes
printenv # print all or part of environment
pwd # print name of current/working directory
top # display Linux processes
tr # translate or delete characters
ps # report a snapshot of the current processes
rm # remove files or directories
rmdir # remove directories
rsync # remote file copy
scp # secure copy (remote file copy program)
sed # stream editor for filtering and transforming text
sleep # suspend execution for an interval of time
sort # sort lines of text file
ssh # OpenSSH SSH client (remote login program)
ssh-keygen # SSH key generation, management and conversion
su # substitute user identity
sudo # execute a command as another user
tail # output the last part of files
tar # manipulate archives files
tr # translate or delete characters
uname # Print operating system name
uniq # report or omit repeated lines
uptime # show how long system has been running
w # Show who is logged on and what they are doing
whereis # locate the binary, source, and manual page files for a command
which # locate a command
wc # print newline, word, and byte counts for each file
xargs # build and execute command lines from standard input
| # redirect standard output to another command
> # redirect standard output
< # redirect standard input
& # send process to background

# Some handy shortcuts:

CTRL+A # go to beginning of line
CTRL+B # moves backward one character
CTRL+C # stops the current command
CTRL+D # deletes one character backward or logs out of current session
CTRL+E # go to end of line
CTRL+F # moves forward one character
CTRL+G # aborts the current editing command and ring the terminal bell
CTRL+K # deletes (kill) forward to end of line
CTRL+L # clears screen and redisplay the line
CTRL+N # next line in command history
CTRL+R # searches in your command history
CTRL+T # transposes two characters
CTRL+U # kills backward to the beginning of line
CTRL+W # kills the word behind the cursor
CTRL+Y # retrieves last deleted string
CTRL+Z # stops the current command, resume with fg in the foreground or bg in the background

# Some important sources:

[Loops sample](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html)
[Variable assignment and arithmetic](http://tldp.org/LDP/abs/html/ops.html)
[Comparison operators](http://tldp.org/LDP/abs/html/comparison-ops.html)
[File test operators](http://tldp.org/LDP/abs/html/fto.html)
[Make your scripts portable](https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html)

- man: *env*, *cut*
- help: *for*, *while*, *until*, *if*

/In this project we learn:

- How to create SSH keys
- What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
- How to use while, until and for loops
- How to use if, else, elif and case condition statements
- How to use the cut command
- What are files and other comparison operators, and how to use them


## For correcting our script we going to use Shellcheck

Shellcheck is a tool that will help you write proper Bash scripts.
It will make recommendations on your syntax, semantic and provide advice
on edge cases that you might not have thought about.

Tasks

0. Create a SSH RSA key pair and Share your public key in file
(**0-RSA_public_key.pub**)

1. A Bash script that displays Holberton School 10 times using for loop
(**1-for_holberton_school**)

2. A Bash script that displays Holberton School 10 times using while loop
(**2-while_holberton_school**)

3. A Bash script that displays Holberton School 10 times using until loop
(**3-until_holberton_school**)

4. A Bash script that displays Holberton School 10 times using while loop
and if statement but for the 9th iteration,
displays Holberton School and then Hi on a new line.
(**4-if_9_say_hi**)

5. A Bash script that loops from 1 to 10 and:

displays bad luck for the 4th loop iteration
displays good luck for the 8th loop iteration
displays Holberton School for the other iterations

use while loop and if, else, elif statements
(5-4_bad_luck_8_is_your_chance)

6. A Bash script that displays numbers from 1 to 20 and:

displays bad luck from China for the 4th loop iteration
displays bad luck from Japan for the 9th loop iteration
displays bad luck from Italy for the 17th loop iteration

Use the while loop (for and until are forbidden)
Use the case statement
(**6-superstitious_numbers**)

7. A Bash script that displays the time for 12 hours and 59 minutes:

display hours from 0 to 12
display minutes from 1 to 59

Use the while loop
We only display the first 70 lines using the head command.
(**7-clock**)

8. A Bash script that displays the content of the current directory
In a list format
Where only the part of the name after the first dash is displayed
You must use the for loop (while and until are forbidden)
Do not display hidden files
(**8-for_ls**)

9. A Bash script that gives you information about the holbertonschool file:

Use if and, else
Bash script should check if the file exists and print:
if the file exists: holbertonschool file exists
if the file does not exist: holbertonschool file does not exist
If the file exists, print:
if the file is empty: holbertonschool file is empty
if the file is no empty: holbertonschool file is not empty
if the file is a regular file: holbertonschool is a regular file
if the file is not a regular file: (nothing)
(**9-to_file_or_not_to_file**)

10. A Bash script that displays numbers from 1 to 100:

Displays FizzBuzz when the number is a multiple of 3 and 5
Displays Fizz when the number is multiple of 3
Displays Buzz when the number is a multiple of 5
Otherwise, displays the number in a list formata
(**10-fizzbuzz**)