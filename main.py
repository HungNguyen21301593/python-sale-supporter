from initdriver import SetupDriver
from target.chotot import Execute as chotot_executor
from target.chotot_hcm import Execute as chotot_hcm_executor
from target.chotot_longan import Execute as chotot_longan_executor
from target.chotot_binhduong import Execute as chotot_binhduong_executor
from target.bds123 import Execute as bds_executor
from target.alonhadat_agent_longan import Execute as alonhadat_agent_longan_executer
import os


def main():
  driver = SetupDriver()
  target = os.getenv('TARGET')
  if target == 'chotot':
      start = int(os.getenv('START_PAGE'))
      end = int(os.getenv('END_PAGE'))
      chotot_executor(driver, start, end)
      return
  if target == 'chotot_hcm':
      start = int(os.getenv('START_PAGE'))
      end = int(os.getenv('END_PAGE'))
      chotot_hcm_executor(driver, start, end)
      return
  if target == 'chotot_longan':
      start = int(os.getenv('START_PAGE'))
      end = int(os.getenv('END_PAGE'))
      chotot_longan_executor(driver, start, end)
      return
    
  if target == 'chotot_binhduong':
      start = int(os.getenv('START_PAGE'))
      end = int(os.getenv('END_PAGE'))
      chotot_binhduong_executor(driver, start, end)
      return
  if target == 'bds123':
      bds_executor(driver)
      return
  if target == 'alonhadat_longan':
      start = int(os.getenv('START_PAGE'))
      end = int(os.getenv('END_PAGE'))
      alonhadat_agent_longan_executer(driver, start, end)
      return
  alonhadat_agent_longan_executer(driver, 1, 500)
#   bds_executor(driver)


if __name__ == '__main__':
  main()
