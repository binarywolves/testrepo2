import pandas as pd
import os

folder = input("Paste the input folder:\t").replace("\\", "/") + "/"
output_folder = input("Enter the output folder:\t").replace("\\", "/") + "/"


def convert_excels(filename):

    path = folder+filename
    output_path = output_folder + "Cleaned_" + filename
    
    df = pd.read_excel(path)
    new_cols = ['Name', 'Email', 'Phone', 'Final', 'How_many_persons', 'Allergies']
    
    df = df[['Question-ID', 'User', 'Answer', 'Answer (Value)']]
    
    pivot_df = pd.pivot_table(df, index='User', columns='Question-ID', values='Answer', aggfunc=lambda x: x)
    # rename columns
    pivot_df.columns = new_cols
    res_df = pivot_df.reset_index()
    res_df['Number_of_persons'] = 0
    for index, row in df.iterrows():
        if row['Question-ID'] == 5:
            res_df.loc[res_df['User'] == row['User'], 'Number_of_persons'] = row['Answer (Value)']
            
    res_df = res_df[['User', 'Name', 'Email', 'Phone', 'Final', 'How_many_persons', 'Number_of_persons', 'Allergies']]
    res_df['Number_of_persons'] = res_df['Number_of_persons'].astype(str)
    res_df['Number_of_persons'] = res_df['Number_of_persons'].replace('0', '')

    res_df = res_df.fillna('')

    res_df.to_excel(output_path, index=False)
    display(res_df)
    print(f"{filename} processed")
    
    
# Get all files in the folder
files = os.listdir(folder)

if len(files) == 0:
    print("No files uploaded")
else:
    total_files = len(files)
    for i, file in enumerate(files, start=1):
        print(f"{i}/{total_files} in progress")
        convert_excels(file)
    print("\n\u2713 All files converted successfully")
