def scores(*num, status=False):
    '''

    :param num: Enter the scores
    :param status: (OPTIONAL) Scores situation.
    :return: Dictionary with the size, max score, min score, average and result  when required.
    '''
    final = dict()
    final['size'] = len(num)
    final['max'] = max(num)
    final['min'] = min(num)
    final['average'] = sum(num)/len(num)
    if status:
        if final['average'] >= 7:
            final['result'] = 'GOOD'
        elif final['average'] >= 5:
            final['result'] = 'MEDIUM'
        else:
            final['result'] = 'BAD'
    return final

# main
marks = scores(10, 2.5, 8.7, status=True)
print(marks)
help(scores)