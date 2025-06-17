1. Bubble Sort (Simple, but inefficient)
    Idea: Repeatedly swap adjacent elements if they are in the wrong order.
    Time: O(n²)
    Why it came first: Very intuitive and easy to implement.
    Limitation: Extremely slow for large lists.

2. Selection Sort (Less swapping)
    Idea: Repeatedly select the smallest element and put it in place.
    Time: O(n²)
    Improvement: Fewer swaps than Bubble Sort.
    Limitation: Still O(n²); doesn’t use comparisons efficiently.

3. Insertion Sort (Good for nearly sorted data)
    Idea: Insert each element into its correct position in a growing sorted list.
    Time: O(n²) worst, but O(n) best case (already sorted).
    Improvement: Better on small or nearly sorted datasets.
    Still not scalable: Not efficient for large unsorted datasets.

4. Shell Sort (Improved Insertion Sort)
    Idea: Insertion sort on elements spaced apart, reducing the gap over time.
    Time: Depends on gap sequence; best known is ~O(n log² n)
    Improvement: Faster than plain Insertion Sort.
    Discovery: Donald Shell, 1959 — saw the need to move elements more efficiently.

5. Merge Sort (Divide and Conquer)
    Idea: Recursively divide the array and merge sorted halves.
    Time: O(n log n) consistently.
    Improvement: Guaranteed performance; stable sort.
    Limitation: Requires extra memory.

6. Quick Sort (Efficient, in-place)
    Idea: Pick a pivot, partition the array, sort each side recursively.
    Time: Average O(n log n), worst O(n²).
    Improvement: Faster in practice than Merge Sort due to in-place sorting.
    Refinement: Choosing a good pivot (e.g., median-of-three) improves performance.

7. Heap Sort (Priority queue based)
    Idea: Build a heap, then extract the max repeatedly.
    Time: O(n log n).
    Improvement: In-place and no worst-case degradation.
    Limitation: Not stable and often slower than Quick Sort in practice.

8. Counting Sort (Non-comparison based)
    Idea: Count occurrences of each value (for integers).
    Time: O(n + k) where k = range of input values.
    Improvement: Linear time for small ranges.
    Limitation: Only works on integers with limited range.

9. Radix Sort (Digit by digit, linear time)
    Idea: Sort by individual digits using Counting Sort as a subroutine.
    Time: O(nk) where k = number of digits.
    Improvement: Handles larger integers efficiently.
    Used for: Large datasets of fixed-width integers/strings.

10. TimSort (Hybrid of Merge + Insertion Sort)
    Idea: Used in Python and Java; splits into runs, uses insertion for small ones, merge for large.
    Time: O(n log n), optimized for real-world data.
    Improvement: Adaptive; takes advantage of existing order.
    Modern application: Standard library sort in many languages.