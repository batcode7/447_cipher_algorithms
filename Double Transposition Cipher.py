cipher_text = input("Please enter the Cipher text: ")
row_sequence = input("Enter the row sequence: ")
col_sequence = input("Enter the column sequence: ")
cipher_matrix = []

#creating the 2D list / matrix
counter = 0
for i in range(len(row_sequence)):
    col_list = []
    for j in range (len(col_sequence)):
        col_list.append(cipher_text[counter])
        counter += 1
    cipher_matrix.append(col_list)

print ("Plain text in matrix: ")
for i in cipher_matrix:
    print(i)

row_seq_list = []
col_seq_list = []
for i in row_sequence:
    row_seq_list.append(int(i) - 1) # indexing starts with 0

for i in col_sequence:
    col_seq_list.append(int(i) - 1) # indexing starts with 0

changed_row = []
ciphared_matrix = []
# copying the rows as given
for i in range(len(cipher_matrix)):
    changed_row.append(cipher_matrix[row_seq_list[i]])

print ("row altered matrix: ")
for i in changed_row:
    print(i)

# changing column after row alteration
for i in changed_row:
    changed_col = []
    for j in range(len(i)):
        changed_col.append(i[col_seq_list[j]])
    ciphared_matrix.append(changed_col)

print ("column altered matrix: ")
for i in ciphared_matrix:
    print(i)

print("Ciphered text: ")
for i in ciphared_matrix:
    for j in range (len(i)):
        print(i[j], end = " ")