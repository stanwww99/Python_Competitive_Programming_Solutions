# List of Hangul initial consonants (초성)
CHO = ('ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ')

# List of Hangul medial vowels (중성)
JOONG = ('ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ')

# List of Hangul final consonants (종성)
# Note: The first element is '' (no final consonant)
JONG = ('','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ')

# Number of test cases
for i in range(int(input())):
    # Read 초성, 중성, 종성 from input
    cho = CHO.index(input())      # index of initial consonant
    joong = JOONG.index(input())  # index of vowel
    jong = JONG.index(input())    # index of final consonant

    # Hangul syllable composition formula:
    #   44032 + (초성 * 588) + (중성 * 28) + 종성
    code = cho * 588 + joong * 28 + jong + 44032

    # Convert Unicode code point to actual Hangul character
    print(chr(code))
