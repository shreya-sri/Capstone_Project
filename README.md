# Voice based form filling assistant for the visually impaired

The objective of this project is to provide a voice integrated system that helps the visually impaored fill forms out on their own. It's a program that runs on a kiosk that could be placed at government offices or banks.

Following are the sequential steps of the working of the project:

STEP 1: The Face Detection module triggers the software’s custom UI, once a person’s presence is detected at the kiosk.

STEP 2: The person is requested to show their Aadhar Card via a voice prompt using the Text to Speech module.

STEP 3: The 12 digit Aadhar Number is scanned using OCR module and the person’s face is recognized & matched with the Aadhar DB using Face Recognition module. This is done to ensure complete security during the form filling process. 

STEP 4: Using Text to Speech & Speech to Text modules, the software sends prompts (form field questions) and collects responses from the user in a voice-based format. 

STEP 5: After each response is spoken out by the user, the response is reconfirmed & the software’s end-to-end built UI transitions to a different screen, indicating the next prompt is to be sent. 

STEP 6: The responses are recorded in the Responses DB


## File Structure
The file structure is slightly different for the main branch and for final_project_kannada

### main
All the code lies in the code folder. Within it, Eel_GUI contains the relevant code. The helper_functions folder contanis the differnet modules used, like OCR, face recognition etc.

### final_project_kannada
This branch is more organized, with the redundant folders removed. The helper_functions folder is the same, but it's now directly in code.

## Execution
To install requirements, use "pip install -r requirements.txt".

To execute the main branch, go to the Eel_GUI folder on command prompt and enter "python app.py".
To execute the final_project_kannada branch, enter "python app.py" in the code folder itself.

The execution however requires some private keys that we could not upload on github. These are keys used for the face recognition module, OCR for aadhar detection and one ore to use notion for our databases.

