#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# Source: https://sites.google.com/site/roguewavesoftwarefrance/tutoriels/Python-Clustering-k-Means

import matplotlib.pyplot as plt

from numpy import array, empty, where

#from imsl.stat.clusterKMeans import clusterKMeans 

xData = [-0.00225554,0.192812,0.549314,0.643484,1.10088,1.16815,1.19169,
         1.43384,1.45402,1.50447,1.50447,1.50447,1.56165,1.52465,1.47757,
         1.80716,1.84752,1.74662,1.74326,1.74662,2.39909,1.51792,1.86097,
         1.66591,1.61209,1.49438,1.51456,1.44393,1.4742,1.49438,1.50447,
         1.36994,1.19505,0.962991,1.15806,1.16815,1.37667,1.43721,1.39012,
         1.46411,1.51792,1.57174,1.5381,1.59864,1.58519,1.58519,1.60537,
         1.62218,1.62555,1.64909,1.23878,1.20514,1.14124,1.12779,1.06052,
         0.959628,0.952901,0.825099,0.626668,0.710749,0.808283,0.791466,
         0.804919,0.845278,0.892363,0.946175,1.01344,1.0807,1.14797,1.16478,
         1.14461,1.02017,1.00335,1.0168,0.986534,0.979807,0.902453,0.932722,
         0.919269,0.89909,0.912543,0.744381,0.613215,0.646848,0.57622,
         0.455144,0.428238,0.360973,0.310525,0.169269,0.206265,0.249987,
         0.286982,0.374426,0.377789,0.401332,0.475323,0.502229,0.663664,
         0.67039,0.0885516,-0.0863363,-0.0358878,-0.190596,0.159179,0.206265,
         0.266803,0.266803,0.293709,0.186085,0.0515561,0.03474,-0.0695201,
         -0.0493407,-0.150238,-0.274677,0.139,0.159179,0.14909,0.122184,
         0.142363,0.152453,0.155816,0.132274,0.0851884,0.065009,0.00447091,
         -0.123332,-0.237682,-0.241045,-0.207412,-0.18387,-0.177143,
         -0.0863363,-0.0358878,0.065009,0.125547,0.0717355,0.0414664,
         0.0582826,0.03474,0.0246503,0.0111974,-0.0123452,-0.008982,
         -0.00561877,-0.0257981,-0.0493407,-0.0325246,0.00783414,-0.008982,
         -0.00225554,-0.0728833,-0.0930627,-0.106516,-0.0930627,-0.109879,
         -0.146874,-0.133421,-0.123332,-0.126695,-0.140148,0.488776,0.482049,
         0.468596,0.482049,0.569493,0.56613,0.704022,0.704022,0.744381,
         0.656937,0.673753,0.704022,0.717475,0.700659,0.693933,0.710749,
         0.730928,0.754471,0.754471,1.13788,1.06389,1.09416,1.07734,1.0807,
         1.05716,1.04707,1.0168,0.999987,0.895727,0.858731,0.848641,
         0.781377,0.798193,0.825099,0.804919,0.811646,0.875547,0.912543,
         0.862094,0.882274,0.889,1.30604,1.3094,1.32286,1.35985,1.38003,
         1.39685,1.41703,1.43048,1.47084,1.43048,1.4103,1.43048,1.46748,
         1.50447,1.47757,1.66254,1.72981,1.71972,1.69954,1.69954,1.67936,
         1.68609,1.65245,1.66591,1.64573,1.62891,1.61546,1.59528,1.57174,
         1.55492,1.5381,1.57174,1.58855,1.59528,1.60873,1.58855,1.63227,
         1.61209,1.61882,1.59528,1.56501,1.56837,1.5381,1.52801,1.50111,
         1.50783,1.52801,1.48429,1.46075,1.45066,1.45402,1.46411,1.49102,
         1.49102,1.49774,1.51792,1.5112,1.53138,1.5381,1.56165,1.57174,
         1.55828,-0.119969,-0.156964,-0.146874,-0.177143,-0.187233,
         -0.204049,-0.220865,-0.254498,-0.241045,-0.247771,-0.247771,
         -0.227592,-0.220865,-0.204049,-0.234318,-0.210776,-0.19396,
         -0.170417,-0.140148,-0.167054,-0.197323,-0.200686,-0.18387]

