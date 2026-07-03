def word_count(text):
    return len(text.split())

def char_count(text):
    return len(text)

def sentence_count(text):
    return len([s for s in text.split('.') if s.strip()])