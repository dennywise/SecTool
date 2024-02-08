import win32evtlog
from lxml import objectify
from datetime import datetime, timezone


def get_events(task_name, events_num):

    """
    task_name: a string from windows logs. e.g: "Microsoft-Windows-LanguagePackSetup/Operational"
    events_num: an integer for numbers of time creation. example: 10
    Output sample: 2022-03-09 08:45:29
    """
    handle = win32evtlog.EvtQuery(task_name, win32evtlog.EvtQueryReverseDirection , "*")
    event = win32evtlog.EvtNext(handle, 70, -1, 0)
    for i in event[-events_num:]:
        root = objectify.fromstring(win32evtlog.EvtRender(i, 1)) 
        paras =  root.System.TimeCreated
        d = datetime.fromisoformat(paras.attrib['SystemTime'][:23]).astimezone(timezone.utc)
        print(d.strftime('%Y-%m-%d %H:%M:%S'))

task_name = input("Enter the task name (e.g. Microsoft-Windows-ReadyBoost/Operational)")
events_num = int(input("Enter the number of logs"))
result = get_events(task_name, events_num)


if __name__ == "__main__": 
    print(result)