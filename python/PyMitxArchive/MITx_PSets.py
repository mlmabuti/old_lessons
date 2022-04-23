# =============================================================================
# # PROBLEM SET #1!!
# =============================================================================
def q19():
    s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', ',o', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    for vowels in s:
        if vowels == "a" or vowels == "e" or vowels == "i" or vowels == "o" or vowels == "u":
            count += 1
    print("number of vowels " + str(count))


def q20():
    s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'bob', 'i', 'j', 'k', 'l',
         'm', 'n', ',o', 'q', 'r', 'bob', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    for i in range(len(s)):
        if s[i:i+3] == 'bob':
            count += 1
    print(count)


def q21():
    s = ['a', 'b', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'p', 'm', 'n', ',o', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    longest = s[0]
    current = s[0]
    for c in s[1:]:
        if c >= current[-1]:
            current += c
            if len(current) > len(longest):
                longest = current
        else:
            current = c
    print("Longest substring in alphabetical order is:", longest)
# =============================================================================
# # PROBLEM SET #2!!
# =============================================================================
