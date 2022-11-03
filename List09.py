def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    i=0
    a=[]
    while i<len(fruits):
        if fruits[i]=='apple':
            a.append(i)
        i+=1
    a.insert(0,len(a))
    return a
print(main(['apple','banana','apple','pear','apple']))