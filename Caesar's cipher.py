"""
Caesar's cipher
(encoder)
"""

cipher_text = input ("Please enter the Cipher text: ")
cipher_list = []
for i in cipher_text:
  cipher_list.append(chr(ord(i) + 3))
print (cipher_list)

"""
Caesar's cipher
(decoder)
"""

cipher_text = input ("Please enter the Cipher text: ")
cipher_list = []
for i in cipher_text:
  cipher_list.append(chr(ord(i) - 3))
print (cipher_list)