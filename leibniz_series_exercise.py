def approximate_pi(n_terms):

    ls = []
    for i in range(n_terms):
        ls.append((-1)**i/(i*2 + 1))
    return 4 * sum(ls)# replace pass with your code
