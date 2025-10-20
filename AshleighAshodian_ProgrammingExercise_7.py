import re

def get_paragraph(): #prompts the user to enter a paragraph of their desired length
    paragraph = input("Please enter a paragraph: ")
    return paragraph #user input

def count_sentences(paragraph): #keeps track of how many sentences there are
    pat = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)' #the pattern from lesson 7.4 tweaked to also include sentences that start with numbers
    sentences = re.findall(pat, paragraph)
    return sentences #sentences is the list of sentences from the user's input

def main():
    paragraph = get_paragraph()
    sentences = count_sentences(paragraph)

    print("Individual sentences:")
    for sentence in sentences:
        print(f"--> {sentence.strip()}") #adds an arrow to each sentence
    print(f"\nTotal number of sentences: {len(sentences)}") #print the number of sentences there are

main()
