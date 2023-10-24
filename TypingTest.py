import random
def generate_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a versatile and powerful programming language.",
        "Practice makes perfect.",
        "Typing tests can help improve your accuracy and speed.",
        "Hello, World!",
    ]
    return random.choice(sentences)


def calculate_accuracy(correct_text, user_input):
    correct_words = correct_text.split()
    user_words = user_input.split()

    if len(correct_words) == 0:
        return 0

    correct_word_count = len(correct_words)
    matching_word_count = sum(1 for a, b in zip(correct_words, user_words) if a == b)
    accuracy = (matching_word_count / correct_word_count) * 100
    return accuracy


def typing_test():
    sentence = generate_random_sentence()
    print("Type the following sentence:")
    print(sentence)

    user_input = input()

    accuracy = calculate_accuracy(sentence, user_input)
    print(f"Your typing accuracy: {accuracy:.2f}%")


if __name__ == "__main__":
    print("Welcome to the Typing Test Program!")
    while True:
        typing_test()
        play_again = input("Do you want to try another typing test? (yes/no): ").lower()
        if play_again != "yes":
            break
