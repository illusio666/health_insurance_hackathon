# ![AI logo](https://media.licdn.com/dms/image/v2/D4E16AQGhs_RRie8XAw/profile-displaybackgroundimage-shrink_350_1400/B4EZhg5by7GcAY-/0/1753972326982?e=1762387200&v=beta&t=YZKH32qYFaO_mb401qru40kGNmlCB7pe0w43oRAXxng)

## Health Insurance Analysis

This repository contains the output of a collaborative educational project focused on analysing health insurance data. The team worked together to clean, transform, and visualise the dataset to uncover insights into how personal and geographic factors influence insurance charges.

## Team Roles 👥

- Project Manager: Rachel Fallon
- Data Architect: Eden Elvin
- Data Analyst (VS Code): Diana Milligan
- Data Analyst (Power BI): Matt Jacobs

## Business Objective 📊

The team was tasked with:

- Analysing healthcare insurance data to understand cost drivers
- Exploring correlations between personal attributes and charges
- Creating interactive dashboards and predictive visuals to support decision-making

## Dataset Content & Overview 📁

- Source: Kaggle – Healthcare Insurance Dataset
- Format: CSV
- Fields include: age, sex, BMI, number of children, smoker status, region, and insurance charges
The dataset was largely clean, requiring minimal preprocessing. One duplicate row was removed. No null values were present.

## Data Preparation Summary 🧹

The data architect performed the following transformations:

- New columns added:
  - Age ranges (18–25, 26–35, etc.)
  - BMI categories (underweight to morbidly obese)
  - Family status (0 = no children, 1+ = has children)
- Formatting:
  - Column names capitalised
  - BMI rounded to 1 decimal place; charges to 2 decimals
- Output:
- Two transformed files were created to support visualisation in VS Code and Power BI

Note: Ethnicity data was not available. Standard BMI ranges were used, though real-world application would require adjustment for ethnic-specific risk thresholds.

## Project Approach 🧠

- Roles were agreed at project start
- Dataset was selected collaboratively to ensure all work was original
- Power BI was chosen for dashboarding due to its accessibility and familiarity
- Hypotheses were defined to guide transformation logic
- Tasks were structured as user stories, labelled and timeboxed
- Stories were bulk-uploaded to GitHub using a CSV-to-issue workflow (repo link)
- The team worked in a virtual environment with twice-daily check-ins

## Hypotheses and validation approach (Diana & Matt)

Hypothesis 1 – Smokers will have higher charges than non smokers
•    Broadly, the hypothesis is correct, with the average charge for non-smokers being 8,440.66 and 32,050.23 for smokers. Visualisation using the “Quit Smoking Campaign” dashboard shows two distinct trend lines, that follow a consistent pattern unaffected by additional factors such as age or region. There is however, some noticeable overlap, where in some cases the two smoker classes, do overlap with some non-smokers paying more than their smoking counter part. Again, looking at the “Quit Smoking Campaign” dashboard, we see a possible reason for this, when we start to consider the client’s BMI as well, as resulting in a much more granular visualisation of the data, with smoking alone providing much of the additional Charges, with BMI underpinning the rest and making those who both smoke and have a high BMI having significantly higher levels of Charges than on average.

Hypothesis 2 – People with a higher BMI will have higher charges
•    All data points suggest that this hypothesis is correct, with the average Charges being 13,279, with Underweight having an average of 8,852, Normal 10,409, Overweight 10,987, Obese 15,352 and Morbidly obese 17,002. From a broader analytical question, we could look at the effects that being Underweight could have on the wider health of the clients, as the data alone shows they have fewer Charges than any other group; however, by medical standards, they could physically benefit from being of Normal weight, but that may result statistically from them having higher charges.
Hypothesis 3 – Some regions will have higher levels of smoking and BMI
•    All data points suggest that this hypothesis is correct, with the Southeast region having higher levels of both Smoking and average BMI, with the national average of BMI being 30.66, and smoking 20.49%, with the Southeast having an average BMI of 33.35 and 25% smoking, an increase of 8.77% and 22% respectively. The Southeast accounts for 27.22% of all people in the data, so statistically, the numbers can be taken as valid; however, at only 364 people, it is hard to develop a wider analysis for the region as a whole, with more information being needed about average levels of smoking and BMI across the entire region, not just the data we have on our clients.

Hypothesis 4 – Young people are less likely to smoke
•    Broadly, this hypothesis, based on the available data, is untrue; however, we lack additional data to understand the nature of why this is the case. The 18-25 bracket has a 21.31% of smokers, falling briefly in the 26-35, before rising to its highest levels with the 36-45 group, before falling to 18.31% and 18.52% respectively in the 46-55 and 56-65 groups. On paper, this can be taken at face value as seeing lower levels of smoking in general; however, it does not address the high-risk nature of smoking and its effect on general health and life expectancy. As such, it is possible to assume that those who had been smoking for an extended period of time have passed away and have been removed from the statistical analysis of this process.

## Mapping business requirements to visualisations (Diana & Matt)

**Requirement 1: Profile the Customer Base**

To understand the demographic and health characteristics of the existing customer portfolio for market segmentation and targeted product development.

Mapped to 'Distribution of Key Metrics' (visualisation 1), which breaks down the customer base by age, BMI, smoking status, and region.

<img width="1015" height="725" alt="image" src="https://github.com/user-attachments/assets/598b3c25-4223-4606-b275-ec143c3acc37" />

**Requirement 2: Identify Key Drivers of Insurance Costs**

To determine which customer attributes have the most significant impact on insurance charges, enabling more accurate pricing and risk assessment.

Mapped to 'Average Charges by Key Metrics' (visualisation 2) and 'Box Plot of Charges by Smoker Status' (visualisation 3), which quantify the financial impact of each variable, with a particular focus on the high cost associated with smoking.

