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



    