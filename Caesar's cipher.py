checker = input ("Please enter 1 to encrypt and 2 to decrypt ")
if checker == 1:
  """
  Caesar's cipher
  (encoder)
  """
  cipher_text = input("Please enter the Cipher text: ")
  cipher_list = []
  for i in cipher_text:
    cipher_list.append(chr(ord(i) + 3))
  print(cipher_list)

else:
  """
  Caesar's cipher
  (decoder)
  """

  cipher_text = input("Please enter the Cipher text: ")
  cipher_list = []
  for i in cipher_text:
    cipher_list.append(chr(ord(i) - 3))
  print(cipher_list)

