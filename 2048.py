import random
import copy

choices = ["w", "s", "a", "d"]


class My2048(object):
    def __init__(self):
        self.array = [[0 for x in range(4)] for x in range(4)]
        self.new_point()

    def print_array(self):
        for x in range(4):
            for y in range(4):
                print("{:^8d}".format(self.array[x][y]), end="")
            print("\n")

    def combine(self, line):
        for i in range(3):
            flag = False
            if line[i] == line[i + 1] and line[i] != 0:
                line[i], line[i + 1] = line[i] * 2, 0
                flag = True
            if line[i] == 0 and line[i + 1] != 0:
                line[i], line[i + 1] = line[i + 1], line[i]
                flag = True
            if flag:
                if line == self.combine(line):
                    return line
        return line

    def transpose_d(self):
        for x in range(4):
            for y in range(2):
                self.array[x][y], self.array[x][-1-y] = self.array[x][-1-y], self.array[x][y]

    def transpose_w(self):
        for x in range(4):
            for y in range(x):
                if x == y:
                    continue
                self.array[x][y], self.array[y][x] = self.array[y][x], self.array[x][y]

    def transpose_s(self):
        for x in range(4):
            for y in range(3-x):
                self.array[x][y], self.array[3-y][3-x] = self.array[3-y][3-x], self.array[x][y]

    def reorganize_array(self, action):
        temp_array = copy.deepcopy(self.array)
        if action == "a":
            for line in self.array:
                self.combine(line)
        elif action == "d":
            self.transpose_d()
            for line in self.array:
                self.combine(line)
            self.transpose_d()
        elif action == "w":
            self.transpose_w()
            for line in self.array:
                self.combine(line)
            self.transpose_w()
        elif action == "s":
            self.transpose_s()
            for line in self.array:
                self.combine(line)
            self.transpose_s()
        if temp_array == self.array:
            self.check_gameover()
            return False
        return True

    def check_gameover(self):
        for x in range(3):
            for y in range(3):
                if self.array[x][y] == self.array[x+1][y] or self.array[x][y] == self.array[x][y+1]:
                    return False
        if self.array[3][3] == self.array[3][2] or self.array[3][3] == self.array[2][3]:
            return False
        for line in self.array:
            if 0 in line:
                return False
        print("game over")
        exit()

    def new_point(self):
        value = random.choice([2, 4])
        zero_array = []
        for x in range(4):
            for y in range(4):
                if self.array[x][y] == 0:
                    zero_array.append([x, y])
        if not zero_array:
            exit(1)
        pos = random.choice(zero_array)
        self.array[pos[0]][pos[1]] = value

    def start(self):
        while True:
            self.print_array()
            print("--------------------------------")
            action = input("please input (wasd): ")
            if action.strip() not in choices:
                continue
            if not self.reorganize_array(action):
                continue
            self.new_point()


if __name__ == '__main__':
    game = My2048()
    game.start()
