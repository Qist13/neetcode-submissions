class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for s in strs:
            string += "$" + str(len(s)) + "#" + s

        return string

    def decode(self, s: str) -> List[str]:
        str_arr = []

        i = 0

        while i < len(s):
            string = ""
            l = ""

            if s[i] == "$":
                j = i + 1

                while s[j] != "#":
                    l += s[j]
                    j += 1

                i = j + 1

            for k in range(i, i + int(l)):
                string += s[k]

            str_arr.append(string)

            i += int(l)

        return str_arr