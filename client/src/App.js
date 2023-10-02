import React, { useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Row, Col, Form, Card, Button } from 'react-bootstrap';
import INTJ from './assets/INTJ.jpg';
import INTP from './assets/INTP.jpg';
import ENTJ from './assets/ENTJ.jpg';
import ENTP from './assets/ENTP.jpg';
import INFJ from './assets/INFJ.jpg';
import INFP from './assets/INFP.jpg';
import ENFJ from './assets/ENFJ.jpg';
import ENFP from './assets/ENFP.jpg';
import ISTJ from './assets/ISTJ.jpg';
import ISFJ from './assets/ISFJ.jpg';
import ESTJ from './assets/ESTJ.jpg';
import ESFJ from './assets/ESFJ.jpg';
import ISTP from './assets/ISTP.jpg';
import ISFP from './assets/ISFP.jpg';
import ESTP from './assets/ESTP.jpg';
import ESFP from './assets/ESFP.jpg';
import Morning from './assets/morning.jpg';
import Afternoon from './assets/afternoon.jpg';
import Evening from './assets/evening.jpg';
import Indoor from './assets/indoor.jpg';
import Outdoor from './assets/outdoor.jpg';
import Social from './assets/social.jpeg';
import NonSocial from './assets/non-social.jpeg';

