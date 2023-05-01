#https://github.com/webaverse-studios/webaverse/issues/108

from Text_generator import generate_text

def generate_variations(input_text, n=3):
    variations = []
    for _ in range(n):
        generated_text = generate_text(f"Generate a varation of this text, return only the varation and nothinf else:\n{input_text}")
        variations.append(generated_text)
    return variations

input_text = "The sky is blue today"
text_variations = generate_variations(input_text)
print(text_variations)