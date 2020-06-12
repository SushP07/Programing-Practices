    def isHappy(self, n: int) -> bool:
        #sums=0
        repeat=[1,4,16,37,58,89,145,42,20]
        #nlist=[]
        if n==1:
            return True
        else:
            while(n not in repeat):
                x=sum(int(i)**2 for i in str(n))
                n=x
                if(n==1):
                        return True
                elif n!=1 and n in repeat:
                        return False
