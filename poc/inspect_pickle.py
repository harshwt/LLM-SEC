import pickletools
import sys

def inspect_pickle(file_path):
    with open(file_path, 'rb') as f:
        pickletools.dis(f)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python inspect_pickle.py <file.pkl>")
        sys.exit(1)
    inspect_pickle(sys.argv[1])
