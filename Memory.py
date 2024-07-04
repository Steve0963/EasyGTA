import ctypes
import pymem
from psutil import process_iter, Process
import Config
from Address import Pointers
from struct import pack

PROCESS_ALL_ACCESS = 0x1F0FFF


def convert_pattern_to_regex(byte_pattern):

    pattern_parts = byte_pattern.split()
    regex_pattern = b""
    for part in pattern_parts:
        if part == "??":
            regex_pattern += b"."
        else:
            regex_pattern += bytes.fromhex(part)
    # print(regex_pattern)
    return regex_pattern


def match_pattern(process_name, module_name, byte_pattern):
    pm = pymem.Pymem(process_name)
    module = pymem.process.module_from_name(pm.process_handle, module_name)

    if not module:
        print(f"Module {module_name} not found in process {process_name}")
        return None

    regex_pattern = convert_pattern_to_regex(byte_pattern)

    addresses = pymem.pattern.pattern_scan_module(
        pm.process_handle, module, regex_pattern, return_multiple=True
    )

    if addresses:
        for address in addresses:
            print(f"Pattern found at address: 0x{address:X}")
        return addresses
    else:
        print("Pattern not found")
        return None


def get_process_id_by_name(process_name):
    for process in process_iter(["pid", "name"]):
        if process.info["name"] == process_name:
            return process.info["pid"]
    return None


def suspend_process():
    try:
        Process(Config.Process.ProcessPids.Process_GTA).suspend()
    except Exception as e:
        print(f"Error suspending process: {e}")


def resume_process():
    try:
        Process(Config.Process.ProcessPids.Process_GTA).resume()
    except Exception as e:
        print(f"Error resumeing process: {e}")


def kill_process():
    try:
        for name, pid in vars(Config.Process.ProcessPids).items():
            if name == "Process_Rockstar_Service" or name.startswith("__"):
                continue
            Process(pid).terminate()
            print(f"进程已结束")
    except Exception as ex:
        print(f"无法结束进程{ex}")


def address_by_offsets(base_address, offsets):
    PID = Config.Process.ProcessPids.Process_GTA
    process = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, PID)
    buffer_size = ctypes.sizeof(ctypes.c_uint64)
    buffer = ctypes.create_string_buffer(buffer_size)
    bytes_read = ctypes.c_uint64()
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
    pid = Config.Process.ProcessPids.Process_GTA
    process = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    buffer_size = ctypes.sizeof(ctypes.c_uint64)
    buffer = ctypes.create_string_buffer(buffer_size)
    bytes_read = ctypes.c_uint64()
    ctypes.windll.kernel32.ReadProcessMemory(
        process, ctypes.c_uint64(address), buffer, buffer_size, ctypes.byref(bytes_read)
    )
    ctypes.windll.kernel32.CloseHandle(process)
    return ctypes.cast(buffer, ctypes.POINTER(data_type)).contents.value


def write_memory(address, type, data):
    pid = Config.Process.ProcessPids.Process_GTA
    data = pack(type, data)
    process = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
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


def read(address, offsets, type):
    return read_memory(address_by_offsets(address, offsets), type)


def write(address, offsets, type, data):
    return write_memory(address_by_offsets(address, offsets), type, data)


def read_GA(index):
    return read_memory(GlobalAddress(index))


def write_GA(index, type, data):
    return write_memory(GlobalAddress(index), type, data)


def calculate_ptr(address):
    return address + read_memory(address + 3) + 7


def GlobalAddress(index):
    return read_memory(
        Pointers.Global_Ptr + 0x8 * (index >> 0x12 & 0x3F), data_type=ctypes.c_uint64
    ) + 8 * (index & 0x3FFFF)

def pid_init():
    for key, name in vars(Config.Process.ProcessNames).items():
        if key.startswith("__"):
            continue
        pid = get_process_id_by_name(name)
        setattr(Config.Process.ProcessPids, key, pid)
    pm = pymem.Pymem(Config.Process.ProcessNames.Process_GTA)
    Config.Process.Game_Base_Address = pm.base_address
    pm.close_process()

def init():
    # 初始化进程pid
    pid_init()
    # 初始化游戏Ptr
    for pointer, value in vars(Pointers).items():
        if pointer.startswith("__"):
            continue
        address = match_pattern(
            Config.Process.ProcessNames.Process_GTA,
            Config.Process.ProcessNames.Process_GTA,
            value,
        )
        setattr(Pointers, pointer, calculate_ptr(address[0]))
