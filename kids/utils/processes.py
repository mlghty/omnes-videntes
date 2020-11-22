import psutil
import datetime

processes = []
pids = []

today = datetime.date.today().strftime("%B %d, %Y")
hour = datetime.datetime.now().strftime("%H:%M:%S")

def get_windows_processes(windows):
    pids = [window["pid"] for window in windows]
    for process in psutil.process_iter():
        with process.oneshot():
            if process.pid in pids:
                pid = process.pid
                p = psutil.Process(pid)
                pids.append(pid)

                # app name
                name = process.name()

                # time
                now = datetime.datetime.now()
                p.create_time()
                before = datetime.datetime.fromtimestamp(p.create_time())
                time = now - before
                # change

                for proc in psutil.process_iter(['pid']):
                    PROCNAME = "explorer.exe"
                    if proc.name() == PROCNAME:
                        x = proc.info['pid']
                        y = psutil.Process(x)
                        y.create_time()
                        b = datetime.datetime.fromtimestamp(y.create_time())
                # change end
                
                # change
                        timedelta =  before - b
                # change end
                        if timedelta < datetime.timedelta(seconds=40):
                            break
                        else:
                            if name in[sublist[2] for sublist in processes]:   # if (any(pid in i for i in processes)):
                                    if time in[sublist[2] for sublist in processes]:
                                        #if time < time[1]:
                                            #time += time
                                            #processes.append([2]
                                            #)
                                        processes.append((time))
                                    break

                            else:
                                processes.append((today,hour,name,time))
    return processes

