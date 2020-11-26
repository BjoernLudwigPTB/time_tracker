import os
import numpy
import pandas
import json
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

import matplotlib.pyplot as plt

# read config file
f = open("config.json", "r")
config = json.load(f)
f.close()

# log file location
log_file = os.path.expanduser(config["log_file"])
df = pandas.read_csv(log_file, parse_dates=[0], index_col=0)

# convert to local timezone
df = df.tz_localize("UTC").tz_convert("Europe/Berlin")

# display only last two weeks of records
cond = (df.index >= df.index.max() - pandas.Timedelta(days=config["report_days"]))
df = df[cond]

# calculate duration
df['duration'] = numpy.roll(df.index.to_series(keep_tz=True).diff(),-1)#.astype("timedelta64[h]")

# clean non-numerical and "Done"-entries
df = df.dropna()
df = df.where(df['action'] != "Done")

# make report
df_grouped = df.groupby([df.index.date, "action"])
report = df_grouped['duration'].sum()
print(report)

ru = report.unstack(0).fillna(pandas.Timedelta(0))

# make a stacked bar plot
bottom = numpy.zeros(len(ru.columns))
for action_label, row in ru.iterrows():
    hours = row.values.astype("double") / (3600 * 1e9)   # nano-seconds to hours
    plt.bar(ru.columns, hours, label=action_label, bottom=bottom)
    bottom += hours

plt.title("Tracked Time in hours")
plt.legend()
plt.show()
