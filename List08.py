def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    n=0
    n=fruits.count('apple')
    i=0
    a=0
    while i<n:
        a=fruits.index('apple')
        fruits.pop(a)
        i+=1

    return fruits
print(main(['apple','banana','apple','pear','apple']))