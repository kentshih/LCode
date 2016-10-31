def best(w,items):
   opt = {}
   ans = _best(w,items,opt)
   return ans

def _best(w,items,opt):
   if w < 0:
      w = 0
   if opt.has_key(w):
      return opt[w]
   if opt.has_key(0) == False:
      takeitems = []
      for i in xrange(0,len(items)):
         takeitems.append(0)
      opt[0] = 0, takeitems

   # print "takeitems: ",takeitems
   maxvalue, maxitem = -1,[]
   maxvalue1, maxitem1 = 0,takeitems
   maxvalue2, maxitem2 = 0,takeitems
   prevalue, previtems = 0,takeitems

   for x in xrange(1,w+1): ## compare every size of bag
      # print "capacity: ", x
      pick = 0
      maxvalue2, maxitem2 = _best(x-1,items,opt)
      # print "maxitem2: ", maxitem2 , "maxvalue2: ", maxvalue2
      prevalue, previtems = -1,[]
      maxvalue, maxitem = -1,[]
      for y in xrange(0,len(items)): ## Compare every items
         # print "look item ", y, "weight: ", items[y][0], "value: ",items[y][1]
         assert items[y][0] > 0, "Error! no weight item!"
         if x >= items[y][0]: ## if size >= item[y]  choose it   
            # print "x-1: ",x-1
            maxvalue1,maxitem1 = _best(x-items[y][0],items,opt)
            # print "maxitem1: ", maxitem1 , "maxvalue1: ", maxvalue1 
            maxitem1 = maxitem1[:]
            maxitem1[y] += 1
            maxvalue1 += items[y][1] 
            # print "item ", y, "maxitem1: ", maxitem1 , "maxvalue1: ", maxvalue1 
            # print "item ", y, "prevalue: ", prevalue , "previtems: ", previtems

         if prevalue < maxvalue1:
            prevalue,previtems = maxvalue1, maxitem1
         
      if prevalue < maxvalue2:
         maxvalue,maxitem = maxvalue2,maxitem2
         # print "item available! ",y
      else:
         maxvalue,maxitem = prevalue, previtems

      # print "set capacity: ", x, "maxvalue: ", maxvalue, "maxitem: ", maxitem, "\n"
      opt[x] = maxvalue,maxitem
         
   return opt[w]
      


if __name__ == '__main__':
   print best(3, [(2, 4), (3, 5)])
   # (5, [0, 1])

   print best(3, [(1, 5), (1, 5)])
   # (15, [3, 0])

   print best(3, [(1, 2), (1, 5)])
   # (15, [0, 3])

   print best(3, [(1, 2), (2, 5)])
   # (7, [1, 1])

   print best(58, [(5, 9), (9, 18), (6, 12)])
   # (114, [2, 4, 2])

   print best(92, [(8, 9), (9, 10), (10, 12), (5, 6)])
   # (109, [1, 1, 7, 1])