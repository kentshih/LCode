def best(w,items):
   opt = {}
   ans = _best(w,items,opt)
   return ans[0],ans[1]

def _best(w,items,opt):
   if w < 0:
      w = 0
   if opt.has_key(w):
      return opt[w]
   itemnum = []
   for y in xrange(0,len(items)):
      itemnum.append(items[y][2])
   if opt.has_key(0) == False:
      takeitems = []
      for i in xrange(0,len(items)):
         takeitems.append(0)
      opt[0] = 0, takeitems, itemnum

   # print "takeitems: ",takeitems
   maxvalue, maxitem, maxremain = -1,[], []
   maxvalue1, maxitem1, maxremain1 = 0,takeitems, itemnum
   maxvalue2, maxitem2, maxremain2 = 0,takeitems, itemnum
   prevalue, previtems, prevremain = 0,takeitems, itemnum
   itemnum = []
   for y in xrange(0,len(items)):
      itemnum.append(items[y][2])

   for x in xrange(1,w+1): ## compare every size of bag
      # print "capacity: ", x
      pick = 0
      maxvalue2, maxitem2,maxremain2 = _best(x-1,items,opt)
      # print "maxitem2: ", maxitem2 , "maxvalue2: ", maxvalue2
      prevalue, previtems = -1,[]
      maxvalue, maxitem = -1,[]

      for y in xrange(0,len(items)): ## Compare every items
         # print "look item ", y, "weight: ", items[y][0], "value: ",items[y][1]
         assert items[y][0] > 0, "Error! no weight item!"
         if x >= items[y][0] and maxremain2[y] > 0: ## if size >= item[y]  choose it   
            # print "x-1: ",x-1
            maxvalue1,maxitem1,maxremain1 = _best(x-items[y][0],items,opt)
            # print "maxitem1: ", maxitem1 , "maxvalue1: ", maxvalue1 
            maxitem1 = maxitem1[:]
            maxitem1[y] += 1
            maxvalue1 += items[y][1] 
            maxremain1 = maxremain1[:] 
            maxremain1[y] -= 1
            # print "item ", y, "maxitem1: ", maxitem1 , "maxvalue1: ", maxvalue1 , "maxremain1: ", maxremain1
            # print "item ", y, "prevalue: ", prevalue , "previtems: ", previtems

         if prevalue < maxvalue1:
            prevalue,previtems, prevremain = maxvalue1, maxitem1, maxremain1
         
      if prevalue < maxvalue2:
         maxvalue,maxitem, maxremain = maxvalue2,maxitem2, maxremain2
         # print "item available! ",y
      else:
         maxvalue,maxitem, maxremain = prevalue, previtems, prevremain
      # print "itemnum: ",itemnum
      # print "set capacity: ", x, "maxvalue: ", maxvalue, "maxitem: ", maxitem, "maxremain: ", maxremain, "\n"

      opt[x] = maxvalue,maxitem, maxremain

         
   return opt[w]

if __name__ == '__main__':
   print best(3, [(9, 5, 2), (4, 5, 3)])

   print best(3, [(2, 4, 2), (3, 5, 3)])
   # (5, [0, 1])

   print best(3, [(1, 5, 2), (1, 5, 3)])
   # (15, [2, 1])

   print best(3, [(1, 5, 1), (1, 5, 3)])
   # (15, [1, 2])

   print best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])
   # (130, [6, 4, 1])

   print best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])
   # (236, [6, 7, 3, 7, 2])