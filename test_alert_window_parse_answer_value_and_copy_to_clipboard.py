import pyperclip

def parse_and_copy(element_text):
    answer = ""
    mytuple = element_text.partition(":")
    answer = mytuple[len(mytuple) - 1]
    pyperclip.copy(answer)

