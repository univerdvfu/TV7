#!/usr/bin/env python3
"""Pymodbus synchronous client example.

An example of a single threaded synchronous client.

usage: simple_sync_client.py

All options must be adapted in the code
The corresponding server must be started before e.g. as:
    python3 server_sync.py
"""

# --------------------------------------------------------------------------- #
# import the various client implementations
# --------------------------------------------------------------------------- #
import pymodbus.client as ModbusClient
from pymodbus import (
    ExceptionResponse,
    FramerType,
    ModbusException,
    pymodbus_apply_logging_config,
)
import struct
from .list import data_registers


def hex_to_float(word):
    # Объединение двух 16-битных слов в одно 32-битное целое число
    combined_value = (word[1] << 16) | word[0]
    
    # Интерпретация 32-битного целого числа как float
    float_value = struct.unpack('>f', struct.pack('>I', combined_value))[0]
    
    return float_value




def run_sync_simple_client(comm, host, port, framer=FramerType.SOCKET, registers_name_kist=None):
    """Run sync client."""
    # activate debugging
    pymodbus_apply_logging_config("DEBUG")
    key_name_rigister = registers_name_kist.keys()
    
    # print("get client")
    if comm == "tcp":
        client = ModbusClient.ModbusTcpClient(
            host,
            port=port,
            framer=framer,
            # timeout=10,
            # retries=3,
            # source_address=("localhost", 0),
        )
    

    # print("connect to server")
    client.connect()
    version = client.read_holding_registers(1,1)
    if int(hex(version.registers[0])[3:], 16) >=20:
         version = "2.21"
    else:
        version = "2.19"
    
    # print("get and verify data")
    for key in key_name_rigister:
        try:
            print(data_registers[f"{key}"]["registers"][f"{version}"]+registers_name_kist[f"{key}"]*2)
            data = client.read_holding_registers(data_registers[f"{key}"]["registers"][f"{version}"]+registers_name_kist[f"{key}"]*2, data_registers[f"{key}"]["data_type"]["bit"] )
            if data_registers[f"{key}"]["data_type"]["type"] == "float":
                registers_name_kist[key] = hex_to_float(data.registers)
            elif data_registers[f"{key}"]["data_type"]["type"] == "unsigned_short":
               
                registers_name_kist[key] = f"{int(hex(data.registers[0])[3:], 16)}.{int(hex(data.registers[0])[:3], 16)}"
                
            # rr = client.read_holding_registers(7704,1)
            
            
        except ModbusException as exc:
            print(f"Received ModbusException({exc}) from library")
            client.close()
            return 0 
       

    #     print("close connection")
    client.close()
    return registers_name_kist


if __name__ == "__main__":
    run_sync_simple_client("tcp", "10.61.32.50", "502")