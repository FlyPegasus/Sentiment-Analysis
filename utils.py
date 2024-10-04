import pandas as pd
from strictjson import strict_json
from groq import Groq


class FileToDataFrame:
    def __init__(self, file_path):
        self.file_path = file_path
        self.dataframe = None
        self.output_dict = None
        self.client = Groq(
            api_key="<api key>",
        )

    def load_file(self):
        if self.file_path.endswith('.csv'):
            self.dataframe = pd.read_csv(self.file_path)
        elif self.file_path.endswith('.xlsx') or self.file_path.endswith('.xls'):
            self.dataframe = pd.read_excel(self.file_path)
        else:
            print("sapex4")
            raise ValueError(
                "Unsupported file format. Please provide a CSV or Excel file.")
        print("File successfully loaded into DataFrame.")
        '''except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")'''

    def llm(self, system_prompt: str, user_prompt: str) -> str:
        # ensure your LLM imports are all within this function

        response = self.client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content

    def analyze(self, text):
        res = strict_json(system_prompt='You are a sentiment analyser. You analyse phrases and score them into [positive, negative, neutral]. You return all classifications and their score in json format.',
                          user_prompt=text,
                          output_format={'Positive': 'Score of Positive',
                                         'Negative': 'Score of Negative',
                                         'Neutral': 'Score of Neutral'},
                          llm=self.llm)
        return res

    def get_dataframe(self):
        if self.dataframe is not None:
            return self.dataframe
        else:
            print("DataFrame is empty. Please load a valid file first.")
            return None

    def output(self):
        self.output_dict = dict()
        for index, row in self.dataframe.iterrows():
            # print(row['Review'])
            text = row['Review']
            self.output_dict[text] = self.analyze(text)
        return self.output_dict
