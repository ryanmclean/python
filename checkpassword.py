import libraries.hibp
import hashlib
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('input_filename',help='The name of the file to read from',default='rawpw.txt')
parser.add_argument('output_filename',help='The name of the CSV file to write to',default='pwprevalence.csv')
args = parser.parse_args()

api = libraries.hibp.api()
sha1 = hashlib.sha1()

if not os.path.exists(args.input_filename):
    print("Error - input filename ({})does not exist.".format(args.input_filename))
    exit(1)
f = open(args.input_filename,'r',encoding='UTF-8')
pwned = open(args.output_filename,'w',encoding='UTF-8')

pwned.write("Password,Hash,Prevalence\n")
for line in f.readlines():
    line = line.strip('\r')
    line = line.strip('\n')
    print("Password: {}".format(line))
    h = hashlib.sha1(line.encode('UTF-8'))
    print("checking hash: {}".format(h.hexdigest().upper()))
    hash_prevalence = api.checkHash(h.hexdigest())
    print("Prevalence of hash is {}".format(hash_prevalence))
    pwned.write("{},{},{}\n".format(line,h.hexdigest(),hash_prevalence))
    print("\n")
f.close()
pwned.close()