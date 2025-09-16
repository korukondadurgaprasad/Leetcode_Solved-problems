class Solution(object):
    def lemonadeChange(self, bills):
        five=0
        ten=0
        for bill in bills:
            if bill==5:
                five+=1
            elif bill==10:
                if five>0:
                    five-=1
                    ten+=1
                else:
                    return False
            else:
                if five>0 and ten>0:
                    five-=1
                    ten-=1
                elif five>=3:
                    five-=3
                else:
                    return False
        return True
            
