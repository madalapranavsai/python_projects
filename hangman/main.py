import random

words = [
    "animal", "banana", "coffee", "friend", "guitar", "hacker", "island", "jungle", "kitten", "laptop",
    "magnet", "nectar", "orange", "planet", "quartz", "rabbit", "silver", "turtle", "united", "vacuum",
    "wallet", "yellow", "zephyr", "beacon", "cruise", "danger", "empire", "fabric", "goblin", "hiccup",
    "insect", "jacket", "keeper", "lavish", "market", "native", "object", "palace", "quiver", "rocket",
    "spider", "ticket", "update", "voyage", "wizard", "anchor", "bishop", "cashew", "dancer", "editor",
    "forest", "glance", "herbal", "injury", "jigsaw", "kimono", "launch", "mingle", "nature", "orbital",
    "poetry", "quaint", "refine", "speech", "turkey", "unfold", "virtue", "wander", "yellow", "zygote",
    "absent", "barrel", "camera", "decent", "elmira", "fusion", "gentle", "honest", "ignite", "joyful",
    "kitten", "liable", "motion", "narrow", "outlet", "pillar", "quench", "resist", "shovel", "tablet",
    "thread", "umpire", "violet", "wonder", "yeasty", "zodiac", "anchor", "breeze", "circle", "driven"
]

chosen_word = random.choice(words)
placeholder = "_" * len(chosen_word)
print(placeholder)

game_over = False
correct_letters = []
incorrect_guesses = []
lives = 6 # Number of incorrect guesses allowed

# Hangman stages
hangman_stages = [
    """
      -----
      |   |
          |
          |
          |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
          |
          |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ---------
    """
]


while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters or guess in incorrect_guesses:
        print("You already guessed that letter.")
        continue

    if guess in chosen_word:
        correct_letters.append(guess)
        display = ""
        for letter in chosen_word:
            if letter in correct_letters:
                display += letter
            else:
                display += "_"
        print(display)

        if "_" not in display:
            game_over = True
            print("You win!")
    else:
        incorrect_guesses.append(guess)
        lives -= 1
        print(hangman_stages[6 - lives]) # Display the hangman stage
        print(f"Wrong! You have {lives} lives left.")
        if lives == 0:
            game_over = True
            print("Game over! The word was:", chosen_word)