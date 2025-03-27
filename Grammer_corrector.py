from textblob import TextBlob

def correct_grammar(text):
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    return corrected_text
text = input("Enter text to correct: ")
corrected_text = correct_grammar(text)
print(f"Corrected: {corrected_text}")