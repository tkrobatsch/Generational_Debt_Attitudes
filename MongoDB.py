#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pprint
import re
import pymongo, json

pp = pprint.PrettyPrinter(indent=1,width=65)

client = pymongo.MongoClient (host="da1.eecs.utk.edu")
db = client ['fdac19mp2']
coll = db ['cmelton3']
# for each dataset
#coll.insert_one ( { 'topic':'student debt', 'first coll.insert_one ( { 'topic':'git URLscoll.insert_one ( { 'topic':'git URLs', 'first dataset': 'largest projects', 'license': 'NA', 'description': 'The list of projects on github with the largest number of starts', 'urls': [ 'url1', 'url2' ] } )
#coll.insert ( { 'topic':'YourTopic', 'title': 'Data title', 'license': 'license', 'description': 'Brief data description', 'urls': [ 'url1', 'url2', ... ] } )

coll.insert ( { 'topic':'Student Debt', 'title': 'Student Loans Owned and Securitized, Outstanding SLOAS', 'license': 'https://research.stlouisfed.org/fred_terms.html', 'description': 'Graph and download economic data for Student Loans Owned and Securitized, Outstanding (SLOAS) from Q1 2006 to Q2 2019 about student, securitized, owned, loans, and USA.', 'urls': [ 'https://fred.stlouisfed.org/series/SLOAS' ] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'Student Loans - UK', 'license': 'http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/', 'description': 'Presents statistics on student loan borrower status and repayments by repayment cohort and tax year, produced by the Student Loans Company', 'urls': [ 'https://find-data-beta-staging.cloudapps.digital/dataset/0c594ccc-854d-4986-9768-7039346d3e89/student-loans'] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'Student Loan Debt', 'license': 'other', 'description': 'A collection of student loan debt summary data, including: debt balance by age, amount, and debt types', 'urls': [ 'https://data.world/finance/student-loan-debt'] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'Average student debt of students at the top 20 U.S. universities in 2018/19', 'license': 'paid', 'description': 'This statistic shows the average debt of students at the top 20 universities in the United States in the academic year 2018/19. ', 'urls': [ 'https://www.statista.com/statistics/621365/median-student-debt-of-students-at-top-us-universities/'] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'Average debt of university graduates in the United States 2016/17, by state (in U.S. dollars)', 'license': 'subscription', 'description': 'This statistic shows the average amount of student debt that graduates had in different states across the United States, following 4 or more years of university in 2016/17', 'urls': [ 'https://www.statista.com/statistics/224863/states-average-student-debt-borrowing-for-graduates-in-the-us/'] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'Provisional impact of student loans, public sector-funded pension scheme changes and other expected data changes introduced in September 2019: Appendix G', 'license': 'UK government', 'description': 'Presents the provisional impacts of changes to be implemented in the public sector finances release scheduled for September 2019 on public sector net borrowing, net debt, net investment, current budget and net financial liabilities.', 'urls': [ 'https://www.ons.gov.uk/economy/governmentpublicsectorandtaxes/publicsectorfinance/datasets/provisionalimpactofstudentloanspublicsectorfundedpensionschemechangesandotherexpecteddatachangesintroducedinseptember2019appendixg'] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'Average student debt of university education graduates in the Netherlands from 2006 to 2016 (in 1,000 euros)', 'license': 'paid', 'description': 'Student debt in the Netherlands from 2006 to 2016', 'urls': [ 'https://www.statista.com/statistics/676708/average-student-debt-of-university-graduates-in-the-netherlands/'] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'National graduates survey, student debt from all sources, by province and level of study', 'license': 'open government', 'description': 'Provides statistics on student debt such as average debt at graduation, percentage of graduates owing large debt after graduation and percentage of graduates with debt who had paid it off at time of interview. These data are presented by province and level of study.', 'urls': [ 'https://open.canada.ca/data/dataset/c75d7a11-ecce-40d6-939a-ba61247bf98a'] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'Student Loans for Higher Education in Scotland', 'license': 'http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/', 'description': 'statistics on the status of student loans borrowers and the change in debt in the financial year.', 'urls': [ 'https://find-data-beta-staging.cloudapps.digital/dataset/e4b00078-698e-4008-8c7b-b8f350346958/student-loans-for-higher-education-in-scotland', 'https://data.gov.uk/dataset/e4b00078-698e-4008-8c7b-b8f350346958/student-loans-for-higher-education-in-scotland' 'https://data.wu.ac.at/schema/data_gov_uk/ZTRiMDAwNzgtNjk4ZS00MDA4LThjN2ItYjhmMzUwMzQ2OTU4'] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'National graduates survey, student debt from all sources, by location of residence at time of interview and level of study', 'license': 'open government', 'description': 'statistics on student debt such as average debt at graduation, percentage of graduates owing large debt after graduation and percentage of graduates with debt who had paid it off at time of interview.', 'urls': [ 'https://open.canada.ca/data/dataset/d954f6ad-82fc-4e61-98e3-27c3b25b56a0', 'https://data.wu.ac.at/schema/www_data_gc_ca/ZDk1NGY2YWQtODJmYy00ZTYxLTk4ZTMtMjdjM2IyNWI1NmEw'] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'Student Loans for Higher Education in England', 'license': 'open', 'description': 'statistics on the status of student loans borrowers and the change in debt in the financial year. The borrowers are English domiciles who studied anywhere in the UK or EU students who studied in England.', 'urls': [ 'https://find-data-beta-staging.cloudapps.digital/dataset/8d383b1e-dee5-4c2a-a6c9-4c9830385bee/student-loans-for-higher-education-in-england','https://data.gov.uk/dataset/8d383b1e-dee5-4c2a-a6c9-4c9830385bee/student-loans-for-higher-education-in-england' 'https://data.wu.ac.at/schema/data_gov_uk/OGQzODNiMWUtZGVlNS00YzJhLWE2YzktNGM5ODMwMzg1YmVl'] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'Student Loans for Higher Education in Northern Ireland', 'license': 'open government', 'description': 'Presents statistics on the status of student loans borrowers and the change in debt in the financial year. The borrowers are Northern Ireland domiciles who studied anywhere in the UK or EU students who studied in Northern Ireland', 'urls': [ 'https://data.gov.uk/dataset/1a04e39b-6ef2-46f3-b55b-705a1e2f5d96/student-loans-for-higher-education-in-northern-ireland', 'https://data.wu.ac.at/schema/data_gov_uk/MWEwNGUzOWItNmVmMi00NmYzLWI1NWItNzA1YTFlMmY1ZDk2'] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'Multivariable logistic regression models of anticipated medical student debt greater than $150,000 by race/ethnicity among 2355 medical students.', 'license': 'creative commons', 'description': 'Multivariable logistic regression models of anticipated medical student debt greater than $150,000 by race/ethnicity among 2355 medical students.', 'urls': [ 'https://figshare.com/articles/_Multivariable_logistic_regression_models_of_anticipated_medical_student_debt_greater_than_150_000_by_race_ethnicity_among_2355_medical_students_/786820'] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'Student loans: average debt on entry to repayment Wales 2009-2018', 'license': 'subscription', 'description': 'Average outstanding student loan debt in Wales on entry to repayment from 2000 to 2018.', 'urls': [ 'https://www.statista.com/statistics/376480/student-loans-wales-average-debt-on-entry-to-repayment-timeline/'] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'Education; education expenditure and CBS/OECD indicators', 'license': 'creative commons', 'description': 'At the two institutions in Texas, the study included a randomized controlled trial that gathered data from nearly 9,000 students and tracked them for up to two years. The final findings from the study indicate that biweekly disbursements do not result in substantial impacts on student outcomes:', 'urls': [ 'uhttps://www.openicpsr.org/openicpsr/project/110265/version/V1/view'] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'Data title', 'license': 'creative commons', 'description': 'This table gives an overview of expenditure on regular education within the Netherlands.', 'urls': [ 'https://data.overheid.nl/dataset/56682-education--education-expenditure-and-cbs-oecd-indicators','https://data.wu.ac.at/schema/data_overheid_nl/OGUwYmNkYWMtNDU2My00YmM1LTg4MzUtYTQxZmVlYTQ2OGE0',''] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'Utah Student Loan Debt by School_Major_Degree 2017', 'license': 'open', 'description': 'Utah student loan debt by major, degree and/or program of study for all Utah public and/or private colleges and universities for Academic year 2017.', 'urls': [ 'https://opendata.utah.gov/Education/Utah-Student-Loan-Debt-by-School_Major_Degree-2017/nwik-ytwn'] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'DaHousing choices made to pay back student debt in the U.S. 2019, by tenureta title', 'license': 'subscription', 'description': 'About one fifth of American adults with student debt had between 20,000 and 30,000 U.S. dollars in student loans to repay.', 'urls': [ 'https://www.statista.com/statistics/1036476/housing-choices-made-pay-back-student-debt-usa-by-tenure/'] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'Postsecondary Education Participants System (PEPS) is the Office of Federal Student Aid', 'license': 'US government', 'description': 'Postsecondary Education Participants System (PEPS) is the Office of Federal Student Aid (FSA) management information system of all organizations that have a role in administering student financial aid and other Higher Education Act programs.', 'urls': [ 'https://catalog.data.gov/dataset/postsecondary-education-participants-system', 'https://data.world/us-ed-gov/d7e1f41d-25c3-4451-8084-e25c482671b4'] } )
coll.insert ( { 'topic':'Student Debt', 'title': 'Studying Up on Higher Education', 'license': 'ESRI', 'description': 'Story Map Journal draws upon the U.S. Department of Educations College Scorecard datasets from 2006 and 2016.', 'urls': [ 'http://hub.arcgis.com/datasets/ccd648e8845847d2947cbc7e0c4ec616','http://maps.torontopolice.on.ca/datasets/ccd648e8845847d2947cbc7e0c4ec616'] } )



# In[3]:


import pprint
import pymongo, json
client = pymongo.MongoClient (host="da1.eecs.utk.edu")
db = client ['fdac19mp2']
coll = db ['audris']
pp = pprint.PrettyPrinter(indent=1,width=65)
for r in coll. find():
  print(pp .pformat (r))  


# In[ ]:




