#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


#solution code here
accounts = pd.read_csv('accounts.csv')
clicks = pd.read_csv('clicks.csv')
products = pd.read_csv('products.csv')
sales_pipeline = pd.read_csv('sales_pipeline.csv')
sales_teams = pd.read_csv('sales_teams.csv')
orchestra = pd.read_json('Orchestra.json')


# 1. Display 'Manager' and 'Grand Total Sales', for sales done by the sales agents reporting these managers

# In[4]:


#solution code here
df1 = sales_pipeline[['sales_agent','close_value']].dropna()
dat1 = df1.groupby(by='sales_agent').apply(sum)[['close_value']]
dat1 = dat1.reset_index()
df1_sol = sales_teams.merge(dat1, how = 'left', left_on='sales_agent', right_on = 'sales_agent')
df1_sol = df1_sol.groupby('manager').apply(sum)[['close_value']]
df1_sol.reset_index(inplace=True)
df1_sol.rename(columns={'manager':'Manager','close_value':'Grand Total Sales'}, inplace=True)
df1_sol


#  2. Display 'Sales Agents' and 'Sales' for those sales where product sold at profit

# In[5]:


#solution code here
df2 = sales_pipeline.merge(products, how = 'left', left_on='product', right_on='product')
df2['profit'] = df2['close_value']-df2['sales_price']
df2 = df2[df2['profit']>0]
df2 = df2[['sales_agent','profit']]
df2_sol = df2.groupby('sales_agent').count().reset_index()
df2_sol.rename(columns={'profit':'Sales'}, inplace=True)
df2_sol.head()


# 3. Display 'Sales Agent' and 'Opportunity Count', for those sales agents who lost atleast two opportunties

# In[8]:


#solution code here
df5 = sales_pipeline[['sales_agent','deal_stage']]
df5 = df5[df5['deal_stage'] == 'Lost']
df5_sol = df5.groupby('sales_agent').count()
df5_sol = df5_sol[df5_sol['deal_stage']>=2].reset_index()
df5_sol.rename(columns={'deal_stage':'Opportunity Count'})
df5_sol.head()


# 4. Display 'Month of Year' vs 'Sales', for GTXBasic. NOTE: "Month of Year" means month year (eg. Jan) and "Month" means month (eg. Jan 2020, Jan 2021 etc)

# In[19]:


#solution code here
sadc=[0]*12
dct={0:"Jan",1:"Feb",2:"Mar",3:"Apr",4:"May",5:"Jun",6:"Jul",7:"Aug",8:"sep",9:"oct",10:"Nov",11:"Dec"}
for s in sales_pipeline.iterrows():
    if(s[1]['product']=="GTXBasic"):
        dt=s[1]['close_date']
        #print(type(dt),str(dt))
        if(str(dt)!="nan"):
            #print(dt[5:7])
            sadc[int(dt[5:7])-1]+=1
    
for i in range(len(sadc)):
    print(dct[i],sadc[i])


# 5. Which sales agent(s) never lost a deal. Display as a dictionary {sales agent:sales}

# In[12]:


#solution code here
df9_dict = {}
df9 = sales_pipeline[sales_pipeline['deal_stage'] == 'Won'][['sales_agent','deal_stage']]
df9 = df9.groupby('sales_agent').count().reset_index()
for i in range(len(df9)):
  df9_dict[df9['sales_agent'].iloc[i]] = df9['deal_stage'].iloc[i]
df9_dict


# Refer & Use Orchestra.json to answer problem 6-9 below

# 6. Display the instrument played by Lehmann Caroline

# In[14]:


for k in orchestra['programs']:
  for l in k['works']:
    if(len(l['soloists'])!=0):
      for m in l['soloists']:
        if(m['soloistName']=='Lehmann, Caroline'):
          print(m['soloistName'] +' plays ' + m['soloistInstrument'])
          break
        else:
          continue
        break
      else:
        continue
      break
    else:
        continue
    break
  else:
    continue
  break  


# 7. Display all vocalists

# In[15]:


#solution code here
vocc=set()
for prog in orchestra['programs']:
     for wor in prog['works']:
            #print("",end=".")
            for sol in wor["soloists"]:
                #print(sol["soloistInstrument"])
                if(sol["soloistInstrument"]=="Vocalist"):
                    #print(sol['soloistName'])
                    vocc.add(sol['soloistName'])
for i in vocc:
    print(i)


# 8. Display orchestra played under program id 2561

# In[16]:


#solution code here
for prog in orchestra['programs']:
    if(prog['programID']=="2561"):
        print(prog['orchestra'])


# Refer & Use Orchestra.xml to answer problem 9-10 below

# 9. Display locations used for event at time 8:15 PM

# In[17]:


#solution code here
import xml.etree.ElementTree as ET
vocc=set()
c=0
tree = ET.parse('Orchestra.xml')
root = tree.getroot()
for child in root[:]: 
    c=c+1 
    #print(child.tag, child.attrib)
    for ch2 in child:
    
        #print(ch2.tag, ch2.attrib)
        if(ch2.tag=="concertInfo"):
            for ch3 in ch2:
                #print(ch3.tag,ch3.attrib)
                
                if (ch3.tag=="Time"):
                    if(ch3.text=="8:15PM"):
                        #print(ch3.text)
                        #print(ch2[1].text)
                        vocc.add(ch2[1].text)
for i in vocc:
    print(i)


# 10. Display total number of programs

# In[18]:


#solution code here
print("number of programs",c)  

