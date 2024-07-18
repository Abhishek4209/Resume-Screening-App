# Resume Screen App README

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Input Data](#input-data)
  - [Running the App](#running-the-app)
  - [Output Data](#output-data)
- [Methodology](#methodology)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The Resume Screen App is a tool designed to automate the process of screening resumes using Natural Language Processing (NLP) techniques, specifically the Term Frequency-Inverse Document Frequency (TF-IDF) method. This application helps recruiters and hiring managers quickly identify the most relevant candidates based on the content of their resumes.

## Features

- **Automated Resume Screening**: Quickly process and rank resumes based on relevance to job descriptions.
- **NLP and TF-IDF**: Utilizes TF-IDF to determine the importance of terms within resumes.
- **User-Friendly Interface**: Simple command-line interface for ease of use.
- **Customizable**: Easily adapt the app for different job descriptions and requirements.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Abhishek4209/Resume-Screening-App
    cd resume-screen-app
    ```

2. **Create and activate a virtual environment**:
    ```sh
    conda create -p venv python==3.11
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Input Data

- **Resumes**: A directory containing resumes in text format.
- **Job Description**: A text file containing the job description.

### Running the App

1. **Prepare your data**: Ensure all resumes are in a single directory and the job description is in a text file.
2. **Run the app**:
    ```streamlit run app.py
   stre
    ```

### Output Data

- **Ranked Resumes**: The app will output a list of resumes ranked by relevance to the job description.

## Methodology

The Resume Screen App uses the TF-IDF method to evaluate the importance of terms in each resume relative to the job description. Here's a brief overview of the steps:

1. **Term Frequency (TF)**: Calculates the frequency of terms in each resume.
2. **Inverse Document Frequency (IDF)**: Evaluates how common or rare a term is across all resumes.
3. **TF-IDF Calculation**: Combines TF and IDF to score each term's importance in the context of the job description.
4. **Resume Ranking**: Aggregates term scores to rank resumes by overall relevance.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes.
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature-branch`
6. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or inquiries, please contact [yourname](abhishekupadhyay9336@gmail.com).

---

Feel free to customize this template according to your specific application details and requirements.