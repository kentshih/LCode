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
   print best(180, [(6, 17, 1), (10, 2, 2), (1, 10, 7), (2, 6, 5), (5, 18, 6), (2, 15, 10), (4, 8, 4), (3, 9, 9), (3, 10, 10), (2, 2, 3)])
# (598, [1, 2, 7, 5, 6, 10, 4, 9, 10, 3])

   print best(177, [(8, 15, 1), (3, 5, 8), (9, 7, 1), (4, 2, 3), (9, 11, 1), (7, 3, 10), (1, 9, 7), (2, 1, 7), (7, 7, 5), (2, 7, 10)])
# (270, [1, 8, 1, 3, 1, 7, 7, 2, 5, 10])

   print best(173, [(4, 7, 6), (2, 20, 5), (3, 2, 7), (4, 13, 1), (2, 11, 3), (4, 12, 1), (6, 17, 6), (5, 2, 1), (3, 11, 2), (3, 9, 1)])
# (349, [6, 5, 7, 1, 3, 1, 6, 1, 2, 1])

   print best(104, [(5, 7, 4), (5, 16, 6), (6, 15, 1), (8, 2, 3), (2, 17, 6), (4, 11, 8), (6, 2, 4), (8, 9, 10), (1, 1, 2), (9, 10, 3)])
# (332, [3, 6, 1, 0, 6, 8, 0, 1, 1, 0])

   print best(156, [(1, 18, 3), (7, 5, 7), (7, 3, 3), (8, 5, 7), (8, 1, 10), (3, 11, 8), (2, 14, 5), (8, 17, 1), (3, 11, 7), (6, 7, 10)])
# (396, [3, 4, 0, 0, 0, 8, 5, 1, 7, 10])