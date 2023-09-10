import time
def typing_speed_test():
    text="The quick brown fox jumps over the dog"
    print("Type the following text:")
    print(text)
    input("Press Enter when you're ready...")
    start_time=time.time()
    user_input=input("Start typing: ")
    end_time=time.time()
    elapsed_time= end_time-start_time
    words_per_minute =len(user_input.split())/(elapsed_time / 60)
    accuracy = calculate_accuracy(user_input,text)
    print(f"\nTime elapsed: {elapsed_time:.2f} seconds")
    print(f"Your typing speed: {words_per_minute:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")
    
def calculate_accuracy(user_input, text):
    correct_characters = sum([1 for a, b in zip(user_input, text) if a == b])
    total_characters = len(text)
    accuracy = (correct_characters / total_characters) * 100
    return accuracy

if __name__ == "__main__":
    typing_speed_test()