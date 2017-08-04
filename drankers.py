import time
import matplotlib.pyplot as plt
from dranker import dranker

def drank_group(number_of_drunker, time_step):
    '''
    酔っぱらいの驟雨団を生成する
    :param number_of_drunker: 酔っぱらいの人数
    :param time_step: 酔っぱらいを何歩歩かせるか
    :return: dranker classが入った配列を返す
    '''
    print("酔っぱらい生成中...")
    drankers = []
    for i in range(number_of_drunker):
        drankers.append(dranker())
        drankers[i].random_walk(time_step)
    return drankers

def plot_drankers_hist(time_step):
    '''
    酔っぱらいの集団がtime_step経過した後にどの位置にいるのかヒストグラムで表示する
    :param time_step: 酔っぱらいを何歩歩かせるか
    :return:
    '''
    hist = []
    number_of_drunkers = len(drankers)
    for i in range(number_of_drunkers):
        hist.append(drankers[i].log[time_step - 1])
    plt.hist(hist, bins=30)
    plt.show()

def plot_drankers_trajectory(drankers):
    '''
    酔っぱらいの集団の軌跡をグラフ化
    :param drankers: dranker classの配列を引数とする
    :return:
    '''
    default_color = 'red'
    print("酔っぱらいの軌跡生成中...")
    for dranker in drankers:
        dranker.plot_log(color=default_color)

if __name__ == '__main__':
    start_time = time.time()

    time_step = 1000
    drankers = drank_group(1000, time_step)
    # plot_drankers_hist(time_step)
    plot_drankers_trajectory(drankers)

    elapsed_time = time.time() - start_time
    print("計算時間{:.2f}[s]".format(elapsed_time))

    plt.show()
