from collections import defaultdict

class memoize:
    def __init__(self, func):
        self.func = func
        self.known_keys = []
        self.known_values = []

    def __call__(self, *args, **kwargs):
        key = (self.func.__name__, args, kwargs) 

        if key in self.known_keys:
            i = self.known_keys.index(key)
            return self.known_values[i]
        else:
            value = self.func(*args, **kwargs)
            self.known_keys.append(key)
            self.known_values.append(value)

            return value

def max_wis2(lst):
    dp = defaultdict(lambda : defaultdict(lambda : (0, None)))
    lst.reverse()
    lst.append(0)
    for i, item in enumerate(lst):
        dp[i]["ignore"] = (dp[i-1]["ignore"][0], (i-1, "ignore")) if dp[i-1]["ignore"][0] > dp[i-1]["pick"][0] \
                          else (dp[i-1]["pick"][0], (i-1, "pick"))
        dp[i]["pick"] = (max(0,item)+dp[i-1]["ignore"][0], (i-1, "ignore"))
    result, ptr = dp[len(lst)-1]["ignore"]
    resultlst = []
    while ptr is not None:
        u,v = ptr
        if v == "pick" and u >= 0 and lst[u] >= 0:
            resultlst.append(lst[u])
        ptr = dp[u][v][1]
    return result, resultlst

@memoize
def max_wis(lst):
    result_p, lst_p = pick(lst, 0)
    result_i, lst_i = ignore(lst, 0)
    return (result_p, lst_p) if result_p >= result_i else (result_i, lst_i)

@memoize
def pick(lst, index):
    if index >= len(lst):
        return 0, []
    item = lst[index]
    result_i, lst_i = ignore(lst, index+1)
    return (result_i, lst_i) if item < 0 else (item+result_i, [item]+lst_i)

@memoize
def ignore(lst, index):
    if index >= len(lst):
        return 0, []
    result_p, lst_p = pick(lst, index+1)
    result_i, lst_i = ignore(lst, index+1)
    return (result_i, lst_i) if result_i > result_p else (result_p, lst_p)

if __name__ == "__main__":

    print max_wis2([])
    print max_wis2([0])
    print max_wis2([7,8,5])
    print max_wis2([7,8,5,6,2])
    print max_wis2([7,8,5,6,2,0])
    print max_wis2([7,8,5,6,2,0,0])

    print max_wis([])
    print max_wis([0])
    print max_wis([7,8,5])
    print max_wis([7,8,5,6,2])
    print max_wis([7,8,5,6,2,0])
    print max_wis([7,8,5,6,2,0,0])

