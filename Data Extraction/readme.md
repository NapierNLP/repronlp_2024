

fromdatabase.py script takes the database.db file and creates combined_results.csv which contains the results and task data from the database.

full_generate_2.py script takes the combined results and merges it with the author provided data as this allows us to query which system was selected by the participant.

attentioncheck.py script checks if there are any tasks in the full_data.csv file that fail the attention check.

remove_attention_fail.py shows which ids failed so that they can be manually removed frmo the database.

count_task_numbers.py uses the combined results csv to ensure there is exactly only three responses per task number.
