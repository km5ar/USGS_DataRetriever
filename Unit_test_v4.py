
"""
Created on Wed Jul 22 19:04:49 2020
5.9 Assignment: Module 5 Live Session Exercise: Testing Activity
Yibo Wang (yw9et)
Ruoyu Zhang (rz3jr)
KEYU CHEN (km5ar)
Yusheng Jiang (yj3tp)
Hyunglok Kim (hk5kp)
"""



## Unit test
import unittest
from USGS_FlowData_utils import *
import datetime
import time
import numpy as np

class USGS_DataRetriever_Test(unittest.TestCase):
    def test__init__id(self):
        data1 = USGS_Gage_DataRetriever('01654000')
        self.assertEqual(len(data1.id),8)
        
if __name__ == '__main__':
    unittest.main()         

class USGS_DataRetriever_Test(unittest.TestCase):
    def test__init__vars_info(self):
        data1 = USGS_Gage_DataRetriever('01654000')
        self.assertEqual(len(data1.vars_info['Variables'][0]['variableID']),5)
        
if __name__ == '__main__':
    unittest.main()   

class USGS_DataRetriever_Test(unittest.TestCase):
    def test__init__vars_info2(self):
        data1 = USGS_Gage_DataRetriever('01654000')
        self.assertEqual(data1.vars_info['Variables'][1]['variableName'],'Discharge(Mean)')
        
if __name__ == '__main__':
    unittest.main()   


class USGS_DataRetriever_Test(unittest.TestCase):
    def test_getStatistics(self):
        test_Stat = data1.getStatistics()
        len(test_Stat)
        self.assertEqual(type(test_Stat),dict)

if __name__ == '__main__':
    unittest.main()  
    


class USGS_DataRetriever_Test(unittest.TestCase):
    def test_getStatistics(self):
        test_Stat = data1.getStatistics()
        self.assertEqual(len(test_Stat),5)
if __name__ == '__main__':
    unittest.main()  
   


class USGS_DataRetriever_Test(unittest.TestCase):
    def test_getUnit(self):
        self.assertEqual(data1.getUnit(),'cms')

class USGS_DataRetriever_Test(unittest.TestCase):
    def test_getDailyDischarge(self):
        test5 = USGS_Gage_DataRetriever("01656120")
        df5 = test5.getDailyDischarge()
        col1 = type(datetime.datetime.strptime(df5["Date"][0],'%Y-%m-%d'))
        col2 = type(float(df5["Flow (cms)"][0]))
        col_list = [col1, col2]
        print(col_list)
        self.assertEqual(col_list, [datetime.datetime, float]) 
        
if __name__ == '__main__':
    unittest.main()  
           


class USGS_DataRetriever_Test(unittest.TestCase):
    
    def test_getVarsMetaData(self):
        test1 = USGS_Gage("01656120")
        df = test1.getVarsMetaData()
        
        col1 = type(df["Variable Name"][0])
        col2 = type(int(df["Variable ID"][0]))
        #col3 = type(df["Start Date"][0])
        #col4 = type(df["End Date"][0])
        col3 = type(datetime.datetime.strptime(df["Start Date"][0],'%Y-%m-%d'))
        col4 = type(datetime.datetime.strptime(df["End Date"][0],'%Y-%m-%d'))
        col_list = [col1, col2, col3, col4]
        print(col_list)
        self.assertEqual(col_list, [str, int, datetime.datetime, datetime.datetime]) 
        
if __name__ == '__main__':
    unittest.main()  
   

class USGS_DataRetriever_Test(unittest.TestCase):
    
    def test_getGeoMetaData(self):
        test4 = USGS_Gage_DataRetriever("01656120")
        res = test4.getGeoMetaData()
        ele1 = type(res['Coordiantes'])
        ele2 = type(res['County'])
        ele3 = type(int(res['CountyFIPS']))
        ele4 = type(int(res['Gage']))
        ele5 = type(res['State'])
        ele_type_list = [ele1, ele2, ele3, ele4, ele5]
        print(ele_type_list)
        self.assertEqual(ele_type_list, [tuple, str, int, int, str]) 
        
if __name__ == '__main__':
    unittest.main()  
   


class USGS_DataRetriever_Test(unittest.TestCase):        
    def test_findLargestEvents(self):
        test = USGS_Gage_DataRetriever("01656120")
        test_1 = test.findLargestEvents(10)
        self.assertEqual(len(test_1),10)
               
if __name__ == '__main__':
    unittest.main() 
    
    
    

