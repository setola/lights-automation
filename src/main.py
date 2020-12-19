from time import sleep

from pymodbus.client.sync import ModbusTcpClient

inputState = [False] * 32
outputState = [False] * 32

clientDI_1 = ModbusTcpClient('192.168.82.77')
clientDO_1 = ModbusTcpClient('192.168.82.76')

clientDO_1.write_coils(1, inputState)

while not sleep(0.05):
    try:
        result = clientDI_1.read_discrete_inputs(1, 32)
        activeButtonsIndexes = [i for i, x in enumerate(result.bits) if x]
        for index in activeButtonsIndexes:
            if inputState[index] != result.bits[index]:
                print(f"Button pressed {index}")
                outputState[index] = not outputState[index]
        inputState = result.bits
        clientDO_1.write_coils(1, outputState)
        clientDI_1.close()
        clientDO_1.close()
    except:
        print("error, resetting")
