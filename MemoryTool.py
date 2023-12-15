import ctypes
import psutil
import win32process
import win32api
PROCESS_ALL_ACCESS = 0x1F0FFF

# 获取软件的进程ID
def get_process_id_by_name(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return process.info['pid']
    return None
GTA_PID=get_process_id_by_name("GTA5.exe")

def getBaseAddress():
    try:
        process_handle = win32api.OpenProcess(PROCESS_ALL_ACCESS,False,GTA_PID)
        base_address = win32process.EnumProcessModules(process_handle)[0]
        win32api.CloseHandle(process_handle)
        return base_address
    except:
        return None
    
GTA_ADDRESS=getBaseAddress()

def suspend():
    try:
        psutil.Process(GTA_PID).suspend()
    except Exception as e:
        print(f"Error suspending process: {e}")

def resume():
    try:
         psutil.Process(GTA_PID).resume()
    except Exception as e:
        print(f"Error resumeing process: {e}")

def endProcess():
    try:
       psutil.Process(GTA_PID).terminate()
       print(f"进程已终止")
    except Exception as ex:
            print(f"无法终止进程: {ex}")


def getValueByOffets(offsets,type):
    process=ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS,False,GTA_PID)
    buffer_size = ctypes.sizeof(ctypes.c_uint64)
    buffer = ctypes.create_string_buffer(buffer_size)
    bytes_read = ctypes.c_uint64(0)
    base_address=GTA_ADDRESS
    if base_address!=None:
        for offset in offsets:
            base_address+=offset
            ctypes.windll.kernel32.ReadProcessMemory(process, ctypes.c_uint64(base_address), buffer, buffer_size, ctypes.byref(bytes_read))
            base_address=ctypes.cast(buffer, ctypes.POINTER(ctypes.c_uint64)).contents.value
        ctypes.windll.kernel32.CloseHandle(process)
        print(ctypes.cast(buffer, ctypes.POINTER(type)).contents.value)
        return ctypes.cast(buffer, ctypes.POINTER(type)).contents.value
    