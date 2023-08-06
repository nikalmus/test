import sys

def get_substrings(string=None, starts_with=None):
    if string is None or starts_with is None:
        print("""Usage: python <script.py> <string> <starts_with>. 
              Use 'c' (consonant) and 'v' (vowel) for <starts_with>.
              Example: python script.py banana c""")
        sys.exit(1)

    vowels = ['a', 'e', 'i', 'o', 'u']
    score={}

    if starts_with == 'c':
        is_not_vowel = lambda char: char not in vowels
    elif starts_with == 'v':
        is_not_vowel = lambda char: char in vowels
    else:
        print("Invalid value for starts_with. Use 'c' for consonants and 'v' for vowels.")
        sys.exit(1)

    for i in range(len(string)):
        if is_not_vowel(string[i]):
            for j in range(i + 1, len(string) + 1):
                sub_substring = string[i:j]
                if sub_substring not in score:
                    score[sub_substring] = 1
                else:
                    score[sub_substring] += 1

    
    return score

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("""Usage: python <script.py> <string> <starts_with>. 
              Use 'c' (consonant) and 'v' (vowel) for <starts_with>"
              Example: python script.py banana c""")
        sys.exit(1)
    if sys.argv[2] not in ['c', 'v']:
        print("Invalid second argument. Use 'c' (consonant) and 'v' (vowel) for <starts_with>")
        sys.exit(1)
    
    string = sys.argv[1]
    starts_with = sys.argv[2]
    score = get_substrings(string, starts_with)
    total = score.values()
    print(total)
    print(score)
