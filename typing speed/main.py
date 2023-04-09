import time

# List of words to be typed
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# Instructions for user
print('Type the following words as quickly and accurately as possible. Press enter when finished.\n')

# Display each word and record the start time
start_time = time.time()
for word in words:
    input_word = input(f'{word}: ')
end_time = time.time()

# Calculate and display the typing speed
num_words = len(words)
typing_time = end_time - start_time
typing_speed = num_words / typing_time
print(f'\nYou typed {num_words} words in {typing_time:.2f} seconds. Your typing speed is {typing_speed:.2f} words per second.')
