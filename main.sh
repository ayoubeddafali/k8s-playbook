python create_all.py

export ANSIBLE_HOST_KEY_CHECKING=False
export ANSIBLE_SSH_RETRIES=5

ansible-playbook -i hosts kube-dependencies.yml
ansible-playbook -i hosts master.yml
ansible-playbook -i hosts workers.yml

