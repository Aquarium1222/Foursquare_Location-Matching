# pip install pygtrans

from pygtrans import Translate, Null


class Translation:
    def __init__(self):
        self.client = Translate()

    def translate(self, source):
        text = self.client.translate(source, target='en')
        if isinstance(text, Null):
            print(text.msg)
            return source
        elif isinstance(source, str):
            return text.translatedText
        return [i.translatedText for i in text]


if __name__ == '__main__':
    trans = Translation()
    result = trans.translate('Al Derwaza	')
    print(result)
    result = result.lower()
    print(result)

    result = trans.translate('屁眼，好痛。')
    print(result)
    result = result.lower()
    print(result)

    result = trans.translate('tattokievrg.org')
    print(result)
    result = result.lower()
    print(result)

    result = trans.translate('やめて')
    print(result)
    result = result.lower()
    print(result)

    result = trans.translate(['やめて', '好屌'])
    print(result)
