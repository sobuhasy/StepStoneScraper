
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
    await page.waitForSelector('.resultContent')

    # Extracts the job listings
    job_listings = await page.querySelectorAll('.resultContent')

    for job in job_listings:
        # Extracts the job title
        title_element = await job.querySelector('h2.title')
        title = await page.evaluate('(element) => element.textContent', title_element)

        # Extracts the company name
        company_element = await job.querySelector('a.company-link')
        company = await page.evaluate('(element) => element.textContent', company_element)

        # Extracts the location
        location_element = await job.querySelector('span.location')
        location = await page.evaluate('(element) => element.textContent', location_element)

        # Extracts the link
        link_element = await job.querySelector('a.job-link')
        link = await page.evaluate('(element) => element.href', link_element)

        # Prints the job title, company name, location, and link
        print({'Job Title/Stellenbezeichnung:', title, 'Company/Unternehmen:', company, 'Location/Standort:', location, 'Link/Link:', link})
