import sys
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

def read_file(filename):
    cr = Credit()

    defs = [
        validate_and_set_vehicle,
        validate_and_set_condition,
        validate_and_set_year,
        validate_and_set_total,
        validate_and_set_duration,
        validate_and_set_dp,
    ]

    with open(filename, 'r') as f:
        lines = f.readlines()
        cnt = 0

        for line in lines:
            val = line.strip()
            
            if defs[cnt](cr, val):
                cnt += 1
            if cnt == len(defs):
                break

    if cnt != len(defs):
        exit(1)
    
    return cr

def prompt_vehicle(cr):
    while True:
        p = 'JENIS KENDARAAN ({}/{})'.format(VEHICLE_MOTORCYCLE, VEHICLE_CAR)
        val = prompt(p)

        if validate_and_set_vehicle(cr, val):
            break

def prompt_condition(cr):
    while True:
        p = 'KONDISI ({}/{})'.format(CONDITION_NEW, CONDITION_USED)
        val = prompt(p)

        if validate_and_set_condition(cr, val):
            break

def prompt_year(cr):
    while True:
        p = 'TAHUN KENDARAAN ({})'.format(YEAR_FORMAT)
        val = prompt(p)

        if validate_and_set_year(cr, val):
            break

def prompt_total(cr):
    while True:
        p = 'JUMLAH PINJAMAN (<=1M)'
        val = prompt(p)

        if validate_and_set_total(cr, val):
            break

def prompt_duration(cr):
    while True:
        p = 'TENOR (1-{})'.format(MAX_DURATION_YEAR)
        val = prompt(p)

        if validate_and_set_duration(cr, val):
            break

def prompt_dp(cr):
    while True:
        p = 'DP'
        val = prompt(p)

        if validate_and_set_dp(cr, val):
            break

def validate_and_set_vehicle(cr, val):
    val = val.upper()
    num = -1

    if val in VEHICLE_MAP:
        num = VEHICLE_MAP[val]

    try:
        cr.set_vehicle(num)
        return True
    except Error as e:
        print_error(str(e))
        return False

def validate_and_set_condition(cr, val):
    val = val.upper()
    num = -1

    if val in CONDITION_MAP:
        num = CONDITION_MAP[val]

    try:
        cr.set_condition(num)
        return True
    except Error as e:
        print_error(str(e))
        return False

def validate_and_set_year(cr, val):
    if not val.isdigit() or len(val) != len(YEAR_FORMAT):
        print_error('format tidak valid')
        return False
    
    try:
        cr.set_year(int(val))
        return True
    except Error as e:
        print_error(str(e))
        return False
    
def validate_and_set_total(cr, val):
    if not val.isdigit():
        print_error('format tidak valid')
        return False
    
    try:
        cr.set_total(int(val))
        return True
    except Error as e:
        print_error(str(e))
        return False

def validate_and_set_duration(cr, val):
    if not val.isdigit():
        print_error('format tidak valid')
        return False
    
    try:
        cr.set_duration(int(val))
        return True
    except Error as e:
        print_error(str(e))
        return False
    
def validate_and_set_dp(cr, val):
    if not val.isdigit():
        print_error('format tidak valid')
        return False
    
    try:
        cr.set_dp(int(val))
        return True
    except Error as e:
        print_error(str(e))
        return False
    
def prompt(p):
    print('{}: '.format(p), end = '')
    return input().strip()

def print_error(msg):
    print(msg, file = sys.stderr)
