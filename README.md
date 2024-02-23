# DynDNS IPv4 and/or IPv6 Dynamic DNS Client

[DynDNS](https://github.com/bulletmark/dyndns/) is a simple Linux client
to update one or more of your dynamic DNS hosting services with the
hosts public IPv4 and/or IPv6 addresses. Just configure your own update
URLs in the configuration file and run it.

DynDNS supports dynamic DNS services which use a simple http or https
URL get update mechanism, such as:

- [Duck DNS](https://duckdns.org/)
- [Dynv6](https://dynv6.com/)
- [Dynu](https://dynu.com/)
- [FreeDNS](https://freedns.afraid.org/)

The above all offer free dynamic DNS services. There is example
configuration for each of these services in the sample
[`dyndns.toml`](https://github.com/bulletmark/dyndns/blob/master/dyndns.toml)
configuration file but note that most (free or paid) dynamic DNS
services should be supported. Extensive configuration instructions are
provided in that file.

Why another dynamic DNS client? I wanted a simple, lightweight app
managed by [systemd](https://systemd.io/), generic and flexible enough
to use with any dynamic DNS service and IP address servers. It should
work with both IPv4 and IPv6 and allow multiple URLs to be set. I didn't
find anything I liked so wrote my own.

Ensure you read the [latest
documentation](http://github.com/bulletmark/dyndns) and the instructions
in the example
[`dyndns.toml`](https://github.com/bulletmark/dyndns/blob/master/dyndns.toml)
file but then ask a question on the DynDNS [discussion
forum](https://github.com/bulletmark/dyndns/discussions) if you still
need clarification about usage or operation.

## Operation

This client runs every `poll_period` (default 10 mins) and determines
your current public IPv4 and/or IPv6 address from a list of configured
public address servers. If any IP address differs from the last address
then an update is sent to the pertinent configured dynamic DNS URLs. You
can configure "&lt;ipv4&gt;" and/or "&lt;ipv6&gt;" placemarkers in your
URLs to be substituted at runtime, and/or for those services that support
it, rely on automatic IP detection. Every `force_period` (default 24
hours), an update is sent regardless to each service. The last IP
addresses determined are stored on change only and are always cached to
disk so they are preserved through reboots. The service URLs, their
parameters to update, the time periods, and the list of IP address
servers can be changed in the configuration file.

## Configuration

You copy the sample
[`dyndns.toml`](https://github.com/bulletmark/dyndns/blob/master/dyndns.toml)
file to your `~/.config/` and then edit it for your requirements. Follow
the examples and instructions in that file.

## Installation

Requires `python` 3.7 or later and a modern Linux `systemd` environment.

1. Clone repository and create configuration:

    ```shell
    $ git clone https://github.com/bulletmark/dyndns.git
    $ cd dyndns
    $ mkdir -p ~/.config
    $ cp dyndns.toml ~/.config
    $ vim ~/.config/dyndns.toml # Add your [[urls]] entries
    ```

2. Create virtual environment (venv) and install service.

    ```shell
    $ python3 -m venv .venv
    $ .venv/bin/pip install -r requirements.txt
    $ sudo cp dyndns.service /etc/systemd/system
    $ sudoedit /etc/systemd/system/dyndns.service # Edit #TEMPLATE# values.
    ```

Note: Alternatively, to create the venv, install the requirement
packages, insert the template values, and enable + start the service you
can use my [pinstall](https://github.com/bulletmark/pinstall) tool. Just
install it and do the following in the `dyndns` directory.

```
$ pinstall venv
$ pinstall service
```

## Starting, Stopping, and Status

To enable starting at boot and also start immediately:

```shell
$ sudo systemctl enable dyndns
$ sudo systemctl start dyndns
```

To stop immediately and also disable starting at boot:

```shell
$ sudo systemctl stop dyndns
$ sudo systemctl disable dyndns
```

Show status:

```shell
$ systemctl status dyndns
```

Show log:

```shell
$ journalctl -u dyndns
```

## Upgrade

`cd` to source dir, as above. Then update the source:

```shell
$ git pull
```

Update `~/.config/dyndns.toml` and `/etc/systemd/system/dyndns.service` if
necessary. Then restart the service.

```shell
$ sudo systemctl restart dyndns
```


## Usage

Type `dyndns -h` to view the usage summary:

```
usage: dyndns [-h] [-v] [-i] [-c CONF]

Update external IP v4 and/or v6 addresses to a dynamic DNS server.

options:
  -h, --help            show this help message and exit
  -v, --verbose         verbose output
  -i, --ignore-cache    ignore cache for startup
  -c CONF, --conf CONF  configuration file, default =
                        ~/.config/dyndns.toml
```

## Summary of Version 2 Changes

- Added the ability to cater for IPv6 addresses.

- Added the ability to configure multiple dynamic DNS server URLs
  instead of just one and also the ability to substitute "&lt;ipv4&gt;"
  and "&lt;ipv6&gt;" placemarkers in the url string.

- Cater for dynamic DNS servers which return one or more text strings
  for success/failure instead of just looking at the HTML response
  status code.

- Changed from [YAML](https://yaml.org/) to [TOML](https://toml.io/en/)
  configuration file format as that is the future for Python apps given
  TOML is now included in the standard packages since Python v3.11. Note
  that `tomli` package gets installed if you are running on < 3.11. This
  change mean any previous personal configuration file must be ported to
  the new format.

- Requires minimum Python version 3.7 instead of 3.6.

## License

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

<!-- vim: se ai syn=markdown: -->
