class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word=[]
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        elements=[]
        if word:
            elements.append(word)
        print(elements)
        return elements

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if word==elements[0]:
            return True
        for i in range(len(elements[0])):
            if word[i:]==elements[0][i:]:
                return True
        return False
def my(elements):


if __name__=="__main__":
    word=["bad","dad"]
    for i in range(0,len(word)):
        obj = WordDictionary().addWord(word[i])
    print("obj:",obj)
    # param_2 = obj.search(word)
    # print(param_2)
