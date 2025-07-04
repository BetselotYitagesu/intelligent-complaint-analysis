Exploratory Data Analysis and Preprocessing Summary

The original dataset from the Consumer Financial Protection Bureau (CFPB) contained 9,609,797 complaint records spanning a broad range of financial products and services. Of these, a substantial portion—6,629,041 records (≈69%)—were missing the core Consumer complaint narrative field. Since narrative text is the foundation for our Retrieval-Augmented Generation (RAG) system, these entries were excluded from further processing.

Focusing the analysis on CrediTrust’s five strategic product categories—Credit card, Personal loan, Buy Now, Pay Later (BNPL), Savings account, and Money transfers—required mapping several inconsistent product names in the dataset into standardized labels. This included combining similar product names such as “Credit card or prepaid card” under Credit card, and loosely associating Virtual currency as a proxy for BNPL due to naming limitations in the CFPB dataset.

After applying both the product category mapping and filtering for non-null narratives, the dataset was reduced to 478,834 complaint records—a clean and focused subset well-suited for semantic embedding and search. This refined dataset strikes a balance between size and relevance, ensuring the downstream pipeline operates on high-quality, business-aligned inputs.

Further analysis of complaint narrative lengths showed a wide range in verbosity, with some users submitting brief one-sentence issues and others writing detailed multi-paragraph narratives. To improve embedding consistency, we cleaned the narratives by:

    Converting text to lowercase,

    Removing URLs and special characters,

    Collapsing excessive whitespace.

The final preprocessed dataset was saved as filtered_complaints.csv and will serve as the input for chunking, embedding, and indexing in the next stage of the pipeline.
