# %%
import requests
import re
from bs4 import BeautifulSoup

class countryList:
    """
    Object with two dictionaries that track countries and their official two-letter abbreviation.
    """
    def __init__(self):
        self.nameToCode, self.codeToName = self.activate()
        self.g_twenty_codes = ["AR",
                               "AU",
                               "BR",
                               "CA",
                               "CN",
                               "FR",
                               "DE",
                               "IN",
                               "ID",
                               "IT",
                               "JP",
                               "KR",
                               "MX",
                               "RU",
                               "SA",
                               "ZA",
                               "TR",
                               "GB",
                               "US"]
        self.g_twenty = self.activate_g_twenty()
        
    def activate(self):
        # Create two dictionaries
        nameToCode, codeToName = {}, {}
        # Ensure whitespace elimination
        name_pattern = re.compile(r"^\s*(.*\w+)\s*$")
        code_pattern = re.compile(r"\s*([A-Z]{2})\s*")
        # Retrieve html page
        req = requests.get("https://www.nationsonline.org/oneworld/country_code_list.htm").text
        soup = BeautifulSoup(req, 'lxml')
        # Get the table with all the necesary rows
        table = soup.find("div", id="content")
        rows = table.find_all("tr")
        # First input worldwide
        nameToCode["WorldWide"] = ""
        codeToName[""] = "Worldwide"

        for row in rows:
            cells = row.find_all("td")
            # So as to eliminate non-country rows
            if len(cells) > 2:
                # Eliminate whitespace
                name = name_pattern.sub(r"\1", cells[1].text)
                code = code_pattern.sub(r"\1", cells[2].text)
                # Assign to two dictionaries
                nameToCode[name] = code
                codeToName[code] = name
                
        return nameToCode, codeToName
    
    def activate_g_twenty(self):
        result = {}
        for code in self.g_twenty_codes:
            result[self.ctn[code]] = code
        return result
    
    @property
    def ntc(self):
        return self.nameToCode
    
    @property
    def ctn(self):
        return self.codeToName
    
    @property
    def g_20(self):
        return self.g_twenty

# %%


