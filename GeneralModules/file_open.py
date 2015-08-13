__author__ = 'Sandesh'
import io


def file_open(filename):
    file = open(str(filename), 'r')
    print('File Opened: ', file.name)
    return file


def file_open(filename, mode):
    file = open(str(filename), str(mode))
    print('File Opened in ' + str(mode) + ': ', file.name)
    return file

