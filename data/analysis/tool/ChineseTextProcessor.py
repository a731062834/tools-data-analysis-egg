#encoding:utf8
import jieba
import re


class ChineseTextProcessor:
    regex_alphabetic = "[a-zA-Z]+"
    regex_numeric = "[0-9]+"

    def __init__(self):
        self.tokenizer = jieba.Tokenizer()

    def get_words(self, text):
        segmented_words = self.tokenizer.tokenize(text)

        words_list = []
        for word in segmented_words:
            if len(word) < 2:
                continue
            if re.match(self.regex_numeric, word):
                continue
            if re.match(self.regex_alphabetic, word):
                continue
            words_list.append(word)
        return words_list

    def split_to_sentences(self, text):
        return re.split("。|！|？", text)
