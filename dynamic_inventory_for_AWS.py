#!/bin/python

import boto3
import json


def get_hosts(ec2,filter):

	fltr={'Name':'tag:Ansible','Value':[filter]}
	hosts=[]
	for ip in ec2.instances.filter(Filters=[fltr]):
		print ip.private_ip_address
		hosts.append(ip.private_ip_address)
	return hosts



def main():
	ec2=boto3.resource("ec2")
	db_hosts=get_hosts(ec2,"db")
	app_hosts=get_hosts(ec2,"app")
#	print	"db: ",db_group
#	print	"app: ",app_group
	all={
		'db':{
			'hosts':db_hosts,
			'vars':{
				'group':'Database Group'
			}
		},

		'app':{
			'hosts':app_hosts,
			'vars':{
				'group':'Application Group'
			}
		}
	}



	print json.dumps(all)


if __name__=="__main__":
	main()
