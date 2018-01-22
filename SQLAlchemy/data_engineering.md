

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
```

### Read CSV Files


```python
file_path_1 = os.path.join("Resources","hawaii_measurements.csv")
file_path_2 = os.path.join("Resources","hawaii_stations.csv")
hawaii_measurements_df = pd.read_csv(file_path_1)
hawaii_stations_df = pd.read_csv(file_path_2)
```

### Drop Nah values


```python
hawaii_measurements_df=hawaii_measurements_df.dropna(how='any')
```

### Export DataFrane to Clean_CSV


```python
hawaii_measurements_df.to_csv("clean_hawaii_measurements.csv", index=False, header=True)
hawaii_stations_df.to_csv("clean_hawaii_stations.csv", index=False, header=True)
```
