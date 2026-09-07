# LLM / RAG Extension

Build this only after the core equity-research project is working.

## Goal
Create a citation-based research assistant that answers questions using Samyang Foods' public filings and IR materials.

## Pipeline
PDF / HTML
→ parsing
→ chunking
→ embeddings
→ vector store
→ retrieval
→ LLM answer
→ citation

## Evaluation set
Build 30-50 finance questions whose answers were manually verified during Project 01.

Evaluate:
- retrieval hit rate
- answer correctness
- numeric consistency
- citation correctness
- hallucination rate

## Example questions
- What factors drove operating-margin changes?
- What capacity expansion plans were disclosed?
- Which regions were highlighted as growth drivers?
- What risks were identified by management?
- How did working capital change as sales grew?

The key portfolio point is not merely "I built a chatbot."
It is "I built and evaluated a finance-domain retrieval system using a manually verified equity-research dataset."
