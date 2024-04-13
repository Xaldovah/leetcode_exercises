#/usr/bin/python3
"""This class module merges two strings alternately and appends the results
"""

class Solution:
    """solution class
    """
    
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merges the strings by adding letters in alternating order, starting with
        word1. If a string is longer than the other, append the additional letters
        onto the end of the merged string

        Return:
            Merged String
        """
        result = ""
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            result += word1[i]
            result += word2[j]
            i += 1
            j += 1

        # Append remaining characters from word1, if any
        while i < len(word1):
            result += word1[i]
            i += 1

        # Append remaining characters from word2, if any
        while j < len(word2):
            result += word2[j]
            j += 1

        return result


def main():
    solution = Solution()
    test_cases = [
            ("abc", "defgh"),  # Expected: "adbecfgh"
            ("apple", "orange"),  # Expected: "aoprplaeonge"
            ("cat", "dog"),  # Expected: "cdaotg"
            ("", "xyz"),  # Expected: "xyz"
            ("abc", ""),  # Expected: "abc"
            ("", ""),  # Expected: ""
    ]

    for word1, word2 in test_cases:
        merged = solution.mergeAlternately(word1, word2)
        print(f"Merged string for '{word1}' and '{word2}': {merged}")


if __name__ == "__main__":
    main()
