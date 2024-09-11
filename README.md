# Advanced Name Auto-Suggestion & Spelling Correction using Tri data structure

## Overview
This project provides an advanced case-insensitive name auto-suggestion system using a Trie data structure and a Tkinter-based graphical user interface (GUI). It also offers spelling correction using the Levenshtein distance algorithm.

## Features
- **Fast Auto-Suggestions**: Powered by a Trie data structure.
- **Spelling Correction**: Helps fix minor typing errors.
- **Interactive GUI**: Simple Tkinter-based interface with real-time suggestions.
- **Case-Insensitive Search**: Works regardless of name capitalization.
- **Advanced Completion**: Tab key auto-completes the top suggestion.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Singhchandann/Auto-Suggestion-using-Tri-data.git
   cd name-autocomplete```
  
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

## How It Works
# Trie Data Structure
Names are stored in a Trie, which allows efficient insertion and searching of names. The search operation is case-insensitive.

# Spelling Correction
Spelling errors are corrected using a similarity algorithm based on Levenshtein distance. If a name is misspelled, similar names are suggested.

# User Interface (Tkinter)
The GUI is built with Tkinter, allowing users to type and receive real-time suggestions. Users can press Tab to auto-complete the top suggestion.
