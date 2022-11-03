def main(fruits,x):
    """
    You will be given a list of fruits. Add x fruit to it from the end and return.
    Args:
        fruits(list): parameter 
        x(str): parameter
    Returns:
        list: return answer
    """
    fruits.insert(len(fruits),x)
    return fruits
print(main(['apple','banana'],'kiwi'))