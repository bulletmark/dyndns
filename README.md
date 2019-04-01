### DynDNS

[DynDNS][REPO] is a small Linux client to update your dynamic DNS
hosting service. Just configure your update URL in the configuration
file. I run this on Arch Linux on an Raspberry Pi and use it with
[duckdns.org][DUCK] but it supports any dynamic DNS service which uses
a simple URL update mechanism.

Why another dynamic DNS client? I wanted a simple, lightweight app
managed by systemd and generic to use with any dynamic DNS service and
IP address servers. I didn't find anything I liked so wrote my own.

The latest version and documentation is available at
http://github.com/bulletmark/dyndns.

### OPERATION

This client runs every `poll_period` (default 5 mins) and determines
your current public IP address from a list of configured address
servers. If this address differs from the last address then an update is
sent to the configured dynamic DNS URL. Every `force_period` (default 2
hours), an update is sent regardless. The last address received is
stored on change only (and with the URL it represents) and always cached
to disk so it lasts through reboots. The service URL to update, the time
periods, and the list of address servers can be changed in the
configuration file.

### INSTALLATION

Requires `python` 3.5+ and a modern Linux `systemd` environment.
Must install the packages `python3-ruamel-yaml` and `python3-requests`.

    git clone https://github.com/bulletmark/dyndns.git
    cd dyndns
    mkdir -p ~/.config
    cp dyndns.conf ~/.config
    vim ~/.config/dyndns.conf # Edit appropriately, e.g. add your API key.

    sudo cp dyndns.service /etc/systemd/system
    sudo vim /etc/systemd/system/dyndns.service # Edit #TEMPLATE# values.

### STARTING, STOPPING, AND STATUS

To enable starting at boot and also start immediately:

    sudo systemctl enable dyndns
    sudo systemctl start dyndns

To stop immediately and also disable starting at boot:

    sudo systemctl stop dyndns
    sudo systemctl disable dyndns

Show status:

    systemctl status dyndns

Show log:

    journalctl -u dyndns

### UPGRADE

`cd` to source dir, as above. Then update the source:

    git pull

Update `~/.config/dyndns.conf` and `/etc/systemd/system/dyndns.service` if
necessary. Then restart the service.

    sudo systemctl restart dyndns

### LICENSE

Copyright (C) 2017 Mark Blakeney. This program is distributed under the
terms of the GNU General Public License.
This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or any later
version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License at <http://www.gnu.org/licenses/> for more details.

[REPO]: https://github.com/bulletmark/dyndns/
[AFRAID]: https://freedns.afraid.org/dynamic/v2/
[DUCK]: https://duckdns.org/

<!-- vim: se ai syn=markdown: -->
