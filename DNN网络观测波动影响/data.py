import re
from matplotlib import pyplot as plt

# 参数依次为list,抬头,X轴标签,Y轴标签,XY轴的范围
def draw_hist(myList,Title,Xlabel,Ylabel,Xmin,Xmax,Ymin,Ymax):
    plt.hist(myList,100)
    plt.xlabel(Xlabel)
    plt.xlim(Xmin,Xmax)
    plt.ylabel(Ylabel)
    plt.ylim(Ymin,Ymax)
    plt.title(Title)
    plt.show()

# 512个数据
s = "1.2785e+00     1.2765e+00     1.2772e+00     1.2790e+00     1.2776e+00     1.2776e+00     1.2786e+00     1.2760e+00     1.2798e+00     1.2766e+00     1.2821e+00     1.2765e+00     1.2790e+00     1.2778e+00     1.2796e+00     1.2768e+00     1.2749e+00     1.2797e+00     1.2779e+00     1.2769e+00     1.2767e+00     1.2794e+00     1.2791e+00     1.2750e+00     1.2788e+00     1.2798e+00     1.2805e+00     1.2773e+00     1.2806e+00     1.2758e+00     1.2759e+00     1.2784e+00     1.2779e+00     1.2803e+00     1.2789e+00     1.2773e+00     1.2785e+00     1.2782e+00     1.2758e+00     1.2766e+00     1.2787e+00     1.2795e+00     1.2790e+00     1.2788e+00     1.2763e+00     1.2783e+00     1.2791e+00     1.2764e+00     1.2770e+00     1.2775e+00     1.2757e+00     1.2799e+00     1.2764e+00     1.2783e+00     1.2791e+00     1.2768e+00     1.2778e+00     1.2797e+00     1.2788e+00     1.2797e+00     1.2794e+00     1.2781e+00     1.2762e+00     1.2763e+00     1.2788e+00     1.2787e+00     1.2786e+00     1.2803e+00     1.2760e+00     1.2786e+00     1.2754e+00     1.2787e+00     1.2760e+00     1.2786e+00     1.2780e+00     1.2774e+00     1.2756e+00     1.2766e+00     1.2789e+00     1.2780e+00     1.2759e+00     1.2781e+00     1.2788e+00     1.2765e+00     1.2779e+00     1.2772e+00     1.2799e+00     1.2790e+00     1.2797e+00     1.2761e+00     1.2759e+00     1.2758e+00     1.2778e+00     1.2802e+00     1.2753e+00     1.2756e+00     1.2781e+00     1.2795e+00     1.2770e+00     1.2774e+00     1.2766e+00     1.2760e+00     1.2791e+00     1.2766e+00     1.2786e+00     1.2767e+00     1.2781e+00     1.2769e+00     1.2765e+00     1.2786e+00     1.2767e+00     1.2782e+00     1.2756e+00     1.2776e+00     1.2759e+00     1.2756e+00     1.2790e+00     1.2790e+00     1.2789e+00     1.2768e+00     1.2775e+00     1.2771e+00     1.2754e+00     1.2751e+00     1.2809e+00     1.2776e+00     1.2759e+00     1.2783e+00     1.2781e+00     1.2785e+00     1.2782e+00     1.2780e+00     1.2768e+00     1.2783e+00     1.2751e+00     1.2765e+00     1.2769e+00     1.2797e+00     1.2798e+00     1.2777e+00     1.2772e+00     1.2770e+00     1.2762e+00     1.2771e+00     1.2792e+00     1.2783e+00     1.2783e+00     1.2799e+00     1.2779e+00     1.2799e+00     1.2757e+00     1.2786e+00     1.2780e+00     1.2766e+00     1.2774e+00     1.2771e+00     1.2778e+00     1.2746e+00     1.2791e+00     1.2795e+00     1.2783e+00     1.2792e+00     1.2769e+00     1.2785e+00     1.2771e+00     1.2786e+00     1.2784e+00     1.2764e+00     1.2783e+00     1.2771e+00     1.2773e+00     1.2783e+00     1.2803e+00     1.2770e+00     1.2789e+00     1.2788e+00     1.2770e+00     1.2794e+00     1.2760e+00     1.2803e+00     1.2804e+00     1.2795e+00     1.2786e+00     1.2771e+00     1.2772e+00     1.2768e+00     1.2786e+00     1.2797e+00     1.2791e+00     1.2809e+00     1.2777e+00     1.2785e+00     1.2797e+00     1.2753e+00     1.2797e+00     1.2773e+00     1.2793e+00     1.2790e+00     1.2786e+00     1.2771e+00     1.2774e+00     1.2777e+00     1.2753e+00     1.2796e+00     1.2771e+00     1.2781e+00     1.2749e+00     1.2762e+00     1.2795e+00     1.2791e+00     1.2755e+00     1.2770e+00     1.2771e+00     1.2799e+00     1.2782e+00     1.2779e+00     1.2768e+00     1.2772e+00     1.2802e+00     1.2779e+00     1.2771e+00     1.2760e+00     1.2760e+00     1.2782e+00     1.2759e+00     1.2777e+00     1.2791e+00     1.2758e+00     1.2794e+00     1.2770e+00     1.2789e+00     1.2762e+00     1.2782e+00     1.2771e+00     1.2782e+00     1.2788e+00     1.2746e+00     1.2776e+00     1.2772e+00     1.2776e+00     1.2786e+00     1.2796e+00     1.2775e+00     1.2783e+00     1.2767e+00     1.2790e+00     1.2792e+00     1.2781e+00     1.2777e+00     1.2767e+00     1.2804e+00     1.2777e+00     1.2779e+00     1.2788e+00     1.2784e+00     1.2803e+00     1.2781e+00     1.2794e+00     1.2797e+00     1.2776e+00     1.2798e+00     1.2792e+00     1.2806e+00     1.2769e+00     1.2764e+00     1.2798e+00     1.2781e+00     1.2771e+00     1.2754e+00     1.2767e+00     1.2777e+00     1.2784e+00     1.2804e+00     1.2774e+00     1.2762e+00     1.2774e+00     1.2774e+00     1.2772e+00     1.2785e+00     1.2774e+00     1.2790e+00     1.2782e+00     1.2795e+00     1.2808e+00     1.2750e+00     1.2797e+00     1.2778e+00     1.2765e+00     1.2780e+00     1.2778e+00     1.2786e+00     1.2782e+00     1.2775e+00     1.2791e+00     1.2784e+00     1.2788e+00     1.2773e+00     1.2754e+00     1.2773e+00     1.2789e+00     1.2787e+00     1.2761e+00     1.2792e+00     1.2796e+00     1.2772e+00     1.2778e+00     1.2775e+00     1.2775e+00     1.2765e+00     1.2787e+00     1.2798e+00     1.2801e+00     1.2762e+00     1.2769e+00     1.2778e+00     1.2768e+00     1.2744e+00     1.2761e+00     1.2763e+00     1.2741e+00     1.2766e+00     1.2796e+00     1.2798e+00     1.2781e+00     1.2776e+00     1.2794e+00     1.2782e+00     1.2777e+00     1.2792e+00     1.2761e+00     1.2753e+00     1.2772e+00     1.2783e+00     1.2778e+00     1.2779e+00     1.2767e+00     1.2786e+00     1.2771e+00     1.2782e+00     1.2778e+00     1.2755e+00     1.2784e+00     1.2777e+00     1.2760e+00     1.2757e+00     1.2795e+00     1.2781e+00     1.2778e+00     1.2785e+00     1.2797e+00     1.2792e+00     1.2769e+00     1.2795e+00     1.2789e+00     1.2768e+00     1.2773e+00     1.2791e+00     1.2750e+00     1.2765e+00     1.2781e+00     1.2771e+00     1.2760e+00     1.2794e+00     1.2774e+00     1.2812e+00     1.2795e+00     1.2763e+00     1.2794e+00     1.2767e+00     1.2786e+00     1.2772e+00     1.2776e+00     1.2787e+00     1.2779e+00     1.2753e+00     1.2734e+00     1.2772e+00     1.2798e+00     1.2793e+00     1.2778e+00     1.2777e+00     1.2775e+00     1.2765e+00     1.2744e+00     1.2791e+00     1.2772e+00     1.2791e+00     1.2782e+00     1.2791e+00     1.2787e+00     1.2765e+00     1.2752e+00     1.2762e+00     1.2786e+00     1.2762e+00     1.2764e+00     1.2770e+00     1.2783e+00     1.2766e+00     1.2759e+00     1.2760e+00     1.2765e+00     1.2770e+00     1.2792e+00     1.2823e+00     1.2748e+00     1.2759e+00     1.2778e+00     1.2801e+00     1.2769e+00     1.2791e+00     1.2769e+00     1.2786e+00     1.2788e+00     1.2784e+00     1.2771e+00     1.2778e+00     1.2785e+00     1.2762e+00     1.2792e+00     1.2750e+00     1.2791e+00     1.2781e+00     1.2747e+00     1.2776e+00     1.2801e+00     1.2782e+00     1.2771e+00     1.2786e+00     1.2805e+00     1.2791e+00     1.2769e+00     1.2786e+00     1.2786e+00     1.2767e+00     1.2772e+00     1.2805e+00     1.2781e+00     1.2792e+00     1.2763e+00     1.2767e+00     1.2768e+00     1.2802e+00     1.2756e+00     1.2791e+00     1.2789e+00     1.2785e+00     1.2784e+00     1.2797e+00     1.2772e+00     1.2782e+00     1.2789e+00     1.2775e+00     1.2769e+00     1.2769e+00     1.2787e+00     1.2770e+00     1.2755e+00     1.2780e+00     1.2769e+00     1.2776e+00     1.2791e+00     1.2780e+00     1.2764e+00     1.2768e+00     1.2773e+00     1.2764e+00     1.2774e+00     1.2753e+00     1.2775e+00     1.2780e+00     1.2756e+00     1.2765e+00     1.2759e+00     1.2762e+00     1.2786e+00     1.2792e+00     1.2766e+00     1.2795e+00     1.2794e+00     1.2778e+00     1.2786e+00     1.2785e+00     1.2797e+00     1.2789e+00     1.2808e+00     1.2786e+00     1.2757e+00     1.2770e+00     1.2778e+00     1.2751e+00     1.2782e+00     1.2794e+00     1.2792e+00     1.2800e+00     1.2770e+00     1.2770e+00     1.2793e+00     1.2771e+00     1.2793e+00     1.2786e+00     1.2786e+00     1.2770e+00     1.2771e+00     1.2764e+00     1.2798e+00     1.2764e+00     1.2766e+00     1.2788e+00     1.2771e+00     1.2788e+00     1.2767e+00";
#把string类型转换为lsit
strAfter = re.sub(' +', ',', s)
listStr = strAfter.split(',')
print(listStr)
#listStr = list(strAfter)
#print(listStr)

freq_dict = {}
for x in listStr :
    freq_dict[x] = freq_dict.get(x, 0) + 1
print(freq_dict)

#draw_hist(listStr,'AreasList','Area','number',50.0,250,0.0,100)   # 直方图展示
#draw_hist(listStr,'perimeterList','Area','number',1,3,0.1,30)