yData = [12.0086,13.1438,14.2058,11.8621,12.9607,12.1184,11.0198,12.4114,
         11.5691,12.9973,12.9973,12.9973,13.2536,13.8396,13.5832,15.4508,
         14.279,13.51,12.9607,12.7776,12.1917,8.63956,-5.34918,-4.14073,
         -5.0196,-5.23932,-4.25059,-3.70129,-3.59143,-3.40833,-3.11537,
         -3.15199,-4.72664,-3.99425,-2.67594,-2.0534,-2.19988,-1.79706,
         -1.17453,-0.99143,-1.17453,-1.98016,-0.735092,-0.625233,-0.954811,
         -1.28439,-1.65059,-1.43087,-1.76044,-1.57735,-0.368895,-0.881571,
         -0.332275,-0.99143,-1.17453,-1.76044,-2.49284,-3.51819,-3.73791,
         -1.61397,-0.661853,-0.515374,-1.57735,-1.28439,-0.625233,
         -0.625233,-0.405515,0.400119,0.400119,0.729696,0.729696,0.729696,
         0.693077,0.876175,0.949415,0.546598,0.473358,0.32688,-0.0759374,
         -0.112557,3.73251,3.69589,3.40294,2.63392,2.34096,1.38885,2.63392,
         2.30434,2.34096,2.4142,2.19449,1.53533,1.05927,1.05927,-2.93228,
         -2.74918,-4.61678,-5.82523,-6.99706,-6.22805,-8.90129,-7.6196,
         -6.85059,-6.48439,-5.67875,-5.53228,-5.67875,-4.6534,-3.99425,
         -4.50692,-2.93228,-3.33509,-3.62805,-4.32382,-5.45904,-6.00833,
         1.68181,1.38885,1.16913,1.24237,0.766316,0.546598,0.25364,0.0339218,
         1.90153,1.42547,1.38885,0.21702,-5.53228,-5.16608,-5.3858,-5.05622,
         -4.76326,-2.56608,-1.57735,-1.02805,-0.735092,-0.185797,-0.112557,
         0.32688,0.436739,0.32688,0.839556,0.766316,0.473358,-0.222416,
         -0.332275,-0.442135,-0.918191,-1.02805,-0.771712,-0.808332,
         -0.844952,-0.588613,-0.698473,-1.10129,-1.06467,-1.57735,
         -1.46749,-1.94354,-2.09002,-2.19988,4.39167,3.91561,3.73251,
         3.62265,4.39167,4.57477,4.28181,4.57477,4.61139,5.0142,4.94096,
         5.0142,5.3804,5.30716,5.7466,5.67336,5.5635,5.70998,6.55223,
         7.4311,7.46772,6.99167,6.62547,6.88181,6.88181,6.40575,6.88181,
         6.47899,5.67336,5.45364,5.34378,5.81984,5.5635,5.7466,6.07618,
         5.89308,6.00294,6.47899,6.33251,6.18603,6.40575,8.38322,8.1635,
         8.12688,8.09026,8.3466,8.7128,8.7128,8.63956,8.74941,8.96913,
         9.48181,9.77477,9.33533,9.51843,9.66491,11.8987,12.0452,12.2283,
         12.448,12.6311,12.8508,13.0705,12.7776,12.5945,12.448,12.3381,
         12.448,12.3381,12.1184,11.9719,11.7522,11.5691,11.7522,11.9353,
         11.5325,11.3494,11.2762,11.1663,10.8367,10.9832,11.0565,11.2396,
         10.9832,11.2029,11.2029,10.9466,10.7269,10.7635,10.7635,10.3973,
         10.0677,10.1776,9.99448,10.3241,10.5072,10.141,10.4339,10.3973,
         10.141,10.1776,10.2508,10.3973,-3.22523,-3.92101,-3.62805,-3.48157,
         -3.48157,-4.14073,-4.21397,-4.28721,-4.14073,-4.03087,-3.59143,
         -3.51819,-3.07875,-3.18861,-2.82242,-2.82242,-2.89566,-3.00551,
         -2.93228,-2.71256,-2.52946,-2.30974,-2.2365]

