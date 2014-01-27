iw_parse
========

Parse the output of iwlist scan to get the Name, Address, Quality, Channel, Encryption Type of all networks broadcasting within your Wireless NIC's reach.

Usage
-----

```bash
iwlist <INTERFACE_NAME> scan | ./iw_parse
```

Replace `<INTERFACE_NAME>` with the system name for your wireless NIC. It is usually something like `wlan0`. The command `iwconfig` will list all of your network interfaces.

Example:

```bash
iwlist wlan0 scan | ./iw_parse
```

Acknowledgements
----------------

* The vast majority of iw_parse was written by Hugo Chargois.

License
-------

iw_parse is free--as in BSD. Hack your heart out, hackers.
