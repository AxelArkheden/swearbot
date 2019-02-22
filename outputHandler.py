import operator

def sort_submission(submission_list):
    return submission_list.sort(key = operator.itemgetter(1), reverse=True)