import math,string,collections

# import inbuilt standard input output
from sys import stdin, stdout


class Dir:
    def __init__(self, name) -> None:
        self.name = name
        self.parent = None
        self.files = []
        self.directories = {}
        self.size = 0
class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

# suppose a function called main() and
# all the operations are performed
def main():
    root = Dir('root')
    current_node = root
    root_size = 0
    # input via .txt file
    with open('input2.txt') as f:
        lines = f.read().splitlines()
    dir_sizes = []
    index = 0
    while index < len(lines):
        info = lines[index].split(' ')
        if info[1] == 'cd':
            if info[2] == '/':
                current_node = root
            elif info[2] in current_node.directories:
                next_dir = current_node.directories[info[2]]
                next_dir.parent = current_node
                current_node = next_dir
            elif info[2] == '..':
                current_node = current_node.parent
            else:
                print('Directory: ', info[2], ' does not exist')
                return
            index += 1
        elif info[1] == 'ls':
            while index + 1 < len(lines) and lines[index + 1][0] != '$':
                index += 1
                if  lines[index][0].isnumeric():
                    # print(lines[index])
                    size, file = lines[index].split(' ')
                    size = int(size)
                    current_node.files.append(File(file, size))
                    current_node.size += size
                    root_size += size
                else:
                    dir_name = lines[index].split(' ')[1]
                    # print(dir_name)
                    current_node.directories[dir_name] = Dir(dir_name)
            index += 1
    def dfs(node):
        if len(node.directories) == 0:
            dir_sizes.append(node.size)
            return node.size
        else:
            size = sum([dfs(child_dir) for name, child_dir in node.directories.items()]) + node.size
            node.size = size
            dir_sizes.append(size)
            return size
    
    dfs(root)
    required_space = 30000000
    total_space = 70000000
    size_to_free = required_space - (total_space - root.size)
    print(min([size for size in dir_sizes if size >= size_to_free]))
    

if __name__ == "__main__":
    main()