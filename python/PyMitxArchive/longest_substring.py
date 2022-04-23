s = "abcsdefghwoiabcdefgabcdefghijklmnopqrstuvwxyzhigjkhdoiahfoiasfsf"
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
# Let's define two strings: The current string of increasing letters and the currently longest string.
# Both strings are initialized with the first letter. (This way we can always read their last letter.)
# Then we iterate over the input string s (starting with the second character).
# If the current character c fulfills the requirement c >= current[-1], we add it to the current solution.
# We possibly store the current string as longest.
# If c does not fulfill the ordering requirement, we start with a new solution current = c.
# Finally, we print the longest string.
# =============================================================================
