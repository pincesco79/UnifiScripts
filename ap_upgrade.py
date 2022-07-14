from unificontrol import UnifiClient
import time
from datetime import date,time as t,datetime
date_obj=date.today()
log_file = open("ap_upgrade_"+str(date_obj)+".txt", "a")
unifi_ctrl= UnifiClient(host="XXX.YYY.WWW.ZZZ", username="username", password="password", site=site['name'])
sites = unifi_ctrl.list_sites()

for site in sites:
   unifi_ctrl= UnifiClient(host="XXX.YYY.WWW.ZZZ", username="username", password="password", site=site['name'])
   devices = unifi_ctrl.list_devices()
   #print("\n" + site['name'] + " " + site['desc'])
   log_file.write("\n" + site['desc']+"\n")
   print("\n" + site['desc']+"\n")
   for device in devices:
     upgrade_started=False
     cur_dev = unifi_ctrl.list_devices(device['mac'])
     if cur_dev[0]['state'] == 1 and  cur_dev[0]['type'] == "uap":
       #print("check next device to be upgraded")
       print(str(datetime.now())+" device: " +  str(cur_dev[0]['mac']) +" loc: " +  str(cur_dev[0]['name'])+ " Upgradable: " + str(cur_dev[0]['upgradable'])+"\n")
       log_file.write(str(datetime.now())+" device: " +  str(cur_dev[0]['mac'])+" loc: " + str(cur_dev[0]['name'])+ " Upgradable: " + str(cur_dev[0]['upgradable'])+"\n")
       #print("mac" + str(cur_dev[0]['mac']) + " state" + str(cur_dev[0]['state']))
       while 'upgradable' in cur_dev[0] and cur_dev[0]['upgradable'] == True :
         if upgrade_started == False:
           unifi_ctrl.upgrade_device(device['mac'])
           log_file.write(str(datetime.now())+" Upgrading ap device" + device['mac']+ " loc: " +  str(cur_dev[0]['name']) +"\n")
           print(str(datetime.now())+" Upgrading ap device" + device['mac']+ " loc: " +  str(cur_dev[0]['name'])+"\n")
           upgrade_started = True

         time.sleep(10)
         cur_dev = unifi_ctrl.list_devices(device['mac'])
log_file.close()
