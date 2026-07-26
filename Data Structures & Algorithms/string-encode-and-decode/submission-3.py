class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for s in strs:
            string += str(len(s)) + "#" + s

        return string

    def decode(self, s: str) -> List[str]:
        str_arr = []

        i = 0

        while i < len(s):
            l = ""
            j = i

            while s[j].isdigit():
                l += s[j]
                j += 1

            start = j + 1

            str_arr.append(s[start:start + int(l)])

            i = start + int(l)

        return str_arr