const App = () => {
  const [formData, setFormData] = useState({
    type_of_activity: 'Relaxing Escape',
    indoor_or_outdoor: 'Indoor',
    number_of_people: 1,
    social: 'social',
    location: '',
    time: 'Morning',
    date: '',
    over_21: false,
    filters: [''],
    personality_type: 'INTJ'
  });
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    const { name, value, type } = e.target;
    console.log("Handling Change for:", name, "with value:", value);

    if (type === 'checkbox') {
      setFormData({
        ...formData,
        [name]: e.target.checked
      });
    } else if (name === 'filters') {
      const newFilters = [...formData.filters];
      if (newFilters.includes(value)) {
        const index = newFilters.indexOf(value);
        newFilters.splice(index, 1);
      } else {
        newFilters.push(value);
      }
      setFormData({ ...formData, filters: newFilters });
    } else {
      setFormData({ ...formData, [name]: value });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Create a URLSearchParams object to handle query parameters.
      const params = new URLSearchParams();

      // Loop through formData keys and values.
      for (const [key, value] of Object.entries(formData)) {
        if (key !== "filters" && value !== null && value !== undefined) {
          // Add non-filter params directly.
          params.append(key, value);
        } else if (key === "filters") {
          // Add each filter as its own 'filter' query parameter.
          value.forEach((filter) => params.append('filters', filter));
        }
      }

      // Fetch data from the API.
      const response = await axios.get('http://127.0.0.1:8000', { params }, {
        headers: {
          'Content-Type': 'application/json',
          // any other headers needed...
        },
      });

      setResult(response.data);
    } catch (error) {
      console.error("Error fetching data: ", error);
      setResult(null);
    }
  };

  const handlePersonalityClick = (type) => {
    console.log("Handling Change for personality type. New value:", type);
    setFormData((prev) => ({
      ...prev,
      personality_type: prev.personality_type === type ? '' : type,
    }));
  };

  const handleActivityTypeClick = (type) => {
    console.log("Handling Change for activity type. New value:", type);
    setFormData((prev) => ({
      ...prev,
      type_of_activity: prev.type_of_activity === type ? '' : type,
    }));
  }

  const handleSocialClick = (type) => {
    console.log("Handling Change for social type. New value:", type);
    setFormData((prev) => ({
      ...prev,
      social: prev.social === type ? '' : type,
    }));
  }

  const handleTimeClick = (type) => {
    console.log("Handling Change for time type. New value:", type);
    setFormData((prev) => ({
      ...prev,
      time: prev.time === type ? '' : type,
    }));
  }

  const handleIndoorOutdoorClick = (type) => {
    console.log("Handling Change for indoor or outdoor type. New value:", type);
    setFormData((prev) => ({
      ...prev,
      indoor_or_outdoor: prev.indoor_or_outdoor === type ? '' : type,
    }));
  }

  const handleFilterClick = (filter) => {
    console.log("Handling Change for filter. New value:", filter)
    console.log("Current filters:", formData.filters);
    setFormData((prevData) => {
      const isFilterActive = prevData.filters.includes(filter);
      const newFilters = isFilterActive
          ? prevData.filters.filter((f) => f !== filter)
          : [...prevData.filters, filter];
      return { ...prevData, filters: newFilters };
    });
  };

  const indoorOutdoorOptions = ["Indoor", "Outdoor"];
  const indoorOutdoorImages = {Indoor, Outdoor}

  const timeOfDayOptions = ["Morning", "Afternoon", "Evening"];
  const timeOfDayImages = {Morning, Afternoon, Evening}

  const socialPreferenceOptions = ["Social", "NonSocial"];
  const socialPreferenceImages = {Social, NonSocial};

  const activityTypeOptions = ["Relaxing Escape", "High-Energy Nightlife", "Outdoor Adventure",
    "Thrill-Seeking Expedition", "Romantic Getaway", "Cultural Exploration", "Family Friendly Outing",
    "Learning Experience", "Active and Sporty", "Luxury Experience"];

  const personalityTypes = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
  ];

  const personalityImages = {
    INTJ,INTP,ENTJ,ENTP,INFJ,INFP,ENFJ,ENFP,ISTJ,ISFJ,ESTJ,ESFJ,ISTP,ISFP,ESTP,ESFP,
  };

  const filters = ["No alcohol", "Peace and quiet", "Child friendly", "Safe", "Thrilling"];


  return (
      <div style={{ backgroundColor: '#f0f0f0', height: '100vh' }}>
        <h1 style={{
          textAlign: "center",
          fontSize: "3em",
          fontWeight: "bold",
          color: "#fff",
          backgroundColor: "#007bff",
          padding: "20px",
          borderRadius: "10px",
          marginBottom: "20px"
        }}>Activity Recommender AI</h1>
        <Form onSubmit={handleSubmit}>
          <Container>
            <h2>Select Type of Activity</h2>
            <Row xs={2} md={2} lg={5}>
              {activityTypeOptions.map((type, index) => (
                  <Col key={index} className="mb-2">
                    <Card style={{ width: '15rem' }}>
                      <Card.Img variant="top" src={personalityImages[type]} sizes={"sm"} />
                      <Card.Body>
                        <Card.Title style={{textAlign: "center"}}>{type}</Card.Title>
                        <Button
                            style={{"textAlign": "center"}}
                            variant={formData.type_of_activity === type ? "success" : "primary"}
                            onClick={() => handleActivityTypeClick(type)}
                            size={"sm"}
                        >
                          {formData.type_of_activity === type ? "Chosen" : "Select"}
                        </Button>
                      </Card.Body>
                    </Card>
                  </Col>
              ))}
            </Row>
          </Container>
          <br />
          <Container>
            <h2>Location</h2>
            <Form.Control
                type="text"
                name="location"
                onChange={handleChange}
                value={formData.location}
                aria-describedby="locationHelpBlock"
            />
            <Form.Text id="locationHelpBlock" muted>
              Please enter your preferred location.
            </Form.Text>
          </Container>
          <br />
          <br />
          <Container>
            <h2>Select Social vs Non Social Preference</h2>
            <Row xs={2} md={2} lg={2}>
              {socialPreferenceOptions.map((type, index) => (
                  <Col key={index} className="mb-2">
                    <Card style={{ width: '30rem' }}>
                      <Card.Img variant="top" src={socialPreferenceImages[type]}
                                sizes={"sm"} style={{ width: '100%', height: '250px', objectFit: 'cover' }} />
                      <Card.Body>
                        <Card.Title style={{textAlign: "center"}}>{type}</Card.Title>
                        <Button
                            variant={formData.social === type ? "success" : "primary"}
                            onClick={() => handleSocialClick(type)}
                            size={"sm"}
                        >
                          {formData.social === type ? "Chosen" : "Select"}
                        </Button>
                      </Card.Body>
                    </Card>
                  </Col>
              ))}
            </Row>
          </Container>
          <br />
          <Container>
            <h2>Time of Day Preference</h2>
            <Row xs={2} md={2} lg={3}>
              {timeOfDayOptions.map((type, index) => (
                  <Col key={index} className="mb-2">
                    <Card style={{ width: '15rem' }}>
                      <Card.Img variant="top" src={timeOfDayImages[type]} sizes={"sm"} />
                      <Card.Body>
                        <Card.Title style={{textAlign: "center"}}>{type}</Card.Title>
                        <Button
                            variant={formData.time === type ? "success" : "primary"}
                            onClick={() => handleTimeClick(type)}
                            size={"sm"}
                        >
                          {formData.time === type ? "Chosen" : "Select"}
                        </Button>
                      </Card.Body>
                    </Card>
                  </Col>
              ))}
            </Row>
          </Container>
          <Container>
            <h2>Select Indoor vs Outdoor Preferences</h2>
            <Row xs={2} md={2} lg={6}>
              {indoorOutdoorOptions.map((type, index) => (
                  <Col key={index} className="mb-2">
                    <Card style={{ width: '7rem' }}>
                      <Card.Img variant="top" src={indoorOutdoorImages[type]} sizes={"sm"} />
                      <Card.Body>
                        <Card.Title style={{textAlign: "center"}}>{type}</Card.Title>
                        <Button
                            variant={formData.indoor_or_outdoor === type ? "success" : "primary"}
                            onClick={() => handleIndoorOutdoorClick(type)}
                            size={"sm"}
                        >
                          {formData.indoor_or_outdoor === type ? "Chosen" : "Select"}
                        </Button>
                      </Card.Body>
                    </Card>
                  </Col>
              ))}
            </Row>
          </Container>
          <br />
          <br />
          <Container>
            <h2>Select Personality Type</h2>
            <Row xs={2} md={2} lg={6}>
              {personalityTypes.map((type, index) => (
                  <Col key={index} className="mb-2">
                    <Card style={{ width: '7rem', margin: '0.5rem'}}>
                      <Card.Img variant="top" src={personalityImages[type]} sizes={"sm"} />
                      <Card.Body>
                        <Card.Title style={{textAlign: "center"}}>{type}</Card.Title>
                        <Button
                            variant={formData.personality_type === type ? "success" : "primary"}
                            onClick={() => handlePersonalityClick(type)}
                            size={"sm"}
                        >
                          {formData.personality_type === type ? "Chosen" : "Select"}
                        </Button>
                      </Card.Body>
                    </Card>
                  </Col>
              ))}
            </Row>
          </Container>
          <br />
          <Container>
            <h2>Number of People:</h2>
            <input type="number" name="number_of_people" onChange={handleChange} value={formData.number_of_people} />
          </Container>
          <br />
          <Container>
            <h2>Date</h2>
            <input type="text" name="date" onChange={handleChange} value={formData.date} placeholder="Sunday 01 January"/>
          </Container>
          <br />
          <Container>
            <h2>Over 21:</h2>
            <label>
              (Check if yes) &nbsp;
              <input type="checkbox" name="over_21" onChange={handleChange} checked={formData.over_21} />
            </label>
          </Container>
          <br />
          <Container>
            <h2>Filters</h2>
            <div className="d-flex flex-wrap">
              {filters.map((filter, index) => (
                  <Card key={index} style={{ width: '18rem', margin: '0.5rem' }}>
                    <Card.Body>
                      <Card.Title>{filter}</Card.Title>
                      <Button
                          variant="primary"
                          onClick={() => handleFilterClick(filter)}
                          active={formData.filters.includes(filter)}
                      >
                        {formData.filters.includes(filter) ? 'Chosen' : 'Select'}
                      </Button>
                    </Card.Body>
                  </Card>
              ))}
            </div>
          </Container>
          <br />
          <div className={"d-grid gap-2"} >
            <Button variant="primary" style={{margin: "0px 5px 20px 5px"}} type="submit">Get Suggestions</Button>
          </div>
        </Form>
        {result && (
            <div>
              <Container className="customHeader">
                <Row>
                  <Col>
                    <h2 style={{textAlign: "center"}}>Your Recommendations!</h2>
                    <p>
                      {result.response_summary}
                    </p>
                  </Col>
                </Row>
              </Container>
              <Container>
                <Row className="d-flex flex-wrap justify-content-center">
                  {result.suggestions.map((suggestion, index) => (
                      <Card className="customCard text-center mb-3" key={index}>
                        <Card.Header>Featured</Card.Header>
                        <Card.Body>
                          <Card.Title>{suggestion.title}</Card.Title>
                          <Card.Text>
                            {suggestion.description}
                          </Card.Text>
                          <Button variant="primary" href={suggestion.url}>Learn More</Button>
                        </Card.Body>
                      </Card>
                  ))}
                </Row>
              </Container>
            </div>
        )}
      </div>
  );
};

export default App;


