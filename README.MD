# Valve Controller Flask Template
The Valve Controller Flask Template contains the framework for quickly building a [full stack](https://www.w3schools.com/whatis/whatis_fullstack.asp) application using your choice of database (PostgreSQL, MySQL, SQLite3) along with secure login and Bootstrap (5) HTML components.

The instructions below describe how to commission a (Raspberry Pi) microcomputer system running (Raspberry Pi OS) Linux with the
[Flask](https://flask.palletsprojects.com/en/2.2.x/) micro-framework that supports a full stack embedded application. **They assume that you are starting from scratch.**

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
8. Select ***WRITE***
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
1. Select ***Localisation Options***
2. Select ***WLAN Country***
3. Select your country
4. Select ***Finish***

Replace the contents of the wpa_supplicant.conf file with the following.

`$sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
        ssid="yourwlanid"
        scan_ssid=1
        psk="yourwlanpassphrase"
        key_mgmt=WPA-PSK
}
```

## Configure SSH
https://garywoodfine.com/setting-up-ssh-keys-for-github-access/

### Enable SSH on Raspberry Pi
`$sudo raspi-config`
1. Select ***Interface Options***
2. Select ***SSH***
3. Select ***Yes***
4. Select ***Ok***
5. Select ***Finish***

### Generate SSH Public/Private Key
`$cd ~`

`$mkdir .ssh`

`$chmod 0700 ~/.ssh`

`$cd ~/.ssh`

`$ssh-keygen -t rsa`

1. Hit enter to accept default settings for all prompts

`$mv id_rsa.pub authorized_keys`

`$ssh -T git@github.com`
1. Answer ***yes*** to question about wanting to connect
2. This should add GitHub to ~/.ssh/known_hosts file

### Add SSH Key to PuTTY Configuration
Install PuTTY from https://www.putty.org/

Follow the instructions at the link below to add your **private key** generated above (id_rsa) to use in your PuTTY session.

https://docs.oracle.com/en/cloud/paas/goldengate-cloud/tutorial-change-private-key-format/
1. Launch the PuTYTGen program
2. Under ***Parameters***, select ***RSA*** and use 2048 for bits in generated key
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
3. Select ***Settings
4. Select ***SSH and GPG keys***
5. Select ***New SSH key***
6. Fill in the fields regarding the key (use id_rsa.pub key from previous step)
7. Select ***Add SSH key***

## Install Python and Other Tools
`$sudo apt-get -y install python3 python3-venv python3-dev`

`$sudo apt-get -y install supervisor nginx git`

`$sudo pip install --upgrade pip`

## Setup git Repository
`$mkdir vctrl`

`$cd ~/vctrl`

`$git init`

`$git clone https://github.com/lairdrt/vctrl.git`

## Install Rust Compiler for Python Cryptography Package
The Python Cryptography package is required for the pyOpenSSL package which is required for OAuth authorization.
OAuth is used to log into the Flask application via third-party providers such as GitHub. The Python Cryptography package is built 
using the Rust compiler.

`$sudo curl https://sh.rustup.rs -sSf | sh`
1. Select option 1 (the default)

`$source $HOME/.cargo/env`

When the Python packages are installed below, the Cryptography package will be built using the Rust compiler.
On a Raspberry Pi Zero W (not Zero 2 W), the build can take up to four (4) hours!

You can uninstall the Rust compiler **AFTER** the Python packages are installed below by issuing hte command:

`$sudo rustup self uninstall`

## Create Virtual Environment and Install Python Packages
`$cd ~/vctrl`

`$python3 -m venv venv`

`$source venv/bin/activate`

`$pip install -r requirements.txt`

## Install MySQL DB (Maria DB)
`$sudo apt install mariadb-server`

`$sudo mysql_secure_installation`
1. Answer ***N*** to prompts regarding setting/changing root password
2. Answer ***Y*** to all other prompts

## Make Database
`$sudo mysql -u root -p`

`>CREATE DATABASE database_name;`

`>CREATE USER 'database_user_name'@'localhost' IDENTIFIED BY 'database_user_password';`

`>GRANT ALL PRIVILEGES ON database_name.* TO 'database_user_name'@'localhost';`

`>ALTER USER database_user_name@localhost IDENTIFIED BY 'database_user_password'; # as necessary`

`>FLUSH PRIVILEGES;`

## Configure Nginx and Supervisor
`$sudo cp ~/vctrl/deployment/nginx/vctrl /etc/nginx/sites-enabled/vctrl`

`$sudo cp ~/vctrl/deployment/supervisor/vctrl.conf /etc/supervisor/conf.d/vctrl.conf`

## Create Your Own SSL Certificate Authority for Serving HTTPS from Your Private Network

https://deliciousbrains.com/ssl-certificate-authority-for-local-https-development/

Steps involved and what they produce:
1. Generate a private key for the root certificate -> myCA.key
2. Generate the root certificate using the private key -> myCA.pem
3. Install the root certificate on Windows 10 -> myCA.pem added to Trusted Root Certification Authorities
4. Generate a private key for the dev site certificate -> vctrl.key
5. Generate a certificate signing request for the dev site certificate -> vctrl.csr
6. Create an X509 V3 certificate extension config file to set the Subject Alternative Names (SAN) for the dev site certificate
7. Generate the dev site certificate using the CSR, the CA private key, the CA certificate, and the config file -> vctrl.crt
8. Configure dev site web server to use private key and signed certificate

File summary:
- myCA.key : CA root certificate private key (requires passphrase)
- myCA.pem : Signed CA root certificate (installed on machines wanting access to your dev site over HTTPS)
- vctrl.key : Dev site certificate private key
- vctrl.csr : Dev site certificate signing request
- vctrl.crt : Signed dev site certificate (installed on dev site HTTPS web server)

### 1. Generate a private key for the root certificate:

`$sudo openssl genrsa -des3 -out myCA.key 2048`

`Enter pass phrase for myCA.key:yourpassphrase`

RESULTS IN: myCA.key

### 2. Generate the root certificate using the private key:

`$sudo openssl req -x509 -new -nodes -key myCA.key -sha256 -days 1825 -out myCA.pem`
```
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:California
Locality Name (eg, city) []:San Diego
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Same Day Rules
Organizational Unit Name (eg, section) []:Development
Common Name (e.g. server FQDN or YOUR name) []:Same Day Rules Root
Email Address []:support@samedayrules.com
```
RESULTS IN: myCA.pem

### 3. Install the root certificate on Windows 10:

Open the Microsoft Management Console by using the Windows + R keyboard combination, typing ***mmc*** and clicking Open
1. Go to File > Add/Remove Snap-in
2. Click Certificates and Add
3. Select Computer Account and click Next
4. Select Local Computer then click Finish
5. Click OK to go back to the MMC window
6. Double-click Certificates (local computer) to expand the view
7. Select Trusted Root Certification Authorities, right-click on Certificates in the middle column under “Object Type” and select All Tasks then Import
8. Click Next then Browse. Change the certificate extension dropdown next to the filename field to All Files (*.*) and locate the myCA.pem file, click Open, then Next
9. Select Place all certificates in the following store > Trusted Root Certification Authorities (the default store)
10. Click Next then click Finish to complete the wizard

Verify that the CA certificate is listed under Trusted Root Certification Authorities > Certificates.

### 4. Generate a private key for the dev site certificate:

`$sudo openssl genrsa -out vctrl.key 2048`

RESULTS IN: vctrl.key

### 5. Generate a certificate signing request for the dev site certificate:

`$sudo openssl req -new -key vctrl.key -out vctrl.csr`
```
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:California
Locality Name (eg, city) []:San Diego
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Same Day Rules
Organizational Unit Name (eg, section) []:Development
Common Name (e.g. server FQDN or YOUR name) []:Same Day Rules Cert
Email Address []:support@samedayrules.com

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:yourpassword
An optional company name []:Same Day Rules
```
RESULTS IN: vctrl.csr

### 6. Create an X509 V3 certificate extension config file to set the Subject Alternative Names (SAN) for the dev site certificate:

We’ll be running openssl x509 because the x509 command allows us to edit certificate trust settings.

`$ sudo nano vctrl.ext`
```
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = localhost
DNS.2 = samedayrules.com
DNS.3 = *.samedayrules.com
IP.1 = 127.0.0.1
IP.2 = 192.168.1.45
```
RESULTS IN: vctrl.ext

### 7. Generate the dev site certificate using the CSR, the CA private key, the CA certificate, and the config file:

`$sudo openssl x509 -req -in vctrl.csr -CA myCA.pem -CAkey myCA.key -CAcreateserial -out vctrl.crt -days 825 -sha256 -extfile vctrl.ext`

We now have three files:
- vctrl.key (the private key)
- vctrl.csr (the certificate signing request, or csr file)
- vctrl.crt (the signed certificate).

We can configure local web servers to use HTTPS with the private key and the signed certificate.

### 8. Configure dev site web server to use private key and signed certificate

Edit the Nginx configuration file for your dev web site to use the new private key and certificate.

`$sudo nano /etc/nginx/sites-enabled/vctrl`

`ssl_certificate /home/webapp/vctrl/deployment/certs/vctrl.crt;`

`ssl_certificate_key /home/webapp/vctrl/deployment/certs/vctrl.key;`
  
  
&copy; 2020-2023 Same Day Rules
