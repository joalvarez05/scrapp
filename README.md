How to Use the Program
This program lets you scrape prices from a website using Python. Below, I’ll walk you through the steps to set it up and get it working.

1) First, before you dive in, you need to install two tools: requests and BeautifulSoup. Just open your terminal and type in the command pip install requests beautifulsoup4.

2) Next, check out line 5 in the code where it says url = '#'. This is where you’ll put the web address of the page you want to get prices from.

3) Now, let’s modify the price class. The program looks for prices on the page using a specific class called showPrice. You’ll need to check the website you’re about to scrape to see what class name it uses. Also, make sure to decide whether to use classes or IDs based on your needs. If you find that the price class is something like "offers," then change it accordingly.

4) Run the program!

5) Finally, the program will search for prices on the webpage and show you all the prices that are less than 10,000 if that's what you want. If it doesn’t find any prices, it’ll let you know that no elements were found.
