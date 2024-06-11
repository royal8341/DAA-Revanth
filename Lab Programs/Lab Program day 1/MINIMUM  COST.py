from collections import defaultdict

def minimizeCost(s):
    n = len(s)
    char_count = defaultdict(int)
    res = []
    for i in range(n):
        if s[i] == '?':
            min_char = min(char_count, key=lambda x: char_count[x]) if char_count else 'a'
            res.append(min_char)
        else:
            res.append(s[i])
            char_count[s[i]] += 1
    return ''.join(res)

# Example usage:
s = "ab?ac?"
print(minimizeCost(s))  # Output depends on specific implementation details
''