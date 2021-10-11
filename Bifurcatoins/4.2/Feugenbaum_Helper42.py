#from datetime import *
from progress.bar import IncrementalBar

def limit(r):   #89063048256 OV
    reses = [0.1]
    for i in range(2000000):
        x0 = reses[len(reses)-1]
        reses.append(r*x0*(1-x0))
    x0 = reses[1999999]
    out = [x0]
    for i in range(1999998, 498, -1):
        if (round(reses[i],4)!=round(x0,4)):
            out.append(reses[i])
        else:
            break
    return rund(out, 4)

def lim(*args):      #сначала шаг, потом глубина, потом точность,
    r = args[0]       #потом точность ответа
    if len(args) > 1:
        deepness = args[1]
        if len(args) > 2:
            exatlyness = args[2]
            if len(args) >3:
                rexatlyness = args[3]
            else:
                rexatlyness = 4
        else:
            rexatlyness = 4
            exatlyness = 4
    else:
        rexatlyness = 4
        exatlyness = 4
        deepness = 20000

    reses = [0.1]

    reses = ending(r, deepness, reses)

    x0 = reses[deepness-1]
    out = [x0]
    for i in range(deepness - 2, 498, -1):
        if (round(reses[i],4)!=round(x0,4)):
            out.append(reses[i])
        else:
            break
    return rund(out, 4)
        
def rund(args, n):
    return [round(i, n) for i in args]

def ending(*args):     #сначала шаг, потом на сколько продлить, потом
    r = args[0]         #предыдущие значения
    if len(args) > 1:
        length = args[1]
        if len(args) > 2:
            reses = args[2]
        else:
            reses = [0.1]
    else:
        reses = [0.1]
        length = 5

    for i in range(length):
        x0 = reses[len(reses)-1]
        reses.append(x0*r*(1-x0))

    return reses

def graph_creator(width, scale):
    #print('Hm')
    graph = []
    
    q = width*scale//100
    #print(width*scale,' iterations remaining')
    bar = IncrementalBar('Countdown', max = q*100)
    for i in range(width*scale):
        bar.next()
        #if (i+1)%q == 0:
        #   print('*',end='')
        #print(i)
        graph.append(lim((i + 1)/(width*scale/3) + 1))
    bar.finish()
    #print()
    #print('OK')
    return graph

'''
w = datetime.now().microsecond/1000000 +datetime.now().second+datetime.now().minute*60

print('hm')
q = graph_creator(1200, 8)
print('OK')

w -= (datetime.now().microsecond/1000000 +datetime.now().second+datetime.now().minute*60)

print(-round(w, 3))
'''

    
#print(len(limit(3.759)))
#print(len(lim(3.759, 2000000)))
#print(lim(1))
#graph = []
#for i in range(1200):    #от 1 до 4
#    graph.append(lim((i+1)/400+1))
#print(graph)

                 
    
    
