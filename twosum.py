#coding=utf-8
def twosum(nums,target):
	for i in xrange(len(nums)):
            for j in xrange(i+1,len(nums)):
            	print "i: ", i , "j: " , j
            	x = nums[i]
            	y = nums[j]
            	
                if x + y == target:
                    return [i, j]
                

if __name__ == '__main__':
	print twosum([0,4,3,0],0)