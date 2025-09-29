# ResearchHelp Backend

FastAPI backend for extracting structure from research PDFs (sections, figures, tables), running OpenAI-powered claim extraction, and finding supporting evidence in the paper.

## Quickstart

1. Create and activate a virtual environment
```bash
python -m venv .venv
".venv\\Scripts\\activate"
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set environment variables
```bash
copy .env.example .env
# Edit .env and add OPENAI_API_KEY=...
```

4. Run the server
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open http://localhost:8000/docs for API docs.

## Project Structure

```
app/
  main.py
  config.py
  routers/
    processing.py
  services/
    pdf_extractor.py
    section_segmenter.py
    openai_claims.py
    evidence_finder.py
  models/
    schemas.py
```

## Security
- This service does not store PDFs by default; files are processed in-memory.
- Validate and sanitize inputs; PDFs can be malformed. Consider sandboxing.

## License
MIT
