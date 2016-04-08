#!/usr/bin/env python
from resource_management import *
import sys, os

config = Script.get_config()

nifi_pid_dir=config['configurations']['nifi-bootstrap-env']['nifi_pid_dir']
nifi_master_pid_file=nifi_pid_dir + '/nifi-master.pid'
nifi_node_pid_file=nifi_pid_dir + '/nifi-node.pid'
