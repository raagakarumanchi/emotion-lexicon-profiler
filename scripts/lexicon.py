def load_nrc_lexicon(path):
    lexicon = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            word, emotion, flag = line.strip().split('\t')
            if int(flag) == 1:
                lexicon.setdefault(emotion, set()).add(word)
    return lexicon  # {emotion: set(words)}
