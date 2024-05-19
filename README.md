### BSidesBNE CTF Challenge Submission Template
Firstly, Thank you! for volunteering some time to help out with the BsidesBNE CTF by creating a challenge for others to enjoy on the day. In order to streamline the process for the other volunteer admins, we kindly request your submission fits within the following guidelines.

## What Kind of Challenge can I make?
Almost anything you like! We typically have all the following CTF categories:
* Web
* Pwn
* Crypto
* Rev
* Beginner
* Trivia
* Misc

Difficulty ranges from beginner challenges (Admin=1 cookie) through to exploiting nuanced programming language quirks or hardware hacking challenges.

##  Submission Files
To assist with your submission, this repository contains an example directory structure for you to follow along.
 
We'd like authors to provide a `challenge.yml` file which details the necessary metadata about the challenge, and a `healthcheck.py` file (where healthcheck's are appropriate). Details about what can be specified in the `challenge.yml` file is documented in the [YAML Challenge spec](https://github.com/CTFd/ctfcli/blob/master/ctfcli/spec/challenge-example.yml).

* `src/` should contain the source files/code for your challenge.
* `dist/` should contain any files which will be published to the CTFd Board for challengers to see. 

## Deployment
The majority of our challenges are hosted and deployed using `docker-compose`, or are static files that a distributed to the CTF players through the dashboard. If your challenge doesn't work that way, no stress, reach out to the team and we can discuss how to accomdate hosting your challenge.

## How To Submit?
Once you have completed your challenge, get in contact with `n0mad17` via Discord or post in the `#ctf-volunteers` channel in the Bsides Discord https://discord.com/invite/A8KUcuuGQC.  
We will can create a private github repository for you to submit your challenge through, and if it is accepted it will be merged into our main challenges repo!
