import random
def common(a,b):
    res=[ ele for ele in a if ele in b]
    return res

if __name__=="__main__":
    a=random.sample(range(1,30),12)
    b=random.sample(range(1,30),16)
    print(a)
    print(b)
    print(common(a,b))

'''a = [1,1,2,3,5,8,13,21,34,55,89]'''
'''b=[1,2,3,4,5,6,7,8,9,10,11,12,13,14] '''
    
