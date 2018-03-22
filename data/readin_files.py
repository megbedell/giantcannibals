import pickle 
import matplotlib.pyplot as plt

modfile = 'redclump_1_nonorm_model.pickle'
with open(modfile, 'rb') as f:
    model = pickle.load(f, encoding='latin1')

datfile = 'redclump_1_alpha_nonorm.pickle'
with open(datfile, 'rb') as f:
    data = pickle.load(f, encoding='latin1')


if True: # plot some shit
    for i in range(0,10000,2000):
        ok = data[:,i,2] < 10.  # mask out the huge error bars
        pts = plt.errorbar(data[:,i,0][ok], data[:,i,1][ok], yerr=data[:,i,2][ok], fmt='o', ls=None, alpha=0.6)
        plt.step(data[:,i,0], data[:,i,1], c=pts[0]._color)
    plt.xlim([16350., 16380.])
    plt.ylim([0.4,1.3])
    