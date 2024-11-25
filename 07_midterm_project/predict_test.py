#!/usr/bin/env python
# coding: utf-8



import requests



url = "http://localhost:9696/predict"

employee_id = 'xyz-123'
employee = {
    "age": 40,
    "gender": "male",
    "years_at_company": 30,
    "job_role": "healthcare",
    "monthly_income": 7008,
    "work-life_balance": "poor",
    "job_satisfaction": "high",
    "performance_rating": "average",
    "number_of_promotions": 0,
    "overtime": "no",
    "distance_from_home": 460,
    "education_level": "associate_degree",
    "marital_status": "married",
    "number_of_dependents": 0,
    "job_level": "senior",
    "company_size": "large",
    "company_tenure": 72,
    "remote_work": "no",
    "leadership_opportunities": "no",
    "innovation_opportunities": "no",
    "company_reputation": "fair",
    "employee_recognition": "high",
}



response = requests.post(url, json=employee).json()
print(response)


if response['attrition'] == True:
    print('add something to the employee to stay %s' % employee_id)
else:
    print('do not need to do anything %s' % employee_id)




