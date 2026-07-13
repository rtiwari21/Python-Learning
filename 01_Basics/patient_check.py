# Question : Check Patient Named - John Smith , Age 20 , New patient

patient_name = input("Enter the Patient Name ")
patient_age = input("Enter the Patient Age ")

if patient_name == 'John' and patient_age == '20':
    print('This is a New Patient')

else:
    print('This is an existing patient')