**Requirement 3: Analyse the Interaction Between Risk Factors**

To understand how different risk factors combine and compound to influence charges, allowing for the creation of more sophisticated and fairer pricing models.

Mapped to 'Age vs. Charges' (visualisation 4) and 'BMI vs. Charges' (visualisation 5), which reveal how factors like smoking interact with age and BMI to amplify costs.

**Requirement 4: Enable Dynamic Data Exploration for Deeper Insights**

To provide a tool for business users to explore the data interactively, identify high-risk customer profiles, and generate actionable insights without deep technical knowledge.

Mapped to 'Interactive BMI vs. Charges Plot' (visualisation 6), which integrates multiple variables (BMI, charges, age, and smoking status) into a single, explorable interface.

## Main data analysis libraries

**Dataset:** Healthcare Insurance

**Dataset source:** https://www.kaggle.com/datasets/willianoliveiragibin/healthcare-insurance

**Libraries used:**

- pandas (for loading, cleaning, and manipulating the dataset in a DataFrame)
- numpy (for performing numerical operations, such as calculating the mean for the bar plots)
- matplotlib.pyplot (for creating and customising the basic structure of the static plots, like figures and axes)
- seaborn (for creating statistically-focused and aesthetically pleasing visualisations on top of matplotlib)
- plotly.express (for creating rich, interactive visualisations that the user can explore)
- warnings (to suppress and manage non-critical warning messages that can clutter the output)



## Analysis techniques used

Given the type and volume of data we had access to in this project, the majority of the analysis is Descriptive in nature, reporting on trends, summarising current data and making observations around it. We have seen patterns develop, often in keeping with the original hypothesis plan we set out; however, this was not always the case, as with smoker levels within different age groups. With additional data, we would have been able to start asking more pointed questions, allowing us to perform Diagnostic analysis, looking at the reasons why smoking levels, for example, decline. Was this because people started to stop? If so, why? Or is their life expectancy shorter, and as such, not a part of the data set for existing customers?

## Dashboard design

A style guide was proposed and agreed by the team to ensure consistency.

It was decided to create 4 tabs - an overview 'Regional Manager Dashboard' which would allow each region to view its own stats/compare to others, a summary tab relating to smokers with a view to creating a marketing campaign, a summary tab aimed at illustrating costs for parents and then a narrative tab. The concept is that the first 3 tabs would contain just data but that, in the real workd, the 4th tab would be updated each month to provide that month's key talking points/proposals.

## Unfixed bugs

There were no unfixed bugs.

## Results

Hypothesis 1: Smokers will have higher charges **(PROVEN)**

<img width="513" height="321" alt="image" src="https://github.com/user-attachments/assets/dee711c5-63e4-4589-8617-252eba9283c5" />


Hypothesis 2: People with higher BMI will have higher charges **(PROVEN)**

<img width="500" height="358" alt="image" src="https://github.com/user-attachments/assets/4d76c950-4d98-4997-b7dd-50282d0f4b12" />


Hypothesis 3: Charges increase with age **(PROVEN)**

<img width="514" height="317" alt="image" src="https://github.com/user-attachments/assets/073d0d9c-b951-4f4f-bdab-9054b9b0a964" />


Hypothesis 4: Charges will vary by region **(PROVEN)**

<img width="485" height="321" alt="image" src="https://github.com/user-attachments/assets/858e693c-848e-4434-878e-ea27ccf712a5" />


## Conclusions & recommendations (Diana & Matt)

Additional data sets would have also allowed us to move into both Predictive and Prescriptive analysis, looking more towards the options and campaigns for our clients. For example, we discussed whether our goal was to improve client health, profits, or a measure of both. Both positions, however, are difficult to explore without both a broader context of health in the regions and the associated costs to those of charges. A company, for example, wanting to maximise profits in the short term may well be perfectly content to have customers smoke at an early stage of their life, knowing that they can charge significantly higher amounts, yet do not take on many, if any of the associated costs that may result in their care later in life. This, put against a company that takes a long-term client-focused approach, may well offer lower costs and monthly premiums for customers who engage in health behaviour, so lowering their BMI and stopping smoking, and as a result both interact and charge their customers in radically different ways.
In short, given the nature of the data and with limited external context, we took time to address possible different business conditions, and this was presented in both our visualisations and dashboards to reflect potential campaigns to look at addressing both regional and broader trends in health and cost analysis, but where ultimately limited by the scope and depth of the data we had available.

## Folder structure

The Jupyter notebook visualisations of the data can be found within the jupyter_notebook folder, along with the data cleaning and transformation .ipynb.

The original and cleaned data sets can be found in the datasets folder.

The Power BI dashboard, Github user stories csv and the import_issues.py (csv_to_github upload utility) can be found in the main folder.

## Ethical Considerations ✅

- No personally identifiable data was present; GDPR compliance was not required
- The dataset used binary sex labels; these were retained as categorical fields to allow future expansion to broader gender constructs

## Credits

The repo template was provide by Code Institute.
The content of these workbooks was informed by training material on the Code Insitute Learning Management System.
Data was obtained from Kaggle.com.
CSV-to-Github uploader utility was forked from FaraiB/csv-to-github and adapted to include extra array fields.

## Content

Data is sourced from Kaggle.com, and is a publicly-available dataset.
Header image is an AI creation from Copilot
BMI ranges provided by NHS.UK website

## Project Media 🖼️

The header image was created by Copilot to represent human–AI collaboration. It is hosted on Rachel Fallon’s LinkedIn profile.

## Acknowledgements

Thanks to fellow students and tutors at Code Institute for their assistance in pulling together this project and fixing the inevitable issues.
