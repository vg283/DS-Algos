# Problem: Given a dictionary of words and a pattern. We need to find ALL possible ways to break down the pattern into
# smaller words such that each of those words are present in the dictionary.
# Solution:
# Recursive approach: Starting from index 0 of the pattern, adding one character at a time, check if the char set (part of the pattern)
# exists in the dictionary. Once there is a match, say at index i, we have to repeat the same for the remaining part of the pattern i.e.
# from i+1 to end of pattern, In recursion terms, we can just ask our assistant (same function with rest of the pattern )to break down the
# remaining part. This would give us just one way of breaking down the pattern. To get ALL the remaining ways, we need to continue matching
# from i+1 onwards. So from 0 to say index j where j > i, we might have another match. After which we can again ask our assistant to break
# down the remaining part of pattern i.e. from j+1 to end of pattern.
#
# By repeating the above process all the way untill the end of pattern we will get ALL possible ways to break down the given pattern
#
# DP approach: Translating the above recursive approach to iterative, we get the below solution
#



# Recursive solution
def wb(text, start, p_output, dict):
    if start == len(text):
        print(p_output)
        return

    for i in range(start, len(text)):
        if text[start:i+1] in dict:
            p_output.append(text[start:i+1])
            wb(text, i+1, p_output, dict)
            p_output.pop()


# DP solution
def wb_dp(txt, dictionary):
    dp_table = []
    for i in range(len(txt)+1):
        dp_table.append([])

    dp_table[len(txt)].append([])
    for i in range(len(txt)-1, -1, -1):
        for j in range(i, len(txt)):
            if txt[i:j+1] in dictionary:
                current_word = txt[i:j+1]
                for s in range(len(dp_table[j+1])):
                    local_str = ""
                    local_str += current_word
                    local_str += " " + ''.join(dp_table[j+1][s])
                    dp_table[i].append(local_str.strip())

    print(dp_table[0])


dictlist = ['leet', 'code', 'leetcode', 'is', 'awe', 'some', 'awesome']
text = "leetcodeisawesome"

#wb(text, 0, [], dict)
wb_dp(text, dictlist)
