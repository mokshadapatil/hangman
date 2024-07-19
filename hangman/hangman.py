import random

categories = {
    'fruits': ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot', 'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon'],
    'flowers': ['rose', 'tulip', 'daisy', 'sunflower', 'daffodil', 'orchid', 'lily', 'marigold', 'hibiscus', 'lavender', 'jasmine', 'violet', 'lotus'],
    'cities': ['paris', 'london', 'newyork', 'tokyo', 'delhi', 'sydney', 'dubai', 'rome', 'berlin', 'mumbai', 'shanghai', 'moscow', 'beijing', 'istanbul', 'vienna'],
    'animals': ['tiger', 'elephant', 'giraffe', 'kangaroo', 'lion', 'zebra', 'panda', 'rabbit', 'koala', 'alligator', 'penguin', 'dolphin', 'octopus']
}

def get_random_word(category):
    return random.choice(categories[category])

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    print('Welcome!')
    print('Choose a category: fruits, flowers, cities, animals')
    category = input('Enter the category: ').lower()

    if category not in categories:
        print("Invalid category. Please choose from 'fruits', 'flowers', 'cities', 'animals'.")
        return

    word = get_random_word(category)
    guessed_letters = set()
    attempts = len(word) + 3
    score = 0

    print(f'Guess the word! Hint: The word is a {category}.')

    while attempts > 0:
        print()
        print(display_word(word, guessed_letters))
        print(f'Attempts left: {attempts}')
        print(f'Guessed letters: {", ".join(guessed_letters)}')

        guess = input('Enter a letter to guess: ').lower()

        if not guess.isalpha() or len(guess) != 1:
            print('Please enter a single letter.')
            continue

        if guess in guessed_letters:
            print('You have already guessed that letter.')
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f'Good guess! The letter {guess} is in the word.')
            if set(word) <= guessed_letters:
                print(f'Congratulations! You guessed the word: {word}')
                score += 10
                print(f'Your score is {score}')
                break
        else:
            attempts -= 1
            print(f'The letter {guess} is not in the word.')

        if attempts == 0:
            print(f'\nGame over! The word was: {word}')
            break

if __name__ == '__main__':
    hangman()