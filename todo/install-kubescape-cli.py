from nis import match
import subprocess

install_cmd = 'curl -s https://raw.githubusercontent.com/armosec/kubescape/master/install.sh \
     | /bin/bash'

def install():
    output = subprocess.check_output(install_cmd, shell=True)
    output = output.decode("utf-8")
    print(f'{output}\n')

install()