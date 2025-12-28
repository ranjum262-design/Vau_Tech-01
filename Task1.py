import pandas as pd
df=pd.read_csv("Student_marks.csv")
print("\n--- Students Marks ---\n",df) 
#COUNT
print("---Count---")
print(f"Total number of students:{len(df)}")

#Filter Marks Greater tham 70
toppers=df[(df['Math']>50)&(df['Science']>50)]
print("\n--Toppers of Math and Science Students are:--\n",toppers[['Name','Math','Science']])

#Total of all subjects
df['Total']=df[['Math','Science','English']].sum(axis=1)
toppers_list = df.sort_values('Total', ascending=False)
print("\n--Total of all Subjects with ranking--\n",toppers_list[['Name','Total']])

#Top 3 ranker
rank_holders = df.sort_values('Total', ascending=False).head(3).assign(Rank=[1, 2, 3])
print("\n--- Top 3 Rankers ---\n",rank_holders[['Rank','Name','Total']])

#Processed data
toppers[['Name','Math','Science']].to_csv('Topper_in_Sci_&_Math.csv', index=False)
toppers_list.to_csv('Total_marks.csv',index=False)
rank_holders[['Rank','Name','Total']].to_csv('rank_holders.csv',index=False)
print("\n[Success] File 'top_performers.csv' and 'total_marks .csv' have been created.")
