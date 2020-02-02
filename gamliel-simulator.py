#!/usr/bin/python3
import random
import sys

PACKETSIZE = int(sys.argv[1])
THRESHOLD  = int(sys.argv[2])
POLICY_NUM = int(sys.argv[3])

LAST_PACKET = (0).to_bytes(8, byteorder='big')

def policy(choice):

    global LAST_PACKET

    if choice == 1:
        return (0).to_bytes(PACKETSIZE, byteorder='big')
    if choice == 2:
        return bytes(bytearray(LAST_PACKET)[-1])
    if choice == 3:
        return LAST_PACKET


infile  = open('./Everytime-We-Touch.au', 'rb')
outfile = open('new-file.au', 'wb') 

def prob():
    return random.randint(1, 100)

l = infile.read(48)
outfile.write(l)

l = infile.read(PACKETSIZE)
LAST_PACKET = l

sequence   = 0
total_sent = 0
while l:
    prob_ = prob()
    if prob_ > THRESHOLD:
        LAST_PACKET = l
        outfile.write(l)
        sequence += 1
    else:
        policyData = policy(POLICY_NUM)
        outfile.write(policyData)

    total_sent += 1
    l = infile.read(PACKETSIZE)

print("Sequence:", sequence)
print("Total", total_sent)
