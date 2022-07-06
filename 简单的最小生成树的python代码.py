import numpy as np
import pandas as pd
# print(type(a))
# print(a)
# a[0][1]=1
# print(a)
def min_index(close_min):
    for i in range(len(close_min)):
        if(close_min[i]!=0):
            break
    min=i
    for k in range(min+1,len(close_min)):
        if(close_min[k]!=0 and close_min[k]<close_min[min]):
            min=k
    return min

def index(v1,w):
    k=0
    for i in range(len(v1)):
        if(v1[i]==w):
            return k
        else:
            k = k + 1

def chushihua():
    n=int(input("输入有几个点"))
    e=int(input('输入有几条边'))
    biao_zhi=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            biao_zhi[i][j]=999
    V=np.zeros((1,n))
    for i in range(n):
        V[0][i]=int(input("构造顶点"))
    print(V)
    print("请输入边的信息：")
    for i in range(e):
        v1=int(input("输入第一个顶点"))
        v2=int(input("输入第二个顶点"))
        w=int(input("输入边的权值"))
        j=index(V[0],v1)
        k=index(V[0],v2)
        print(j,k)
        if(j>=0 and k>=0):
            biao_zhi[j][k]=w
            biao_zhi[k][j]=w
    return biao_zhi,V
def print_arc(arc):
    print("此图的矩阵为：")
    for i in range(len(arc)):
        for j in range(len(arc)):
            print(arc[i][j],end='\t')
        print('\n')
def prime(gg,start,V):
    sum = np.zeros((2, len(V[0])))
    k=index(V[0],start)
    for i in range(len(V[0])):
        if(i!=k):
            sum[0]=start
            sum[1][i]=gg[k][i]
    sum[1][k]=0
    for i in range(len(V[0])-1):
        k=min_index(sum[1])
        print('{}->{}-权重为{}'.format(sum[0][k],V[0][k],sum[1][k]))
        sum[1][k]=0
        for j in range(len(V[0])):
            if(gg[k][j]<sum[1][j]):
                sum[0][j]=V[0][k]
                sum[1][j]=gg[k][j]

    print("\n")
def daoru():
    file=input("输入你的文件的绝对路径")
    data = pd.read_excel(file, header=0)
    data1 = data.iloc[:, 1:]
    data1 = data1.fillna(value=999)
    data1 = data1.replace(0, 999)
    data1=np.array(data1)
    n=int(input("输入顶点数："))
    V = np.zeros((1, n))
    for i in range(n):
        V[0][i] = int(input("构造顶点"))
    print(V)
    return data1,V
print("欢迎来到最小生成树之prim算法")
choice=int(input("输入你是文件输入还是手指头输入：1,文件输入。2，手指头敲"))
if choice==2:
    ars=chushihua()
    print_arc(ars[0])
    k=int(input("输入从哪里开始"))
    prime(ars[0], k, ars[1])
if choice==1:
    data=daoru()
    print(data[0],data[1])
    k = int(input("输入从哪里开始"))
    prime(data[0], k, data[1])




