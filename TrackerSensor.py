from machine import ADC

class TrackerSensor():
    # 0/IR2 - 2/IR4
    pins = []
    ir = []
    
    # Calibration / Norm paramemeters
    irmin = 65535
    irmax = 0
    
    def __init__(self, ArrayPins):
        self.pins = ArrayPins
        print(self.pins)
        for i in range(len(self.pins)):
            self.ir.append(ADC(self.pins[i]))
            print(i)
    
    def calibrate(self):
        for i in range(len(self.ir)):
            ir_val = self.ir[i].read_u16()
            if (ir_val < self.irmin):
                self.irmin = ir_val
            elif (ir_val > self.irmax):
                self.irmax = ir_val
    
    def read_calibrated(self):
        results = []
        for i in range(len(self.ir)):
            ir_cal = (self.ir[i].read_u16() - self.irmin) * 1000 / (self.irmax - self.irmin)
            results.append(ir_cal)
    
        return results

    def read_line(self):
        ir_norm = self.read_calibrated()
        
        y = d = 0
        for i in range(len(ir_norm)):
            y += (i * 1000) * ir_norm[i]
            d += ir_norm[i]
        return y / d
    
    def read_stopped(self):
        ir_norm = self.read_calibrated()
        for i in ir_norm:
            if i > 500:
                return False
        return True
