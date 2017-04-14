import csv
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import stdev
import argparse


def run_code():

    synDist = None
    ranDist = None

    missRand = []
    gotSyn = []
    ks = []

    homDir = './result'
    dim = args.dim
    
    with open('{}/randdist_k={}.csv'.format(homDir, dim)) as f:
        ranDist = list(csv.reader(f))
        ranDist = [float(a[0]) for a in ranDist]

    with open('{}/syndist_k={}.csv'.format(homDir, dim)) as f:
        synDist = list(csv.reader(f))
        synDist = [float(a[0]) for a in synDist]

    sd = stdev(ranDist)

    ks.append(dim)
    missRand.append(sum(1.0 if abs(rd) > sd else 0.0 for rd in ranDist)/len(ranDist))
    gotSyn.append(sum(1.0 if abs(rd) > sd else 0.0 for rd in synDist)/len(synDist))

    print(" With k={} \n Misclassified random pairs: {} \n Accurately classified synonyms: {} \n"
          .format(dim, missRand[-1], gotSyn[-1]))
    
    if args.plot is 1:
        ax = sns.distplot(ranDist,label="Random pairs",kde=False,hist=True)
        ax = sns.distplot(synDist,label="Pairs of synonyms",kde=False,hist=True)
        ax.set_xlabel("Inner product between vectors")
        ax.set_ylabel("Frequency")
        ax.set_yscale("log")
        ax.legend()
        ax.axvline(sd)
        ax.axvline(-sd)

        plt.show()


if __name__ == '__main__':

    p = argparse.ArgumentParser()
    p.add_argument('--dim', type=int, default=0)
    p.add_argument('--plot', type=int, default=0)
    args = p.parse_args()
    
    run_code()
        
