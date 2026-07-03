import sys
from .image import resize

def main():
    args = sys.argv

    if len(args) < 2:
        print("Usage: allpy <command>")
        return

    cmd = args[1]

    if cmd == "resize":
        input_file = args[2]
        width = int(args[3])
        height = int(args[4])
        output = args[5]

        resize(input_file, (width, height), output)
        print("Image resized!")

if __name__ == "__main__":
    main()