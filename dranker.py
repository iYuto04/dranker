import numpy as np
import matplotlib.pyplot as plt

class dranker:
    '''
    酔歩運動の主役,酔っぱらいさん
    '''
    __position = 0
    log = []
    def __init__(self):
        self.__position = 0
        self.log = []
        self.log.append(self.__position)
    def __one_step(self):
        '''
        右に行くのか左に行くのか1/2で計算して自分の位置(__position)を更新する
        '''
        judge = np.random.random()
        if judge < 0.5:
            self.__position -= 1
        elif judge >+ 0.5:
            self.__position += 1
        else:
            print('error!')
            print('The value of judge is {}'.format(judge))

    def random_walk(self,step):
        '''
        引数で何歩歩くかを計算する.
        logに酔っ払いの歩いた軌跡が入っている
        :param step: 酔っ払いを何歩動かすか
        :return:
        '''
        for i in range(step):
            self.__one_step()
            self.log.append(self.__position)

    def plot_log(self,color = None):
        '''
        酔っぱらいの軌跡をグラフ化
        :param color: グラフの色を文字列で指定できる
        :return:
        '''
        plt.plot(self.log,color=color)
        # plt.show()



if __name__ == '__main__':
    Yuto = dranker()
    Yuto.random_walk(30)
    Yuto.plot_log()
    plt.show()
