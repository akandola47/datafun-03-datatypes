

# import from local util_datafun_logger.py
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)


def house_tuples():
      # Create some tuples
    house_prices = ("avergae, cheap, expensive")
    house_sizes = ("small,average, big")


    logger.info(f"{house_prices =}")
    logger.info(f"{house_sizes = }")

    # tuple concatenation
    tupleCat = house_prices + house_sizes

    # tuple repetition
    tupleAThrice = house_prices * 3


    # TODO: Start using this f-string "syntactic sugar" for quick ouptut
    # just add space = space inside the curly braces
    # it will print the name of the variable and the value
    logger.info(f"{house_prices = }")
    logger.info(f"{house_sizes = }")
    logger.info(f"{tupleCat = }")
    logger.info(f"{tupleAThrice = }")

    # tuple membership testing

    house_color = (red, blue, green)
    hasBlue = blue in house_color  # True
    hasFour = yellow in house_color  # False

    # tuple indexing (0 is first, -1 is last, or 1 less than the length)

    my_tuple = (1,2,3,4)
    first = my_tuple[0]
    second = my_tuple[1]
    third = my_tuple[2]
    last = my_tuple[-1]

    # Use tuples to return multiple values from a function

    def divide_and_remainder(dividend, divisor):
        quotient = dividend // divisor
        remainder = dividend % divisor
        return quotient, remainder

    q, r = divide_and_remainder(100, 30)
    logger.info(f"Quotient: {q}, Remainder: {r}")


def illustrate_sets():
 

    set1 = {1, 2, 3, 4, 5}
    set2 = {2,4,6,8,10}

    logger.info(f"set1 = {set1}")
    logger.info(f"set2 = {set2}")

    # set union
    setC = set1 | set2

    # set intersection
    setD = set1 & set2

    # set difference
    setE = set1 - set2

    # sets are often used to remove duplicates from a list
    # after gettin the set, convert it back to a list with list() or []
    listWords = ["slow, fast average"]
    setWords = set(listWords)
    listWordsNoDuplicates = list(setWords)
    listWordsNoDuplicates = [setWords]  # same as above


def illustrate_dictionaries():
    

    houseA_dict = {"house": "townhouse", "price": expensive, "size": 134}
    houseB_dict = {"house": "suburban", "price": cheap, "size": 152}

    logger.info(f"houseA_dict = {houseA_dict}")
    logger.info(f"houseB_dict = {houseB_dict}")

    assessment_dict = {"low": 0, "medium": 1, "high": 2}
    logger.info(f"assessment_dict = {assessment_dict}")

    data_dict = {
        "house": ["townhouse", "downtown", "apartment"],
        "age": [25, 30, 35,],
        "income": [60000, 70000, 80000],
    }
    logger.info(f"data_dict = {data_dict}")

    word_counts_dict = {}
    for word in word_list:
        if word in word_counts_dict:
            word_counts_dict[word] += 1
        else:
            word_counts_dict[word] = 1

    logger.info("Word count is a good way to begin processing text.")
    logger.info(f"Given text_simple.txt, the word_counts_dict = {word_counts_dict}")

    # IMPORTANT: Dictionary comprehesions - the preferred approach

    # Create a dictionary of word counts from a list of words
    # A dictionary is always key:value pairs
    # Say "I want word:count for each word in word_list"
    # Cast the result to a dictionary by using curly braces {}
    word_counts_dict2 = {word: word_list.count(word) for word in word_list}

    # Spend most of your practice on comprehensions - they are
    # key to transforming data in Python.

    logger.info("Given text_simple.txt and comprehensions,")
    logger.info(f"the the word_counts_dict2 = {word_counts_dict2}")


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!
# Remember, code blocks must be indented consistently after a colon.

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    # call your functions here
    illustrate_tuples()
    illustrate_sets()
    illustrate_dictionaries()

    show_log()
