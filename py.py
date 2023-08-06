from collections import Counter

def canConstruct(ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomeNoteCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)

        for item, value in ransomeNoteCounter.items():
            if item in magazineCounter.keys():
                if value <= magazineCounter[item]:
                    continue
                else: 
                    return False
            else:
                return False
        return True

ransomNote = "pa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))