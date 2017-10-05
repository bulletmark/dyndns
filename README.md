### DynDNS

[DynDNS][REPO] is a small client to update your dynamic DNS hosting
service. Just configure your update URL in the configuration file. I run
this on Arch Linux on an Raspberry Pi and use it with
[afraid.org][AFRAID] but it supports any dynamic DNS service which uses
a simple URL update mechanism.

Why another dynamic DNS client? I wanted something simple, lightweight,
and generic to use with any dynamic DNS service. I didn't find anything
I liked so wrote my own.

The latest version and documentation is available at
http://github.com/bulletmark/dyndns.

### INSTALLATION

Requires `python` 3.5+ and a modern `systemd` environment.

    python3 -m venv env
    env/bin/pip install -U pip
    env/bin/pip install -r requirements.txt
    cp dyndns.conf ~/.config
    vim ~/.config/dyndns.conf # Edit appropriately, e.g for your API key.

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

<!-- vim: se ai syn=markdown: -->
