#Man tonestam ke code gharbal eratosten ro in ghadr kotah benevisam :)
def SOE(n):
    nums = [i for i in range(2,n+1)]
    prime = set(list(map(lambda x: x if True not in [x/i == x//i for i in range(2,int(x**(1/2))+1)] else None,nums)))
    prime.remove(None)
    prime = list(prime)
    prime.sort()
    return prime


print(SOE(2000))
