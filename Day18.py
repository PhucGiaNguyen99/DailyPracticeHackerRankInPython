class Day18:
    def __init__(self):
        self.stack = []
        self.queue = []

    def popCharacter(self):
        return self.stack.pop()

    def pushCharacter(self, char):
        self.stack.append(char)

    def dequeueCharacter(self):
        char = self.queue[0]
        self.queue = self.queue[1:]
        return char

    def enqueueCharacter(self, char):
        self.queue.append(char)

    def isPalindrome(self, s):
        l = len(s)
        for i in range(l):
            day18.pushCharacter(s[i])
            day18.enqueueCharacter(s[i])

        isPalindrome = True

        ''' pop the top character from stack 
        dequeue the first character from queue
        compare both the characters'''
        for i in range(l // 2):
            if day18.popCharacter() != day18.dequeueCharacter():
                isPalindrome = False
                break
        return isPalindrome


if __name__ == '__main__':
    # read the string s
    s = input()

    # create the Day18 object
    day18 = Day18()

    # finally print whether string s is a palindrome or not
    if day18.isPalindrome(s):
        print("The word, " + s + ", is a palindrome!")
    else:
        print("The word " + s + ", is not a palindrome!")
