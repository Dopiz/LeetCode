def subdomainVisits(self, cpdomains):
    """
    :type cpdomains: List[str]
    :rtype: List[str]
    """
    dic = {}

    for d in cpdomains:
        visit = int(d.split(' ')[0])
        name = d.split(' ')[1]
        name_list = name.split('.')

        for i in range(len(name_list)):
            url = '.'.join(name_list[i:])
            if url in dic:
                dic[url] += visit
            else:
                dic[url] = visit

    res = []

    for k, v in dic.items():
        res.append(str(v) + ' ' + k)        

    return res