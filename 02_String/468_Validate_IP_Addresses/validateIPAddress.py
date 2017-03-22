'''
Problem:
	- Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.
	IPv4 addresses are canonically represented in dot-decimal notation, 
		which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;
	Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.
	
	IPv6 addresses are represented as eight groups of four hexadecimal digits, 
		each group representing 16 bits. 
	The groups are separated by colons (":"). 
		For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. 
	Also, we could omit some leading zeros among four hexadecimal digits 
		and some low-case characters in the address to upper-case ones, 
		so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address
	(Omit leading zeros and using upper cases).
	However, we don't replace a consecutive group of zero value 
		with a single empty group using two consecutive colons (::) to pursue simplicity. 
	For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

	Besides, extra leading zeros in the IPv6 is also invalid. 
	For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.
----------------------------------------------------------------------------------------------------
Examples: 
	172.16.254.1: IPv4 					172.16.254.01: invalid
	2001:0db8:85a3:0000:0000:8a2e:0370:7334: IPv6
	2001:db8:85a3:0:0:8A2E:0370:7334		 IPv6
	2001:0db8:85a3::8A2E:0370:7334 			 invalid
	02001:0db8:85a3:0000:0000:8a2e:0370:7334 invalid
----------------------------------------------------------------------------------------------------
Solution: 
		Try to split by . to check if it's IPv4

Then 	Try to split by : to check if it's IPv6
If cannot do both: return neither
'''
class Solution(object):
	def validIPAddress(self, IP):
		split_by_v4, split_by_v6 = IP.split('.'), IP.split(':')
		# Try v4
		if len(split_by_v4) == 4:
			for a_token in split_by_v4:
				if not a_token.isdigit() or not 0 <= int(a_token) < 256 or (a_token[0] == '0' and len(a_token) > 1):
					return "Neither"
			return "IPv4"
		# Try v6
		def is_hex(token):
			hex_digits = set("0123456789abcdefABCDEF")
			for a_chr in token:
				if a_chr not in hex_digits:
					return False
			return True
		if len(split_by_v6) == 8:
			for a_token in split_by_v6:
				if not a_token or len(a_token) > 4 or not is_hex(a_token):
					return "Neither"
			return "IPv6"
		return "Neither"
def validIPAddress(IP):
	split_by_v4, split_by_v6 = IP.split('.'), IP.split(':')
	# Try v4
	if len(split_by_v4) == 4:
		for a_token in split_by_v4:
			if not a_token.isdigit() or not 0 <= int(a_token) < 256 or (a_token[0] == '0' and len(a_token) > 1):
				return "Neither"
		return "IPv4"
	# Try v6
	def is_hex(token):
		hex_digits = set("0123456789abcdefABCDEF")
		for a_chr in token:
			if a_chr not in hex_digits:
				return False
		return True
	if len(split_by_v6) == 8:
		for a_token in split_by_v6:
			if len(a_token) == 0 or len(a_token) > 4 or not is_hex(a_token):
				return "Neither"
		return "IPv6"
	return "Neither"
print validIPAddress("172.16.254.1")
print validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
print validIPAddress("2001:0db8:85a3::8A2E:0370:7334")
print validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334")
print validIPAddress("20EE:FGb8:85a3:0:0:8A2E:0370:7334")
