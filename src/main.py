import os
import logging
from argparse import ArgumentParser

NAMES_TO_LEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR
}



def initialize_logger(verbosity, log_file):

    # set the format the be nice
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    logging.root.setLevel(logging.DEBUG)

    # set the log level
    level = NAMES_TO_LEVELS[verbosity.lower()]

    # make the logger output to stdout
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logging.root.addHandler(console_handler)

    # make the logger output to log_file path if given
    # this appender should print every level
    if log_file:
        # make directory of target file
        log_dir = os.path.dirname(log_file)
        if log_dir != "":
            os.makedirs(log_dir, exist_ok=True)

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logging.root.addHandler(file_handler)

def read_from_file(file_path):
    logging.debug(f"checking if file exist at: {file_path}")
    if not os.path.exists(file_path):
        logging.error(f"file not found: {file_path}")
        return None
    
    with open(file_path, "r") as file:
        return list(file)


def parse_arguments():
    parser = ArgumentParser()
    
    parser.add_argument("-v", "--verbosity", default="info",
                        choices=NAMES_TO_LEVELS.keys())

    parser.add_argument("--log-file", default=None)

    parser.add_argument("-i", "--inputs", nargs="*", default=[],
                        help="files to read")

    return parser.parse_known_args()[0]


def main():
    args = parse_arguments()
    initialize_logger(args.verbosity, args.log_file)

    logging.debug("starting main")

    for file_path in args.inputs:
        logging.info(f"processing file: {file_path}")
        lines = read_from_file(file_path)
        if lines:
            for line in lines:
                if line != "\n":
                    logging.debug(line)

if __name__ == '__main__':
    main()