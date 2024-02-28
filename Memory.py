import ctypes
from psutil import process_iter, Process
from win32process import EnumProcessModules
from win32api import OpenProcess, CloseHandle
import Initial as ini
from struct import pack

PROCESS_ALL_ACCESS = 0x1F0FFF


def get_process_id_by_name(process_name):
    for process in process_iter(["pid", "name"]):
        if process.info["name"] == process_name:
            return process.info["pid"]
    return None


ini.PID = get_process_id_by_name(ini.PROCESS_NAME)


def getBaseAddress():
    try:
        process_handle = OpenProcess(PROCESS_ALL_ACCESS, False, ini.PID)
        base_address = EnumProcessModules(process_handle)[0]
        CloseHandle(process_handle)
        return base_address
    except:
        return None


GTA_ADDRESS = getBaseAddress()


def suspend():
    try:
        Process(ini.PID).suspend()
    except Exception as e:
        print(f"Error suspending process: {e}")


def resume():
    try:
        Process(ini.PID).resume()
    except Exception as e:
        print(f"Error resumeing process: {e}")


def KillProcess():
    try:
        Process(ini.PID).terminate()
        print(f"process already killed")
    except Exception as ex:
        print(f"cant stop proess {ex}")


def address_by_offsets(offsets):
    process = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, ini.PID)
    buffer_size = ctypes.sizeof(ctypes.c_uint64)
    buffer = ctypes.create_string_buffer(buffer_size)
    bytes_read = ctypes.c_uint64()
    base_address = GTA_ADDRESS
    if base_address != None:
        for offset in offsets[:-1]:
            base_address += offset
            ctypes.windll.kernel32.ReadProcessMemory(
                process,
                ctypes.c_uint64(base_address),
                buffer,
                buffer_size,
                ctypes.byref(bytes_read),
            )
            base_address = ctypes.cast(
                buffer, ctypes.POINTER(ctypes.c_uint64)
            ).contents.value
        ctypes.windll.kernel32.CloseHandle(process)
        return base_address + offsets[-1]


def read_memory(address, data_type=ctypes.c_ulong):
    # print(hex(address))
    process = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, ini.PID)
    buffer_size = ctypes.sizeof(ctypes.c_uint64)
    buffer = ctypes.create_string_buffer(buffer_size)
    bytes_read = ctypes.c_uint64()
    ctypes.windll.kernel32.ReadProcessMemory(
        process, ctypes.c_uint64(address), buffer, buffer_size, ctypes.byref(bytes_read)
    )
    ctypes.windll.kernel32.CloseHandle(process)
    return ctypes.cast(buffer, ctypes.POINTER(data_type)).contents.value


def write_memory(address, type, data):
    # print(hex(address))
    data = pack(type, data)
    process = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, ini.PID)
    if process:
        buffer_size = len(data)
        buffer = ctypes.create_string_buffer(data)

        bytes_written = ctypes.c_uint64()
        success = ctypes.windll.kernel32.WriteProcessMemory(
            process,
            ctypes.c_uint64(address),
            buffer,
            buffer_size,
            ctypes.byref(bytes_written),
        )
        ctypes.windll.kernel32.CloseHandle(process)
        return success != 0
    else:
        return False
