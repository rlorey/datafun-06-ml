# Data Card: Life Expectancy

# 📋 Life Expectancy Data Card

This data card provides essential documentation and context for the tracking dataset used to train our predictive life expectancy regression models.

## 🌐 Dataset Context
* **Source:** World Health Organization (WHO) / Global Health Observatory (GHO)
* **Scope:** Global health tracking across multiple countries and regions over a multi-year period.
* **Target Variable:** `Life expectancy` (The average number of years a newborn infant would live if prevailing patterns of mortality at the time of its birth were to stay the same throughout its life).

## 📊 Dataset Characteristics
* **Number of rows:** 2,938 records
* **Number of columns:** 22 features
* **Format:** Tabular `.csv`
* **Cleaned Parameters:** Column spaces stripped out, empty target parameters handled via rigorous data-cleaning workflows.

## 🔍 Full Column Glossary
The dataset contains the following 22 attributes compiled by the WHO:

* **Country:** The specific country name tracking the observation.
* **Year:** The specific calendar year of data collection.
* **Status:** Developed or Developing status parameter.
* **Life expectancy:** Target metric measured in years.
* **Adult Mortality:** Probability of dying between 15 and 60 years per 1000 population.
* **infant deaths:** Number of Infant Deaths per 1000 population.
* **Alcohol:** Per capita consumption (in liters of pure alcohol).
* **percentage expenditure:** Expenditure on health as a percentage of Gross Domestic Product per capita (%).
* **Hepatitis B:** Hepatitis B (HepB) immunization coverage among 1-year-olds (%).
* **Measles:** Number of reported cases per 1000 population.
* **BMI:** Average Body Mass Index of entire population.
* **under-five deaths:** Number of under-five deaths per 1000 population.
* **Polio:** Polio (Pol3) immunization coverage among 1-year-olds (%).
* **Total expenditure:** General government expenditure on health as a percentage of total government expenditure (%).
* **Diphtheria:** Diphtheria tetanus toxoid and pertussis (DTP3) immunization coverage among 1-year-olds (%).
* **HIV/AIDS:** Deaths per 1,000 live births HIV/AIDS (0-4 years).
* **GDP:** Gross Domestic Product per capita (in USD).
* **Population:** Population of the country.
* **thinness 1-19 years:** Prevalence of thinness among children and adolescents for Age 1 to 19 (%).
* **thinness 5-9 years:** Prevalence of thinness among children for Age 5 to 9 (%).
* **Income composition of resources:** Human Development Index in terms of income composition of resources (index ranging from 0 to 1).
* **Schooling:** Number of years of education (independent predictor variable).

## ⚠️ Known Artifacts & Operational Notes
* **Data Limits:** Contains structured bounds like `Schooling = 0` which require close attention due to model underprediction risks.
* **Linearity Discrepancies:** Structural residual checks reveal heteroscedasticity and non-linear properties when modeling mid-to-low education parameters directly against mortality timelines.


## References

- [Life Expectancy Data Documentation](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who)
- [Data Cards Playbook (toolkit)](https://pair-code.github.io/datacardsplaybook/)
- Data Cards convention: Pushkarna, Zaldivar, and Kjartansson (2022),
  _Data Cards:_
  _Purposeful and Transparent Dataset Documentation for Responsible AI_,
  ACM FAccT. <https://doi.org/10.1145/3531146.3533231>

---

[◄ Back to Home](index.md)
