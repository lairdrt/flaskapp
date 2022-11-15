# Valve Controller Flask Template
The Valve Controller Flask Template contains the framework for quickly building a [full stack](https://www.w3schools.com/whatis/whatis_fullstack.asp) application using your choice of database (PostgreSQL, MySQL, SQLite3) along with secure login and Bootstrap (5) HTML components.

The instructions below describe how to commission a (Raspberry Pi) microcomputer system running (Raspberry Pi OS) Linux with the
[Flask](https://flask.palletsprojects.com/en/2.2.x/) micro-framework that supports a full stack embedded application. They assume that you are starting from scratch.

## Hardware
1. [Raspberry Pi (Zero 2 W)](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)
2. [Power supply](https://www.raspberrypi.com/products/micro-usb-power-supply/)
3. [MicroSD memory card](https://www.tomshardware.com/best-picks/raspberry-pi-microsd-cards)
4. [MicroSD USB card reader](https://www.amazon.com/Adapter-Standard-Connector-Smartphones-Function/dp/B01BXSKPES/ref=asc_df_B01BXSKPES)

If you have issues setting up either the wireless LAN connection or SSH, you may also need:

5. [Computer monitor](https://www.samsung.com/ca/monitors/curved/curved-monitor-27-inch-lc27f396fhnxza/)
6. [Wireless USB keyboard/mouse/dongle](https://www.amazon.com/Logitech-MK270-Wireless-Keyboard-Mouse/dp/B079JLY5M5/ref=sr_1_4)
7. [USB Micro to USB adapter](https://www.adafruit.com/product/2910)
8. [Micro-HDMI to HDMI adapter](https://www.adafruit.com/product/1358)

And you'll usually need some form of development station, assuming a laptop computer.

## Install Raspberry Pi OS on the MicroSD Card
1. Insert MicroSD card into the card reader
2. Insert the USB card reader into the laptop
3. Download and install [Raspberry Pi OS imager software](https://www.raspberrypi.com/software/) on the laptop
4. Launch the imager program
5. Choose the operating system: Raspberry Pi OS Lite 32-bit
6. Choose the storage device: MicroSD Card (you just plugged in)
7. Type CTRL + Shift + X to preconfigure the OS
- Set the locale
- Set the wireless LAN SSID and passphrase
- Set the SSH public key
8. Select 'WRITE'
9. After the write operation is complete, exit the imager program
10. Eject the USB card reader and remove the MicroSD card from the reader
11. **Make sure power is OFF** on the Raspberry Pi
12. Insert the MicroSD card into the Raspberry Pi memory card slot

## Connect Monitor/Keyboard to Raspberry Pi
Preconfiguring the Raspberry Pi **may** result in the WLAN and SSH working, but probably not. So, you'll want to connect the
monitor and keyboard to the Raspberry Pi so that you can log into the OS and make changes.

1. Connect the monitor to the Raspberry Pi using the micro-HDMI adapter and a standard HDMI cable
2. Connect the wireless USB keyboard/mouse dongle to the Raspberry Pi using the USB micro adapter
3. Apply power to the Raspberry Pi (should see green lights flash as OS is loaded)

You should be able to log into the Raspberry Pi using the default credentials: Username='pi' Password='raspberry'

## Update OS
`$sudo apt-get -y update`

`$sudo apt-get -y upgrade`
## Configure Wireless LAN
`$sudo raspi-config`
1. Select 'Localisation Options'
2. Select 'WLAN Country' (US is under 'US United States')
3. Select 'Finish'

## Configure SSH
https://garywoodfine.com/setting-up-ssh-keys-for-github-access/

### Enable SSH on Raspberry Pi
`$sudo raspi-config`
1. Select 'Interface Options'
2. Select 'SSH'
3. Select 'Yes'
4. Select 'Ok'
5. Select 'Finish'

### Generate SSH Public/Private Key
`$cd ~`

`$mkdir .ssh`

`$chmod 0700 ~/.ssh`

`$cd ~/.ssh`

`$ssh-keygen -t rsa`

1. Hit enter to accept default settings for all prompts

`$mv id_rsa.pub authorized_keys`

`$ssh -T git@github.com`
1. Answer 'yes' to question about wanting to connect
2. This should add GitHub to ~/.ssh/known_hosts file

### Add SSH Key to PuTTY Configuration
Install PuTTY from https://www.putty.org/

Follow the instructions at the link below to add your **private key** generated above (id_rsa) to use in your PuTTY session.

https://docs.oracle.com/en/cloud/paas/goldengate-cloud/tutorial-change-private-key-format/
1. Launch the PuTYTGen program
2. Under 'Parameters', select 'RSA' and use 2048 for bits in generated key
3. Load your existing private key that you generated above (and saved locally)
4. After you've loaded your existing private key, save the new key as a .ppk file that can be loaded by PuTTY
5. Exit PuttyGen
6. Launch PuTTY
7. Configure settings for a new session
8. Under Connection -> SSH -> Auth, find and open the .ppk file you just saved
9. You should now be able to connect to your Raspberry Pi using SSH

### Add SSH Key to GitHib Account
Follow the instructions at the link below to add your **public key** to GitHub so that you can manage your Raspberry Pi software.

https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
1. Log into your [GitHub](https://github.com) account
2. Select dropdown for your account
3. Select 'Settings'
4. Select 'SSH and GPG keys'
5. Select 'New SSH key'
6. Fill in the fields regarding the key (use id_rsa.pub key from previous step)
7. Select 'Add SSH key'

## Install Python
`$sudo apt-get -y install python3 python3-venv python3-dev`

`$sudo apt-get -y install supervisor nginx git`

`$sudo pip install --upgrade pip`

## Setup git Repository
`$mkdir vctrl`

`$cd ~/vctrl`

`$git init`

`$git clone https://github.com/lairdrt/vctrl.git`

## Create Virtual Environment and Install Python Packages
`$cd ~/vctrl`

`$python3 -m venv venv`

`$source venv/bin/activate`

`$pip install -r requirements.txt`

## Install MySQL DB (Maria DB)
`$sudo apt install mariadb-server`

`$sudo mysql_secure_installation`
1. Answer 'N' to prompts regarding setting/changing root password
2. Answer 'Y' to all other prompts

## Make Database
`$sudo mysql -u root -p`

`>CREATE DATABASE database_name;`

`>CREATE USER 'database_user_name'@'localhost' IDENTIFIED BY 'database_user_password';`

`>GRANT ALL PRIVILEGES ON database_name.* TO 'database_user_name'@'localhost';`

`>ALTER USER database_user_name@localhost IDENTIFIED BY 'database_user_password'; # as necessary`

`>FLUSH PRIVILEGES;`


&copy; 2020-2023 Same Day Rules
