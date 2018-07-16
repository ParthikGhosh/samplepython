import struct
import base64

# Method for encoding ints with base64 encoding
def encode(n):
	data = struct.pack("i", n)
	s = base64.b64encode(data)
	return s

# Method for decoding ints with base64 encoding 
def decode(s):
	data = base64.b64decode(s)
	n = struct.unpack("i", data)
	return n[0]

# Checks the request object to see if the call was successful
def is_successful(response):
	if 200 <= response.status_code and response.status_code <= 299:
		return True
	else:
		return False