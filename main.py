# This is the introductory file for this programs repository
# In this file you will be guided through downloading your Instagram profiles information and how you can use this repository to find out specific information

def _introduction():
    print("Welcome!")
    print("Follow these simple steps to access and display various information related to your Instagram account: \n")
    _directions()

def _directions():
    print("1: Open Instagram on your computer and log in to the account you want to use.")
    print("2: Find the hamburger button in the bottom left corner of your screen, click it, and select \"Settings.\" This action will take you to another page.")
    print("3: On the displayed information page, locate and click \"See more in Account Center\" in the upper middle section. You'll be redirected again.")
    print("4: Now, click on \"Your Information Permissions,\" then \"Download Information,\" and finally, select \"Request Download.\"")
    print("5: To finish, click \"Complete Copy,\" fill in the date range, your email, and choose the JSON format. Submit the request. \n")
    print("Now, simply wait for Instagram to notify you via email when the download is ready!")

_introduction()