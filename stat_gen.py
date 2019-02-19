
import os
base_path = os.getcwd()


py_count = 0
idl_count = 0
h_count = 0

py_line_count = 0
idl_line_count = 0
h_line_count = 0




def iter_folder(path):
    global py_count
    global idl_count
    global h_count
    global py_line_count
    global idl_line_count
    global h_line_count

    files = list(
        os.path.join(path, f) for f in os.listdir(path)
        if '__init__' not in f
    )

    for f in files:
        if f.endswith('.h'):
            h_count += 1
            with open(f, 'r') as fle:
                h_line_count += len(fle.readlines())

        elif f.endswith('.idl'):
            idl_count += 1
            with open(f, 'r') as fle:
                idl_line_count += len(fle.readlines())

        elif f.endswith('.py'):
            py_count += 1
            with open(f, 'r') as fle:
                py_line_count += len(fle.readlines())

        elif os.path.isdir(f):
            iter_folder(f)

shared = os.path.join(base_path, 'shared')
km = os.path.join(base_path, 'shared')
um = os.path.join(base_path, 'shared')
ucrt = os.path.join(base_path, 'shared')

iter_folder(shared)
iter_folder(km)
iter_folder(um)
iter_folder(ucrt)


template = '''\
current statistics

total number of C code files {0}
number of files converted {1}

total number of C code lines {2}
number of line converted {3}

percentage of files completed: {4:.2f} %
percentage of line of code converted {5:.2f} %

'''

print template.format(
    h_count,
    py_count,
    h_line_count,
    py_line_count,
    (float(py_count) / float(h_count)) * 100.0,
    (float(py_line_count) / float(h_line_count)) * 100.0
)
