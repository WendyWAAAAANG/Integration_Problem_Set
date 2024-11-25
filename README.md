# Dataset Project: Integration Problem Set
### Author: Ruoxin Wang
### Date: Nov.26.2024

## Overview
This project aims to create a dataset specifically designed for the automatic generation of integration problems. It will serve as the basis for training LLMs to generate integration problems. The problems will be labeled by difficulty and category, making it easy for users to select problems.

## Motivation
Generating diverse and enough integration problems for practice or exams can be time-consuming. We provide this dataset for fine-tuning LLMs and ask LLMs to generate integration problems. Compared to letting LLMs generate problems directly, a dataset built with symbolic computation and verified mathematical problems ensures higher accuracy and strict adherence to mathematical rules than GPT-generated questions. Secondly, this dataset offers diverse problem types and controlled difficulty levels, something GPT might struggle with in maintaining consistency. Automating the generation of integration problems can provide students with endless opportunities for practice and help them get a deeper conceptual understanding. And teachers can benefit from automated systems that reduce the workload of creating custom problem sets. This system could also be valuable in building AI educational technology platforms.

## What Has Been Done Before / Existing Datasets?
1. ![Google-DeepMind Mathematics Dataset](https://github.com/google-deepmind/mathematics_dataset): Provides a variety of mathematical problems, including algebra and calculus, but does not focus specifically on integration problems.
2. ![Khan Academy](https://www.khanacademy.org/math/calculus-1): Popular online learning platform offering integration practice problems, but these problems are not structured as datasets suitable for machine learning tasks.
3. ![Symbolab](https://www.symbolab.com/), ![Paul’s Online Math](https://tutorial.math.lamar.edu/) and ![Wolfram Alpha](https://www.wolframalpha.com/): Widely used online calculators capable of solving integration problems, but they are not designed for large-scale dataset generation.

## Data Type
The dataset in JSON format, consists of a wide variety of integration problems, difficulty level, and category. Below is an example demonstrating how data will be stored:
```bash
  [
      {
          "difficulty": "Advanced",
          "category": "Integration by Parts",
          "question": "\u222b\nxtan(x)\ncos2(x)\n dx"
      },
      {
          "difficulty": "Basic",
          "category": "Partial Fractions",
          "question": "\u222bcos(3t)sin(8t)dt"
      },
  ]
```

## Uniqueness About This Dataset
Nowadays, there is no large-scale dataset available in the public domain explicitly focusing on integration problems, although the collection of integration problems in a systematic manner can be an effective way to meet the requirement of problem generation. Current datasets are insufficient for teaching advanced calculus problem generation and do not contain detailed step-by-step problems which is an important component of learning.
1. Comprehensive Coverage of Integration Techniques: The dataset will incorporate all forms of integration issues with basic, intermediate, and advanced integration issues covered. It includes basic integration, substitution, integration by parts, etc Integration by parts computes the integral with the help of integration of other functions.
2. Diversity of Functions: The dataset will include integrals of various classes of functions which in fact will include polynomial, trigonometric, logarithmic, exponential, and hyperbolic functions.

## Power Analysis


## Data Collection Protocol
1. Textbooks: Stewart’s Calculus, Apostol’s Calculus
2. Web Scraping from Open-Source Online Platform:![Symbolab](https://www.symbolab.com/), ![Paul’s Online Math](https://tutorial.math.lamar.edu/)

## Open Source Dataset
The open-source dataset can be found at: ![Roxanne-WANG/Integration_Problem_Set](https://huggingface.co/datasets/Roxanne-WANG/Integration_Problem_Set)

## Explory Data Analysis
**1. Category Distribution**
![Figure_1](https://github.com/user-attachments/assets/89ded859-a8aa-410a-9ed7-8e3c398f4f04)
  - The most frequent category is "Trigonometric Substitution", followed by "Constant Rule", and "Multiple Integrals".
  - Less frequent categories include "Integration by Parts", "Partial Fractions", and "Power Rule".
  - Trigonometric Substitution appears to dominate, likely indicating its prevalence in integration problems or its importance in the dataset focus.
  - Graph Summary: A horizontal bar chart highlights the frequency of each category, emphasizing the dominance of certain categories over others.

**2. Question Length Distribution**
![Figure_2](https://github.com/user-attachments/assets/ed490643-1ffc-4256-ba61-fc5603687872)
  - Most questions have a length between 8 and 14 characters, indicating a tendency for a concise representation of problems.
  - There is a right-skewed distribution, with fewer questions having lengths exceeding 25 characters.
  - Longer questions might represent more complex integrals with multiple terms or variables.
  - Graph Summary: A histogram with a KDE overlay shows the distribution of question lengths, with a peak of around 10 characters.

**3. Difficulty Distribution**
![Figure_3](https://github.com/user-attachments/assets/e14cf74e-01ad-4ea9-9290-0db0c6ef1cb9)
  - Questions are evenly distributed across the three difficulty levels: Advanced, Moderate, and Basic.
  - Advanced problems slightly outnumber the others, suggesting a focus on challenging questions.
  - The uniform distribution ensures representation across skill levels, making the dataset comprehensive for different audiences.
  - Graph Summary: A vertical bar chart illustrates the similar proportions of problems in each difficulty tier.

**4. Word Cloud Analysis**
![Figure_4](https://github.com/user-attachments/assets/43dfa821-22bb-4f16-a435-b5c8230900ab)
  - Common terms in questions include symbols like x, dx, sin, cos, and numerical constants such as 2, 3, and 4.
  - These terms indicate a heavy focus on single-variable integrals and common trigonometric or polynomial components.
  - Patterns like tan, ln, and higher powers suggest questions often involve transcendental functions or logarithmic integrations.
  - Graph Summary: A word cloud visualizes the most frequently occurring terms, emphasizing the focus on fundamental and advanced mathematical symbols.

## License
This dataset is licensed under the [MIT License](https://opensource.org/licenses/MIT).



