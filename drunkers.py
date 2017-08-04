import time
import matplotlib.pyplot as plt
from drunker import drunker

def drunk_group(number_of_drunker, time_step):
    '''
    酔っぱらいの驟雨団を生成する
    :param number_of_drunker: 酔っぱらいの人数
    :param time_step: 酔っぱらいを何歩歩かせるか
    :return: drunker classが入った配列を返す
    '''
    print("酔っぱらい生成中...")
    drunkers = []
    for i in range(number_of_drunker):
        drunkers.append(drunker())
        drunkers[i].random_walk(time_step)
    return drunkers

def plot_drunkers_hist(time_step):
    '''
    酔っぱらいの集団がtime_step経過した後にどの位置にいるのかヒストグラムで表示する
    :param time_step: 酔っぱらいを何歩歩かせるか
    :return:
    '''
    hist = []
    number_of_drunkers = len(drunkers)
    for i in range(number_of_drunkers):
        hist.append(drunkers[i].log[time_step - 1])
    plt.hist(hist, bins=30)
    plt.show()

def plot_drunkers_trajectory(drunkers):
    '''
    酔っぱらいの集団の軌跡をグラフ化
    :param drunkers: drunker classの配列を引数とする
    :return:
    '''
    default_color = 'red'
    print("酔っぱらいの軌跡生成中...")
    for drunker in drunkers:
        drunker.plot_log(color=default_color)

if __name__ == '__main__':
    start_time = time.time()

    time_step = 1000
    drunkers = drunk_group(1000, time_step)
    # plot_drunkers_hist(time_step)
    plot_drunkers_trajectory(drunkers)

    elapsed_time = time.time() - start_time
    print("計算時間{:.2f}[s]".format(elapsed_time))

    plt.show()
