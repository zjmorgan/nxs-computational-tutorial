# nxs-computational-tutorial-2025

## Agenda

### Set up 
1. Log into `analysis.sns.gov`
2. Run script `start_jupyter.sh` provided by Jean B. in /EXAMPLES/NXS2025/

### Intro presentation (powerpoint) 30-45 mins. 
 * What is scientific software (MG) 
 * Version control: Git and GitHub (MG) 
 * Environment management (micromamba, pixi and pip) (JB): 
 * Running python options: scripts, python interpreter, IDE, jupyter (JB) 
 * Intro to file systems at ORNL. Where are my neutron data stored? Oncat (AS) 
 * AI (YZ)

### Tutorial  

#### Malcolm tutorial

* create a git repo

#### Jean tutorial
 
 * Open notebook, Explanation of notebook (shift enter, shift enter...) 
 * Cell: imports:  
 * Exercise 1: Import data from ascii to numpy array. Do this multiple ways. Mention pandas. 
 * Exercise 2: Plot with matplotlib. Make it interactive. Show errors? 
 * Exercise 3: Extend script to for loop over multiple files 
 * Exercise 4: Create widget to do Exercise 3.  

BREAK (AS) 

#### Zach Tutorial 2 

 * Exercise 4 (SciPy): Set up fit to a peak: initial conditions, define to fit, define residual, define fit range, interpret errors (variance-covariance matrix) 
 * Exercise 5: Use LMFIT for same process.  
 * Advanced Exercise 1: Event data: Inspect nxs file with HDFView, 
 * Load neutron data and log metadata from nxs file with h5py. 
 * Advanced Ex 2: histogram events (with log binning) 
 * Super Advanced Ex 3: Re-use fitting script, fit peaks, plot position versus experimental log.   

### AI Tutorial 3

 * Brief intro to LLM and relevant techniques (e.g., `RAG`), from a research user point of view.
 * Tools for research
    * `notebookLM`
    * `NapkinAI`
    * `Perplexity`
    * image generation models/tools.
 * Tools for programming
    * Web-based chat services (`chat.com`, `gemini`, `claude`, etc.)
    * IDEs, such as `Cursor`, `GitHub Copilot` in `VSCode`, `Zed`, `VSCodium`, ... you name it...
    * CLI tools, `Codex` by `OpenAI`, `Claude Code` by `Anthropic`, `Gemini CLI` by `Google`, etc.
 * Integrations
    * Unified platform for LLMs, e.g., `OpenRouter`
    * Self-hosted options
        * Personal service with access to LLMs through APIs.
        * Pay by API call, counting by input/output tokens
        * `LobeHub`, `Dify`, etc.
        * `Dify` as an example for demo
            * LLMs access
            * Tools integration, search via `Google` & `Perplexity`, `Slack`, `DALL-E`, etc.
            * Personal knowledge base for RAG
    * Implementation in workflow platforms
        * `n8n` as an example
            * Chat to GPT models in `Slack`
            * AI summary and auto posting
