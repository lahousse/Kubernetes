# Kubernetes
Kubernetes locally on RPI cluster

What is Kubernetes?

Kubernetes is an open-source container-orchestration system for automating computer application deployment, scaling, and management. It was originally designed by Google and is now maintained by the Cloud Native Computing Foundation.
To explain it in simple words: Kubernetes allows you to create a kind of “container” in which your program can run completely isolated and run without interference of other programs which makes it very fast. You could run GTA in a container, Minecraft in another and Call of Duty in another. But what if you create 10 containers for GTA, 10 for Minecraft and 10 for Call of Duty? Well you guessed it, it runs even faster. 
Kubernetes was originally created for the cloud and this version is called K8S. We will use K3S, a lighter and quicker version of Kubernetes which can be installed locally on our RPI.
You have one master/pilot (Kubernetes uses terms of planes) the rest are nodes (other RPI’s). The master gives out the instructions, let’s the nodes do the work and when done he collects the results. For this project I will be using four RPI’s but it can be done with one RPI. Yes, I said that you need one RPI to be the master and the other ones to be the nodes so logically you would at least need two but you can let it be the master of its own node. 

In this project you will learn to:
-	Setup a Raspberry Pi (RPI) headless
-	Install Kubernetes locally (K3S)
-	Create K3S cluster
- create/read a yaml file for the manifest
- wrap files in docker
- run a program in Kubernetes
- extract results

Requirements:
-	Min one RPI
-	Power cable 
-	eth cable + port
-	Ssd
-	Pc
-	Access to wifi



Let’s get started!

setup

1.	Download RPI imager (https://www.raspberrypi.com/software/)
ssd > pc > open RPI imager > chose os > RPI os other > lite > choose storage(your ssd) > write 

ssd > RPI > connect the power > let it boot up, give it a few minutes

ssd > pc > go to your ssd > boot file should be on the ssd (if not you didn’t let the RPI boot up properly so try this again) > open “cmdline.txt” > 
Print the text between the “ after the text line and don't forget to adjust the code. By typing “ipconfig/all” in your cmd you can find all the info (if you are connected to your wifi) to fill the gaps. Very important: wifi on your laptop needs to be the same as your eth cables.

“
cgroup_memory=1 cgroup_enable=memory ip=your ip address of an unused subnet::default gateway:subnet mask:chose a name, has to be different for every node/master:eth0:off
”

save file > open “config.txt” > print “arm_64bit=1” on the bottom of the file >
Open powershell > type the letter your boot assigns this will probably be a I or a D and “:” > print “new-item ssh” >
Ssd > RPI > eth cable > let it boot up > open cmd on your pc > ping the ip of RPI. “ssh pi@your master ip” to enter RPI from your pc > “sudo su -” to get in the root > “sudo iptables -F” > “reboot” >
“ssh pi@your master ip” > “sudo su –“ > now we will download K3S 
“curl -sfl https://get.k3s.io|K3S_KUBECONFIG_MODE=”644” sh -s –“ > “kubectl get nodes” to see the nodes  

If you want to add more RPI’s (worker nodes) follow this next step 
“cat/var/lib/rancher/k3s/server/node-token” > a token will pop up, copy this > New cmd > “ssh pi@your node ip” > “sudo su –“ >
 “
curl -sfl https://get.k3s.io|K3S_TOKEN=”your token you copied” K3S_URL=https://your master ip:6443 K3S_NODE_NAME=”give it a name” sh -
“

