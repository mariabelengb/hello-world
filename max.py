import os 

img_src_dir = input("Drop image source directory: ")

#STEP 4
#Determine last element
def lastID():

    #Create list of files for image directorie
    img_list_4 = os.listdir(img_src_dir)
    
    #Create lists of the same files than before but sorted
    sorted_img_list_4 = sorted(img_list_4)
    
    #Only file names
    img_fn_list_4 = [os.path.splitext(os.path.basename(i))[0] for i in sorted_img_list_4]
    
    print("The IDs have been created")
    number = int(max(img_fn_list_4))
    print("Last element: " + str(number))
        
lastID()        
