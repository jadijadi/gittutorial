import sys

def input_func(string):
    pred_arr=string.split(',')

    #remove white spaces around values if there is
    for i in range(len(pred_arr)):
        pred_arr[i]=pred_arr[i].strip()

    #change str values to corresponding int values  
    index = pred_arr.index('-')
    pred_arr.remove('-')
    pred_arr = [int(i) for i in pred_arr]
    pred_arr.insert(index,'-')
    
    length=len(pred_arr)

    #creating and computing suffix array as pos
    pos=[None]*length
    pos[0]=length-1
    r=0
    while pred_arr[r]!='-':
        pos[pred_arr[r]]=pos[r]-1
        r=pred_arr[r]

    #print the computed suffix array:
    print(*pos,sep=",")
    
if __name__ == '__main__':
    input_func(open(sys.argv[1]).read().strip())
