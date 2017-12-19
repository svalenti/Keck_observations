'''
Make an observing plan for Dec 2017 night
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
dates = ['2017-12-18']

#Add objects not in table (e.g. ones that you don't want to calculate the age and current
#magnitude of
sn2016bkv = choose_targets.target('2016bkv', dates[0], ra='10:18:19.31', dec='+41:25:39.3')
iPTF14hls = choose_targets.target('14hls', dates[0], ra='09:20:34.30', dec='+50:41:46.8')
sn2017fzw = choose_targets.target('sn2017fzw', dates[0], ra='06:21:34.77', dec='-27:12:53.5')
sn2017fgc = choose_targets.target('sn2017fgc', dates[0], ra= '01:20:14.45',  dec='+03:24:10.1')
sn2017fbu = choose_targets.target('sn2017fbu', dates[0], ra='02:11:06.98',   dec='+03:50:36.4') 
sn2015fel = choose_targets.target('sn2015fel', dates[0], ra='03:09:12.76', dec='+27:31:16.95') 
sn2017hyy = choose_targets.target('sn2017hyy', dates[0], ra='04:33:05.96',  dec='-26:07:40.5')
other_objects = [sn2016bkv, iPTF14hls, sn2017fzw, sn2017fgc, sn2017fbu, sn2015fel, sn2017hyy]

for date in dates:
    ofile = open('{}_{}_targets.txt'.format(date, observatory), 'w')
    ofile = choose_targets.write_header(ofile, date, observatory)
    fig = plt.figure(figsize=(11, 8.5))
    ax = fig.add_axes([0.125,0.175,0.6, 0.75])
    ax.axes.set_prop_cycle(choose_targets.cycler_ls)
    label = []
    tbdata = supernova_typeII_catalog.get_cat()
    for snname in tbdata['SN']:
        sn = choose_targets.target(snname, date)
        sn = choose_targets.calc_mag_age(sn)
        sn, ax = choose_targets.check_visibility(sn, observatory, ax)
        choose_targets.write_output_table(ofile, sn)
        if sn.plotted is True:
            label.append(sn.name)
    for sn in other_objects:
        sn.date = Time(date)
        sn, ax = choose_targets.check_visibility(sn, observatory, ax, fmt=':')
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
    plt.savefig('{}_{}_visibility.pdf'.format(date, observatory), orientation='landscape')
    #plt.close()