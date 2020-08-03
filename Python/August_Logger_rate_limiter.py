class Logger:
    def __init__(self):
        self.data=dict()
        
    def shouldPrintMessage(self,timestamp, message):
        if message not in self.data or timestamp-self.data[message]>=10:
            self.data[message]=timestamp
            return True
        else:
            return False


if __name__=="__main__":
    inp=[[1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]]
    c=Logger()
    for i in range(len(inp)):
        print(c.shouldPrintMessage(inp[i][0],inp[i][1]))
