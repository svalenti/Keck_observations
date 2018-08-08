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

from astroplan import download_IERS_A
download_IERS_A()
    
observatory = 'keck'
dates = ['2018-08-11']

#Add objects not in table (e.g. ones that you don't want to calculate the age and current
#magnitude of
sn2018cow = choose_targets.target('2018cow', dates[0], ra='16:16:00.22 ', dec='+22:16:04.8') #day 50; 19.5 Vmag
sn2017ivv = choose_targets.target('2017ivv', dates[0], ra='20:28:49.84', dec='-04:22:57.3') #II; day 150; 19.5 Vmag
sn2016iks = choose_targets.target('2016iks', dates[0], ra='23:07:21.47 ', dec='+02:54:28.3') #Ia; day 700; 21 V mag
sn2013fs = choose_targets.target('2013fg', dates[0], ra='23:19:44.67', dec='+10:11:04.49') #IIn
sn2012ec = choose_targets.target('2012ec', dates[0], ra='02:45:59.88', dec='-07:34:27.01') #IIP
sn2017gmr = choose_targets.target('2017gmr', dates[0], ra='02:35:30.15', dec='-09:21:15.0')
sn2017hpi = choose_targets.target('2017hpi', dates[0], ra='08:15:43.47', dec='-28:51:19.8')
sn2017fbu = choose_targets.target('2017fbu', dates[0], ra='02:11:06.98', dec='+03:50:36.4')
sn2017gaw = choose_targets.target('2017gaw', dates[0], ra='01:15:35.23', dec='-00:50:40.3')
sn2018dfy = choose_targets.target('2018dfy', dates[0], ra='21:43:32.91 ', dec='+43:32:58.2') #day 25, 18.5mag??? could be brighter

other_objects = [sn2018cow,sn2017ivv,sn2016iks,sn2013fs ,sn2012ec ,sn2017gmr,sn2017hpi,sn2017fbu,sn2017gaw,sn2018dfy]




for date in dates:
    ofile = open('{}_{}_targets.txt'.format(date, observatory), 'w')
    ofile = choose_targets.write_header(ofile, date, observatory)
    fig = plt.figure(figsize=(11, 8.5))
    ax = fig.add_axes([0.125,0.175,0.6, 0.75])
    ax.axes.set_prop_cycle(choose_targets.cycler_ls)
    label = []
    for sn in other_objects:
        sn.date = Time(date)
        sn, ax = choose_targets.check_visibility(sn, observatory, ax, fmt='-')
        if sn.plotted is True:
            label.append(sn.name)
    ofile.close()
    ax = choose_targets.add_airmass_axis(ax)
    ax = choose_targets.add_twilight(ax, observatory, date)
    label.append('12deg twilight')
    leg = ax.legend(label, bbox_to_anchor=(1.10, 1), fontsize='x-small')
    leg.draggable()
    ax.grid()
    ax.set_title('{} {}'.format(date, observatory))
    plt.savefig('{}_{}_viable_objects.pdf'.format(date, observatory), orientation='landscape')
    #plt.close()