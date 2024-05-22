import psutil
from pyinjector import inject

def main():
    print("Waiting for program...")
    # Iterate over all running process
    while True:
        for proc in psutil.process_iter():
            try:
                if proc.name() == "StarRail.exe":
                    print("Found")
                    print(proc.name(), proc.pid)
                    inject(proc.pid, "d3d11.dll")
                    return
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

if __name__ == "__main__":
    main()
