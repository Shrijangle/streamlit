import streamlit as st
import pandas as pd
data={'Task':['Extract','Transform','load'],
    'Status':['Completed','In Progress','Pending']
    }
dt=pd.DataFrame(data)
st.write('ETL pipeline exicution status',dt)
