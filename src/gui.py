import tkinter as tk
from src.trie import Trie
from src.spell_corrector import correct_spelling
import json

class AutocompleteApp:
    def __init__(self, root, trie, unique_names):
        self.trie = trie
        self.unique_names = unique_names
        self.last_word_start = -1
        self.init_gui(root)

    def init_gui(self, root):
        root.title("Advanced Autocomplete")
        self.search_box = tk.Entry(root, width=50)
        self.search_box.bind("<KeyRelease>", self.update_suggestions)
        self.search_box.bind("<Tab>", self.auto_complete)
        self.search_box.pack()

        self.suggestion_list = tk.Listbox(root, width=50)
        self.suggestion_list.pack()

    def update_suggestions(self, event):
        query = self.search_box.get().strip()
        if query:
            suggestions = []
            query_words = query.split()
            for word in query_words:
                word_suggestions = self.trie.search(word)
                if word_suggestions:
                    suggestions.extend(word_suggestions)
            if not suggestions:
                suggestions = correct_spelling(query, self.unique_names)
            self.display_suggestions(suggestions)
        else:
            self.suggestion_list.delete(0, tk.END)

    def display_suggestions(self, suggestions):
        self.suggestion_list.delete(0, tk.END)
        for suggestion in suggestions[:4]:
            self.suggestion_list.insert(tk.END, suggestion)

    def auto_complete(self, event):
        selected_suggestion = self.suggestion_list.get(0)
        query = self.search_box.get()
        last_space_index = query.rfind(' ', 0, len(query))
        if last_space_index != -1:
            self.search_box.delete(last_space_index + 1, tk.END)
        else:
            self.search_box.delete(0, tk.END)
        self.search_box.insert(tk.END, selected_suggestion)

def run_app():
    with open('data/unique_name.txt', 'r', encoding='UTF8') as file:
        unique_names = json.load(file)
    trie = Trie()
    for name in unique_names:
        trie.insert(name)
    
    root = tk.Tk()
    app = AutocompleteApp(root, trie, unique_names)
    root.mainloop()
