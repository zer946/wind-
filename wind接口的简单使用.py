#!/usr/bin/env python
# coding: utf-8

# In[1]:


from WindPy import w


# In[2]:


w.start()


# In[6]:


import pandas as pd


# In[ ]:


# 一年期LPR，从2016年到2021年的数据


# In[71]:


lpr = w.edb("M0096870", "2016-01-01", "2020-12-19","Fill=Previous")


# In[72]:


df_lpr = pd.DataFrame(lpr.Data, columns=lpr.Times, index=lpr.Codes).T


# In[73]:


df_lpr.plot()


# In[ ]:


# 利用wind接口查询债券信息


# In[84]:


code=input("请输入债券wind代码")
debtinfo = w.wss(code, "sec_name,comp_name,agency_leadunderwriter,baserate",usedf=True)
debtinfo


# In[ ]:





# In[ ]:




