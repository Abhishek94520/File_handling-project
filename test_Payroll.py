import unittest , mock
import os

from numpy import delete


from Payroll import copyFile, deleteFile , findBaseSalary, createPending, getDate, processPayroll

class TestPayrollAuto(unittest.TestCase):
    def test_copyFile(self):
        src = 'account/Payroll.txt'
        dst = 'work/' + 'test_file' + '.txt'
        copyFile(src ,dst)
        self.assertTrue(os.path.exists(dst))

    def test_deleteFile(self):
        path = r'C:\Users\Abhishek\Desktop\PayrollAutomation\delete'
        file_name = 'abc.txt'
        with open(os.path.join(path, file_name), 'w') as fp:
            fp.write('Create a new text file!')

        deleteFile('./delete/abc.txt')
        self.assertFalse(os.path.exists(file_name)) 

    def test_findbasesalary(self):
        empDetails = 'demo.xlsx'
        findBaseSalary(empDetails)
        self.assertTrue(os.path.exists(empDetails))
    
    def test_createpending(self):
        file_name = "pending/pending.xlsx"
        file =  ['XD/IND/160', 'XD/IND/1071', 'XD/IND/4447']
        header = ['Employee ID']
        createPending(file)
        self.assertTrue(os.path.exists(file_name))

    def test_processPayroll(self):
          date = getDate() 
          file = 'Employee_salary_' + date + "_.xlsx"
          path = 'payroll/' + file
          dst = 'share/' + file
          print('Moving file from', path , ' to ', dst)
          toProcess= {}
          toProcess = findBaseSalary(toProcess)
          processPayroll(toProcess)
          self.assertTrue(os.path.exists(dst))


