#!/bin/bash

export USER_PASS="SENHA_SUDO"
sshpass -p $USER_PASS ssh hzanin@10.11.16.116 "sync ; echo -e $USER_PASS | sudo -S docker stop postgres ; echo -e $USER_PASS | sudo -S sh -c 'echo 3 > /proc/sys/vm/drop_caches' echo -e $USER_PASS | sudo -S docker start postgres"
