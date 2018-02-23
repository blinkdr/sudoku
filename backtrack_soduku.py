import time
class Suku(object):

    def __init__(self, data):
        self.data = data    # 9*9的一个二维数组

    def solve(self):
        x, y = self.get_next()
        # 二维数组中全部都不为零时结束
        if x == -1 and y == -1:
            return True
        # 尝试用1-9去填为0的位置
        for num in range(1,10):
            # 条件满足
            if self.check_num(x,y,num):
                # 当前位置赋值
                self.data[x][y] = num
                # 尝试下一个未填位置
                if self.solve():
                    return True
                # 条件不满足时，赋值为0
                self.data[x][y] = 0

    def get_next(self):
        for i in range(9):
            for j in range(9):
                if self.data[i][j] == 0:
                    return i,j
        return -1,-1

    def check_num(self,x,y,num):
        # 行检查
        for value in self.data[x]:
            if value == num:
                return False
        # 列检查
        for i in range(9):
            if self.data[i][y] == num:
                return False
        # 九宫检查
        row, col = x//3*3, y//3*3
        rc = self.data[row][col:col+3] + self.data[row+1][col:col+3] + self.data[row+2][col:col+3]
        for value in rc:
            if value == num:
                return False
        return True

    def start_solve(self):
        start_time = time.time()
        if self.solve():
            for row in self.data:
                print(row)
        else:
            print('can not solve the suku!')
        end_time = time.time()
        print('\nused time {}s.'.format(end_time-start_time))

if __name__ == '__main__':
    board = [
        [8,0,0,0,0,0,0,0,0],
        [0,0,3,6,0,0,0,0,0],
        [0,7,0,0,9,0,2,0,0],
        [0,5,0,0,0,7,0,0,0],
        [0,0,0,8,4,5,7,0,0],
        [0,0,0,1,0,0,0,3,0],
        [0,0,1,0,0,0,0,6,8],
        [0,0,8,5,0,0,0,1,0],
        [0,9,0,0,0,0,4,0,0]
    ]

    soku = Suku(board)
    soku.start_solve()

# [8, 1, 2, 7, 5, 3, 6, 4, 9]
# [9, 4, 3, 6, 8, 2, 1, 7, 5]
# [6, 7, 5, 4, 9, 1, 2, 8, 3]
# [1, 5, 4, 2, 3, 7, 8, 9, 6]
# [3, 6, 9, 8, 4, 5, 7, 2, 1]
# [2, 8, 7, 1, 6, 9, 5, 3, 4]
# [5, 2, 1, 9, 7, 4, 3, 6, 8]
# [4, 3, 8, 5, 2, 6, 9, 1, 7]
# [7, 9, 6, 3, 1, 8, 4, 5, 2]
#
# used time 0.055077314376831055s.