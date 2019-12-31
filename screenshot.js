const puppeteer = require('puppeteer');


async function screenshot(url, path) {
	const browser = await puppeteer.launch();
	const page = await browser.newPage();
	await page.goto(url);
	await page.screenshot({ fullPage: true, path: path });
	await browser.close();
};


screenshot("https://digital-land.github.io/", "screenshot.png");
