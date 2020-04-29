# checkDNS

Vor dem Start des Containers können im Ordner `checkDNS/app/` die DNS-Namen angepasst werden. 

```bash
podman run -it --rm -v $(pwd)/app/:/usr/src/app sebastianzoll/checkdns:latest ocp4.example.com
```
