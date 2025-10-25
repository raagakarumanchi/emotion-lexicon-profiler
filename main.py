# Load text
with open('data/the_social_network.txt', 'r') as f:
    script = f.read()

# Load lexicon
from scripts.lexicon import load_nrc_lexicon
lexicon = load_nrc_lexicon('data/nrc_lexicon.txt')

# Tokenize
from scripts.preprocess import clean_and_tokenize
tokens = clean_and_tokenize(script)

# Analyze
from scripts.analyze import tag_emotions
df = tag_emotions(tokens, lexicon)
df.to_csv("output/emotion_counts.csv")

# Visualize
import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(x=df['count'], y=df.index, palette='muted')
plt.title("Top Emotions in The Social Network")
plt.xlabel("Word Count")
plt.ylabel("Emotion")
plt.tight_layout()
plt.savefig("output/emotion_plot.png")
plt.show()
