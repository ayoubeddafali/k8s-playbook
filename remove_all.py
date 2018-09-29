import digitalocean
import os

TOKEN = os.getenv("DO_TOKEN")
manager = digitalocean.Manager(token=TOKEN)
my_droplets = manager.get_all_droplets()
for droplet in my_droplets:
    droplet.destroy()

print("=> Destroying All Droplets")

my_domains = manager.get_all_domains()
for domain in my_domains:
    domain.destroy()

print("=> Deleting All Domains")
