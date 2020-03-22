
# python-logging

this is an example on how to use python logging mechanisms

specifically, we gonna use ```logging``` module

## how to run

    # no inputs
    python src/main.py

    # with inputs
    python src/main.py --inputs data/lorem.txt data/not-exists.txt

    # set console verbosity
    python src/main.py --verbosity debug --inputs data/lorem.txt

    # set verbose log file
    python src/main.py --log-file app.log --inputs data/lorem.txt