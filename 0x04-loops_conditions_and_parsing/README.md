### Loops, conditions and parsing

## In this project we learn:

- How to create **SSH keys**
- What is the advantage of using **#!/usr/bin/env bash** over **#!/bin/bash**
- How to use while, until and for loops
- How to use **if, else, elif** and **case** condition statements
- How to use the cut command
- What are files and other comparison operators, and how to use them


## Some important sources:

- [Loops sample](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html)
- [Variable assignment and arithmetic](http://tldp.org/LDP/abs/html/ops.html)
- [Comparison operators](http://tldp.org/LDP/abs/html/comparison-ops.html)
- [File test operators](http://tldp.org/LDP/abs/html/fto.html)
- [Make your scripts portable](https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html)

- man: *env*, *cut*
- help: *for*, *while*, *until*, *if*

## In this project we learn:

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

## Tasks

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