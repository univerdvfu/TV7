import pymodbus.client as ModbusClient
from pymodbus import (
    ExceptionResponse,
    FramerType,
    ModbusException,
    pymodbus_apply_logging_config,
)
import struct



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
    # key_name_rigister = registers_name_kist.keys()
    
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
    version = client.read_holding_registers(7816,1)
    print(int(hex(version.registers[0])[:3], 16))
    
    print(version.registers)
    if int(hex(version.registers[0])[3:], 16) >=20:
         version = "2.21"
    else:
        version = "2.19"
    
    
       

    #     print("close connection")
    client.close()
    return registers_name_kist


if __name__ == "__main__":
    run_sync_simple_client("tcp", "10.61.32.50", "502")