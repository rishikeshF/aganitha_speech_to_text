from speech_text import speech_text

example_1 = "It costs twelve hundred forty eight dollars only"
example_2 = "Give me four hundred dollars for buying tripple A standard mask"
example_3 = "C M is going to visit our city next evening"
example_4 = "Password is Double B followed by Tripple A"
example_5 = "I am in need of fifty thousand dollars for paying college fees"
example_6 = "Your salary might be two hundred dollars after completion of this course"

text_converter = speech_text()

print(text_converter.speech_to_text(example_1))
print(text_converter.speech_to_text(example_2))
print(text_converter.speech_to_text(example_3))
print(text_converter.speech_to_text(example_4))
print(text_converter.speech_to_text(example_5))
print(text_converter.speech_to_text(example_6))


