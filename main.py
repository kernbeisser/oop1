from reporting import AccountingReport, StaffingReport, ScheduleReport
from model import EmployeeData

employeeData = EmployeeData()
employees = employeeData.getEmployeeData()

reports = []
reports.append(AccountingReport(emp_list=employees))
reports.append(StaffingReport(emp_list=employees))
reports.append(ScheduleReport(emp_list=employees))

for report in reports:
    report.print_report()

