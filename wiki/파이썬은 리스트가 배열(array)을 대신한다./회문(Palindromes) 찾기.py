"""
문제 설명

주어진 문자열이 회문이면 True, 회문이 아니면 False를 반환한다.

입력: madam, 출력: True
출력: tomato, 출력: False
"""
# My
def palindromes(target):
    for i in target:
        if i == target[-1]:
            target = target.replace(i, '')
            if len(target) == 1:
                return True
        else:
            return False

## Test code
words = ["racecar", "rotor", "tomato", "별똥별", "코끼리"]
for word in words:
    print(f"Is '{word}' palindrome?  {palindromes(word)}")

# 문자열 슬라이싱 이용하기
## Test code
word = "racecar"
if word == word[::-1]:
    print(True)
else:
    print(False)

# 포인터 두 개를 이용하기
def is_palindrome(word: str) -> bool:
    """문자열 word가 회문(palindrome)인지 검사한다.
    Arguments:
        word (str): 회문인지 검사할 문자열
    Return:
        bool: 회문이면 True, 그렇지 않으면 False를 반환
    """
    left: int = 0
    right: int = len(word)-1
    while left < right:
        if word[left] != word[right]:
            return False
        left, right = left + 1, right - 1
    return True

## Test code
words = ["racecar", "rotor", "tomato", "별똥별", "코끼리"]
for word in words:
    print(f"Is '{word}' palindrome?  {is_palindrome(word)}")