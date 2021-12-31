import os

def get_names():
    for root, directories, files in os.walk(path, topdown=True):
        for name in files:
            print(os.path.join(root, name))
        for name in directories:
            print(os.path.join(root, name))



if __name__ == "__main__":
    path = '/Users/olgazienovieva/Documents/projects/Python-Hillel/Python-Hillel-2021'
    get_names()
    