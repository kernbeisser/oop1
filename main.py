from employee import Manager, Attendant, Cook, Mechanic
from reporting import AccountingReport, StaffingReport, ScheduleReport
from shift import MorningShift, AfternoonShift, NightShift

employees = [Manager("Vera", "Schmidt",2000, MorningShift()),
Attendant("Chuck", "Norris",1800, MorningShift()),
Attendant("Samantha", "Carrington",1800, AfternoonShift()),
Cook("Roberto", "Jacketti",2100, MorningShift()),
Mechanic("Dave", "Dreißig",2200, MorningShift()),
Mechanic("Tina", "River",2300, AfternoonShift()),
Mechanic("Ringo", "Rama",1900, AfternoonShift()),
Mechanic("Chuck", "Raney",2300, NightShift())]

reports = []
reports.append(AccountingReport(emp_list=employees))
reports.append(StaffingReport(emp_list=employees))
reports.append(ScheduleReport(emp_list=employees))

for report in reports:
    report.print_report()

