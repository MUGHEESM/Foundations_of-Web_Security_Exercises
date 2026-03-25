import subprocess


def ping_host(host: str) -> str:
    cmd = f"ping -n 1 {host}"
    return subprocess.getoutput(cmd)
