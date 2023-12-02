# This is a sample Pcolthon script.
import os
import helpers
import num2words

def run():
    lines = helpers.read_2Dfile('P1-1.test')
    s = helpers.StringHelpers()
    sum = 0
    for l in lines:
        sumline = 0
        print(l)
        nums = s.FindNumsInStr(l)
        debug = ""
        for n in nums:
            debug += str(nums[n])
        #print(debug)
        print(nums)
        keys = list(nums.keys())
        first_key = keys[0]
        keylen = len(keys)-1
        last_key = keys[keylen]
        sumline += int(nums[first_key] + nums[last_key])
        #print(sumline)
        sum += sumline
    print(sum)
    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
