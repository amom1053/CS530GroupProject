import random
import time

def generate_random_sentence(num_words):
    with open("wordlist.txt") as words_file:
        common_words = words_file.read().splitlines()

    return ' '.join(random.choice(common_words) for _ in range(num_words))


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
    # Get input
    try:
        num_words = int(input("Provide length for typing test: "))
    except:
        print("Invalid length provided, will use default of 25 words.")
        num_words = 25
    
    typing_test_string = generate_random_sentence(num_words)
    
    print("Type the following text:")
    print(typing_test_string)
    
    input("\nPress enter to begin timer:")

    start_time = time.time()
    user_input = input()
    end_time = time.time()
    
    time_taken = end_time - start_time
    words_per_minute = (len(user_input)/time_taken) / 5 * 60
    
    accuracy = calculate_accuracy(typing_test_string, user_input)
    print(f"Your typing accuracy: {accuracy:.2f}%, with a speed of {words_per_minute} words per minute.")


if __name__ == "__main__":
    print("Welcome to the Typing Test Program!")
    while True:
        typing_test()
        while True:
            play_again = input("Do you want to try another typing test? (yes/no): ").lower()
            if play_again == "no":
                print("Thank you for using the Typing Test Program. Goodbye!")
                exit()                                              # Exit the program if the user enters 'no'
            elif play_again == "yes":
                break                                               # Exit the inner while-loop if the user enters 'yes'
            else:
                print("Invalid input. Please enter 'yes' or 'no'.") # Asks the question again