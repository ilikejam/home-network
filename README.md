# home-network

Ansible, docker, etc for personal services

## Requirements

You'll need:
* Ansible
* ansible-playbook
* jq
* bw (bitwarden cli)

## Secrets

Secrets are in bitwarden. Do:
```
$ bw logout
$ bw login
$ bw sync
$ bw unlock
$ export BW_SESSION="xxxxx"
```
before running ansible.

## Instances

### Wiki

Create a droplet with:
`$ createdroplet -t permanent -i centos-7-x64 -r lon1 -n wiki-lon1`

Assign the floating IP that matches the docs DNS name in the DO UI, then assign the wiki tag:
`$ droplet -a <dropletID> -t wiki`

Run ansible again:
`$ cd <ansible> && ansible-playbook -i digital_ocean.py -l <floatingIP> site.yml`
