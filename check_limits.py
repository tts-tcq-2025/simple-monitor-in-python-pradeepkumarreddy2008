def rangeCheck(value, minv, maxv):
    minCheck = (minv == 'NA' or value >= minv)
    maxCheck = (maxv == 'NA' or value <= maxv)
    
    return (
        minCheck and
        maxCheck
    )
        
def battery_is_ok(temperature, soc, charge_rate):
    
    rangeChecksMessages = {
        "Temperature ": rangeCheck(temperature, 0, 45),
        "soc ": rangeCheck(soc, 20, 80),
        "charge_rate ": rangeCheck(charge_rate, 'NA', 0.8)
    }
    
    for label,checkResult in rangeChecksMessages.items():
        if not checkResult:
            print(label + "out of range")
    
    
    return all(rangeChecksMessages.values())

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
