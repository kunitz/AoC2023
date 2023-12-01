import os
import num2words

def read_file(filename):
    current_dir = dir_path = os.path.dirname(os.path.realpath(__file__))
    filename_fullpath = os.path.join(current_dir, filename)
    #print(f'{filename_fullpath}')
    # open file in read mode
    file = open(filename_fullpath, "r")

    # read whole file to a string
    data = file.read()
    #print(f'{data}')
    # close file
    file.close()
    return data

def read_2Dfile(filename):
    fileData = read_file(filename)
    return fileData.splitlines()

def sortDict(d: dict):
    #keys = list(d.keys())
    #keys.sort()
    #return {i: d[i] for i in keys}
    return dict(sorted(d.items()))

class StringHelpers:
    def __init__(self) -> None:
        self.LookupNums = []
        self.buildStringLookup()

    def buildStringLookup(self):
        for x in range(10):
            self.LookupNums.append(str(x))
            #self.LookupNums.append(num2words.num2words(x))

    def FindNumsInStr(self, string):
        str_indexes = {}
        for num in self.LookupNums:
            index = 0
            s = string
            while num in s:
                nums = [num,num2words.num2words(num)]
                for n in nums:    
                    i = s.find(n)
                    index = index + i
                    str_indexes[index] = n
                    s_start = i+1
                    s_end = len(s)
                    s = s[s_start:s_end]
                    index = index + len(n)
        return sortDict(str_indexes)
