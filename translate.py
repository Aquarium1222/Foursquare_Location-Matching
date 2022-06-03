# sudo pip install googletrans==4.0.0-rc1

import string

from googletrans import Translator

translator = Translator()


def translate_text(text, dest = 'en'):
    # translator = Translator()
    result = translator.translate(text, dest).text
    return result


result = translate_text('Al Derwaza	')
print(result)
result = result.lower()
print(result)

result = translate_text('屁眼，好痛。')
print(result)
result = result.lower()
print(result)

text = 'tattokievrg'.replace('.', '. ')
result = translate_text(text)
print(result)
result = result.lower()
print(result)
