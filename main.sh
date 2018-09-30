
export ANSIBLE_HOST_KEY_CHECKING=False
export ANSIBLE_SSH_RETRIES=5

ansible-playbook -i hosts main.yml

