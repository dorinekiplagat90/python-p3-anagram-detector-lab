
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        # store the original word in lowercase for case-insensitive comparison
        self.word = word.lower()

    def match(self, candidates):
        matches = []
        sorted_word = sorted(self.word)  # sorted letters of the original word

        for candidate in candidates:
            candidate_lower = candidate.lower()
            # skip if candidate is identical to the original word
            if candidate_lower == self.word:
                continue
            # check if sorted letters match
            if sorted(candidate_lower) == sorted_word:
                matches.append(candidate)

        return matches
