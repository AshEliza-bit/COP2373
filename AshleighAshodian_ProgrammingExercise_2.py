def get_spam_matches(message, spam_phrases):
    # return a list of spam phrases found in the message
    found = []
    message_lower = message.lower()
    for phrase in spam_phrases:
        phrase_lower = phrase.lower()
        count = message_lower.count(phrase_lower)  # count all matches/times a word is repeated
        found.extend([phrase] * count)  # add the phrase as many times as it repeats in the email message
    return found

def calculate_score(found_phrases):
    return len(found_phrases) # return the spam score based on how many phrases were found

def main():
    # the list of spam phrases
    spam_phrases = [
        '100% guarantee', '100% satisfaction', 'act now',
        'be the first', 'be your own boss', 'call now', 'click below',
        'deal for a limited time', 'double your income', 'earn extra money',
        'exclusive deal', 'fast cash', 'free', 'free gift', 'free membership',
        'giveaway', 'lowest price', 'miracle chance', 'new customers only',
        'no catch', 'no interest', 'not a scam', 'not junk', 'once in a lifetime',
        'prize', 'risk free', 'sign up for', 'take action', 'while supplies last',
        'winner', 'world famous'
    ]

    message = input("Please enter your email message: ") # get user input
    found = get_spam_matches(message, spam_phrases) # read/scan message for spam phrases in the list above
    score = calculate_score(found)     # calculate likeliness of it being spam based on spam score
    if score == 0:
        likelihood = "Not spam"
    elif score <= 3:
        likelihood = "Might be spam"
    else:
        likelihood = "Probably spam"

    # Step 6: Display results
    print("\n--- Spam Check Results ---")
    print("Spam Score:", score)
    print("Likelihood:", likelihood)
    if found:
        print("Triggered phrases:", found)
    else:
        print("No spam phrases detected.")

main()
