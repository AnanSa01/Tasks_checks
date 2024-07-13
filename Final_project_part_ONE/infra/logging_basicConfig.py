import logging


# this function is to call the setUp in every page rather the building it everytime.
class LoggingSetup:
    logging.basicConfig(filename='../final_project.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%y %H:%M:%S')
