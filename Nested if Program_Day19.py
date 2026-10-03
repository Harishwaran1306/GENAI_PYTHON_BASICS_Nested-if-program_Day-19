#Nested If
#Write a code to check whether a person can donate the blood based on the BMI Level and Hemoglobin level



print('='*50)
print('*****Blood Donation Status*****')
print('='*50)



Weight_kg =         float(input('Enter Weight in Kg:'))
Height_cm =         float(input('Enter Height in cm:'))
Height_m  =         Height_cm /100
BMI       =         Weight_kg /( Height_m *Height_m )
Age       =         int(input('Enter Age:'))
Hemoglobin_lvl =    float(input('Enter Hemoglobin level in g/dL:'))
print('Your BMI Level is ', BMI)

                         
                       
if Age >= 18:
    print('Correct Age, Eligible to donate')
    if BMI >= 18.5 and BMI<= 28:
        print('Correct BMI, Eligible to donate')
        if Hemoglobin_lvl > 12.5:
            print('Correct Hemoglobin_lvl,Eligible to donate')
        else:
             print('low Hemoglobin_lvl,Not Eligible to donate')
    elif BMI < 18:
        print('Low BMI, Not Eligible to donate')
    elif BMI > 29:
        print('High BMI, Not Eligible to donate')
    else:
        print('The BMI is ' ,BMI, 'So Not Eligible to donate')
        
else:
    print('Low Age , Not Eligible to donate')
