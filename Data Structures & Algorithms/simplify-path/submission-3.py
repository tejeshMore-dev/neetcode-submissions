class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []

        for word in paths:
            if word == "." or word == "":
                continue
            elif word == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(word)

        return "/" + "/".join(stack)