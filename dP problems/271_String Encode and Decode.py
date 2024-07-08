'''
String Encode and Decode
Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
'''


def encode(strs):
    #Encoding using (length of incoming string)#(String) and so on
    res = ""
    for i in strs:
        res+=str(len(i))+"#"+i
    return res


def decode(s):
    res=[]
    index=0
    i, j = index, index
    while j<len(s):
        if s[j]!="#":
            j+=1
        else:
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            i=j+length+1
            j=i
    return res




Input= ["we","say",":","yes","!@#$%^&*()"]
s=encode(Input)
print(F"Encoded String : {s}")
print("Decoded list : ")
print(decode(s))