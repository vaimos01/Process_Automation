import os
import glob

def merge_files(folder_name,folder_path,output_path):
  files = glob.glob(os.path.join(folder_path,folder_name)+"/*.csv")
  file_name = os.path.join(output_path,folder_name)+".csv"
  try:
    os.remove(file_name)
  except OSError as error:
    print(error)

for file in sorted(files):
  print(file)
  df = pd.read_csv(file,index_col=None, delimiter=",", escapechar ="\\")

if not os.path.isfile(file_name):
  df.to_csv(file_name,header='column_names',index=False)
else:
  df.to_csv(file_name,mode='a',header=False,index=False)

  
  
