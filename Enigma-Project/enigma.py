# Enigma Template Code for CNU Information Security 2022
# Resources from https://www.cryptomuseum.com/crypto/enigma

# This Enigma code implements Enigma I, which is utilized by 
# Wehrmacht and Luftwaffe, Nazi Germany. 
# This version of Enigma does not contain wheel settings, skipped for
# adjusting difficulty of the assignment.

from copy import deepcopy
from ctypes import ArgumentError

# Enigma Components
ETW = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

WHEELS = {
    "I" : {
        "wire": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "turn": 16
    },
    "II": {
        "wire": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "turn": 4
    },
    "III": {
        "wire": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "turn": 21
    }
}

UKW = {
    "A": "EJMZALYXVBWFCRQUONTSPIKHGD",
    "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
    "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL"
}

# Enigma Settings
SETTINGS = {
    "UKW": None,
    "WHEELS": [],
    "WHEEL_POS": [],
    "ETW": ETW,
    "PLUGBOARD": []
}

def next_alphabet(input):
  return ETW[ETW.find(input) + 1]

# Wheel Rotation
def rotate_wheels():

   # print(SETTINGS["WHEEL_POS"])

    if SETTINGS["WHEELS"][0]["turn"] - SETTINGS["WHEEL_POS"][2] > 0 :
      SETTINGS["WHEELS"][0]["wire"] = SETTINGS["WHEELS"][0]["wire"][1:] + SETTINGS["WHEELS"][0]["wire"][0]
      SETTINGS["WHEEL_POS"][2] += 1
    else:
      SETTINGS["WHEEL_POS"][2] = 0
      if SETTINGS["WHEELS"][1]["turn"] - SETTINGS["WHEEL_POS"][1] > 0 :
        SETTINGS["WHEELS"][1]["wire"] = SETTINGS["WHEELS"][1]["wire"][1:] + SETTINGS["WHEELS"][1]["wire"][0]
        SETTINGS["WHEEL_POS"][1] += 1
      else:
        SETTINGS["WHEEL_POS"][1] = 0
        if SETTINGS["WHEELS"][2]["turn"] - SETTINGS["WHEEL_POS"][0] > 0 :
          SETTINGS["WHEELS"][1]["wire"] = SETTINGS["WHEELS"][1]["wire"][1:] + SETTINGS["WHEELS"][1]["wire"][0]
          SETTINGS["WHEEL_POS"][0] += 1
        else:
          SETTINGS["WHEEL_POS"][0] = 0
        

  
    
    # Implement Wheel Rotation Logics
    
    pass


def apply_settings(ukw, wheel, wheel_pos, plugboard):
    if not ukw in UKW:
        raise ArgumentError(f"UKW {ukw} does not exist!")
    SETTINGS["UKW"] = UKW[ukw]

    wheels = wheel.split(' ')
    for wh in wheels:
        if not wh in WHEELS:
            raise ArgumentError(f"WHEEL {wh} does not exist!")
        SETTINGS["WHEELS"].append(WHEELS[wh])

    wheel_poses = wheel_pos.split(' ')
    for wp in wheel_poses:
        if not wp in ETW:
            raise ArgumentError(f"WHEEL position must be in A-Z!")
        SETTINGS["WHEEL_POS"].append(ord(wp) - ord('A'))
    
    plugboard_setup = plugboard.split(' ')
    for ps in plugboard_setup:
        if not len(ps) == 2 or not ps.isupper():
            raise ArgumentError(f"Each plugboard setting must be sized in 2 and caplitalized; {ps} is invalid")
        SETTINGS["PLUGBOARD"].append(ps)

# Enigma Logics Start

# Plugboard
def pass_plugboard(input):
    for plug in SETTINGS["PLUGBOARD"]:
        if str.startswith(plug, input):
            return plug[1]
        elif str.endswith(plug, input):
            return plug[0]
    return input
  

# ETW
def pass_etw(input):
    return SETTINGS["ETW"][ord(input) - ord('A')]

# Wheels
def pass_wheels(input, reverse = False):

    if reverse == False:
      # print(SETTINGS["WHEELS"])
      # print(SETTINGS["WHEEL_POS"])
      
      # print(SETTINGS["WHEELS"][0]["wire"][ord(input) - ord('A')])
      index_I = SETTINGS["WHEELS"][0]["wire"][ord(input) - ord('A')]
      
      # print(SETTINGS["WHEELS"][1]["wire"][ord(index_I) - ord('A') - SETTINGS["WHEEL_POS"][2]])
      index_II = SETTINGS["WHEELS"][1]["wire"][ord(index_I) - ord('A') - SETTINGS["WHEEL_POS"][2]]

      # print(SETTINGS["WHEELS"][2]["wire"][ord(index_II) - ord('A') - SETTINGS["WHEEL_POS"][1]])
      index_III = SETTINGS["WHEELS"][2]["wire"][ord(index_II) - ord('A') - SETTINGS["WHEEL_POS"][1]]
      return index_III
    else:
      #print(SETTINGS["WHEELS"])
      #print(input)
      index_III = ETW[SETTINGS["WHEELS"][2]["wire"].find(input)]
      #print(index_III)
      index_II = ETW[SETTINGS["WHEELS"][1]["wire"].find(index_III)]
      #print(index_II)
      temp = ord(index_II) - ord('A') + SETTINGS["WHEEL_POS"][2]
      if temp > 25:
        temp -= 25
      index_I = ETW[SETTINGS["WHEELS"][0]["wire"].find(ETW[temp])]
      #print(index_I)
      return index_I
      
    
    # Implement Wheel Logics
    # Keep in mind that reflected signals pass wheels in reverse order

# UKW
def pass_ukw(input):
    return SETTINGS["UKW"][ord(input) - ord('A')]

# Enigma Exec Start
plaintext = input("Plaintext to Encode: ")
ukw_select = input("Set Reflector (A, B, C): ")
wheel_select = input("Set Wheel Sequence L->R (I, II, III): ")
wheel_pos_select = input("Set Wheel Position L->R (A~Z): ")
plugboard_setup = input("Plugboard Setup: ")

apply_settings(ukw_select, wheel_select, wheel_pos_select, plugboard_setup)

for ch in plaintext:
    rotate_wheels()
  
    encoded_ch = ch
    encoded_ch = pass_plugboard(encoded_ch)
    encoded_ch = pass_etw(encoded_ch)
    #print(encoded_ch)
    encoded_ch = pass_wheels(encoded_ch)
  
    encoded_ch = pass_ukw(encoded_ch)
    encoded_ch = pass_wheels(encoded_ch, reverse = True)
    encoded_ch = pass_plugboard(encoded_ch)

    print(encoded_ch, end='')
