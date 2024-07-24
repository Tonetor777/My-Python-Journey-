#  Phone Number and Email Address Extractor
""" Say you have the boring task of finding every phone number and email 
address in a long web page or document. If you manually scroll through 
the page, you might end up searching for a long time. But if you had a program that could search the text in your clipboard for phone numbers and 
email addresses, you could simply press ctrl-A to select all the text, press 
ctrl-C to copy it to the clipboard, and then run your program. It could 
replace the text on the clipboard with just the phone numbers and email 
addresses it finds """

import re , pyperclip
text = str(pyperclip.paste())
matchdic = {"phone":[] , "email":[]}
allmatches = ""

phoneNumber = re.compile(r'''(\+2519|09) (\d{8})''' , re.VERBOSE)
emailregex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z.-]+ 
\.[a-zA-z]{2,4}                   
)''' , re.VERBOSE)



matches = phoneNumber.findall(text)
emails = emailregex.findall(text)
matchdic["phone"].extend(code+phone for (code , phone) in matches )
matchdic["email"].extend(email for email in emails)

def joinmatches (data):
    global allmatches
    allmatches += f"{'Phone Numbers':<20}{'Emails':<30}\n"
    allmatches += "-"*50 + "\n"
    max_length = max(len(matchdic["phone"]), len(matchdic["email"]))
    for i in range (max_length):
        phone = data["phone"][i] if i < len(data["phone"]) else ""
        email = data["email"][i] if i < len(data["email"]) else ""
        allmatches += f"{phone:<20}{email:<30}\n"

joinmatches(matchdic)
pyperclip.copy(allmatches)

# Use the text below to try it
""" 
Hello everyone,

I hope this message finds you well. As we prepare for the upcoming project, I wanted to share some important contact details and updates with you.

First, for any project-related queries, please reach out to the following individuals:

1. John Doe, our project manager, can be contacted at +251911234567 or via email at john.doe@example.com. He will be your primary point of contact for any major concerns.
2. Jane Smith, our lead developer, is available at 0911123456. She prefers communication via her work email, jane.smith@devteam.com.
3. For design-related questions, you can contact Michael Brown at +251922345678 or michael.brown@designpro.com.
4. Our QA specialist, Emily Davis, can be reached at 0912234567. Her email address is emily.davis@qateam.org.
5. Finally, for any administrative issues, please get in touch with David Johnson at +251933456789. His email is david.johnson@adminsupport.net.

Additionally, for general inquiries, you may contact our support team at support@company.com. For media and public relations, reach out to pr@company.com.

Thank you for your attention to these details. We look forward to a successful collaboration.

Best regards,
Management Team

"""