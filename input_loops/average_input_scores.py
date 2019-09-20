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
    last_name = input("Enter your last name: ")
    first_name = input("Enter you first name: ")
    scores = []
    score = 0
    sentinel = -1
    while score >= 0:
        try:
            score = float(input("Please enter a score or -1 when finished: "))
        except ValueError:
            print("Numbers only")
        else:
            if score == sentinel:
                break
            else:
                scores.append(score)
    avg_scores = average(scores)
    print(last_name + ', ' + first_name + ' grade:' '% 5.2f' % avg_scores)

"""My code is prompting user for name
and scores. If a string is entered a value error is raised
and a message is displayed.
"""