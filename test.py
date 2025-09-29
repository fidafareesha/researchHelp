from grobid_client.grobid_client import GrobidClient
from bs4 import BeautifulSoup
import os
import json


def parse_div(div, parent_title=""):
    """Recursively parse <div> sections and subsections."""
    head = div.find("head").get_text() if div.find("head") else "Unknown"
    title = f"{parent_title} > {head}" if parent_title else head

    # Collect only direct paragraphs (avoid child subsections’ paragraphs)
    text = " ".join([p.get_text() for p in div.find_all("p", recursive=False)])

    # Create section object
    section = {
        "title": title,
        "content": text,
        "subsections": []
    }

    # Recursively parse child <div> (subsections)
    for sub_div in div.find_all("div", recursive=False):
        section["subsections"].append(parse_div(sub_div, parent_title=title))

    return section


def extract_sections_with_subsections(tei_file):
    if not os.path.exists(tei_file):
        raise FileNotFoundError(f"File not found: {tei_file}")

    with open(tei_file, "r", encoding="utf-8") as f:
        xml_content = f.read()


    xml_content = xml_content.replace('xmlns="http://www.tei-c.org/ns/1.0"', "")

    soup = BeautifulSoup(xml_content, "lxml-xml")

    sections = []
    # Allow recursion inside the whole document
    for div in soup.find_all("div"):
        sections.append(parse_div(div))

    return sections




client = GrobidClient(config_path="grobid_client_config.json")

client.process("processFulltextDocument", "./test")
tei_file = "./test/test.grobid.tei.xml"
sections = extract_sections_with_subsections(tei_file)

output_file = "sections.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(sections, f, indent=4, ensure_ascii=False)
    

print("Processing complete. Check the 'out' directory for results.")