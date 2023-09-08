"""
Arshpreet Kandola
Domain: Buisness
Date: September 8 2023
"""

import random

from util_datafun_logger import setup_logger

# Set up logging .............................................

logger, logname = setup_logger(__file__)


house_names = ["townhouse", "highrise", "farmhouse","suburbanhouse","apartment"]

house_outcomes = ["buy", "sell", "lease"]

house_prices = ["cheap", "average","expensive"]

house_colors = ["red", "green", "blue", "yellow", "orange", "purple"]

house_size = ["small", "average", "big", "huge"]

def combine_twolists_zip():
    uadept_tuple= tuple(zip(house_size, house_prices))
    logger.info(f"combined list into tuple : {uadept_tuple}")

def new_list_set():
    lst_new=tuple(set(house_prices))
    logger.info(f"new tuple using set(): {lst_new}")

def combine_lists_len():
    using_len = len(house_prices)
    logger.info(f"length of list: {using_len}")
    house_tuple= [(house_prices[i], house_size[i]) for i in range (0, len(house_prices))]
    logger.info(f"using len to combine two lists into tuple: {house_tuple}")


def random_choice():
    rand_value = random.choice(house_names)
    logger.info(f"print random word value: {house_names}")

def create_random_sentence():
    rand_sentence= random.sentence
    logger.info(f"print random sentnce value: {house_names}")


    """Create a random sentence from our pre-defined lists"""
    logger.info("Calling create_random_sentence()")

    # Create a random sentence
    # e.g. "The angry dog runs quickly."
    sentence = (
        f"The {random.choice(house_names)} {random.choice(house_colors)} "
        f"{random.choice(house_outcomes)} {random.choice(house_prices)}."
    )

    logger.info(f"Random sentence: {sentence}")

def process_text_textnames():
    with open("IntroToPython-master/datafun-03-datatypes/text_textnames.txt","r") as fileboject:
        text=fileboject.red()
        list_names=text.split()
        list_names_sorted=sorted(list_names)
        unique_names= set(list_names)
        print(len(list_names))


#


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())




if __name__ == "__main__":
    logger.info("Calling functions from main block")

    pick_randomvalue()
    combine_twolists_zip()
    new_list_set()
    combine_lists_len()
    process_text_textnames()

    
