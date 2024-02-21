class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        cur_str = ""
        cur_num = 0
        for character in s:
            if character.isdigit():
                cur_num = cur_num*10 + int(character)
            elif character == "[":
                stack.append(cur_num)
                stack.append(cur_str)
                cur_num = 0
                cur_str = ""
            elif character == "]":
                prev_str = stack.pop()
                prev_num = stack.pop()
                cur_str = prev_str + cur_str * prev_num
            else:
                cur_str +=character
        while stack:
            cur_str = stack.pop() + cur_str
        return cur_str
        