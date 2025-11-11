import pandas as pd

data = pd.read_csv(r"C:\Users\sarvesh jathar\Downloads\countries of the world.csv")

data_txt = pd.read_csv(r"C:\Users\sarvesh jathar\Downloads\countries of the world.txt", sep = "\t")
data_txt.head()

data_txt2 = pd.read_table(r"C:\Users\sarvesh jathar\Downloads\countries of the world.txt")
data_txt2.head()

data_json = pd.read_json(r"C:\Users\sarvesh jathar\Downloads\json_sample.json")
data_json.head()

data_excel = pd.read_excel(r"C:\Users\sarvesh jathar\Downloads\world_population_excel_workbook.xlsx")
data_excel.head()

data_excel = pd.read_excel(r"C:\Users\sarvesh jathar\Downloads\world_population_excel_workbook.xlsx", sheet_name = "Sheet1")
data_excel.head()

pd.set_option("display.max_rows", 235)
pd.set_option("display.max_columns", 40)

data_excel = pd.read_excel(r"C:\Users\sarvesh jathar\Downloads\world_population_excel_workbook.xlsx", sheet_name = "Sheet1")
data_excel

data_excel.info()


data_excel.shape

data_excel.loc[224]

data_excel.iloc[224]

data_pop = pd.read_csv(r"C:\Users\sarvesh jathar\Downloads\world_population.csv")
data_pop.head()

data_pop[data_pop["Rank"] < 10] 

data_pop[data_pop["Country"].isin(["Bangladesh", "India"])]

data_pop[data_pop["Country"].str.contains("United")]

data_pop2 = data_pop.set_index("Country")
data_pop2.head()

data_pop2.filter(items = ["India"], axis = 0)

data_pop2.filter(items = ["India"], axis = 0)

data_pop2.filter(like = "Chi", axis = 0)

data_pop2.loc["India"]

data_pop[data_pop["Rank"]<10].sort_values(by = "2022 Population", ascending = False)

data_pop = pd.read_csv(r"C:\Users\sarvesh jathar\Downloads\world_population.csv", index_col = "Country")
data_pop.head()

data_pop.reset_index(inplace = True)

data_pop.head()

data_pop.set_index("Country", inplace = True)
data_pop.head()

data_pop.reset_index(inplace = True)

data_pop.head()

data_pop.set_index(["Continent", "Country",], inplace = True)
data_pop.head()

dataf = pd.read_csv(r"C:\Users\sarvesh jathar\Downloads\Flavors.csv")
dataf

dataf.groupby("Base Flavor")["Flavor Rating"].sum()

dataf.groupby("Base Flavor").agg({"Flavor Rating" : ["mean", "max", "count", "sum"]})

data1 = pd.read_csv(r"C:\Users\sarvesh jathar\Downloads\LOTR.csv")
data1.head()

data2 = pd.read_csv(r"C:\Users\sarvesh jathar\Downloads\LOTR 2.csv")
data2.head()

data1.merge(data2, how = "inner")

data1.merge(data2, how = "inner", on = ["FellowshipID", "FirstName"])

data1.merge(data2, how = "inner")

data1.merge(data2, how = "inner", on = ["FellowshipID", "FirstName"])

data1.merge(data2, how = "left")

data1.merge(data2, how = "right")

data1.merge(data2, how = "outer")

data1.set_index("FellowshipID", inplace = True)
data2.set_index("FellowshipID", inplace = True)
