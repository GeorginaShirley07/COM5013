def binary_search(result, target):
    # searches for a book in the sorted list of books using binary search algorithm
    # avg time complexity: O(log n)
    left = 0
    right = len(result)-1
    #while there is a valid range, it will keep searching for the target book.
    while left <= right:
        # finds the middle index of the search range
        mid = (left + right) //2
        if result[mid].title.lower() == target.lower():
            return result[mid]
        #searches the right half of the list if the title is greater than the mid point.
        elif result[mid].title.lower() < target.lower():
            left = mid+1
        else:
            right = mid-1
        #returns none if the book is not found.
        return None

