from pathlib import Path
import csv

def count_ij(d):
    count_i = 0; count_j=0
    for i in range(d[2],d[3]+1):
        if i%d[6] == 0:
            count_i += 1
    for j in range(d[4],d[5]+1):
        if j%d[6] == 0:
            count_j += 1
    return count_i, count_j

def make_dat(d, Inputfiles, num):
    count_i, count_j = count_ij(d)
    with open("output/output.dat",mode='w') as f:
        for DepWater in Inputfiles:
            num += 1
            with open("input/" + str(DepWater.name), newline='') as file:
                f.write("title=output\n")
                f.write('VARIABLES="IG","JG","value"\n')
                f.write('ZONE T= "{times}"  i= {IGrid} ,j= {JGrid}\n'
                        .format(times=num, IGrid=count_i, JGrid=count_j))
                print("open {file} now!".format(file=str(DepWater.name)))
                reader = csv.reader(file,delimiter=',')
                i = 1
                for row in reader:
                    for j in range(d[4],d[5]+1):
                        if i%d[6] == 0 and j%d[6] == 0:
                            f.write('{}, {}, {}\n'.format(i,j,row[j]))
                    i+=1

def main():
    with open("init.csv",mode='r') as initfile:
        d = list(map(int,initfile.read().rstrip().split('\n')))
    Inputfiles = Path('input/').glob('*.csv')
    make_dat(d, Inputfiles, 0)

if __name__ == '__main__':
    main()