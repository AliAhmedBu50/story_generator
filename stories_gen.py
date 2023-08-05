import time
import random
import os
import glob
import textwrap
border = "================================"
def selected():
    print("In this mode you choose the stories you want")
    print("how long do you want your story to be?")
    print(border)
    print("Enter '1' for 1 minute long stories")
    print("Enter '3' for 3 minute long stories")
    print("Enter '5' for 5 minute long stories")
    print(border)
    story_length2 = input("Enter the length of the story you want")
    if story_length2 in ["1", "3", "5"]:
        directory_path = "./" + story_length2
        txt_files = glob.glob(os.path.join(directory_path, "*.txt"))
        index = 1
        for file_path in txt_files:
            print(index,": ",os.path.splitext(os.path.basename(file_path))[0])
            index+=1
        choice = int(input("Choose story "))
        story_printer(txt_files[choice-1])
        stories()
        continue_reading()
def story_printer(path):
    with open(path, "r") as file:
        text = file.read()
        width = 100
        wrapped_text = textwrap.fill(text, width)
        time.sleep(2.23421)
        print(wrapped_text)

def random_story():
        print(border)
        print("how long do you want your story to be?")
        print(border)
        print("Enter '1' for 1 minute long stories")
        print("Enter '3' for 3 minute long stories")
        print("Enter '5' for 5 minute long stories")
        print(border)
        story_length = input("now choose how long do you want your story to be ")
        if story_length in ["1","3","5"]:
            directory_path = "./" + story_length
            txt_files = glob.glob(os.path.join(directory_path, "*.txt"))
            random_number = random.randint(0, len(txt_files)-1)
            #print(random_number)
            #for file_path in txt_files:
            #print(os.path.splitext(os.path.basename(file_path))[0])
            story_printer(txt_files[random_number])
            continue_reading()
def continue_reading():
    continue_stop = int(input("Would you like another story? Enter 1 for another story and enter 2 to stop "))
    if continue_stop == 1:
        stories()
    elif continue_stop == 2:
        quit()


        #random_file_path = random.choice(file_paths)

        #print(file_contents)
    else:
        print("ERROR 404: (INVALID INPUT)")
        print("Please try another input")
        time.sleep(2)
        stories()
def stories():
    random_selected = input("Enter 1 to read random stories or enter 2 to read selected stories ")
    if random_selected == "1":
        random_story()

    elif random_selected == "2":
        selected()
    else:
        quit()
if __name__ == "__main__":
    print(""" _____ _                     _____                           _             
/  ___| |                   |  __ \                         | |            
\ `--.| |_ ___  _ __ _   _  | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 `--. \ __/ _ \| '__| | | | | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
/\__/ / || (_) | |  | |_| | | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
\____/ \__\___/|_|   \__, |  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                      __/ |                                                
                     |___/                                                 """)
    print("""//#,,*,****############((,................../*...........                  
,//*(,,***/############((,,**..... ....... .//,.......,....                
,,,##(,/,/##############(,,,*(/..............*.  ...........               
/,,##################(##(/,,,,,,,,,,,,.,,,,................                
***((/(##############/*//,,,,,,,,,,,,,,,,,,.,.,,,,,...  .....              
*,*/(#(######((##/***/*,,,.......,..,,,,*,,,,,**,*,,,,.     ..             
,*/#########(*//,,,*,,,.................,,,*,*,,****,,,,.   ....           
##(########,,,*/,//*...... .. ...  ..........,,.,,,,*,*,,.  .....          
*/#(/***/(//****//,....  ...,.  ..,,..,,... .,,....,,*,,*,.  .....         
,//,,,,,/**,,,,##(,..   ...**..,/######(#(((##(,..,,,,,*,*,      .         
##/(#((/,*/*(####(.. ... ,/#####%%%%%%%%%######(,..,,,,.,,,.      .        
(**////(*//######(.. .,*/((#######%%%%%%%%%#%%%##(/,,...,,,.  ,          ..
/(*/(*((#((((#((#(,  .*///((((######((/,,.,,,,,**/###*. .....,,.           
**////**(#((((((((/ .*...,,,,,,*((((/*,.,******,  .,....*####%*,.          
,***/**(((((((((((/ .,*,,*,,,,,,.....*,,/%,.,/(((/#(##..,*/**(,,,.        .
,.(****(((((((((((((./*,,*/,*//*.(%%,,(//////##%/%#####(%((#(,,,,,,.       
,,((//(#(((((((((((/.,/((////((,/#%%%(,#%%%%&&(,%%%#####(%&%%,,,,,,.       
,(((((((((((((((((..*//*****//*##%&&&%&%///((#########(/#%%%/,,......      
((((((((((((((/.....,(*(((((/((((###(/*/(#((///((((#((*,,*//,*.            
(((((((((((/....***/*////////((//***/(###((*,*/((((SSS((/**,,**      ,..      
((((((((/... ((/**,****,///*,..,**(//(/(/((((/////((///**,               ..
*,,......  ,(*,,,,,,**,((///////((/(###(//((((/(//(/(/..,**/*/,            
.....  .,//*,,,,,*//,*///*////////***//(####((//////(#%%%#@%       ,*,.  ,/
. ,,,,.*,*,,(/*,,,,*#&/*(&(((*//(((#######(///***//((#%%#@@@#       .,   **
/(.*/***.,,,,,**,,,**,.#&//##/***////////*******//(((#%&@@@&@@&        ....
*,.**,,,,*,....,,/,*,&%&((##*****************////((((&#@@@@@@@@@&%*       .
.,//*,.,.,,,.,(&&&&&&%%&/###////////******/////(((((#%##@@@@@@@@@@@@@@@(   
...,**.,*,&&@@@@&&%&&%&&/###((////////////////((((((%##((%@@@@&&@&&@@@@@@@@
***,,/&@&&%@&&%%&&&&&%&#/#####/////////////((((((((#%%##(%%#&&@@@&&@@@@@&@@
.,,&&%@@@%&##@&%%@@@%&%#/%%%#%#%(/(((((((((((###%%%%%@%#%&&&&&@@@&%@@@@&&@@""")
    print(border)
    print("Welcome to The Stories program")
    print(border)
    print("Made by: Ali Bukhamsin")
    stories()
