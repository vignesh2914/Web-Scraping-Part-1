from bs4 import BeautifulSoup

with open ('home.html', 'r') as html_file:
    content = html_file.read()
    print(content)

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify()) #-->similar to home.html pretify does
#-----------------------------------------------------------------    
    # tags = soup.find('h5') #--> gives only one h5 taged member
#-----------------------------------------------------------------   
    # tags = soup.find_all('h5')
    # print(tags)
#-----------------------------------------------------------------
    # forms_needs = soup.find_all('h5')
    # for course in forms_needs:
    #     print(course.text)
#-----------------------------------------------------------------
    # course_cards = soup.find_all('div', class_ = 'card') #class should end with _
    # for course in course_cards:
    #     course_name = course.h5.text
    #     course_price= course.a.text

    #     print(course_name)
    #     print(course_price)
#-----------------------------------------------------------------
    
    
    course_cards = soup.find_all('div', class_ = 'card') #class should end with _

    for course in course_cards:
        course_name = course.h5.text
        course_price= course.a.text.split()[-1]

        print(course_name)
        print(course_price)


