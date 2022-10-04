# Wiki

A simple Wiki API where users can create new revisions of documents and search for either all or a specific title of a document.  

This project is made with:  
- Python3
- FastAPI
- SQLAlchemy
- SQLite

This project features:
- Testing with Pytest

### Specifications
1. A wiki is a collection of documents
2. Documents are lumps of plain text. No graphics, attachments, or formatting
3. Each document is uniquely identified by a title that is a maximum of 50 characters in
length. This title does not change for the life of a document
4. A document can have multiple revisions, as it is updated over time. We store all
historical revisions of a document
5. We should be able to view the document as it was at any point in time. I.e. we can use
any timestamp to fetch a revision e.g. If we have a document at time 1pm and time
3pm, then sending a timestamp of 2pm should return the document as it was at time
1pm.

## Running The Project Locally

### Installation

1. Open the Git Bundle  

2. Create a virtual environment
   ```sh
   python3 -m venv /path/to/new/virtual/environment
   ``` 
3. Activate your virtual environment
   ```sh
   source your-virt-env-folder/bin/activate
   ``` 
4. Install the requirements
   ```sh
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```  
    
### Usage

- Start the server
  ```sh
  uvicorn main:app --reload
  ```
- View your Swagger UI and test the endpoints manually
  ```sh
  http://127.0.0.1:8000/docs
  ``` 

### Testing

You can run the tests using:
```shell script
pytest -s -v
```

## Implementation  


The following endpoints were built:  

GET /documents  
This should return a list of available titles.  

GET /documents/\<title\>  
This should return a list of available revisions for a document.

POST /documents/\<title\>  
This allows users to post a new revision of a document.  
It should receive JSON in the form: {content: ‘new content...’}.  

### Error Handling

- Title validation was done in the handler, since it's the handler's concern and not the database's.  
- The 'create new revision' function does not check if the title already exists. It creates a new revision of that doc and a new entry to the database, whether that will be the first revision of a title (that title actually gets created), or a later revision of a title.  
- An exception is raised (again, at the handler level) when the user is trying to view a title that does not exist.  
- A custom exception was created in the case that the title is longer than 50 characters in order to make the error clearer than a generic 'Invalid data' error. This is also clearer than having a restriction at the db model (e.g. max 50 chars).

### Testing  

- A testing database was created, so that the tests won't use the production database and mess with the data.  
- Normally, we would truncate instead of dropping all the tables in the test db. However, SQLite would not allow this.  
- Ideally, there would be another, separate test file that tests the db api.  
- Normally, there would be test classes and initial set up steps before defining the tests.  
- Future work includes to aim for 100% test coverage and include tests for all edge cases.  

### Future Work

- Ideally, a post request would return the data that were created.  
- Furthermore, it would be good to utilise the DocumentDisplay schema (which has already been created) in order to return only the relevant data from the db entry we are retrieving or creating.  
- A test file that tests the db api.  
- Implement the following endpoints:  

  GET /documents/\<title\>/\<timestamp\>  
  This should return the document as it was at that timestamp.  

  GET /documents/\<title\>/latest  
  This should return the current latest version of the document.  
