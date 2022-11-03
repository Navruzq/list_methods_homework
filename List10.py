def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    i=0
    a=0
    b=0
    s=[]
    while i<len(list1):
       a=list1.count(1)
       b=list1.count(0)
       i+=1
    s.insert(0,a)
    s.insert(1,b)
    return s
print(main([1,0,0,0,1,0,1,0]))