class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        
        res = ''
        for idx in range(len(str_num)):
            if str_num[idx] == '6':
                res += '9'
                break
            else:
                res += '9'
        
        if idx+1 != len(str_num):
            res += str_num[idx+1:]
            
        return  int(res)