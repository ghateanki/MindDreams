import os, time
import datetime
import pandas
def delete_old(data_path: str, days: int):
    """ take the filepath and no of days back to deleted the files,
    and delete the empty folders"""
    now = time.time()
    for f_path,folders_list,files_list in os.walk(data_path):
        print('path checking is:',f_path)
        if files_list:
            Date = []
            # checking it has more than 10 files or not
            if len(files_list) >10:
                for file_ in files_list:
                    """comparing with the modified time of the file"""
                    # days is to take no of back days to delte the files
                    if os.path.getmtime(os.path.join(f_path,file_)) < now - (days* 86400):
                        print("removed file is ",file_,
                        datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(f_path,file))).strftime('%Y-%m-%d %H:%M:%S'))
                        os.remove(os.path.join(f_path,file_))
        elif not folders_list:
            os.rmdir(f_path)
            print("removed empty folder", f_path)



if __name__ == "__main__":
    print("This code deleted the empty foldes and 10 days or 30 days last modified days\
        depends on the no of backed days count")
    data_path = input("Please provide the path:")
    days = int(input("Please provide backed days count:"))
    delete_old(data_path, days)