from main_logic import process_source_page, find_high_level_class
from main_logic import get_relevent_tag, extract_and_save_content
from page_links import links
# Using undetected_chromedriver to avoid bot detection
import undetected_chromedriver as uc 

## Setting Parameters ##
link_index = 10  # 1-based index
page = 'zsource_page.txt'
content_filter='//div[@class]'

top_class=50
lower_percentile=5
upper_percentile=95
output_file='zoutput.txt'
include_links= False  # whether to include links in the output
url = links[link_index - 1]  # zero based index

debug_mode= True # whether to print debug information
# headless = True  # whether to run browser in headless mode

if __name__ == "__main__":


     # Step 1: Load the webpage and save the HTML
     print(f"Fetching URL: {url}")
     driver = uc.Chrome(headless=False, use_subprocess=False)
     driver.get(url)
     # Wait for manual CAPTCHA solving if needed
     input('Please solve any CAPTCHA or "Are you a robot?"')
     # Save the entire HTML page
     with open(page, 'w', encoding='utf-8') as f:
          f.write(driver.page_source)
     print(f"Page saved as {page}.")
     driver.quit()


     # Step 2: Process the saved HTML to find top classes
     tree, top_items = process_source_page(url, page, content_filter, top_class, debug_mode)
     print(f"Processed source page and identified top classes.")

     # Step 3: Identify high-level class based on text content analysis
     high_level_class = find_high_level_class(tree, top_items, lower_percentile, upper_percentile, debug_mode)

     tag_name = get_relevent_tag(tree, high_level_class, debug_mode)

     # Step 4: Extract and save content from high-level class elements
     extract_and_save_content(url, tree, high_level_class, tag_name, include_links, output_file)
     