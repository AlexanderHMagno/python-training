word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "pear", "plum", "peach", "pineapple", "plum", "pear", "peach", "pineapple", "plum", "pear", "peach", "pineapple"]

hangman_stages = [
    # 0 lives (Dead)
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
    # 1 life
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    # 2 lives
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    # 3 lives
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    # 4 lives
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    # 5 lives
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    # 6 lives (Full health)
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """
]
