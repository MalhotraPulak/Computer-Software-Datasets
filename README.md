## Computer Software Datasets

### Directory structure:
- Each data source has its own folder
- Inside the folder there are self contained jupyter notebooks and python scripts for data processing and collection
- Analysis folder as jupyter notebooks for different kinds of analysis, the gephi project is also present

### Dataset
`./datasets` contains final structured dataset released by us.
```
.
├── dense
│   ├── apt_data.tsv
│   ├── brew_data.tsv
│   ├── choco_data.tsv
│   ├── macports_brew_merge_data.tsv
│   └── macports_data.tsv
└── complete
    ├── apt_data.tsv
    ├── brew_data.tsv
    ├── choco_data.tsv
    ├── macports_brew_merge_data.tsv
    └── macports_data.tsv
```

### Reading Dataset
Use the following command to load dataset in python as a DataFrame.
```py
import pandas as pd
df = pd.read_csv(<path_to_data_file>, sep='\t')
```

### Link to Excel Files:
1. [Apt-Excel-file](https://docs.google.com/spreadsheets/d/1xMWIbQw3vuSdO-bKMQYdxH0ox1-Ckt71Y_mqIO-bjAU/edit?usp=sharing)
2. [Brew-Excel-file](https://docs.google.com/spreadsheets/d/1LkNQTG8Nu0ONNNnATUMilGVKmjavDm6pj_NH_8jzRXU/edit?usp=sharing) 
3. [Macports-Excel-file](https://docs.google.com/spreadsheets/d/1LisdoIsNnNSzJHk5JFwWm6hLP_eqOszEa2lj2JeRQ5I/edit?usp=sharing) 
4. [Choco-Excel-file](https://docs.google.com/spreadsheets/d/1VM-qBJIr9Z_pJQzqMsiB6cQg6DmLdwKMfl954XW1Pjk/edit?usp=sharing)
5. [Merged-Excel-file](https://docs.google.com/spreadsheets/d/13huwHpRTHHjiHj8x2J0V7aVnweD_SJguzOUy4Gfx29M/edit?usp=sharing)
