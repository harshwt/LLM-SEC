# Secure AI Supply Chain Experiment

This directory contains the artifacts, documentation, and Proof of Concepts (POCs) for experiments conducted on AI Supply Chain Security. The project focuses on detecting and mitigating vulnerabilities in Machine Learning models, specifically targeting unsafe serialization formats and malicious model architectures.

## Overview

Machine Learning models are often shared using serialization formats that can execute arbitrary code upon loading. This project demonstrates how an attacker can hide malicious payloads inside model files and how security analysts can detect them using static analysis tools.

### Key Objectives
1. **Unsafe Pickle Analysis**: Identifying arbitrary code execution payloads hidden in `.pkl` files.
2. **Model Extraction**: Using decompilation tools to extract the exact malicious payloads from serialized models.
3. **Malicious Model Architectures**: Detecting arbitrary Python code execution hidden inside Keras/TensorFlow `.h5` model architectures (e.g., via `Lambda` layers).
4. **Safe Alternatives**: Demonstrating why formats like `.safetensors` are more secure alternatives to Python's native `pickle`.

## Tools Utilized
- **[ModelScan](https://github.com/protectai/modelscan)**: Used to scan serialized models for unsafe operators (like `os.system`).
- **[Fickling](https://github.com/trailofbits/fickling)**: A decompiler, static analyzer, and bytecode rewriter for Python pickle objects.
- **Custom H5 Inspector**: A custom script (`inspect_h5_model.py`) used to parse HDF5 model files and look for suspicious layers like `Lambda`.

## Directory Structure
- `assets/`: Contains screenshots and visual artifacts from the lab environment experiments.
- `docs/`: Detailed walkthroughs and documentation of the analysis (e.g., `static_analysis_walkthrough.md`).
- `poc/`: Proof of Concept scripts demonstrating how the vulnerabilities are crafted (e.g., `malicious_pickle_demo.py`).

## Getting Started
Please refer to the [Static Analysis Walkthrough](./docs/static_analysis_walkthrough.md) for a step-by-step breakdown of how the models were analyzed and what vulnerabilities were uncovered.
