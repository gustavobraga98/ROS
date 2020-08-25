import subprocess

f = open('replaced.txt', 'r')

for line in f:
    if line.startswith('Install') or line.startswith('Purge'):
        packages = line.split()
        for i in range(1, len(packages)):
            print 'Do you want to install ' + packages[i] + '? [y/n]'
            input = raw_input()
            if input == 'y':
                print 'beginning install'
                p = subprocess.Popen('apt-get install ' + packages[i], shell=True)
                p.wait()
            else:
                print 'not installing'