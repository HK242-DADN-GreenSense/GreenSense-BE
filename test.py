import json
IOT_ENV = "/home/khoitrananh/working/CO3109/greensense_be/iot_env.json"

def change_mode(device: str, mode: str, threshold: int | None = None) -> None:
    with open(IOT_ENV, 'r') as fopen:
        current_modes = json.load(fopen)
        
    current_modes[device]['mode'] = mode
    
    if threshold:
        current_modes[device]['threshold'] = threshold
    else:
        current_modes[device]['threshold'] = None
        
    
    with open(IOT_ENV, 'w') as fwrite:
        json.dump(current_modes, fwrite)
        
def get_mode(device: str) -> str:
    with open(IOT_ENV, 'r') as fopen:
        current_modes = json.load(fopen)
    
    if device not in current_modes:
        return ""
    
    return current_modes[device]['mode']
        
def get_modes_info() -> dict:
    with open(IOT_ENV, 'r') as fopen:
        current_modes = json.load(fopen)

    return current_modes


def test(temperature_list, angle_list):
    print(temperature_list)
    print(angle_list)
    sorted_temperature_angle_pairs = sorted(zip(temperature_list, angle_list), key=lambda x: x[0])
    sorted_temperature_list, sorted_angle_list = zip(*sorted_temperature_angle_pairs)
    print(sorted_temperature_list)
    print(sorted_angle_list)

if __name__ == "__main__":
    test([30, 90, 50, 40], [45, 90, 75, 50])