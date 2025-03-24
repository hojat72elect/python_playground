if __name__ == '__main__':
    # string formatting in python
    year = 2016
    event = "Referendum"
    print(f"Results of the {year} {event}.\n")

    # Another way of string formatting (more verbose)
    yes_votes = 42_572_654
    total_votes = 85_705_149
    percentage = yes_votes / total_votes
    print("{:-9} YES votes {:2.2%}".format(yes_votes, percentage))
