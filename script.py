import nbformat

# Load your notebook
notebook_path = "ScientificPaperSummarization_QnA_cleaned.ipynb"
nb = nbformat.read(notebook_path, as_version=nbformat.NO_CONVERT)

# Remove broken widgets metadata
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

# Save the fixed notebook
fixed_path = notebook_path.replace(".ipynb", "_fixed.ipynb")
nbformat.write(nb, fixed_path)

print(f"✅ Fixed notebook saved as: {fixed_path}")
