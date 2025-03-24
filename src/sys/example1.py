import sys

if __name__ == '__main__':
    print(f"All the Python paths of this python project are these : \n")
    for path in sys.path:
        print(path)

    sys.path.append('/ufs/guido/lib/python')