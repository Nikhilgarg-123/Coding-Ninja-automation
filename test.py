import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import pyperclip
import time
import getpass
import pyautogui

dollar = "$" * 99

# User Inputs

print('\n', dollar)


print('')
print("welcome to Coding Ninja")
print(">>This is automated file for the basics of recusion part at the coding ninjas ")
print(">>DAA")
print("*"*100)
print("made by Nikhil Garg (NG)")
print("*"*100)
print(" If anybody find any difficulty in running this file please whatsapp me at +918699470729")
print('\n',dollar)

userid=input("enter your email id : ")
password = getpass.getpass(prompt='Coding Quotient Password:')


driver = webdriver.Chrome(executable_path=".\\chromedriver.exe")   #path of driver

driver.get('https://classroom.codingninjas.com/app/classroom/batch/13514/contents/topics')

time.sleep(15)
driver.find_element_by_xpath('/html/body/app-root/app-codezen/div/app-login/div/div/div/auth-social-login-button/button').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="phoneEmail"]').send_keys(userid)
driver.find_element_by_xpath('//*[@id="mat-dialog-0"]/auth-login-dialog/div/auth-login-signup/div/auth-initial-login-form/div/div[3]/section/div/form/div[2]/div/button').click()

time.sleep(10)

driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys(password)
time.sleep(10)

driver.find_element_by_xpath('//*[@id="mat-dialog-0"]/auth-login-dialog/div/auth-login-signup/div/auth-user-login-form/div/div[2]/form/div[2]/div/button').click()
time.sleep(10)




##############mcq#############

driver.get("https://classroom.codingninjas.com/app/classroom/me/15255/content/286517/offering/3931898/problem/1235")
time.sleep(20)
driver.find_element_by_xpath('//*[@id="mat-radio-4"]/label/span[1]/span[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/div/div/app-classroom-button/a').click()
time.sleep(3)


driver.get("https://classroom.codingninjas.com/app/classroom/me/15255/content/286517/offering/3931898/problem/1236")
time.sleep(20)
driver.find_element_by_xpath('//*[@id="mat-radio-2"]/label/span[1]/span[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/div/div/app-classroom-button/a').click()
time.sleep(3)


driver.get("https://classroom.codingninjas.com/app/classroom/me/15255/content/286517/offering/3931898/problem/1234")
time.sleep(20)
driver.find_element_by_xpath('//*[@id="mat-radio-11"]/label/span[1]/span[1]').click()

time.sleep(3)
driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/div/div/app-classroom-button/a').click()
time.sleep(3)


## print number
driver.get("https://classroom.codingninjas.com/app/classroom/me/15255/content/286517/offering/3931894/problem/1176")

time.sleep(30)

