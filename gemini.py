import os
import json
import google.generativeai as genai
from google.api_core import retry

class Gemini:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config={
                "temperature": 0.7,
                "top_p": 0.9,
                "max_output_tokens": 4096,
            }
        )
        
        self.prompt_template = """
        Analyze this resume and provide structured JSON feedback with two fields:
        1. 'review': Detailed professional feedback focusing on:
           - Formatting and structure
           - Content relevance and clarity
           - Keyword optimization
           - Areas for improvement
        2. 'revisedResume': A rewritten version incorporating suggested improvements
        
        Resume Content:
        {resume_text}
        
        Return only valid JSON with these two fields. Do not include markdown formatting.
        """

    @retry.Retry(deadline=30)
    def review(self, resume_text):
        try:
            prompt = self.prompt_template.format(resume_text=resume_text)
            response = self.model.generate_content(prompt)
            
            if not response.text:
                raise ValueError("Empty response from API")
            
            # Clean response and parse JSON
            cleaned_response = response.text.replace("```json", "").replace("```", "").strip()
            return json.loads(cleaned_response)
            
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON response from API")
        except Exception as e:
            raise RuntimeError(f"API Error: {str(e)}")