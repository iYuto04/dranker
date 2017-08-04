import numpy as np
import matplotlib.pyplot as plt

class drunker:
    '''
    酔歩運動の主役,酔っぱらいさん
    '''
    __position = 0
    log = []
    def __init__(self):
        self.__position = 0
        self.log = []
        self.log.append(self.__position)
    def __one_step(self, option=None):
        '''
        右に行くのか左に行くのか1/2で計算して自分の位置(__position)を更新する
        '''
        if option == None:
            judge = np.random.random()
            if judge < 0.5:
                self.__position -= 1
            elif judge >+ 0.5:
                self.__position += 1
            else:
                print('error!')
                print('The value of judge is {}'.format(judge))
        elif option == 'float':
            self.__position += 2 * np.random.random() - 1
        else:
            print('option error!')

    def random_walk(self,step,option=None):
        '''
        引数で何歩歩くかを計算する.
        logに酔っ払いの歩いた軌跡が入っている
        :param step: 酔っ払いを何歩動かすか
        :param option: 'float'を指定すると酔歩運動を実数で表現
        :return:
        '''
        for i in range(step):
            self.__one_step(option=option)
            self.log.append(self.__position)

    def plot_log(self,color = None):
        '''
        酔っぱらいの軌跡をグラフ化
        :param color: グラフの色を文字列で指定できる
        :return:
        '''
        plt.xlim(0, len(self.log))
        plt.plot(self.log,color=color)
        # plt.show()



if __name__ == '__main__':
    Yuto = drunker()
    Yuto.random_walk(30)
    Yuto.plot_log()
    plt.show()
