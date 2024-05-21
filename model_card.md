# Gut Neural Mapping AI Model Card

Last updated: May 2024

Inspired by [Model Cards for Model Reporting (Mitchell et al.)](https://arxiv.org/abs/1810.03993), we’re providing some accompanying information about the parameters of our developed Gut NM AI model.

## Model Overview

**Model Name:** Gut Neural Mapping AI Model  
**Version:** 1.0  
**Developer:** Kamrul Foysal, Ph.D., Data Science Analyst, Mayo Clinic 
**Model Type:** Deep Learning with Transfer Learning and Graph Search Algorithm

## Model Description

The Gut Neural Mapping AI Model is designed to map and analyze the enteric neurons in the enteric nervous system (ENS) using advanced deep learning and graph search algorithms. This model leverages transfer learning on open-source datasets to enhance the efficiency and accuracy of neural mapping.

### Key Features:
- **Transfer Learning:** Utilizes pre-trained models on extensive open-source datasets to improve performance and reduce training time.
- **Graph Search Algorithm:** Implements advanced graph search techniques for efficient and precise mapping of neural connections within the ENS.
- **Deep Learning Architecture:** Employs state-of-the-art deep learning algorithms to process complex neural data and identify patterns.
- **Software User Interface:** Visualizes neuron in 3D image and control for Human in the loop mapping with feedback.  
- **Real-time Mapping:** Develop capabilities for real-time neural mapping in clinical settings

## Intended Use

### Applications:
- **Neuroscience Research:** Facilitating detailed studies of the enteric nervous system and its functions.
- **Neuron Classification:** Extracting Morphological feature for accurate classification of neurons in the enteric nervous system.
- **Educational Purposes:** Serving as a tool for teaching and demonstrating neural mapping techniques in academic settings.

### Users:
- Neuroscientists
- Medical Researchers
- Educators in Neuroscience and Gastroenterology
- Biomedical Engineers

## Technical Specifications

### Input Data:
- **Data Type:** Neural imaging data from various open-source datasets
- **Format:** Nd2, tiff, DICOM, NIfTI, or other standard medical imaging formats
- **Preprocessing:** Data normalization, augmentation, and transformation techniques applied for optimal model performance

### Model Architecture:
- **Base Model:** Software Architecture developed in Python- tkinter package
- **Transfer Learning Model:** Pre-trained model and fine-tuned on neural imaging datasets (Neurofinder, Bigneuron, Fluroscent Neural Cell Dataset, C. ELegans neuron dataset)
- **Graph Search Algorithm:** Custom-designed algorithm based on dijkstra's algorithm for efficient neural mapping

### Output:
- **Neural Maps:** Detailed graphical representations of binarized object of single neurons in the ENS in 3D
- **Metrics:** Dice Coefficient, Intersection over Union (IoU), and other relevant performance metrics for object detection

## Performance

### Benchmarking:
- Compared against traditional neural mapping techniques and other AI-based models in the field
- Demonstrated superior performance in terms of speed and accuracy

## Ethical Considerations

- **Data Privacy:** Dataset developed in-house at Mayo Clinic Department of Physiology and Biomedical Engineering 
- **Bias Mitigation:** Regular audits and updates to prevent and correct any biases in the model
- **Transparency:** Detailed documentation and model explainability tools provided to users

## Limitations

- **Data Dependency:** Model performance is highly dependent on the quality and diversity of input data
- **Generalization:** May require additional fine-tuning for specific use cases or unique datasets

## Future Work

- **Enhanced Training:** Incorporate larger and more diverse datasets for training
- **Model Optimization:** Further optimize graph search algorithms for faster processing


## How to Use

1. **Data Preparation:** Ensure input data is in the correct format and preprocessed appropriately.
2. **Model Deployment:** Integrate the model into your research or diagnostic pipeline.
3. **Analysis:** Utilize the generated neural maps for research insights, diagnostic purposes, or educational demonstrations.

## Acknowledgments

This model leverages open-source datasets and pre-trained models, acknowledging the contributions of the open-source community and researchers in the field of neural imaging and deep learning.

For more detailed information and access to the model, please contact foysal.mdkamrulhasan@mayo.edu.

---

**Disclaimer:** This model card is intended to provide an overview and guide for the Gut Neural Mapping AI Model. Users are responsible for ensuring ethical use and compliance with relevant regulations.


