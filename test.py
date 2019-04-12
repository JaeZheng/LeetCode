from collections import defaultdict

s = "barfoothefoobarman"
word_len = 3
cur = 0
while cur<=len(s):
    print(s[cur:cur+word_len])
    cur += word_len