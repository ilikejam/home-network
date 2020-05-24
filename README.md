# home-network

Ansible, docker, etc for personal services

## Requirements

You'll need:
* Ansible 2.X
* ansible-playbook
* jq

## Secrets

DigitalOcean API token should be exported as `$DO_API_TOKEN`
Github webhook secret should be exported as `$GH_WEBHOOK_SECRET`
Github deploy priv key should be at `~/.ssh/id_github_deploy`

## Instances

### Wiki

Create a droplet with:
`$ createdroplet -t permanent -i centos-7-x64 -r lon1 -n wiki-lon1`

Assign the floating IP that matches the docs DNS name in the DO UI, then assign the wiki tag:
`$ droplet -a <dropletID> -t wiki`

Run ansible again:
`$ cd <ansible> && ansible-playbook -i digital_ocean.py -l <floatingIP> site.yml`
