import os

class file(object):

    def FindFile(self):

        self.__my__test()

    def __my__test(self):
        path1 = 'c:\\'
        path2 = 'home'
        path3 = 'filename'
        Path = os.path.join(path1,path2,path3)
        print(Path)


if __name__ == '__main__':
    game = file()
    game.FindFile()

