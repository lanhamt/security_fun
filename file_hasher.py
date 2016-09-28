#!/usr/bin/python

import os
import hashlib


hashes = {}


def hash_file(file):
    '''
    Given a file name path, returns the
    md5 hash of the file.
    '''
    md5 = hashlib.md5()
    with open(file, 'rb') as fd:
        md5.update(fd.read())
    return md5.hexdigest()


def hash_files(path=os.getcwd()):
    '''
    Given a path, performs a recursive
    walk on the path and for each file
    in the directory and all subdirectories,
    attempts to calculate the file's hash and
    adds it to the dict of file names -> hashes.

    NOTE!! adds only the file name (not it's full
    path) to associate with the hash.
    '''
    for dirpath, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(dirpath, file)
            try:
                h = hash_file(file_path)
                hashes[file] = h
            except Exception, e:
                print 'error on file: ', file_path
                print str(e)


def csv_print():
    '''
    Uses the global dict of file name to hashes
    to print each name and hash in csv format.
    '''
    for f, h in hashes.iteritems():
        print '{file},{hash}'.format(file=f, hash=h)


if __name__ == '__main__':
    hash_files()
    csv_print()
