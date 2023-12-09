#the program of word search puzzle
# Function to take user input for the board dimensions and its letters
def board_input():
    m = int(input("enter the number of rows of the board:"))
    n= int(input("Enter the number of columns of the board:"))
    matrix=[]
    for i in range(m):
        row=[]
        for j in range(n):
            letter=input(f"Enter the letter in the {j+1} column of the {i+1} row of the Matrix:")
            row.append(letter)
        matrix.append(row)   
    return matrix

# Function to take user input for the words separated by commas
def words_input():
    words = input("Please enter words with a comma between them: ")
    return [item.strip() for item in words.split(",")]

# Function to search for words in the matrix
def word_search(words, matrix):
    result_matrix=[]
    for word in words:
        first_letter = word[0]
        found = False
         # Loop through the matrix to find the first letter of the word
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == first_letter:
                    # If found, check if the whole word is present in the matrix
                    if find_word_in_matrix(word, matrix, i, j):
                        found = True
                        result_matrix.append(word)
                        break
            if found:
                break
    return result_matrix

# Function to check if a word is present in the matrix starting from a given position
def find_word_in_matrix(word, matrix, i, j):
    for k in range(1, len(word)):
        found = False
        # Check adjacent positions for the next letter of the word
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[ni][nj] == word[k]:
                found = True
                i, j = ni, nj
                break
        # If the next letter is not found in any adjacent position, return False    
        if not found:
            return False
    return True 

# Get user input for the board and words                    
user_board=board_input()
user_words=words_input()  

# Print the user input board and words
print("Board:")
for row in user_board:
    print(row)
print("Words:", user_words)

# Search for words in the board and print the result
user_search=word_search(user_words,user_board)
print(user_search)

        
        
