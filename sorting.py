class Sorting:
    # sorts books alphabetically by title using merge sort algorithm
    #time complexity: O(n log n)
    def merge_sort(books):
        #best case, the list with 0 or 1 items is already sorted
        if len(books) <= 1:
            return books
        mid = len(books) // 2
        left = merge_sort(books[:mid])
        right = merge_sort(books[mid:])
        #merges the sorted halves together
        return merge(left, right)

    def merge(left, right):
        # combines the two sorted lists into a single list
        result = []
        #compares the first elements of each list and adds the smaller title (alphabetically)
        while left and right:
            if left[0].title < right[0].title:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        #adds any remaining books
        result.extend(left or right)
        return result