#----------------------------------------------------------------------------
# Mise � l'�chelle des donn�es
#----------------------------------------------------------------------------
xs = ys = []
minx, miny = min(xData), min(yData)
rangex, rangey = max(xData) - minx, max(yData) - miny
for i in range(0, len(xData), 1):
    xs.append((xData[i] - minx) / rangex)
    ys.append((yData[i] - miny) / rangey)
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
# Effectue l'analyse par cluster KMeans
#----------------------------------------------------------------------------
cluster_means = []
cluster_ssq = []
cluster_counts =[]
data = empty(shape=(len(yData), 2))
for i in range(0, len(xData), 1):
    data[i][0], data[i][1] = xData[i], yData[i]
    n_clusters = 3
    cluster_seeds = empty(shape=(n_clusters, 2))
    m = minc = len(xData)/n_clusters - 1
    for i in range(0, n_clusters, 1):
        cluster_seeds[i][0],cluster_seeds[i][1] = data[m][0],data[m][1]
        m = m + minc
        
        # cluster_group = clusterKMeans(2, data, cluster_seeds,
        #                               clusterCounts=cluster_counts,
        #                               clusterMeans=cluster_means,
        #                               clusterSsq=cluster_ssq)
        # cluster_means = array(cluster_means)
        # cluster_means = cluster_means.reshape(n_clusters, 2)
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
# Mise en place des axes, titres et labels
#----------------------------------------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(xData, yData, s=30, c='w', marker='o')
ax1.set_xticks([-0.5, 0, 0.5, 1.0, 1.5, 2.0, 2.5])
ax1.set_yticks([20, 15, 10, 5, 0, -5, -10])
ax1.set_xlabel("Indice de Couleur B-V")
ax1.set_ylabel("Magnitude Absolue V")
ax1.yaxis.tick_left()
ax1.xaxis.tick_bottom()
ax2 = fig.add_subplot(111, frameon=False)
ax2.yaxis.tick_right()
ax2.xaxis.tick_top()
ax2.set_yscale('log')
ax2.set_ylim(10e-6, 10e6)
ax2.set_yticks([10e-6, 10e-3, 10e0, 10e3, 10e6])
ax2.set_yticklabels(['10e-6', '10e-3', '10e0', '10e3', '10e6'], fontsize=11)
ax2.set_xticks([0.018, 0.18, 0.342, 0.504, 0.666])
ax2.set_xticklabels(["35,000", "10,000", "6,000", "4,000", "3,000"])
ax2.yaxis.set_label_position('right')
ax2.xaxis.set_label_position('top')
ax2.set_xlabel(u"Temp�rature Effective, K")
ax2.set_ylabel(u"Luminosit�, Soleil=1")
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
# Mise en couleurs des donn�es
#----------------------------------------------------------------------------
#center_color = ['r', 'g', 'b', 'm', 'y', 'k', 'c', 'w']
#for i in range(0, n_clusters, 1):
#    ax1.scatter([cluster_means[i][0]], [cluster_means[i][1]], s=180,
#                c=center_color[i], marker='d')
#    indices = where(cluster_group == i + 1)
#    datax, datay = data[:, 0], data[:, 1]
#    tempx, tempy = datax[indices], datay[indices]
#    ax1.scatter(tempx, tempy, s=30, c=center_color[i], marker='o', alpha=0.5)
ax1.scatter(data[:,0], data[:,1], s=30, c='k', marker='o', alpha=0.5)
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
# Trac� des annotations
#----------------------------------------------------------------------------
font = {'fontname'   : 'Courier',
        'color'      : 'r',
        'fontweight' : 'bold',
        'fontsize'   : 9}

soleilfont = {'fontname'   : 'Courier',
              'color'      : 'r',
              'fontweight' : 'bold',
              'fontsize'   : 12}

wd = ax1.text(0.6, 16, 'Naines\nBlanches', font, color='k', alpha=1)
rg = ax1.text(1.9,1,u'G�antes\nRouges',font,color='k', alpha=1)
bg = ax1.text(-0.3,-7.5,u'G�antes\nBleues',font,color='k', alpha=1)
ms = ax1.text(-0.2,3.55,u'S�quence\nPrincipale',font,color='k', alpha=1)
soleil = ax1.text(0.35, 7.,'Soleil',soleilfont,color='k', alpha=1)
soleilX = [0.6]
soleilY = [4.7]
sequencePrincipaleX = [-0.4, 0.0, 0.4, 0.8, 1.2, 1.6]
sequencePrincipaleY = [-5., 2.5, 4.75, 7.5, 9., 13.5]
soleilScatter = ax1.scatter(soleilX, soleilY, s=65, c='y', marker='o',
                            alpha=1)
sequence = ax1.plot(sequencePrincipaleX, sequencePrincipaleY, 'k')
ax1.set_ylim([20,-10])
ax1.set_xlim([-0.5,2.5])
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
# Affichage
#----------------------------------------------------------------------------
plt.show()
