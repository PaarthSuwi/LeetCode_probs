# ============================================================
# LeetCode 824 - Goat Latin
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# A sentence S is given. The rule is:
# - If a word begins with a vowel: append "ma"
# - If a word begins with a consonant: move the first letter to the end, append "ma"
# - Add one 'a' at the end of each word per its 1-indexed position.
# Return the final sentence.
#
# Example:
#   Input:  sentence = "I speak Goat Latin"
#   Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
#
# Constraints:
#   - 1 <= sentence.length <= 150
#   - sentence consists of English letters and spaces.
#   - sentence has no leading or trailing spaces.
#
# ============================================================
# THEORY / APPROACH:
# Split sentence into words. For each word (1-indexed position i):
# - If vowel start: word + "ma" + "a"*i
# - If consonant start: word[1:] + word[0] + "ma" + "a"*i
#
# Time Complexity:  O(n^2)  — due to string concatenation for 'a's
# Space Complexity: O(n)
# ============================================================

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set('aeiouAEIOU')
        words = sentence.split()
        result = []
        for i, word in enumerate(words, 1):
            if word[0] in vowels:
                result.append(word + 'ma' + 'a' * i)
            else:
                result.append(word[1:] + word[0] + 'ma' + 'a' * i)
        return ' '.join(result)
