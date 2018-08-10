'''
Make an observing plan for August 2018 night
'''
import os
import sys
from astropy.time import Time
#Clone a local copy from: https://github.com/abostroem/observing
observing_dir = '../../../observing'
if not os.path.exists(observing_dir):
    print('Please download a local copy of the observing scripts from: https://github.com/abostroem/observing')
    sys.exit()
sys.path.append(observing_dir)
import choose_targets
import supernova_typeII_catalog
from matplotlib import pyplot as plt

from astroplan import download_IERS_A, plots
#download_IERS_A()
    
observatory = 'keck'
dates = ['2018-08-11']

#Add objects not in table (e.g. ones that you don't want to calculate the age and current
#magnitude of
sn2017ivv = choose_targets.target('2017ivv', dates[0], ra='20:28:49.84', dec='-04:22:57.3') #II; day 150; 19.5 Vmag
sn2016iks = choose_targets.target('2016iks', dates[0], ra='23:07:21.47 ', dec='+02:54:28.3') #Ia; day 700; 21 V mag
sn2013fs = choose_targets.target('2013fs', dates[0], ra='23:19:44.67', dec='+10:11:04.49') #IIn
sn2017gmr = choose_targets.target('2017gmr', dates[0], ra='02:35:30.15', dec='-09:21:15.0')
sn2017fbu = choose_targets.target('2017fbu', dates[0], ra='02:11:06.98', dec='+03:50:36.4')
sn2017gaw = choose_targets.target('2017gaw', dates[0], ra='01:15:35.23', dec='-00:50:40.3')
sn2018dfy = choose_targets.target('2018dfy', dates[0], ra='21:43:32.91 ', dec='+43:32:58.2') #day 25, 18.5mag??? could be brighter
sn2013ej = choose_targets.target('2013ej', dates[0], ra='01:36:48.16', dec='+15:45:31.0')
sn2017eaw = choose_targets.target('2017eaw', dates[0], ra='20:34:44.24', dec='+60:11:35.9')

other_objects = [sn2017ivv,sn2016iks,sn2013fs ,sn2013ej ,sn2017gmr,sn2017fbu,sn2017gaw,sn2018dfy, sn2017eaw]

sn2017iit = choose_targets.target('2017iit', dates[0], ra='05:03:20.16', dec='+18:27:03.1')
sn2018coq = choose_targets.target('2018coq', dates[0], ra='22:55:06.10', dec = '+11:15:28.3')
sn2017hcc = choose_targets.target('2017hcc', dates[0], ra='00:03:50.57', dec='-11:28:28.7')


backup_objects = [sn2017iit, sn2018coq, sn2017hcc]

my_cycler = [i for i in choose_targets.combine_cycler]
for date in dates:
    ofile = open('{}_{}_targets.txt'.format(date, observatory), 'w')
    ofile = choose_targets.write_header(ofile, date, observatory)
    fig = plt.figure(figsize=(11, 8.5))
    ax = fig.add_axes([0.125,0.175,0.6, 0.75])
    #ax.axes.set_prop_cycle(choose_targets.combine_cycler)
    label = []
    style_indx = 0
    for sn in other_objects:
        sn.date = Time(date)
        sn, ax = choose_targets.check_visibility(sn, observatory, ax, fmt=my_cycler[style_indx])
        if sn.plotted is True:
            label.append(sn.name)
            style_indx += 1
    for sn in backup_objects:
        sn.date = Time(date)
        sn, ax = choose_targets.check_visibility(sn, observatory, ax, fmt={'color':my_cycler[style_indx]['color'], 'linestyle':':'})
        if sn.plotted is True:
            label.append(sn.name)
            style_indx += 1
    ofile.close()
    ax = choose_targets.add_airmass_axis(ax)
    ax = choose_targets.add_twilight(ax, observatory, date)
    label.append('12deg twilight')
    leg = ax.legend(label, bbox_to_anchor=(1.10, 1), fontsize='x-small')
    leg.draggable()
    fig = plt.gcf()
    ax_list = fig.axes
    ax_list[0].set_zorder(100)
    ax_list[0].grid(True)
    ax.set_title('{} {}'.format(date, observatory))
    plt.savefig('{}_{}_viable_objects.pdf'.format(date, observatory), orientation='landscape')
    #plt.close()