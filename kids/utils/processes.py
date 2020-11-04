import psutil


def get_size(bytes):
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"

        bytes /= 1024


def get_windows_processes(windows):
    pids = [window["pid"] for window in windows]
    processes = []

    for process in psutil.process_iter():
        with process.oneshot():
            if process.pid in pids:
                pid = process.pid
                name = process.name()
                status = process.status()
                cpu_percent = process.cpu_percent()

                try:
                    memory_usage = get_size(process.memory_full_info().uss)
                #except PermissionError:  # Fix permission error on this or else it wont for protected proccesses 
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    memory_usage = "0MB"

                threads = process.num_threads()

                processes.append((
                    pid,
                    name,
                    status,
                    cpu_percent,
                    memory_usage,
                    threads
                ))

    return processes
