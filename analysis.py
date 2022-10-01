import pandas as pd
import matplotlib.pyplot as plt

wdi = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

wdi_subset = wdi[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ]
]

plt.plot(
    wdi_subset["GDP per capita (constant 2010 US$)"],
    wdi_subset["Mortality rate, infant (per 1,000 live births)"],
)

plt.show()
