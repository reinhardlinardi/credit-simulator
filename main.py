import sys
from input import read_prompt, read_file

def main():
    try:
        argc = len(sys.argv)-1

        if argc == 0:
            cr = read_prompt()
        else:
            cr = read_file(sys.argv[1])
        
        # simulate

    except KeyboardInterrupt:
        pass

main()
