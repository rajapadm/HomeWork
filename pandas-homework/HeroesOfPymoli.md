

```python
import os
import json
import pandas as pd
```


```python
data_df=pd.read_json('purchase_data.json')
data_df2=pd.read_json('purchase_data2.json')
```


```python
players=len(data_df['SN'].unique())
print(f"Total Players is {players}")
pd.DataFrame({"Total Players":[players]})
```

    Total Players is 573
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
item_cnt = len(data_df['Item ID'].unique())
total_purchase = len(data_df)
total_revenue = data_df['Price'].sum()
avg_price = total_revenue/total_purchase
```


```python
breakdown=pd.DataFrame({"Total Items":[item_cnt],
                       "Total Purchases":[total_purchase],
                       "Total Revenue":[total_revenue],
                       "Average Purchase Price":[avg_price]})
breakdown=breakdown.round(2)
breakdown["Average Purchase Price"]=breakdown["Average Purchase Price"].map("${:,.2f}".format)
breakdown["Total Revenue"]=breakdown["Total Revenue"].map("${:,.2f}".format)

breakdown
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Total Items</th>
      <th>Total Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>$2.93</td>
      <td>183</td>
      <td>780</td>
      <td>$2,286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
total_gender=len(data_df['Gender'])
genders=data_df['Gender'].value_counts()
total_male=data_df['Gender'].value_counts()['Male']
total_female=data_df['Gender'].value_counts()['Female']
total_other=data_df['Gender'].value_counts()['Other / Non-Disclosed']
percentage_male=total_male/total_gender * 100
percentage_female=total_female/ total_gender * 100
percentage_other = total_other/total_gender * 100
gender_df = pd.DataFrame({"Gender":['Male','Female','Other'],
                         "Total Percentage":[percentage_male,percentage_female,percentage_other],
                         "Total Count":[total_male,total_female,total_other]})
gender_df=gender_df.round(2)

gender_df["Total Percentage"]=gender_df["Total Percentage"].map("{:,.2f}%".format)

gender_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Total Count</th>
      <th>Total Percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Male</td>
      <td>633</td>
      <td>81.15%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Female</td>
      <td>136</td>
      <td>17.44%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Other</td>
      <td>11</td>
      <td>1.41%</td>
    </tr>
  </tbody>
</table>
</div>




```python

m_data=data_df[data_df['Gender']=="Male"]
m_total_price=sum(m_data['Price'])
m_avg=m_total_price/total_male
m_norm = total_revenue/total_male
f_data=data_df[data_df['Gender']=="Female"]
f_total_price=sum(f_data['Price'])
f_avg=m_total_price/total_female
f_norm = total_revenue/total_female
o_data=data_df[data_df['Gender']=="Other / Non-Disclosed"]
o_total_price=sum(o_data['Price'])
o_avg=m_total_price/total_other
o_norm = total_revenue/total_other

norm=pd.DataFrame({"Gender": ["Male","Female","Other"],
                  "Purchase Count":[total_male,total_female,total_other],
                  "Average Purchase Price":[m_avg,f_avg,o_avg],
                 "Total Purchase Price":[m_total_price,f_total_price,o_total_price],
                 "Normalized Total":[m_norm,f_norm,o_norm]})

norm=norm.round(2)
norm["Average Purchase Price"]=norm["Average Purchase Price"].map("${:,.2f}".format)
norm["Normalized Total"]=norm["Normalized Total"].map("${:,.2f}".format)
norm["Total Purchase Price"]=norm["Total Purchase Price"].map("${:,.2f}".format)

norm

#norm_test = pd.DataFrame({"Gender": })

#df_norm_test = pd.DataFrame(columns=('Gender', 'Total Count','Total Revenue'))

#gender_list = ["Male", "Female", "Other"]

#i=0
#data_object = []
#for i in range(0, len(gender_list)):
#    #print(gender)
#    data_object.append(gender_list[i])
#    data_object.append(gender_df.loc[gender_df['Gender'] == gender_list[i]]['Total Count'].values[0])
#    #data_object.append(gender_df.loc[gender_df['Gender']== gender_list[i]][])
#    print(breakdown['Total Revenue'][0])
#    print(gender_df.loc[gender_df['Gender'] == gender_list[i]]['Total Count'].values[0])
#    data_object.append(breakdown['Total Revenue'][0]/(gender_df.loc[gender_df['Gender'] == gender_list[i]]['Total Count'].values[0]))
#data_object.append(data_df[data_df['Gender']==gender])
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Gender</th>
      <th>Normalized Total</th>
      <th>Purchase Count</th>
      <th>Total Purchase Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>$2.95</td>
      <td>Male</td>
      <td>$3.61</td>
      <td>633</td>
      <td>$1,867.68</td>
    </tr>
    <tr>
      <th>1</th>
      <td>$13.73</td>
      <td>Female</td>
      <td>$16.81</td>
      <td>136</td>
      <td>$382.91</td>
    </tr>
    <tr>
      <th>2</th>
      <td>$169.79</td>
      <td>Other</td>
      <td>$207.85</td>
      <td>11</td>
      <td>$35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
bins = [10, 14, 19, 23, 27, 31, 35, 39, 43, 45] 
bin_names=["0-10","10-14","14-19","19-23","23-27","27-31","31-35","35-39","40-45"]
max(data_df['Age'])
```




    45




