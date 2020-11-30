import psutil
import datetime
processes = []

today = datetime.date.today().strftime("%d/%m/%Y")
hour = datetime.datetime.now().strftime("%H:%M:%S")
name = ""

def chop_microseconds(delta):
    return delta - datetime.timedelta(microseconds=delta.microseconds)

def get_windows_processes(windows):
    pids = [window["pid"] for window in windows]
    for process in psutil.process_iter():
        with process.oneshot():
            if process.pid in pids:
                pid = process.pid
                p = psutil.Process(pid)
                # app name
                #name = process.name()
                for window in windows:
                    if window['pid'] == pid: #searching for movie id in the given dictionary
                        name = window['title']
                        break
                # time
                now = datetime.datetime.now()
                p.create_time()
                before = datetime.datetime.fromtimestamp(p.create_time())
                time = now - before
                ftime = chop_microseconds(time)
                
                # change
                for proc in psutil.process_iter(['pid']):
                    PROCNAME = "explorer.exe"
                    if proc.name() == PROCNAME:
                        x = proc.info['pid']
                        y = psutil.Process(x)
                        y.create_time()
                        b = datetime.datetime.fromtimestamp(y.create_time())
                        timedeltaS =  before - b # the time diffrence between explorer.exe and proccess
                        timedelta = chop_microseconds(timedeltaS)

                # change end
                
                        if timedelta < datetime.timedelta(seconds=40):  # can change the seconds depedning how fast the user logsin and opens a program
                            break                                       # else issues appear
                        if name in[sublist[2] for sublist in processes]:   
                                for i in range(len(processes)):        #from begining to end
                                    if name in processes[i][2]:       #if name is found then
                                        converted=list(processes[i])   #converted will store corrosponding tuple in list form.. as list is mutable
                                        oldtime = converted[3]
                                        if time > oldtime:
                                            diffrence = time - oldtime
                                            newtime = oldtime + diffrence
                                            converted[3]=chop_microseconds(newtime)
                                            processes[i]= tuple(converted)
                                        if time < oldtime:
                                            newtime = oldtime + time
                                            converted[3]=chop_microseconds(newtime)
                                            processes[i]= tuple(converted)
                        else:
                            processes.append((today,hour,name,ftime))
    return processes    

