# DocChat

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

  
</div>

![Langchain][Langchain1]

<b>Dependencies:</b> Langchain, Pinecone, OpenAI, Streamlit

<!-- ABOUT THE PROJECT -->
## About The Project

DocChat is a web application which uses **Retrieval Augmented Generation (RAG)** to answer user queries about a document given a desired response type and complexity.

The application utilizes:
- **LangChain** for chaining LLM operations
- **OpenAI's text-embedding-ada-002 model** for document embeddings
- **Pinecone** for vector storage and similarity search
- **Streamlit** for the user interface

Below are some of the key features of DocChat:

- **Upload & Process PDFs**: Users can upload their PDF files to be processed instantly
- **Dynamic Querying**: Ask questions related to document content with AI-driven responses
- **Response Customization**: Adjust response format and difficulty level
- **Cloud-based Processing**: Ensures quick and accurate retrieval of document insights.

<!-- GETTING STARTED -->
## Getting Started

**Prerequisites: Python 3.8+, pip, Git**

1. Clone this repository and navigate to the local project folder
2. Install dependencies
   ```
   pip install -r requirements.txt
   ```
3. Create .env file in main directory
   ```
   touch .emv
   ```
4. Set your environment variables
   ```
   OPENAI_API_KEY=your-openai-api-key
   PINECONE_API_KEY=your-pinecone-api-key
   INDEX_NAME=your-pinecone-environment
   ```
5. Run the app
   ```
   streamlit run app.py
   ```
   
<!-- CONTRIBUTING -->
## Project Views

<img src="views/image1.png" alt="main"  width="auto" height="auto">



<!-- CONTACT -->
## About

Author: Ronoy Sarkar

Project Link: [https://github.com/ronoys/DocChat](https://github.com/ronoys/DocChat)


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments


* [README Template](https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



[Langchain1]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white](https://img.shields.io/badge/LangChain-0050EF?style=for-the-badge&logo=LangChain&logoColor=white

