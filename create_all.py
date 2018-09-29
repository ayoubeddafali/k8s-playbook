import digitalocean
import os, sys, subprocess, random

TOKEN = os.getenv("DO_TOKEN")
manager = digitalocean.Manager(token=TOKEN)

keys = manager.get_all_sshkeys()

droplets = ["k8sMaster", "k8sSlave1", "k8sSlave2"]

for droplet in droplets :
    d = digitalocean.Droplet(token=TOKEN,
        name="gen-temp-{}".format(droplet),
        region='sfo2', # Amster
        image='centos-7-x64', # Ubuntu 14.04 x640
        size_slug='s-2vcpu-2gb',  # 512MB
        ssh_keys=keys, #Automatic conversion
        backups=False)

    d.create()

f =  open("hosts", "w")
my_droplets = manager.get_all_droplets()
print("=> {} machines has been created : ".format(len(my_droplets)))
k8s_slaves = []
seen = []

while len(seen) != len(my_droplets):
    for droplet in my_droplets:
        if droplet.name in seen:
            continue
        else :
            if droplet.status == "active":
                seen.append(droplet.name)
                print(" - {}".format(droplet.name))
                if "Slave" in droplet.name:
                    k8s_slaves.append(droplet.ip_address)
                elif "Master" in droplet.name:
                    f.write("\n[master]\n{}\n".format(droplet.ip_address))
    my_droplets = manager.get_all_droplets()

f.write("\n[workers]\n")

for ip in k8s_slaves:
    f.write("{}\n".format(ip))

f.close()
