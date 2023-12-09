def board_input():
    m = int(input("Enter the number of rows of the board: "))
    n = int(input("Enter the number of columns of the board: "))
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            letter = input(f"Enter the letter in the {j+1}. column of the {i+1}. row of the Matrix: ")
            row.append(letter)
        matrix.append(row)
    return matrix

def words_input():
    words = input("Please enter words with a comma between them: ")
    return [item.strip() for item in words.split(",")]

def word_search(words, matrix):
    for word in words:
        first_letter = word[0]
        found = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == first_letter:
                    if find_word_in_matrix(word, matrix, i, j):
                        found = True
                        print(f"The word '{word}' is found in the matrix starting at position ({i+1}, {j+1}).")
                        break
            if found:
                break

def find_word_in_matrix(word, matrix, i, j):
    for k in range(1, len(word)):
        found = False
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[ni][nj] == word[k]:
                found = True
                i, j = ni, nj
                break
        if not found:
            return False
    return True

# Kullanýcýdan board ve words bilgilerini al
board = board_input()
word_list = words_input()

# Oluþturulan board'u ve words listesini yazdýr
print("Board:")
for row in board:
    print(row)
print("Words:", word_list)

# Kelimeleri matriste ara
word_search(word_list, board)


