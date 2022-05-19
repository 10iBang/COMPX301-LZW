# Taukoriri Nooti 1322671
# Partner
# version 3
import string

# things to do
# -encode using LZW algo, test trie, output phrase numbers
# MultiWayTrie node
class MultiWayTrieNode:

    # Node class
    def __init__(self):

        self.children = [None] * 4096

        # Boolen to notify end of the world
        self.isEndOfWord = False

        self.phrasenumber = 0


# Multiway trie dictionary
class MultiWayTrie:
    # MultiWayTrie structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return MultiWayTrieNode()

    # insert into the trie
    def insert(self, word, phrasenum):
        current = self.root
        length = len(word)
        for i in range(length):
            index = word[i]
            # if current character is not present
            # add to trie
            if not current.children[index]:
                current.children[index] = self.getNode()
            current = current.children[index]
            current.phrasenumber = phrasenum

        # mark as the end of the word
        current.isEndOfWord = True

    def search(self, word):
        # Search word in the trie
        current = self.root
        # gets the length
        length = len(word)
        # for each level in the trie depending on the word
        for level in range(length):
            # set index
            index = word[level]

            if not current.children[index]:
                return False
            current = current.children[index]

        return current != None #and current.isEndOfWord

    def getPhraseNumber(self, word, phrasenum):
        # Search word in the trie
        current = self.root
        # gets the length
        length = len(word)
        # for each level in the trie depending on the word
        for level in range(length):
            # set index
            index = word[level]

            if not current.children[index]:
                print("hello")
                current.children[index] = self.getNode()
                current.phrasenumber = phrasenum
                return current.phrasenumber
            current = current.children[index]
            print(" Phrasenumbers : ",current.phrasenumber)

        return current.phrasenumber


multiwaytrie = MultiWayTrie()


def main():
    try:
        
        # testing purpose
        output = ["Not present in trie", "Present in trie"]
        # Trie object
        mt = MultiWayTrie()
        phrasenum = 256
        pn = 0


        for x in range(256):
            mt.insert(chr(x).encode(), x)
            print(chr(x).encode(), x)
            pn = pn + 1
        print(pn)
        # take name of the file
        file = input("File name: ")
        # print file name
        print("Reading file " + file + " ..")

        # phrasenumber list
        phraselist = []
        leng = 0

        # Reading file as stream of bytes
        # open file
        with open(file, "rb") as f:
            fo = open("output.txt", "w")
            # first input
            currentchar = ""
            checkinput = ""
            ph = ""
            while True:

                # Readfirst line from the file
                line = f.readline()
                # print line read from the file
                length = len(line)
                for i in range(length):
                    # next input char
                    nxtchar = line[i]

                    nextchar = chr(nxtchar)
                    print("current:",currentchar, "")
                   # print("nextchar:",nextchar, "")

                    checkinput = currentchar + nextchar

                    check = checkinput.encode()
                    print("current + nextchar:", check)

                    p = currentchar.encode()
                    c = nextchar.encode()
                    d = p + c
                   # print("p:", p, "c:", c, "d:", d)
                    # If current char + next input char is in the dictionary                       
                    if mt.search(check):

                        # first input char + next input char
                        currentchar = currentchar + nextchar
                        print("found something")
                        print("\n")                      

                    else:
                        ph = str(ph)
                        currenlength = len(currentchar)
                        b = i+1
                        print("b", b)
                        if i+1 > length:#and currenlength > 1:
                            print("if")
                            mt.insert(check, pn)
                            print("added:",checkinput, "phrasenum:", pn)
                            ph = str(pn)
                            fo.write(ph)
                            fo.write("\n")
                            print(ph)
                            
                        elif currenlength > 1:
                            print("length", length)
                            print("i", i)
                            if i + 1 == length:
                                print("nice")
                                code = currentchar.encode()
                                ph = mt.getPhraseNumber(code, pn)
                                ph = str(ph)
                                fo.write(ph)
                                print(ph)
                                fo.write("\n")
                                leng = length
                                break
                            else:
                                print("elif")
                                code = currentchar.encode()
                                ph = mt.getPhraseNumber(code, pn)
                                print(code,output[mt.search(code)])
                                ph = str(ph)
                                fo.write(ph)
                                print(ph)
                                fo.write("\n")
                        else:
                            if i + 1 == length:
                                code = currentchar.encode()
                                code = ord(code)
                                code = str(code)
                                fo.write(code)
                                fo.write("\n")
                                print(code)
                                break
                            else:
                          #      print("else")
                                code = currentchar.encode()
                                code = ord(code)
                                code = str(code)
                                fo.write(code)
                                fo.write("\n")
                                print(code)
                                phraselist.append(ph)
                            
                        # print(mt.getPhraseNumber())
                        # add P+C to the string table
                        mt.insert(check, pn)
                        print("added:",checkinput, "phrasenum:", pn)
                        pn = pn + 1
                            
                            
                        # P=C
                        d = currentchar.encode()
                        print("test:", currentchar, "code:", d)
                        currentchar = nextchar

                        #PRINT NEW LINE
                        print("\n")
                # break out of the while loop and close file
                # when we have read all lines in the file
                if not line:
                    break
        # output code for P
        print(currentchar)
        lengt = len(currentchar)
        if lengt > 1:
            code = nextchar.encode()
            code = ord(code)
            code = str(code)
            fo.write(code)
            fo.write("\n")
            print(code)
            phraselist.append(ph)
        else:
            code = currentchar.encode()
            ph = mt.getPhraseNumber(code, pn)
            ph = str(ph)
            fo.write(ph)
            print(ph)
            print("Finish reading file..")
            # output to file
            fo.close()
            f.close()
    
    except Exception as e:
        print(e)

main()