Select(driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/app-codemirror-editor/div[1]/div[4]/select')).select_by_visible_text('C++ (g++ 5.4)')

time.sleep(10)

driver.find_element_by_class_name("CodeMirror-code").click()

pyautogui.hotkey('ctrl', 'a')

pyperclip.copy("""


void print(int n){
    if(n == 1){
        cout << n << " ";
        return;
    }
    
    print(n - 1);
    cout << n << " ";
}




""")

pyautogui.hotkey('ctrl', 'v')

time.sleep(5)

driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/div/div[2]/app-classroom-button/a').click()

time.sleep(15)


## power
driver.get("https://classroom.codingninjas.com/app/classroom/me/15255/content/286517/offering/3931893/problem/1121")
time.sleep(15)
Select(driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/app-codemirror-editor/div[1]/div[4]/select')).select_by_visible_text('C++ (g++ 5.4)')
time.sleep(5)
driver.find_element_by_class_name("CodeMirror-code").click()
pyautogui.hotkey('ctrl', 'a')

pyperclip.copy("""

void print(int n){
    if(n == 0) return;
    print(n-1);
    cout<<n<<" ";
}""")


pyautogui.hotkey('ctrl', 'v')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/div/div[2]/app-classroom-button/a').click()
time.sleep(15)


## NUmber of digits

driver.get("https://classroom.codingninjas.com/app/classroom/me/15255/content/286517/offering/3931895/problem/1175")
time.sleep(15)
Select(driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/app-codemirror-editor/div[1]/div[4]/select')).select_by_visible_text('C++ (g++ 5.4)')
time.sleep(5)
driver.find_element_by_class_name("CodeMirror-code").click()
pyautogui.hotkey('ctrl', 'a')

pyperclip.copy("""

int count(int n){
  if(n == 0){
    return 0;
  }
  int smallAns = count(n/10);
	return 1 + smallAns;
}

""")

pyautogui.hotkey('ctrl', 'v')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/div/div[2]/app-classroom-button/a').click()
time.sleep(15)



##sum of array

driver.get("https://classroom.codingninjas.com/app/classroom/me/15255/content/286517/offering/3931900/problem/1123")

time.sleep(20)
Select(driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/app-codemirror-editor/div[1]/div[4]/select')).select_by_visible_text('C++ (g++ 5.4)')
time.sleep(5)
driver.find_element_by_class_name("CodeMirror-code").click()
pyautogui.hotkey('ctrl', 'a')




pyperclip.copy("""
int sum(int input[], int n) {
	if(n == 1) return input[0];
	return input[0] + sum(input+1, n-1);
}

""")
pyautogui.hotkey('ctrl', 'v')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/div/div[2]/app-classroom-button/a').click()
time.sleep(15)


## first index

driver.get("https://classroom.codingninjas.com/app/classroom/me/15255/content/286517/offering/3931902/problem/1130")

time.sleep(15)
Select(driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/app-codemirror-editor/div[1]/div[4]/select')).select_by_visible_text('C++ (g++ 5.4)')
time.sleep(5)
driver.find_element_by_class_name("CodeMirror-code").click()
pyautogui.hotkey('ctrl', 'a')

pyperclip.copy("""

int firstIndex(int input[], int size, int x) {
	if(size == 0) return -1;
    if(input[0] == x) return 0;
    int ans = firstIndex(input+1, size-1, x);
    if(ans != -1) return ans + 1;
    else return -1;
}
""")

pyautogui.hotkey('ctrl', 'v')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/div/div[2]/app-classroom-button/a').click()
time.sleep(15)


## last index

driver.get("https://classroom.codingninjas.com/app/classroom/me/15255/content/286517/offering/3931903/problem/1134")

time.sleep(15)
Select(driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/app-codemirror-editor/div[1]/div[4]/select')).select_by_visible_text('C++ (g++ 5.4)')
time.sleep(5)
driver.find_element_by_class_name("CodeMirror-code").click()
pyautogui.hotkey('ctrl', 'a')

pyperclip.copy("""
int lastIndex(int input[], int size, int x){
    if(size == 0) return -1;
    int ans = lastIndex(input+1, size-1, x);    
    if(ans == -1){
        if(input[0] != x) return -1;
        else return 0;
    }    
    else return ans + 1; 
}

""")

pyautogui.hotkey('ctrl', 'v')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/div/div[2]/app-classroom-button/a').click()
time.sleep(15)


## all indices

driver.get("https://classroom.codingninjas.com/app/classroom/me/15255/content/286517/offering/3931904/problem/1135")


time.sleep(15)
Select(driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/app-codemirror-editor/div[1]/div[4]/select')).select_by_visible_text('C++ (g++ 5.4)')
time.sleep(5)
driver.find_element_by_class_name("CodeMirror-code").click()
pyautogui.hotkey('ctrl', 'a')


pyperclip.copy("""

int allIndexes(int input[], int size, int x, int output[]) {
 if(size == 0) return 0;
    int ans = allIndexes(input+1, size-1, x, output);
    for(int i=0; i<ans; i++) output[i] += 1;
    if(input[0] == x){
        for(int i=ans-1; i>=0; i--) output[i+1] = output[i]; 
        output[0] = 0;
        return ans + 1;
    }
    else return ans;
}
int allIndexes2(int input[], int size, int x, int output[]){
    if(size == 0) return 0;
    int ans = allIndexes2(input, size-1, x, output);
    if(input[size - 1] == x){
        output[ans] = size - 1;
        return ans + 1;
    }
    else return ans;
}

""")

pyautogui.hotkey('ctrl', 'v')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/div/div[2]/app-classroom-button/a').click()
time.sleep(15)

## check Number

driver.get("https://classroom.codingninjas.com/app/classroom/me/15255/content/286517/offering/3931901/problem/1124")


time.sleep(15)
Select(driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/app-codemirror-editor/div[1]/div[4]/select')).select_by_visible_text('C++ (g++ 5.4)')
time.sleep(5)
driver.find_element_by_class_name("CodeMirror-code").click()
pyautogui.hotkey('ctrl', 'a')

pyperclip.copy("""

bool checkNumber(int input[], int size, int x) {
  if(size==0)
      return false;
    
 if(input[0]==x)
     return true;
    
    bool checksmaller= checkNumber(input +1,size-1,x);
    return checksmaller;

}

"""
)

pyautogui.hotkey('ctrl', 'v')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="right-container"]/app-problem-detail-right-panel/div/div[2]/app-classroom-button/a').click()
time.sleep(15)









