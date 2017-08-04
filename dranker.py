import numpy as np
import matplotlib.pyplot as plt

class dranker:
    __position = 0
    log = []
    def __init__(self):
        self.__position = 0
        self.log = []
        self.log.append(self.__position)
    def __one_step(self):
        judge = np.random.random()
        if judge < 0.5:
            self.__position -= 1
        elif judge >= 0.5:
            self.__position += 1
        else:
            print('error!')
            print('The value of judge is {}'.format(judge))

    def random_walk(self,step):
        for i in range(step):
            self.__one_step()
            self.log.append(self.__position)

    def plot_log(self,color = None):
        plt.plot(self.log,color=color)
        # plt.show()



if __name__ == '__main__':
    Yuto = dranker()
    Yuto.random_walk(30)
    Yuto.plot_log()
    plt.show()
