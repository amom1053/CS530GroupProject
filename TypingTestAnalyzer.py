# Main class i guess
import TypingTest
import TestStats

def main():
  num_words = 5
  typingtest_instance = TypingTest.TypingTest(num_words)
  print("Type the following text:")
  print(typingtest_instance.get_typing_test_string())
  input("\nPress enter to begin timer:")
  test_stats = typingtest_instance.begin_typing_test()
  print(test_stats.getWPM())
  print(test_stats.getAccuracy())
  print(test_stats.getTimeTaken())
  
  

main()
  
    