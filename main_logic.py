from lxml import html
import heapq
from urllib.parse import urljoin
import statistics

### Offline Logic: Analyze saved HTML and extract high-level content ###

# Main function to process the saved HTML page
def process_source_page(url, source_page, content_filter='//*[@class]', top_class=50, debug_mode=False):
    # Main function to process the saved HTML page
    ## Step 1: Load the saved HTML page
    page = ''
    with open(source_page, 'r', encoding='utf-8') as html_file:
        page = html_file.read()

    tree = html.fromstring(page)

    ## get only required content ##
    web_content = tree.xpath(content_filter)

    #------------------------------// finding top_itms //---------------------------------------------------------#
    
    return tree, top_items



# ----------------------------------------------------------------------------------------------------------------------------------



# Identify high-level class based on text content analysis
def find_high_level_class(tree, top_items, lower_percentile=5, upper_percentile=95, debug_mode=False):

    max_len = 0
    high_level_class = None

   #--------------------------//rest of the code //--------------------------------------------#

    return high_level_class


# -----------------------------------------------------------------------------------------------------------------------

# Determine the most relevant tag name for the high-level class elements
def get_relevent_tag(doc, high_level_class, debug_mode=False):

    # Collect all elements with the same class
    elements = doc.xpath(f"//*[contains(@class, '{high_level_class}')]")

    #--------------------------// finding most relevent tag name //---------------------------------------------#

    print(f"Most relevant tag name: {closest_tag_name}")
    return closest_tag_name




# Extract and save content from high-level class elements
def extract_and_save_content(url, tree, high_level_class, tag_name, include_links, output_file='zoutput.txt'):
    if high_level_class is not None:
        try:
            ## Get the desirable elements
            high_level_elements = tree.xpath(f'//{tag_name}[contains(@class, "{high_level_class}")]')
            data = []
            links_in_data = []
            base_url = url
            for element in high_level_elements:
                # Clean and normalize text
                text = element.text_content().strip().replace('\n', ' ').replace('\t', ' ')
                while '  ' in text:
                    text = text.replace('  ', ' ')
                
                data.append(text)
                raw_links = element.xpath('.//a/@href')
                all_links = []

                for href in raw_links:
                    # Add raw link
                    all_links.append(href)
                    # Add absolute link if relative
                    if href and not href.lower().startswith(('http://', 'https://', 'mailto:', 'javascript:')):
                        abs_link = urljoin(base_url, href)
                        all_links.append(abs_link)
                links_in_data.append(all_links)

            with open(output_file, 'w', encoding='utf-8') as f:
                for i, (item, link) in enumerate(zip(data, links_in_data)):
                    f.write(f'## Element {i+1} ##\n')
                    f.write('-'*80)
                    f.write(f'\nText: \n{item}\n\n')
                    if include_links:
                        f.write(f'Links: \n{link}\n')
                    f.write('-'*80 + '\n\n')



        except (Exception):
            print("Could not extract high-level elements due to session, timeout, or selector error.")
    else:
        print("No high-level class found.")