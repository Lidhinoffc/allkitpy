import re

def remove_spaces(text):
    return text.replace(" ", "")

def remove_extra_spaces(text):
    return re.sub(r'\s+', ' ', text).strip()

def remove_numbers(text):
    return re.sub(r'\d+', '', text)