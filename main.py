import asyncio
from pyppeteer import launch

async def main():
    # Launches the browser
    browser = await launch(headless=False)
    page = await browser.newPage()

    # Navigates to the Stepstone website
    await page.goto('https://www.stepstone.de/')

    # Waits for the search input to be available
    await page.waitForSelector('#text-input-what')
    await page.waitForSelector('#text-input-where')

    # Types the search query
    await page.type('#text-input-what', 'Werkstudent Python')
    await page.type('#text-input-where', 'Darmstadt')

    # Clicks the search button
    await page.click('button[type="submit"]')

    # Waits for the search results to be available
    await page.waitForNavigation()

    job_listings = await page.querySelectorAll('.resultContent')
    for job in job_listings:
        # Extracts the job title
        title_element = await job.querySelector('h2.jobTitle span[title]')
        title = await page.evaluate('(element) => element.textContent', title_element)

        # Extracts the company name
        company_element = await job.querySelector('div.company_location[data-testid="company_name"]')
        company = await page.evaluate('(element) => element.textContent', company_element)

        # Extracts the location
        location_element = await job.querySelector('div.company_location[data-testid="job_location"]')
        location = await page.evaluate('(element) => element.textContent', location_element)

        # Extracts the link
        link_element = await job.querySelector('a[data-testid="job-link"]')
        link = await page.evaluate('(element) => element.href, link_element')

        # Prints the job title, company name and location
        print({'Job Title/Stellenbezeichnung:', title, 'Company/Unternehmen:', company, 'Location/Standort:', location, 'Link/Link:', link})

    # Closes the browser
    await browser.close()

# Runs the main function
if __name__ == '__main__':
    asyncio.run(main())


"""
    # Waits for the search results to be available
    await page.waitForSelector('.job-element')

    # Extracts the search results
    results = await page.evaluate('''
        Array.from(document.querySelectorAll('.job-element')).map(jobElement => ({
            title: jobElement.querySelector('.job-element__title').innerText,
            company: jobElement.querySelector('.job-element__company').innerText,
            location: jobElement.querySelector('.job-element__location').innerText,
            date: jobElement.querySelector('.job-element__date').innerText,
            link: jobElement.querySelector('.job-element__title a).href
            }))
        ''')
    
    # Prints the search results
    print(results)

    # Closes the browser
    await browser.close()

if __name__ == '__main__': 
    asyncio.get_event_loop().run_until_complete(main())
"""