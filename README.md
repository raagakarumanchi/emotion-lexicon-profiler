# Emotional Lexicon Profiler

A simple tool that analyzes the emotional language in movie scripts using the NRC Emotion Lexicon.

This project takes a screenplay and figures out what emotions are most common in the dialogue and narration. It's useful for understanding the emotional tone of different scripts or comparing how different writers handle emotions in their work.

## What it does

The tool reads through a movie script and identifies words that are associated with different emotions. It uses the NRC Emotion Lexicon, which is a database that maps thousands of words to eight basic emotions: anger, fear, joy, sadness, trust, anticipation, surprise, and disgust.

After processing the text, it gives you a count of how many emotion-related words appear in each category and creates a visual chart showing the results.

## How it works

1. **Load the script**: Reads a text file containing the screenplay
2. **Clean the text**: Removes formatting, converts to lowercase, and breaks it into individual words
3. **Remove noise**: Filters out common words like "the", "and", "is" that don't carry emotional meaning
4. **Find emotions**: Checks each word against the emotion lexicon to see what feelings it's associated with
5. **Count and visualize**: Adds up the emotion counts and creates a bar chart

## What you need

- Python 3.8 or newer
- The packages listed in requirements.txt
- A movie script in plain text format
- The NRC Emotion Lexicon file

## Installation

```bash
# Get the code
git clone https://github.com/yourname/emotional-lexicon-profiler.git
cd emotional-lexicon-profiler

# Install the required packages
pip install -r requirements.txt

# Download the English language model for spaCy
python -m spacy download en_core_web_sm

# Download stopwords for NLTK
python -m nltk.downloader stopwords
```

## Running the analysis

```bash
python main.py
```

This will process the script in `data/the_social_network.txt` and create:
- `output/emotion_counts.csv` - A spreadsheet with the emotion counts
- `output/emotion_plot.png` - A bar chart showing the results

## Example: The Social Network

I tested this on Aaron Sorkin's screenplay for The Social Network. Here's what it found:

<p align="center">
  <img src="output/emotion_plot.png" alt="Emotion Analysis Results" width="600"/>
</p>

The script has a lot of anger-related words (67 instances), followed by fear (54), joy (33), sadness (30), and trust (28). This makes sense for a movie about betrayal and legal battles.

## Project structure

```
emotional-lexicon-profiler/
├── data/
│   ├── the_social_network.txt       # The script file (you need to add this)
│   └── nrc_lexicon.txt              # The emotion word database
├── scripts/
│   ├── lexicon.py                   # Loads the emotion database
│   ├── preprocess.py                # Cleans and processes the text
│   └── analyze.py                   # Counts emotions and creates results
├── notebooks/
│   └── EmotionalLexiconProfiler.ipynb  # Jupyter notebook version
├── output/
│   ├── emotion_counts.csv           # Results in spreadsheet format
│   └── emotion_plot.png             # Visual chart
├── requirements.txt                  # Python packages needed
└── README.md                        # This file
```

## Getting the script file

The Social Network script isn't included in this repo because of copyright. To run the example, you'll need to:

1. Go to ScriptSlug or another script site
2. Download The Social Network screenplay
3. Save it as `data/the_social_network.txt`
4. Make sure it's plain text (no PDF formatting)

## Customizing for other scripts

You can easily analyze other scripts by:

1. Putting your script file in the `data/` folder
2. Updating the filename in `main.py`
3. Running the analysis

The tool works with any plain text file, so you could analyze novels, plays, or any other text with emotional content.

## What this demonstrates

This project shows how to:
- Process text with Python libraries like spaCy and NLTK
- Use pre-built emotion databases for analysis
- Create visualizations with matplotlib and seaborn
- Structure code in a clean, modular way
- Apply NLP techniques to real-world content

## Future improvements

Some ideas for making this better:
- Analyze emotions by character instead of the whole script
- Show how emotions change throughout the story
- Compare multiple scripts side by side
- Build a web interface for uploading scripts
- Add more sophisticated emotion detection using AI models

## Technical details

The main libraries used:
- **spaCy**: For breaking text into words and finding word roots
- **NLTK**: For filtering out common words
- **pandas**: For organizing and analyzing the data
- **matplotlib/seaborn**: For creating charts
- **NRC Emotion Lexicon**: The emotion word database

## Troubleshooting

If you get errors:
- Make sure you've installed all the requirements
- Check that the script file exists in the data folder
- Verify the NRC lexicon file is in the right place
- Try running the commands one by one to see where it fails

## Contributing

Feel free to improve this project! Some areas that could use work:
- Better error handling
- Support for more file formats
- More visualization options
- Performance improvements for large scripts