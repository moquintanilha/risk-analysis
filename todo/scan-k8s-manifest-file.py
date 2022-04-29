from nis import match
import subprocess

scan_cmd = 'kubescape scan https://github.com/armosec/kubescape'

def scan():
    output = subprocess.check_output(scan_cmd, shell=True)
    output = output.decode("utf-8")
    print(f'{output}\n')

scan()