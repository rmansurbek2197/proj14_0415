# 61
class SortDigits:
    def __init__(self, n):
        self.n = n
    def solve(self):
        return "".join(sorted(str(self.n)))

print(SortDigits(int(input())).solve())

# 62
class SortString:
    def __init__(self, s):
        self.s = s
    def solve(self):
        return "".join(sorted(self.s))

print(SortString(input()).solve())

# 63
class SortStringDesc:
    def __init__(self, s):
        self.s = s
    def solve(self):
        return "".join(sorted(self.s, reverse=True))

print(SortStringDesc(input()).solve())

# 64
class UniqueChars:
    def __init__(self, s):
        self.s = s
    def solve(self):
        return len(set(self.s))

print(UniqueChars(input()).solve())

# 65
class MaxChar:
    def __init__(self, s):
        self.s = s
    def solve(self):
        return max(self.s)

print(MaxChar(input()).solve())
