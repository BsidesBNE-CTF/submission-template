#!/usr/bin/env python3
"""
The whole purpose of this solve script is to validate that the challenge is solveable, from start to finish.
Try and replicate all of the network interactions necessary to solve the challenge inside the solve script, rather than skipping straight to the end and checking if the flag is correct.
Also for extra points - if sensible you can do integrity checking of web pages etc. with an md5sum or similar.
# Don't forget to add timeouts to any network connections/requests.
"""

import argparse

# fill out this one for socket based challenges
def solve(host, port=12345):
	try: 
		# solve challenge, return True if challenge is working as intended
		return True
	except:
		# exception
		return False

# fill out this one for web based challenges
def solve(target):
	try: 
		# solve challenge, return True if challenge is working as intended
		return True
	except:
		# exception
		return False

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Healthcheck')
	parser.add_argument('--connection-info', help='Either in the format `nc <host> <port>` or `http[s]://host[:port]`', required=True)
	args = parser.parse_args()
	conn = args.connection_info
	if conn[:3] == "nc ":
		_, host, port = conn.split(' ')
		ok = solve(host, port)
	elif conn[:5] == "http":
		target = conn
		ok = solve(target)
	if ok:
		print("challenge_name is good") # change challenge name
		exit(0)
	else:
		print("challenge_name is bad") # change challenge name
		exit(1)
