"""Bubble Sort
"""


def bubblesort(items):
	for i in range(0,len(items)-1):
		for j in range(0,len(items)-i-1):
			if items[j] > items[j+1]:
				tmp=items[j]
				items[j]=items[j+1]
				items[j+1]=tmp
	return items
	
items=[2,5,9,1,56,3,9]	
print bubblesort(items)		

