# ReproNLP 2024 - Edinburgh Napier University Lab

This is the analysis code, data extraction code, and raw result data for the Edinburgh Napier University lab in the 2024 ReproNLP Challenge. 

This study reproduces [Data-to-text Generation with Entity Modeling](https://aclanthology.org/P19-1195) (Puduppully et al., ACL 2019).

We filled the Human Evaluation Datasheet (HEDs) which can be found in `napiernlp-reprohum2024-datasheet.json` or see the [ReproHum2024 Central HEDs Repo](https://github.com/nlp-heds/repronlp2024).

The analysis folder consists of:
1. `Chart.py and Chart-original.py` - Used to generate the graphs used in the paper publishing our results.
2. `analysis-withdecrem.py` - This is the analysis code used to calculate the relative preference percentage for each system.
3. `full_data.csv` - This is a copy of the raw data for use with the nalysis-withdecrem.py
4. `type1_analysis_cv.py` - This is the code used to calculate the coefficient of variation (CV) ajusted for small sampled, See [paper here](https://aclanthology.org/2022.cl-4.21/) and [code here](https://github.com/asbelz/coeff-var).
5. `type2_analysis.py` - This is the code used to calculate Pearson's r and Spearman's rho.

The data extraction folder consists of:
1. `database.db` - This is the raw database file extracted from the [webapp we used](https://github.com/nlgcat/reprohum-prolific-webapp) to host the reproduction.
2. `author_data.csv` - This is the data provided to us by the original authors, consisting of the task and raw model outputs.
3. `fromdatabase.py` - This script takes the database.db file and creates combined_results.csv which contains the results and task data from the database.
4. `full_generate_2.py` - This script takes the combined results and merges it (into full_data.csv) with the author provided data as this allows us to query which system was selected by the participant in the results.
5. `attentioncheck.py` - This script checks if there are any tasks in the full_data.csv file that fail the attention check.
6. `remove_attention_fail.py` - This script uses the output of attentioncheck.py to provide the researcher with which the IDs to be removed from the database.db and prevented from answering further reruns on prolific.

We also provide `study metadata.txt` which contains additional metadata about the study.
Additionally, we provide the original and reproduction result charts as pngs.

Finally, results data can be found in `Data Extraction/full_data.csv`

**Identifiable information has been replaced with 'XXX'**

---
[Lewis Watson](https://lnwatson.co.uk) and [Dimitra Gkatzia](https://dimitragkatzia.wordpress.com)
