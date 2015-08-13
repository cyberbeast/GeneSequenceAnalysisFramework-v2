import collections

def print_graph(d):
    for k, v in d.items():
        # print(k, end='')
        # print()
        if isinstance(v, dict):
            print_graph(v)
            print()
        else:
            print("{0} : {1}".format(k, v))