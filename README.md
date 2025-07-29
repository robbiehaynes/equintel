# Equintel

AI-powered horse racing prediction system that fetches, processes, and analyzes race data.

## Overview

Equintel is a data pipeline system that:

1. Fetches racecards and results from TheRacingAPI
2. Processes and formats the data
3. Uploads the processed data to a Supabase database
4. Provides tools for data analysis and model training

The system runs on GitHub Actions workflows to automatically update data daily.

## Architecture

Equintel consists of two main data pipelines:

### Racecards Pipeline
- **Fetch**: Retrieves daily racecards from TheRacingAPI
- **Format**: Processes raw JSON into structured dataframes
- **Upload**: Stores formatted data in Supabase

### Results Pipeline
- **Fetch**: Retrieves race results from TheRacingAPI
- **Format**: Processes raw JSON into structured dataframes
- **Upload**: Stores formatted data in Supabase

## Setup

### Prerequisites
- Python 3.9+
- [uv](https://github.com/astral-sh/uv) package manager
- Supabase account
- TheRacingAPI credentials

### Environment Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/equintel.git
cd equintel
```

2. Create and activate virtual environment:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

4. Create a `.env` file with your credentials:
```
API_URL=https://your-racing-api.com/api
API_USER=your_username
API_PASS=your_password
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

## Usage

### Manual Data Pipeline Execution

To manually run the racecards pipeline:
```bash
python racecards/fetch.py
python racecards/format.py
python racecards/upload.py
```

To manually run the results pipeline:
```bash
python results/fetch.py
python results/format.py
python results/upload.py
```

### Jupyter Notebook

For exploratory data analysis and model development:
```bash
jupyter notebook equintel.ipynb
```

## Automated Workflows

Equintel uses GitHub Actions for automation:

- **Racecards Pipeline**: Runs daily at 05:15 UTC to fetch the day's racecards
- **Results Pipeline**: Runs daily at 22:15 UTC to fetch the day's race results

The workflows can also be triggered manually from the GitHub Actions tab.

## Data Structure

### Racecards Data
- Race details: ID, course, distance, type, etc.
- Horse details: ID, name, age, sex, etc.
- Race conditions: going, weather, surface, etc.

### Results Data
- Race ID
- Horse ID
- Position
- Draw

## Development

### Adding Features

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Environment Variables for GitHub Actions

Set these in your repository settings under Secrets and Variables:

- `API_URL`: Base URL for the racing API
- `API_USER`: Username for API authentication
- `API_PASS`: Password for API authentication (as a secret)
- `SUPABASE_URL`: Your Supabase project URL
- `SUPABASE_KEY`: Your Supabase service key (as a secret)

## Project Structure

```
equintel/
├── racecards/         # Racecards pipeline
│   ├── fetch.py       # API fetching script
│   ├── format.py      # Data processing script
│   └── upload.py      # Supabase upload script
├── results/           # Results pipeline
│   ├── fetch.py       # API fetching script
│   ├── format.py      # Data processing script
│   └── upload.py      # Supabase upload script
├── output/            # Processed data storage
├── .github/workflows/ # CI/CD pipeline definitions
├── equintel.ipynb     # Jupyter notebook for analysis
└── requirements.txt   # Python dependencies
```

## Contact

For queries or suggestions, contact robhaynes0420@gmail.com
