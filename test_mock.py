import unittest , mock
import os

from numpy import delete


from Payroll import copyFile, deleteFile , findBaseSalary,  getDate, processPayroll

class TestPayrollAuto(unittest.TestCase):
    @mock.patch('Payroll.copyFile')

    def test_copyFile(self,mock_copFile):
        src = 'account/Payroll.txt'
        dst = 'work/' + 'test_file' + '.txt'
        copyFile(src ,dst)
        self.assertTrue(os.path.exists(dst))

    @mock.patch('Payroll.deleteFile')
    def test_deleteFile(self,mock_deleteFile):
        path = r'C:\Users\Abhishek\Desktop\PayrollAutomation\delete'
        file_name = 'abc.txt'
        with open(os.path.join(path, file_name), 'w') as fp:
            fp.write('Create a new text file!')

        deleteFile('./delete/abc.txt')
        self.assertFalse(os.path.exists(file_name)) 



    @mock.patch('Payroll.processPayroll')
    def test_processPayroll(self,mock_processPayroll):
          date = getDate() 
          file = 'Employee_salary_' + date + "_.xlsx"
          path = 'payroll/' + file
          dst = 'share/' + file
          print('Moving file from', path , ' to ', dst)
          toProcess= {}
          toProcess = findBaseSalary(toProcess)
          processPayroll(toProcess)
          self.assertTrue(os.path.exists(dst))

