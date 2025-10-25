from collections import Counter
import pandas as pd

def tag_emotions(tokens, lexicon):
    emotion_counts = {e: 0 for e in lexicon}
    for word in tokens:
        for emotion, words in lexicon.items():
            if word in words:
                emotion_counts[emotion] += 1
    return pd.DataFrame.from_dict(emotion_counts, orient='index', columns=['count']).sort_values(by='count', ascending=False)
