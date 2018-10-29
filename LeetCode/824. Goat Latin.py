def toGoatLatin(self, S):
    """
    :type S: str
    :rtype: str
    """
    slist = S.split()

    for idx, word in enumerate(slist):

        if word[0] in 'aeiouAEIOU':
            slist[idx] += 'ma'
        else:
            slist[idx] = slist[idx][1:] + slist[idx][0] + 'ma'
        slist[idx] += 'a' * (idx+1)

    return ' '.join(word for word in slist)