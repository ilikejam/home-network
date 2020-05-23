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
