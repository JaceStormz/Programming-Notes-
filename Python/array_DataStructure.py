# 08/10/2026
# array_DataStructure.py

monthly_Exp = [2200,2350,2600,2130,2190]


print(f"${monthly_Exp[1] - monthly_Exp[0]} spent extra")
print(f"${monthly_Exp[0] + monthly_Exp[1] + monthly_Exp[2]} expenses for the first quarter")
print(f"Did I spend $2000 in any month? {2000 in monthly_Exp}")
monthly_Exp.append(1980)
print(f"expenses at end of June: {monthly_Exp}")
monthly_Exp[3] = monthly_Exp[3] -200
print(f"Made a correction {monthly_Exp}")