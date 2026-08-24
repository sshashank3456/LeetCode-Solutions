class Solution:
    def addDigits(self, num: int) -> int:
        while(num>=10):
            sum=0
            temp= num
            for i in range(temp):
                ld=temp%10
                sum=sum+ld
                temp=temp//10
            num=sum
        return num
                