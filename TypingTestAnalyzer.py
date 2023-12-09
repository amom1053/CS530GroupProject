# Main class
import TypingTest
import FingerDetection
import threading

num_words = 5
fingerDetectionInstance = FingerDetection.FingerDetection(0.15)
fingerDetectionInstance.startVideoCapture()
typingtest_instance = TypingTest.TypingTest(num_words)


def typingTestThreadFunc():
    typingtest_instance.begin_typing_test()


def fingerDetectionThread():
    fingerDetectionInstance.startGrabbingData()


def main():
    print("Type the following text:")
    print(typingtest_instance.get_typing_test_string())
    input("\nPress enter to begin timer and enter when finished: ")

    # Begin threads for typing test and opencv finger detection
    opencvThread = threading.Thread(target=fingerDetectionThread)
    typingTestThread = threading.Thread(target=typingTestThreadFunc)
    typingTestThread.start()
    opencvThread.start()

    # Wait for threads to finish before grabbing the data
    typingTestThread.join()
    opencvThread.join()
    test_stats = typingtest_instance.getTestStats()
    dataList = fingerDetectionInstance.getData()

    # Prints out data gather from the test
    print("Words Per Minute: " + str(test_stats.getWPM()))
    print("Accuracy: " + str(test_stats.getAccuracy()))
    print("Time Taken: " + str(test_stats.getTimeTaken()))
    print("Total Number of Movements: " + str(len(dataList)))
    print("Recommended Number of Movements: " + str(len(typingtest_instance.get_typing_test_string())))


main()
    
