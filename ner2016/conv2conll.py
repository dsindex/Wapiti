from __future__ import print_function
import sys
import argparse

class Conv:
    def __init__(self):
        self.task = 'conv'

    def conv_bucket(self, bucket):
        for line in bucket:
            line = line.replace('\t', ' ')
            if line[0] == '#': continue
            tokens = line.split()
            size = len(tokens)
            assert(size == 5)
            morph = tokens[0]
            tag = tokens[1]
            etype = tokens[2]
            pred = tokens[4]
            if '/' in pred : pred = pred.split('/')[0]

            if '_' in etype:
                suffix, label = etype.split('_')
                etype = suffix + '-' + label
            if '_' in pred:
                suffix, label = pred.split('_')
                pred = suffix + '-' + label

            print(morph, tag, 'X', etype, pred)
        print('')

    def conv(self):
        bucket = []
        while 1:
            try: line = sys.stdin.readline()
            except KeyboardInterrupt: break
            if not line: break
            line = line.strip()
            if not line and len(bucket) >= 1:
                self.conv_bucket(bucket)
                bucket = []
            if line : bucket.append(line)
        if len(bucket) != 0:
            self.conv_bucket(bucket)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    args = parser.parse_args()

    c = Conv()
    c.conv()
