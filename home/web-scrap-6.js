const puppeteer = require('pyppeteer');
const { Builder, By, Key, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');

(async () => {
    // Launch a headless Chrome browser with Puppeteer
    const browser = await pyppeteer.launch();
    const page = await browser.newPage();
    
    // Enable request interception
    await page.setRequestInterception(true);
    
    // Listen for XHR requests
    page.on('request', async (request) => {
        if (request.resourceType() === 'xhr') {
            console.log('XHR Request URL:', request.url());
            
            // Here you can extract data from the XHR response or perform other actions
        }
        request.continue();
    });
    
    // Simulate login with Selenium WebDriver
    const driver = await new Builder()
        .forBrowser('chrome')
        .setChromeOptions(new chrome.Options().headless())
        .build();
    
    await driver.get('https://example.com/login');
    
    // Find username and password fields, fill them, and click login
    await driver.findElement(By.id('username')).sendKeys('your_username');
    await driver.findElement(By.id('password')).sendKeys('your_password', Key.RETURN);
    
    // Wait for page to load after login
    await driver.wait(until.urlIs('https://example.com/dashboard'), 10000);
    
    // Close Selenium WebDriver
    await driver.quit();
    
    // Close the browser when done
    await browser.close();
})();
