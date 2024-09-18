#!/usr/bin/python3
def multiple_returns(sentence):
    sentencelen = len(sentence)
    if sentencelen > 0:
        return (sentencelen, sentence[0])
    return (0, None)i
