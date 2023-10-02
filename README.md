# Activity Recommendation AI

## Overview

The Activity reccomendation AI utilizes the capabilities of Metaphor Systems and ChatGPT 
(Generative Pre-trained Transformer) to generate activity suggestions based on user inputs and personality traits.
It leverages natural language processing to understand user inputs and generate creative, engaging, and 
personality-tailored activity suggestions in a human-like manner.

## Features

- **User Input Processing:** Gathers and processes user inputs to understand preferences and constraints.
- **Personality Trait Utilization:** Uses inputs related to personality traits as specified in the Myers-Briggs 
Personality Theory (like MBTI types) to tailor suggestions.
- **Intelligent Suggestions:** Leverages Metaphor and GPT to generate creative and relatable localized and personalized
activity suggestions.
- **Responsive API:** Offers a user-friendly API that can be interacted with to obtain intelligent, tailored suggestions.
  
## Prerequisites

- [Python](https://www.python.org/) (3.7 or higher)
- [Conda](https://docs.conda.io/en/latest/) (for managing and sharing environments)
- [Metaphor API Key](https://metaphor.systems) (You need to sign up on Metaphor’s platform to get an API key)
- [OpenAI API Key](https://www.openai.com) (You need to sign up on OpenAI's platform to get an API key)

## Limitations
Given that the project was whipped up in a few hours, here's a few limitations:
- Slow responses. Average response time is ~ 30-45 seconds due to chain of LLM & Metaphor requests
- No input validation
- No error handling so far
- No unit tests
- Inputs not thoroughly tested and may throw errors unexpectedly

## Installation & Setup

### 1. Clone the Repository

```bash
git clone git@github.com:codermanz/ActivityRecommenderAI.git
cd AncitivtyRecommenderAI
cd placesRecommendationAPI
```
### 2. Set Up Conda Environment

Create a new environment and install dependencies using the provided `apiRequirements.yml` file.

```bash
conda env create -f apiRequirements.yml
```
Activate the environment:

```bash
conda activate metaphorProject
```
### 3. API Keys & Environment Variables

Store your Metaphor API key securely using environment variables. Ensure to replace `[Your-API-Key]` with your actual key.

```bash
echo "export METAPHOR_API_KEY=[Your-API-Key]" >> ~/.bashrc
echo "export OPENAI_API_KEY=[Your-API-Key]" >> ~/.bashrc
source ~/.bashrc
```
_Note: For other shells or operating systems, adapt the storage method accordingly._

Alternatively, create a .env file within placesRecommendationAPI/api/ and store your API keys there. Ensure 
to replace `[Your-API-Key]` with your actual key. The script's load_dotenv() function will automatically load the
environment variables from the .env file.

### 4. Running the Server Locally

Navigate to the project directory and run the following command:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Your server should be up and running locally on `http://127.0.0.1:8000/`. You can make API requests to this URL using tools like `curl`, Postman, or directly through your application.

## Usage

### Making API Requests

Make a GET request to the server, ensuring to pass the required query parameters, such as personality traits, preferences, etc.

Example using `curl`:

```bash
curl "http://127.0.0.1:8000?personality_type=INTJ&type_of_activity=relaxing escape&indoor_or_outdoor=indoor&number_of_people=1&social=social&location=San Francisco Bay Area&time=evening&date=Sunday October 1&over_21=true&filters=no music&filters=no alchohol"
```

## Client Set up and Usage

There's also a patched up front end that'll allow you to see quick results. To run the front end, navigate to the
client directory and run the following commands:

```bash
npm install
npm start
```
Ensure the Django RESTful framework is running at the same time as this client. You should be able to now access this 
client through localhost:3000. Please be patient after pressing submit to get results. It takes a while to process the
request and generate the results. Give it at least 45 seconds!

# API Documentation

## Overview

The Activity Preference Generator API generates personalized activity suggestions based on the provided user inputs in the form of query parameters. This document outlines the required parameters, their acceptable values, and usage.

## API Endpoint

```
GET /suggestions
```

### Query Parameters

#### 1. `activity_type` (required)
Describes the desired nature of the activities.

- **Relaxing Escape**
- **High-Energy Nightlife**
- **Outdoor Adventure**
- **Thrill-Seeking Expedition**
- **Romantic Getaway**
- **Cultural Exploration**
- **Family Friendly Outing**
- **Learning Experience**
- **Active and Sporty**
- **Luxury Experience**

_Example:_
```
activity_type=Relaxing+Escape
```

#### 2. `indoor_outdoor` (required)
Specifies preference for indoor or outdoor activities.

- **Indoor**
- **Outdoor**

_Example:_
```
indoor_outdoor=Outdoor
```

#### 3. `num_people` (required)
Indicates the number of people participating. Should be a number.

_Example:_
```
num_people=4
```

#### 4. `social_preference` (required)
Indicates if the user prefers social or non-social activities.

- **social**
- **non-social**

_Example:_
```
social_preference=social
```

#### 5. `location` (required)
Specifies the city or locality for the activities. Should be a valid city or locality name.

_Example:_
```
location=New+York+City
```

#### 6. `time` (required)
Specifies the preferred time for the activity.

- **Morning**
- **Afternoon**
- **Evening**

_Example:_
```
time=Afternoon
```

#### 7. `date` (required)
Indicates the preferred date for the activity, formatted as "Day of the week", "Date of the month", "Month".

_Example:_
```
date=Saturday+30+September
```

#### 8. `over_21` (required)
Boolean indicating if participants are over 21.

- **True**
- **False**

_Example:_
```
over_21=True
```

#### 9. `filters` (required)
A list of strings indicating any additional filters or preferences. For each index in the string, create a new 
filters' parameter. If you don't want any filters, leave the other side of the equality as blank. Do not omit the 
parameter. The following is examples of how to structure your filters:

- **No alcohol**
- **Peace and quiet**
- **Music filled**

_Example:_
```
filters=No+alcohol,filters=Peace+and+quiet
```

#### 10. `personality_type` (required)
Indicates the Myers-Briggs Personality Type (MBTI) of the user.

- Any one of the 16 MBTI personality types: ISTJ, ISFJ, INFJ, INTJ, ISTP, ISFP, INFP, INTP, ESTP, ESFP, ENFP, ENTP, ESTJ, ESFJ, ENFJ, ENTJ.

_Example:_
```
personality_type=INTJ
```

## Example Request

```
http://127.0.0.1:8000?personality_type=INTJ&type_of_activity=high-energy nightlife&indoor_or_outdoor=outdoor&number_of_people=5&social=non-social&location=New York&time=evening&date=Sunday October 1rst&over_21=false&filters=
```
or with filters:
```
http://127.0.0.1:8000?personality_type=INTJ&type_of_activity=relaxing escape&indoor_or_outdoor=indoor&number_of_people=1&social=social&location=San Francisco Bay Area&time=evening&date=Sunday October 1&over_21=true&filters=no music&filters=no alchohol
```

---

Ensure to properly URL-encode parameter values to ensure consistency and reliability in requests. The parameters should be concatenated using `&` and space should be encoded as `+` or `%20`.

### Expected Responses

- **200 OK:** The request was successful and the response will contain generated activity suggestions.
- **400 Bad Request:** The request was malformed or missing parameters. Ensure all required parameters are passed.


## Acknowledgements

- Metaphor API for natural language generation capabilities
- GPT (OpenAI) for backend natural language processing/Large Language Model capabilities

---