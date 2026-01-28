from groq import Groq
from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas
import os 

#manually add the API key here 
client = Groq(api_key='GROQ_API_KEY') #setting up the client 


def llm_call(user_prompt, system_instruction): 

    print(f"instruction to the llm: {system_instruction}")

    response = client.chat.completions.create(

        model = "llama-3.1-8b-instant", #choosing the model 

        messages = [
            {"role":"system", "content": system_instruction},
            {"role": "user", "content": user_prompt }
        ],

        temperature = 0.4

        #other keys: top_k, top_p, max_tokens 
    )

    print(response.choices[0].message.content)

#higher temp = creative 
#system instruction creates the base, like "You are a HR filtering resumes" and user message is "Tell me th best way to", 0.3 has better answers. 
#top_k defines top tokens. internal filter
#top_p. value lies between 0 to 1. nuclear samplampling. if top_p = 0.8, it gives top <= 80%
#max_tokens = 10000 - defines bucket of total request and response. 

#doesn't work without internet connection. 

def pdf_to_text(filename):

    doc = PdfReader(filename)

    file = f"{filename.split('.')[0]}.txt"
    
    with open(file, 'w') as dest_file:
        
        for page in doc.pages: 

            line = page.extract_text()

            dest_file.write(line)

    return file

def llm_call_until_0(user_input, system_instruction): 

    n = 1

    while n not in [0, '0']: 

        llm_call(user_input, system_instruction)

        print("---------------")
        print("Exectued the llm call")
        print("---------------")

        n = (input("To exit enter 0. else, type any other key: "))

def HR_role(): 

    print("Activating the function.")

    job_description = '''About the work from home job/internship
    Selected intern's day-to-day responsibilities include:

    1. Collaborate with our team of experienced developers to design and implement Python-based solutions for our clients
    2. Write clean, efficient, and maintainable code to develop software applications and tools
    3. Participate in code reviews and provide constructive feedback to your peers
    4. Assist in troubleshooting and resolving technical issues to ensure the smooth functioning of our applications
    5. Learn and utilize best practices in software development to contribute to the success of our projects
    6. Stay up-to-date with the latest trends and advancements in Python development to enhance your skills
    7. Take initiative in tackling new challenges and contribute creative ideas to improve our products and processes'''

    system_instruction = f'''You are the HR of my company. Help me choose valuable employees for my company. 
    judge the given resume and determined whether he is a valuable employee or not. check whther they match with the job description: {job_description} or not. 
    The resume is given ad the user prompt. Be a harsh critic'''

    resume_file_name = input("Please upload your resume pdf to this directory and enter it's name here: ")

    print("Converting the pdf to text")

    text_file = (pdf_to_text(resume_file_name))

    print("calling the llm function to judge the Resume.")

    with open(text_file, 'r') as read_file: 
        resume_text = read_file.readlines()

    resume_text = " ".join(lines for lines in resume_text  )

    #DEBUG print(resume_text)

    llm_call(resume_text, system_instruction)

    print("Exected the call")

def main(): 

    #pdf_to_text('Resume.pdf')

    system_instruction = "You are my tutor." 

    user_prompt = input("Enter the user prompt over here: ") #taking the user prompt 

    #llm_call_until_0( user_prompt, system_instruction)

    HR_role()


if __name__ == '__main__': 

    #print("Please enter your API key: ")

    #groq api key is in notepad

    HR_role()
