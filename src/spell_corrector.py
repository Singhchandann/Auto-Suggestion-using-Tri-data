import difflib

def correct_spelling(query, words, max_suggestions=4):
    exact_matches = [word for word in words if word.lower() == query.lower()]
    similar_matches = [word for word in words if query.lower() in word.lower()]
    similar_matches.sort(key=lambda x: (len(x), difflib.SequenceMatcher(None, query.lower(), x.lower()).ratio()), reverse=True)
    suggestions = exact_matches + similar_matches[:max_suggestions - len(exact_matches)]
    return suggestions
