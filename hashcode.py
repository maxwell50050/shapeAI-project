# -*- coding: utf-8 -*-
"""
created by sanchit
"""
#Challenge 1

import hashlib

string = input(str("Enter the text: "))

hashoutput = hashlib.md5(string.encode('utf-8'))
#using hexdigest()
print("The hexadecimal equivalent of HASH is: ", end = "")
print(hashoutput.hexdigest())