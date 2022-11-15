import pip
pip.main(["install", "openpyxl"])
pip.main(["install", "pandas"])
import pandas as pn
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

df_licenciamiento_institucional = pd.read_excel(r'https://www.datosabiertos.gob.pe/sites/default/files/Licenciamiento%20Institucional_7.csv', header= 0) 
