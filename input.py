import sys
from enums import Vehicle, Condition
from credit import *
from constant import *

def read_prompt():
    cr = Credit()
    
    prompt_vehicle(cr)
    prompt_condition(cr)
    prompt_year(cr)
    prompt_total(cr)
    prompt_duration(cr)
    prompt_dp(cr)

    return cr

def prompt_vehicle(cr):
    while True:
        p = 'JENIS KENDARAAN ({}/{})'.format(VEHICLE_MOTORCYCLE, VEHICLE_CAR)
        val = prompt(p).upper()
        enum = -1

        if val == VEHICLE_MOTORCYCLE:
            enum = Vehicle.MOTORCYCLE
        elif val == VEHICLE_CAR:
            enum = Vehicle.CAR

        try:
            cr.set_vehicle(enum)
            break
        except Error as e:
            print_error(str(e))

def prompt_condition(cr):
    while True:
        p = 'KONDISI ({}/{})'.format(CONDITION_NEW, CONDITION_USED)
        val = prompt(p).upper()
        enum = -1

        if val == CONDITION_USED:
            enum = Condition.USED
        elif val == CONDITION_NEW:
            enum = Condition.NEW

        try:
            cr.set_condition(enum)
            break
        except Error as e:
            print_error(str(e))

def prompt_year(cr):
    while True:
        p = 'TAHUN KENDARAAN ({})'.format(YEAR_FORMAT)
        val = prompt(p)

        if not val.isdigit() or len(val) != len(YEAR_FORMAT):
            print_error('format tidak valid')
            continue

        try:
            cr.set_year(int(val))
            break
        except Error as e:
            print_error(str(e))

def prompt_total(cr):
    while True:
        p = 'JUMLAH PINJAMAN (<=1M)'
        val = prompt(p)

        if not val.isdigit():
            print_error('format tidak valid')
            continue

        try:
            cr.set_total(int(val))
            break
        except Error as e:
            print_error(str(e))

def prompt_duration(cr):
    while True:
        p = 'TENOR (1-{})'.format(MAX_DURATION_YEAR)
        val = prompt(p)

        if not val.isdigit():
            print_error('format tidak valid')
            continue

        try:
            cr.set_duration(int(val))
            break
        except Error as e:
            print_error(str(e))

def prompt_dp(cr):
    while True:
        p = 'DP'
        val = prompt(p)

        if not val.isdigit():
            print_error('format tidak valid')
            continue

        try:
            cr.set_dp(int(val))
            break
        except Error as e:
            print_error(str(e))

def read_file(filename):
    pass

def prompt(p):
    print('{}: '.format(p), end = '')
    return input().strip()

def print_error(msg):
    print(msg, file = sys.stderr)
