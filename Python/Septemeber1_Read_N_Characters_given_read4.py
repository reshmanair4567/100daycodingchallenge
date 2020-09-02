
class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        idx=0
        while n>0:
            buf4=[""]*4
            remain=read4(buf4)
            if remain<1:
                return idx
            for i in range(min(remain,n)):
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
        return idx