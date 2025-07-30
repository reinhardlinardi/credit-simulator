import sys
from simulator import CreditSimulator
from input import read_prompt, read_file

def main():
    try:
        argc = len(sys.argv)-1

        if argc == 0:
            credit = read_prompt()
        else:
            credit = read_file(sys.argv[1])

        cs = CreditSimulator()
        cs.set_credit(credit)
        cs.simulate()

        print(cs.get_avg_monthly())

    except KeyboardInterrupt:
        pass

main()
