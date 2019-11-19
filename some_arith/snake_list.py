# -*- coding: utf-8 -*-
# 这是一个很有意思的遍历二次数组的方式
# 类似蛇盘踞一样遍历整个数组

source_list = [[11, 12, 13, 14, 15, 16],
               [21, 22, 23, 24, 25, 26],
               [31, 32, 33, 34, 35, 36],
               [41, 42, 43, 44, 45, 46],
               [51, 52, 53, 54, 55, 56],
               [61, 62, 63, 64, 65, 66]]

start = (0, 0)
end = (0, 6)
# (x, y)
# (0,0)->(0,6), (1,6)->(6,6), (5,6)->(6,0) ()->(1,1)


def h_l(source, start_tp, end_tp):
    # 水平左遍历
    for item in range(start_tp[1], end_tp[1]):
        print source[start_tp[0]][item]


def h_r(source, start_tp, end_tp):
    # 水平右遍历
    for item in range(end_tp[1]+1, start_tp[1]):
        print source[start_tp[0]-1][len(source[0]) - item - 1]


def v_d(source, start_tp, end_tp):
    # 垂直向下遍历
    for item in range(start_tp[0]+1, end_tp[0]):
        print source[item][start_tp[1]-1]


def v_u(source, start_tp, end_tp):
    # 垂直向上遍历
    for item in range(end_tp[0], start_tp[0]-1):
        print source[len(source) - item - 1][start_tp[1]]


def get_point(source):
    for x in range(0, max(len(source[0]), len(source))):
        if x >= (max(len(source[0]), len(source)) / 2):
            break
        yield (x, x), (x, len(source)-x), (len(source[0]) - x, len(source)-x), (len(source[0]) - x, x), (x+1, x+1)


if __name__ == "__main__":
    # h_l(source_list, (0, 0), (0, 6))
    # h_r(source_list, (0, 6), (6, 6))
    # v_d(source_list, (0, 0), (6, 0))
    # v_u(source_list, (6, 0), (0, 0))
    # print source_list[3][3]
    for s1, s2, s3, s4, s5 in get_point(source_list):
        print s1, s2, s3, s4, s5
        h_l(source_list, s1, s2)
        v_d(source_list, s2, s3)
        h_r(source_list, s3, s4)
        v_u(source_list, s4, s5)
