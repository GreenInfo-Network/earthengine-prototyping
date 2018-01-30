### Description

Some early R&D into using Google Earth Engine to do some calculations and work. The ultimate idea would be to replicate something on the order of www.BayAreaGreenPrint.org which handles 20 polygon layers plus a 30-variable "fishnet" point file.


### The Server

For this early R&D, I created a specific Amazon EC2 instance.

The Amazon EC2 instance being used is in the **us-west-2 zone**, and is named "GEE early R&D"

Its IP address is 35.164.16.236

This is intentionally very small and edging into the free tier: a *t2.micro with the default 8 GB disk space*.

OS is Amazon Linux AMI

The chosen security (firewall) configuration is the Default Security Group, allowing SSH from the GIN VPN only. The SSH username is **ec2-user** and the SSH key is the default "GreenInfo SSH key for 2017 Templated Instances"


### GEE API Library & Docs

Noted in the GEE API Github: **The API is in active development, and users should expect the API to change. When (not if) API changes occur, applications that use the API will likely need to be updated.**

Noted: Python for 64-bit Windows doesn't work well, and it is recommended not to use it https://groups.google.com/forum/#!msg/google-earth-engine-developers/iq8EPUVI1e8/i3Zf01nMVywJ

https://developers.google.com/earth-engine/

https://github.com/google/earthengine-api

I went with the manual installation here, as opposed to one of the Docker prospects. This was because I don't know Docker, and also to get more at the nuts-and-bolts for the inevitable need for flexibility and operating on disparate systems where Docker may not be an option.
* The manual installation went fine following the directions here: https://developers.google.com/earth-engine/python_install_manual
* Don't forget the section on "Setting Up Authentication Credentials"
  * Note that the API instructions are incorrect on this one, and instead you will run `earthengine authenticate` from CLI.
  * The new process has you visit a website to issue a token. For a real project, this token would be appropriate to log in P drive or 1Password.
  * As noted in the docs, this will write a file `$HOME/.config/earthengine/credentials`

