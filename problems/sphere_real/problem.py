from collections import OrderedDict
class Problem():
    def __init__(self):
        space = OrderedDict()
        nparam = 10
        for i in range(nparam):
            space['p%d'%(i+1)] = (-5,5)
        self.space = space
        self.params = self.space.keys()
        self.starting_point = [-5] * nparam

if __name__ == '__main__':
    instance = Problem()
    print(instance.space)
    print(instance.params)

