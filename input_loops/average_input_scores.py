""" Author: Michael Harmon
    Last Date Modified: 9/19/2019
    Description: This program will use a basic while loop
    to calculate the average from a list of scores.
"""


def average(score_list):
    scores_total = 0
    items = len(score_list)
    for i in score_list:
        scores_total += i
        items - 1
    avg = scores_total / items
    return round(float(avg), 2)


if __name__ == '__main__':
    scores = []
    print(average(scores))
