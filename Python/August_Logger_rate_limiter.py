class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data=dict()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.data or timestamp-self.data[message]>=10:
            self.data[message]=timestamp
            return True
        else:
            return False


if __name__=="__main__":
    inp=[[],[1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]]
    obj=Logger()
    param_1 = obj.shouldPrintMessage(timestamp,message)



    # print("p",len(inp))
    # for i in range(len(inp)):
        # c.shouldPrintMessage(inp[i][0],inp[i][1])
