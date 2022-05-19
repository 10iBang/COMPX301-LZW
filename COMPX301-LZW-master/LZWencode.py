# Taukoriri Nooti 1322671
# Partner
# version final version
import string
import fileinput

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

        return current != None  # and current.isEndOfWord

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
                current.children[index] = self.getNode()
                current.phrasenumber = phrasenum
                return current.phrasenumber
            current = current.children[index]

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
            # print(chr(x).encode(), x)
            pn = pn + 1
        # print(pn)
        # take name of the file
        # file = input("File name: ")

        # print file name
        # print("Reading file " + file + " ..")

        # phrasenumber list
        phraselist = []
        leng = 0

        # Reading file as stream of bytes
        # open file
        ##        with open(file, "rb") as f:

        # fo = open("output.txt", "w")
        # first input
        currentchar = ""
        checkinput = ""
        ph = ""
        for line in fileinput.input():
            currentchar = ""
            # Readfirst line from the file
            # line = f.readline()
            # print line read from the file
            length = len(line)
            for i in range(length):
                # next inptu char
                nxtchar = line[i]

                nextchar = nxtchar
                # print("nextchar:",nextchar, "")

                checkinput = currentchar + nextchar

                check = checkinput.encode()

                p = currentchar.encode()
                c = nextchar.encode()
                d = p + c
                # print("p:", p, "c:", c, "d:", d)
                # If current char + next input char is in the dictionary
                if mt.search(check):

                    # first input char + next input char
                    currentchar = currentchar + nextchar

                else:
                    ph = str(ph)
                    currenlength = len(currentchar)
                    b = i + 1
                    if i + 1 > length:  # and currenlength > 1:
                        mt.insert(check, pn)
                        ph = str(pn)
                        print(ph)

                    elif currenlength > 1:
                        if i + 1 == length:
                            code = currentchar.encode()
                            ph = mt.getPhraseNumber(code, pn)
                            ph = str(ph)
                            print(ph)
                            leng = length
                            break
                        else:
                            code = currentchar.encode()
                            ph = mt.getPhraseNumber(code, pn)
                            ph = str(ph)
                            print(ph)
                    else:
                        if i + 1 == length:
                            code = currentchar.encode()
                            code = ord(code)
                            code = str(code)
                            print(code)
                            break
                        else:
                            code = currentchar.encode()
                            code = ord(code)
                            code = str(code)
                            print(code)
                            phraselist.append(ph)

                    # print(mt.getPhraseNumber())
                    # add P+C to the string table
                    mt.insert(check, pn)
                    pn = pn + 1

                    #
                    d = currentchar.encode()
                    currentchar = nextchar
            # break out of the while loop and close file
            # when we have read all lines in the file
        # output code for P
        # print(currentchar)
        lengt = len(currentchar)
        if lengt > 1:
            code = nextchar.encode()
            code = ord(code)
            code = str(code)
            print(code)
            phraselist.append(ph)
        else:
            code = currentchar.encode()
            ph = mt.getPhraseNumber(code, pn)
            ph = str(ph)
            print(ph)
            # print("Finish reading file..")
            # output to file

    except Exception as e:
        print(e)


main()
