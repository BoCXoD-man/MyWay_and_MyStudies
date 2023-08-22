from collections import Counter

def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        counter = Counter(s)

        if counter['('] == counter[')'] and \
            counter['['] == counter[']'] and \
            counter['{'] == counter['}'] :
            return True
        else:
            return False

assert isValid('(){}[]') == True
assert isValid('({}[]') == False