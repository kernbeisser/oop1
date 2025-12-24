from employee import Manager, Attendant, Cook, Mechanic
from shift import MorningShift, AfternoonShift, NightShift

class EmployeeData:
    def getEmployeeData(self):
        return [Manager("Vera", "Schmidt",2000, MorningShift()),
Attendant("Chuck", "Norris",1800, MorningShift()),
Attendant("Samantha", "Carrington",1800, AfternoonShift()),
Cook("Roberto", "Jacketti",2100, MorningShift()),
Mechanic("Dave", "Dreißig",2200, MorningShift()),
Mechanic("Tina", "River",2300, AfternoonShift()),
Mechanic("Ringo", "Rama",1900, AfternoonShift()),
Mechanic("Chuck", "Raney",2300, NightShift())]
