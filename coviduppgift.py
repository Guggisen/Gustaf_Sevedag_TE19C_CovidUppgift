import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

cirkel = 0
punkt = 0
stapel = 0


val = float(input("Vilken av följande 3 grafer vill du använda dig utav när du studerar coronafallen? För cirkeldiagram-skriv 1. För Stapeldiagram - skriv 2 och för punktdiagram skriver du 3."))

if val == 1:
  cirkel = float(input("Vill du undersöka coronafalls skillnaden mellan könen eller mellan de olika landskapen i Sverige? För att välja kön skriv 1, för att välja landskap skriv 2."))

if val == 2:
  stapel = float(input("Vill du undersöka coronafalls skillnaden mellan könen eller mellan de olika landskapen i Sverige? För att välja kön skriv 1, för att välja landskap skriv 2."))

if val == 3:
  punkt = float(input("Vill du undersöka coronafalls skillnaden mellan könen eller mellan de olika landskapen i Sverige? För att välja kön skriv 1, för att välja landskap skriv 2."))
 

if cirkel == 1:
  df = pd.read_csv("Gender_Data.csv")
  plt = px.pie(df, values='Total_Deaths', names='Gender', title='Andel avlidade män repsektive kvinnor i Covid 19')

  plt.show()


  df = pd.read_csv("Gender_Data.csv")
  plt = px.pie(df, values='Total_ICU_Admissions', names='Gender', title='Andel intensivvårdade män repsektive kvinnor i Covid 19')

  plt.show()

  df = pd.read_csv("Gender_Data.csv")
  plt = px.pie(df, values='Total_Cases', names='Gender', title='Andel insjuknade män repsektive kvinnor i Covid 19')

  plt.show()

if cirkel == 2: 
  df = pd.read_csv("Regional_Totals_Data.csv")
  plt = px.pie(df, values='Total_Cases', names='Region', title='Här är ett cirkeldiagram över alla olika regioners totala fall.')

  plt.show()


if punkt == 2:

  df = pd.read_csv("Regional_Totals_Data.csv")

  plt = px.scatter(df, x="Region", y="Total_Cases", 
                 title="Reginernas coronafall",
                )

  plt.show() 

if punkt == 1:

  df = pd.read_csv("Gender_Data.csv")

  plt = px.scatter(df, x="Gender", y="Total_Cases", 
                 title="Totala fall för varje kön",
                )

  plt.show()

  df = pd.read_csv("Gender_Data.csv")

  plt = px.scatter(df, x="Gender", y="Total_ICU_Admissions", 
                 title="Intensivvårdade för varje kön",
                )

  plt.show()  

  df = pd.read_csv("Gender_Data.csv")

  plt = px.scatter(df, x="Gender", y="Total_Deaths", 
                 title="Antal döda kvinnor repsektive män",
                )

  plt.show() 


if stapel == 1:
  df = pd.read_csv("Gender_Data.csv")

  plt.bar(df["Gender"],df["Total_Cases"])
  plt.title('Antal coronasmittade per kön')
  plt.xlabel('Kön')
  plt.ylabel('Antal infekterade')

  plt.show()

  df = pd.read_csv("Gender_Data.csv")

  plt.bar(df["Gender"],df["Total_ICU_Admissions"])
  plt.title('Antal coronasmittade per kön')
  plt.xlabel('Kön')
  plt.ylabel('Antal infekterade')

  plt.show()
  
  df = pd.read_csv("Gender_Data.csv")

  plt.bar(df["Gender"],df["Total_Deaths"])
  plt.title('Antal coronasmittade per kön')
  plt.xlabel('Kön')
  plt.ylabel('Antal infekterade')

  plt.show()

if stapel == 2:
  df = pd.read_csv("Regional_Totals_Data.csv")

  plt.bar(df["Region"],df["Total_Cases"])
  plt.title('Antal coronasmittade i Sveriges regioner')
  plt.xlabel('Regioner')
  plt.ylabel('Antal smittade per region')
  plt.xticks(rotation=90)
  
  plt.show()
