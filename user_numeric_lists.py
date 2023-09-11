"""

Purpose: Illustrate options for working with numeric lists in Python.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

Uses only Python Standard Library modules and a local logger module.

"""

# import from standard library
import statistics
import math

# import from local files
from util_datafun_logger import setup_logger

# Set up logging .............................................

# Call the setup_logger function
logger, logname = setup_logger(__file__)

# Define shared data ..........................................

# define a variable with some univariant data
# (one varabile, many readings)
score_list = [
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
list1 = [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,29,20]
listx = [2,4,6,8,10,12,14,16,18,20]
listy=[3,6,9,12,15,18,21,24,27,30]


# Define functions ........................................


def illustrate_list_statistics():
    """This function illustrates descriptive statistics for a numric list."""
    mean_value1=statistics.mean(list1)
    mean_value1=statistics.mean(listx)
    mean_value1=statistics.mean(listy)

    median_value=statistics.median(list1)
    median_value=statistics.median(listx)
    median_value=statistics.median(listy)

    mode_value=statistics.mode(list1)
    mode_value=statistics.mode(listx)
    mode_value=statistics.mode(listy)

    st_dev_value1= statistics.stdev(list1)
    st_dev_valuex= statistics.stdev(listx)
    st_dev_valuey= statistics.stdev(listy)

    logger.info(f"score_list: {score_list}")


def illustrate_list_correlation_and_prediction():
    """This function illustrates correlation and prediction for a numric list."""

    correlation=statistics.correlation(listx,listy)
    slope, intercept= statistics.linear_regression(listx,listy)
    logger.info(f"correlation between x and y: {correlationxy}")

    
    logger.info(f"xtimes_list: {xtimes_list}")
    logger.info(f"yvalues_list: {yvalues_list}")
    logger.info(f"The equation of the best fit line is: y = {slope}x + {intercept}")

    # Once we have learned the slope and intercept
    # of the best-fit straight line through the data,
    # we can use it to make predictions

    # Predict the y value for a given x value outside the range of the data

def illustrate_list_built_in_functions():
    # BUILT-IN FUNCTIONS ......................................
    # Many built-in functions work on lists
    # try min(), max(), len(), sum(), sorted(), reversed()

    # Using the score list provided above, do the following:
    # Calcuate the max and min scores
    max_value = max(listx)
    min_value = min(listx)
    
    max_value = max(listy)
    min_value = min(listy)

    max_value = max(list1)
    min_value = min(list1)

    length1=len(list1)
    lengthx=len(listx)
    lengthy=len(listy)

    sum1=sum(list1)
    sumx=sum(listx)
    sumy=sum(listy) 

    average1=sum(list1)/ len(list1)
    averagex=sum(listx)/ len(listx)
    averagey=sum(listy)/ len(listy)

    set1=set(list1)
    setx=set(listx)
    sety=set(listy)

    list1=sorted(list1)
    listx=sorted(listx)
    listy=sorted(listy)

    list1=sorted(list1,reverse=True)
    listx=sorted(listx,reverse=True)
    listy=sorted(listy,reverse=True)

def illustrate_list_methods():
    """This function illustrates methods that can be called on a list"""

    """

     LIST METHODS ............................................... 

     Here are some common methods that operate on an instance of a list.

     append(x): Add an item to the end of the list.
     extend(iterable): Add all the items from an iterable (such as another list)
          to the end of the list.
     insert(i, x): Insert an item at a given position.
     remove(x): Remove the first occurrence of an item.
     pop([i]): Remove the item at the given position in the list, 
     and return it. If no index is specified, 
     removes and returns the last item in the list.
     clear(): Remove all items from the list.
     index(x[, start[, end]]): Return the index of the first occurrence of
          an item.
     count(x): Return the number of occurrences of an item.
     sort(key=None, reverse=False): Sort the items in the list 
          in ascending order.
     reverse(): Reverse the order of the items in the list.
     copy(): Return a shallow copy of the list.

     """

    # append an item to the end of the list
    lst = [1, 2, 3,4]
    lst.append(5)

    # extend the list with another list
    lst.extend([7, 8, 9])

    # insert an item at a given position (0 = first item)
    i = 0
    newvalue = 24
    lst.insert(i, newvalue)

    # remove an item
    item_to_remove = 5
    lst.remove(item_to_remove)
    print(lst)

    # Count how many times 111 appears in the list
    ct_of_24 = lst.count(24)

    # Sort the list in ascending order using the sort() method
    asc_scores2 = lst.sort()

    # Sort the list in descending order using the sort() method
    desc_scores2 = lst.sort(reverse=True)

    # Copy the list to a new list
    new_scores = score_list.copy()
    logger.info(f"new_scores is: {new_scores}")

    # Remove the first item from the new list
    # The first item in a list is at index 0
    # Think of it as an offset from the beginning of the list
    first = lst.pop(0)
    
    print(lst)
    # Remove the last item from the new list
    # The last item in a list is at index -1
    last = lst.pop(1)

    # Remove the item at index 3 from the new list
    fourth = lst.pop(3)
    print(lst)

def illustrate_list_transformations():
    """This function illustrates transformations that can be applied to a list"""

    logger.info("Score list: {score_list}")

    # TRANFORMATIONS ............................

    # FILTER and MAP are critical tranformations in big data applications

    # Use the built-in function filter() anywhere you need to filter a list
    # Filter the new list to only include scores greater than 100
    # You could pass in a named function, but honestly this is easier
    # Say "KEEP x such that x > 100 is True" given score_list
    # Cast the result using square brackets to get back a list
    scores_over_100 = [filter(lambda x: x > 100, lst)]
    logger.info(f"Scores over 100: {scores_over_100}")

    # Use the built-in function map() anywhere you need to transform a list

    # Map each element to its square
    # Say "map x to x squared" given score_list
    # Cast the result using square brackets to get a list
    doubled_scores = [map(lambda x: x * 2, lst)]
    logger.info(f"Doubled scores: {doubled_scores}")

    # Map each element to its square root
    # Say "map x to the square root of x" given score_list
    # remember to cast the result to a list (using square brackets)
    sqrt_scores = map(lambda x: math.sqrt(x), lst)
    logger.info(f"Square root of scores: {sqrt_scores}")

    # Map each element (radius) to its area
    radius_list = [1, 2, 3, 4, 5]
    logger.info(f"Radius list: {radius_list}")
    # Say "map r to pi r squared" given radius_list
    # cast the result to a list using square brackets
    area_list = [map(lambda r: math.pi * r * r, radius_list)]
    logger.info(f"Area of circles: {area_list}")


def illustrate_list_comprehensions():
    """This function illustrates list comprehensions"""

    logger.info("Score list: {score_list}")

    # TRANFORMATIONS - Using List Comprehensions
    # List comprehensions are a concise way to create lists
    # They work like map and filter, but are more concise
    # They are the preferred "pythonic" way to do transformations
    # They are faster than map / filter - it's quite impressive when you master them!

    # With comprehensions, we start with what we WANT
    # Filter the new list to only include scores greater than 100
    # Say "KEEP x (for each x in score_list) IF  x > 100"
    # Cast the result to a list using square brackets

    scores_over_100 = [x for x in lst if x > 100]
    logger.info("Scores over 100 (using list comprehensions!): {scores_over_100}")

    # Try again "keep x (for each x in score_list) IF  x < 42"
    scores_under_42 = [x for x in lst if x < 42]
    logger.info("Scores under 42 (using list comprehensions!): {scores_under_42}")

    # Map each element to its square
    # Say "give me x squared (for each x in score_list)"
    # Cast the result to a list using square brackets

    doubled_scores = [x * 2 for x in lst]
    logger.info("Doubled scores (using list comprehensions!): {doubled_scores}")

    # Map each element to its square root
    # Say "give me the square root of x (for each x in score_list)"
    # Cast the result to a list using square brackets
    sqrt_scores = [math.sqrt(x) for x in lst]

    radius_list = [1, 2, 3, 4, 5]
    logger.info(f"Given radius_list: {radius_list}")

    # Map each element (radius) to its area
    # Say "give me pi r squared (for each r in radius_list)"
    # Cast the result to a list using square brackets
    area_list = [math.pi * r * r for r in radius_list]
    logger.info(f"Area of circles: {area_list}")

    # Map each element (radius) to its circumference
    # Say "give me 2 pi r (for each r in radius_list)"
    # Cast the result to a list using square brackets
    circumference_list = [2 * math.pi * r for r in radius_list]
    logger.info(f"Circumference of circles: {circumference_list}")

    logger.info("Mastering comprehesions is a valuable skill for data scientists.")
    numbers = [1, 2, 3, 4]
    squares = [x**2 for x in numbers]
    logger.info(f"Given numbers: {numbers}")
    logger.info(f"Squares of numbers using [x ** 2 for x in numbers] is {squares}")


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

if __name__ == "__main__":
    calculate_correlation_and_prediction
    calculate_statistics

    show_log()

