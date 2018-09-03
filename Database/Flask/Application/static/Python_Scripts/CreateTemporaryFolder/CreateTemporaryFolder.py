import os
import errno

def createFolder():
    tmpPath = os.path.join(os.path.dirname(__file__), '../../')
    os.chdir(tmpPath)
    directory = 'tmp'
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    return