checker = input ("Please enter 1 to encrypt and 2 to decrypt ")
cipher_text = input("Please enter the Cipher text: ")
if checker == "1":
  """ Caesar's cipher(encoder) """
  for i in cipher_text:
    print(chr(ord(i) + 3), end=" ")
else:
  """ Caesar's cipher(decoder) """
  for i in cipher_text:
    print(chr(ord(i) - 3), end=" ")

