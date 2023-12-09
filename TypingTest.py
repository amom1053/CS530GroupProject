import random
import time
import TestStats

class TypingTest:
    def __init__(self, num_words: int) -> None:
        self._accuracy = None # instantiate accuracy score
        self.num_words = num_words
        self.typing_test_string = self._generate_random_sentence(self.num_words)
        self.test_statistics = TestStats.TestStats()
    
    # Private helper class to generate sentence based on the num_words input
    def _generate_random_sentence(self, num_words):
        with open("wordlist.txt") as words_file:
            common_words = words_file.read().splitlines()
            
        return ' '.join(random.choice(common_words) for _ in range(num_words))

    # Private helper class which returns accuracy
    def _calculate_accuracy(self, correct_text, user_input):
        correct_words = correct_text.split()
        user_words = user_input.split()

        if len(correct_words) == 0:
            return 0

        correct_word_count = len(correct_words)
        matching_word_count = sum(1 for a, b in zip(correct_words, user_words) if a == b)
        accuracy = (matching_word_count / correct_word_count) * 100
        return accuracy

    # Get typing test string
    def get_typing_test_string(self) -> str:
        return self.typing_test_string
    

    # Begin typing test
    def begin_typing_test(self):
        # Need to move this outside the class
        start_time = time.time()
        user_input = input()
        end_time = time.time()
        time_taken = end_time - start_time
        # words_per_minute = len(user_input.split()) / (time_taken / 60)
        words_per_minute = (len(user_input)/time_taken) / 5 * 60
        
        
        self.test_statistics.setTimeTaken(time_taken).setWPM(words_per_minute).setAccuracy(self._calculate_accuracy(self.typing_test_string, user_input))
        
    def getTestStats(self) -> TestStats:
        return self.test_statistics