```python
#groups = data_df.groupby(pd.cut(data_df.Age, 13))
#groups
age_dem=data_df
age_dem["Range"]=pd.cut(age_dem["Age"],bins,labels=bin_names)

range_cnt=age_dem["Range"].value_counts()
range_cnt

avgby_bin=age_dem.groupby("Range").mean()["Price"]
totalby_bin=age_dem.groupby("Range").sum()["Price"]
normby_bin=totalby_bin/range_cnt

final_bin= pd.DataFrame({"Purchase Count":range_cnt,
                         "Average Purchase Price":avgby_bin,
                         "Total Purchase Value":totalby_bin,
                         "Normalized Totals":normby_bin})


final_bin=final_bin.round(2)

final_bin["Average Purchase Price"]=final_bin["Average Purchase Price"].map("${:,.2f}".format)
final_bin["Total Purchase Value"]=final_bin["Total Purchase Value"].map("${:,.2f}".format)

final_bin.sort_index()                                        

#final =
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Normalized Totals</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0-10</th>
      <td>$2.70</td>
      <td>2.70</td>
      <td>31</td>
      <td>$83.79</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>$2.91</td>
      <td>2.91</td>
      <td>133</td>
      <td>$386.42</td>
    </tr>
    <tr>
      <th>14-19</th>
      <td>$2.88</td>
      <td>2.88</td>
      <td>265</td>
      <td>$763.08</td>
    </tr>
    <tr>
      <th>19-23</th>
      <td>$3.03</td>
      <td>3.03</td>
      <td>168</td>
      <td>$508.66</td>
    </tr>
    <tr>
      <th>23-27</th>
      <td>$2.96</td>
      <td>2.96</td>
      <td>60</td>
      <td>$177.40</td>
    </tr>
    <tr>
      <th>27-31</th>
      <td>$3.11</td>
      <td>3.11</td>
      <td>42</td>
      <td>$130.64</td>
    </tr>
    <tr>
      <th>31-35</th>
      <td>$2.75</td>
      <td>2.75</td>
      <td>30</td>
      <td>$82.38</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>$3.19</td>
      <td>3.19</td>
      <td>16</td>
      <td>$51.03</td>
    </tr>
    <tr>
      <th>40-45</th>
      <td>$2.72</td>
      <td>2.72</td>
      <td>1</td>
      <td>$2.72</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Top 5 Spenders
player_pcnt=data_df.groupby("SN").count()["Item ID"]
player_avg=data_df.groupby("SN").mean()["Price"]
player_total=data_df.groupby("SN").sum()["Price"]

player_dataframe=pd.DataFrame({"Purchase Count":player_pcnt,
                     "Average Purchase Price":player_avg,
                     "Total Purchase Value":player_total})

player_dataframe=player_dataframe.sort_values("Total Purchase Value",ascending=False).head()
#player_dataframe[:5]
player_dataframe
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>3.412000</td>
      <td>5</td>
      <td>17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>3.390000</td>
      <td>4</td>
      <td>13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>3.185000</td>
      <td>4</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>4.243333</td>
      <td>3</td>
      <td>12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3.860000</td>
      <td>3</td>
      <td>11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Top 5 Items
item_pcnt=data_df.groupby(["Item Name","Item ID"]).count()["SN"]
item_avg=data_df.groupby(["Item Name","Item ID"]).mean()["Price"]
item_total=data_df.groupby(["Item Name","Item ID"]).sum()["Price"]

item_dataframe=pd.DataFrame({"Purchase Count":item_pcnt,
                     "Item Price":item_avg,
                     "Total Purchase Value":item_total})

item_dataframe["Item Price"]=item_dataframe["Item Price"].map("${:,.2f}".format)
item_dataframe["Total Purchase Value"]=item_dataframe["Total Purchase Value"].map("${:,.2f}".format)
item_dataframe=item_dataframe.sort_values("Purchase Count",ascending=False).head()
item_dataframe
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item Name</th>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <th>39</th>
      <td>$2.35</td>
      <td>11</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>Arcane Gem</th>
      <th>84</th>
      <td>$2.23</td>
      <td>10</td>
      <td>$22.30</td>
    </tr>
    <tr>
      <th>Retribution Axe</th>
      <th>34</th>
      <td>$4.14</td>
      <td>9</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>Trickster</th>
      <th>31</th>
      <td>$2.07</td>
      <td>9</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>Serenity</th>
      <th>13</th>
      <td>$1.49</td>
      <td>9</td>
      <td>$13.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
item_dataframe=item_dataframe.sort_values("Total Purchase Value",ascending=False).head()
item_dataframe
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item Name</th>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Retribution Axe</th>
      <th>34</th>
      <td>$4.14</td>
      <td>9</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <th>39</th>
      <td>$2.35</td>
      <td>11</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>Arcane Gem</th>
      <th>84</th>
      <td>$2.23</td>
      <td>10</td>
      <td>$22.30</td>
    </tr>
    <tr>
      <th>Trickster</th>
      <th>31</th>
      <td>$2.07</td>
      <td>9</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>Serenity</th>
      <th>13</th>
      <td>$1.49</td>
      <td>9</td>
      <td>$13.41</td>
    </tr>
  </tbody>
</table>
</div>


