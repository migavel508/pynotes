
from datetime import datetime
import os
import subprocess
from pathlib import Path

# Directories
NOTEBOOK_DIR = "./notebooks"  # Directory containing .ipynb files
OUTPUT_DIR = "./content"     # Directory for .md files (Pelican content directory)

# Step 1: Convert notebooks to Markdown
def convert_notebooks_to_markdown(notebook_dir, output_dir):
    notebook_dir = Path(notebook_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for notebook in notebook_dir.glob("*.ipynb"):
        print(f"Converting {notebook} to markdown...")
        cmd = [
            "jupyter",
            "nbconvert",
            "--to",
            "markdown",
            "--output-dir",
            str(output_dir),
            str(notebook),
        ]
        subprocess.run(cmd, check=True)
        # Add metadata to the generated Markdown file
        add_metadata_to_markdown(output_dir / f"{notebook.stem}.md")

# Step 2: Add metadata to Markdown
def add_metadata_to_markdown(markdown_file):
    # Get file modification time and format it as YYYY-MM-DD
    file_mtime = datetime.fromtimestamp(Path(markdown_file).stat().st_mtime)
    formatted_date = file_mtime.strftime("%Y-%m-%d")

    metadata = f"""---
title: {markdown_file.stem.replace('_', ' ').title()}
date: {formatted_date}
author: Raja CSP
---
"""
    print(f"Adding metadata to {markdown_file}...")
    content = markdown_file.read_text()
    markdown_file.write_text(metadata + "\n" + content)

# Step 3: Generate site with Pelican
def generate_site_with_pelican(content_dir):
    print("Generating site with Pelican...")
    cmd = ["pelican", str(content_dir)]
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    # Ensure required directories exist
    Path(NOTEBOOK_DIR).mkdir(parents=True, exist_ok=True)
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    # Convert notebooks and generate site
    convert_notebooks_to_markdown(NOTEBOOK_DIR, OUTPUT_DIR)
    generate_site_with_pelican(OUTPUT_DIR)

    print("Site generated successfully!")

