### Install Suricata

Official docs: https://docs.suricata.io/en/latest/quickstart.html

```shell
sudo add-apt-repository ppa:oisf/suricata-stable
sudo apt update
sudo apt install suricata jq
```

After installing Suricata, you can check what version of Suricata you have running and with what options as well as the service state:

```shell
sudo suricata --build-info
sudo systemctl status suricata
```


### Configure Suricata


1. Figure out which network interface you want to listen on. *(Probably eth0 for this lab)*

    ```shell
    ip addr
    ```

1. In `/etc/suricata/suricata.yaml`, modify the $HOME_NET variable to only contain your VM-s public IP. Example

```shell
HOME_NET: "[xxx.xx.xxx.xxx/32]"
```

1. For this lab we would want to listen on eth0, but make sure that is already configured in the `af-packet` section.
    Also under the `af-packet` make sure that the following options are commented in and with the correct value:

    ```shell
    cluster-id: 99
    cluster-type: cluster_flow
    defrag: yes
    use-mmap: yes
    tpacket-v3: yes
    ```

### Signatures aka rules

Let's stick with the default ETOpen ruleset for now, so run `sudo suricata-update`.

### Running

Restart suricata for changes to take effect

```shell
sudo systemctl restart suricata
```


Debugging and verifying it works:

```shell
sudo tail -f /var/log/suricata/suricata.log
```

and for statistics:

```shell
sudo tail -f /var/log/suricata/stats.log
```

### Alerts

You can either view `/var/log/suricata/fast.log` or `/var/log/suricata/eve.json` for more details.
If no alerts are appearing, run the following test command, that has a signature in the ETOpen ruleset for these cases:

```
curl http://testmynids.org/uid/index.html
```

This should generate the following line in `/var/log/suricata/fast.log`:

```shell
07/26/2023-17:43:56.617890  [**] [1:2100498:7] GPL ATTACK_RESPONSE id check returned root [**] [Classification: Potentially Bad Traffic] [Priority: 2] {TCP} 18.66.122.20:80 -> 164.92.198.169:40316
```
